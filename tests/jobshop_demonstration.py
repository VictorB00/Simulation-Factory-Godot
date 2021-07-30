import threading
import time
import unittest
import subprocess
import os

from ..clients.python_client.CompleteClient import CompleteClient

class OtherTest(unittest.TestCase):

    def setUp(self):
        self.client = CompleteClient("localhost",10000)
        
        self.sim = subprocess.Popen([os.environ["GODOT_PATH"], "--main-pack", " Simulation-Factory-Godot/simu/simulation.pck",
            "--scenario", os.environ["GITHUB_WORKSPACE"] + "/simu/scenarios/new_scenario_multirobots.json", 
            "--environment", os.environ["GITHUB_WORKSPACE"] + "/simu/environments/env_6_machines.json",
            "--jobshop", os.environ["GITHUB_WORKSPACE"] + "/simu/jobshop/instances/ft06.txt",
            "--robot_controller", "teleport",])

        self.assertTrue(self.client.wait_for_server(10))

    def tearDown(self):
        self.stop_threads = True
        for thread in self.threads:
            thread.join()

        self.client.kill()
        self.sim.kill()
        self.sim.wait()

    def test_jobshop(self):
        self.run_solver()
        self.load_jobshop()

        #wait until static information on robots is received (supposed to be received at same time for all robots so wait only for first robot)
        self.assertTrue(self.client.StateClient.wait_condition(lambda state : 'robot0' in state, timeout=10))
        self.robots_list = self.client.StateClient.robots_list()

        self.stop_threads = False
        self.lock = threading.Lock()   
        self.commands_to_be_done = []
        self.new_command_available = threading.Event()

        self.threads = []
        for robot in self.robots_list:
            new_thread = threading.Thread(target=self.robot_thread, args=[robot])
            new_thread.daemon = True
            self.threads.append(new_thread)
            new_thread.start()

        
        self.machines_progressions = [0 for k in range(self.nb_machines)] #id of next package in list of package to be processed by this machine

        self.jobs_progressions = [0 for k in range(self.nb_jobs)] #for each job (which corresponds to a package in the simulation), 
                                                             #id of the next task to be done, or a value of nb_machines if all tasks done
                                                             # and nb_machines+1 if the package has been delivered
        final_progressions = [self.nb_machines+1 for k in range(self.nb_jobs)] 
        timeout = 500
        start_time= time.time()

        self.packages_task_in_progress = [False for k in range(self.nb_jobs)] #used to know if each package is currently waiting to have a task done
                                                                             #which if true means in the queue of task to be done by robot there is one linked to this package

        while self.jobs_progressions!=final_progressions:
            for package_id in range(self.nb_jobs):
                #check next task for each jobs except job where all tasks have been done and package have been delivered
                if not(self.packages_task_in_progress[package_id]):

                    if self.jobs_progressions[package_id] == self.nb_machines:
                        #case where all tasks have been done and the package needs to be delivered to the output_machine
                        output_machine = self.find_output_machine()
                        package_name = self.package_name(package_id)

                        is_ready_to_pick = self.client.StateClient.belt_type(self.client.StateClient.package_location(package_name)) == "output"

                        if is_ready_to_pick :
                            #self.carry_to_machine(package_name, output_machine)
                            self.packages_task_in_progress[package_id] = True
                            self.commands_to_be_done.append((package_name, output_machine))
                            self.new_command_available.set()

                            #if all package are done wait for this final one to be processed by the output_machine
                            if self.jobs_progressions==final_progressions:
                                self.assertTrue(self.client.StateClient.wait_condition(lambda state :  state[package_name]['Package.location'] == output_machine, timeout=0))
                                self.assertTrue(self.client.StateClient.wait_condition(lambda state : state[output_machine]['Machine.progress_rate'] == 1, timeout=0))

                    elif self.jobs_progressions[package_id] < self.nb_machines:
                        #case of standard task where the package needs to be delivered to the corresponding machine
                        package_name = self.package_name(package_id)

                        #find id of next machine the package needs to be processed by
                        job_content = self.machines[package_id] 
                        
                        machine_id = job_content[self.jobs_progressions[package_id]] -1 #- 1 because in jobshop file machines number start at 1
                        
                        machine_order = self.all_machines_order[machine_id]
                        machine_next_task = machine_order[self.machines_progressions[machine_id]]
                        
                        #check if this task is the next one for this machine in the order found by the solver
                        is_next_one = machine_next_task == (package_id,self.jobs_progressions[package_id])
                        #check that the package is ready to pick (if it is on an output belt)
                        is_ready_to_pick = self.client.StateClient.belt_type(self.client.StateClient.package_location(package_name)) == "output"

                        if is_next_one and is_ready_to_pick:
                            #self.carry_to_machine(package_name, machine_name)
                            self.packages_task_in_progress[package_id] = True
                            self.commands_to_be_done.append((package_id, machine_id))
                            self.new_command_available.set()


            current_time = time.time()
            if current_time - start_time >= timeout:
                break
            time.sleep(0.1)

    def robot_thread(self, robot_name):
        while not(self.stop_threads) and self.new_command_available.wait(10):
            next_command = None
            self.lock.acquire()
            if self.commands_to_be_done != []:
                next_command = self.commands_to_be_done.pop(0)
            else :
                self.new_command_available.clear()
            self.lock.release()

            if next_command != None:
                package_id, machine_id = next_command
                package_name = self.package_name(package_id)

                machine_name = None
                if machine_id==-1: #codes for output machine
                    machine_name = self.find_output_machine()
                else:
                    machine_name = self.machine_name(machine_id)
                self.carry_to_machine(robot_name, package_name, machine_name)

                self.jobs_progressions[package_id] +=1
                if machine_id!=-1:
                    self.machines_progressions[machine_id] +=1
                    self.packages_task_in_progress[package_id] = False
        
    def package_name(self, package_id):
        return "package" + str(package_id)

    def machine_name(self, machine_id):
        return "machine" + str(machine_id)

    def load_jobshop(self):
        #load the jobshop file and parse it
        lines_split = []
        with open(os.environ["GITHUB_WORKSPACE"] + "/simu/jobshop/instances/ft06.txt") as f:
            line = f.readline()
            while line:
                lines_split.append(line.split(" "))
                line = f.readline()

        self.nb_jobs=int(lines_split[1][0])
        self.nb_machines=int(lines_split[1][1])

        self.times = []
        for k in range(3, 3 + self.nb_jobs):
            new_array = []
            for value in lines_split[k][:-1]:
                new_array.append(float(value))
            self.times.append(new_array)
				
        self.machines = []
        for k in range(4 + self.nb_jobs, 4 + 2*self.nb_jobs):
            new_array = []
            for value in lines_split[k][:-1]:
                new_array.append(int(value))
            self.machines.append(new_array)

    def run_solver(self):
        subprocess.run(["aries/target/release/jobshop",
        os.environ["GITHUB_WORKSPACE"] + "/simu/jobshop/instances/ft06.txt", "-o", "solution.txt"], stdout=subprocess.PIPE)

        self.all_machines_order = []
        with open('solution.txt') as f:
            line = f.readline()
            while line:
                machine_order = []
                print( line)
                line_split = line.split("\t")
                for element in line_split[1:-1]:
                    job, task = int(element[1]), int(element[4])
                    machine_order.append((job, task))
                line = f.readline()   
                self.all_machines_order.append(machine_order)



    def find_output_machine(self):
        machines_list = self.client.StateClient.machines_list()
        for machine in machines_list :
            if self.client.StateClient.machine_type(machine) == 'output_machine':
                return machine

    def charge(self, robot):
        #makes the robot go to a charging area and wait until battery is full
        action_id = self.client.ActionClientManager.run_command(['go_charge',robot])
        self.assertTrue(self.client.ActionClientManager.wait_result(action_id, timeout=10))

        self.assertTrue(self.client.StateClient.wait_condition(lambda state : state[robot]['Robot.battery'] == 1, timeout=10))

    def position_robot_to_belt(self, robot, belt):
        #takes as argument a belt
        #makes the robot go to an interact area of the belt and face the belt
        interact_area = self.client.StateClient.belt_interact_areas(belt)[0]
        action_id = self.client.ActionClientManager.run_command(['navigate_to_area',robot, interact_area])
        self.assertTrue(self.client.ActionClientManager.wait_result(action_id, timeout=10))
        action_id = self.client.ActionClientManager.run_command(['face_belt',robot ,belt, 5])
        self.assertTrue(self.client.ActionClientManager.wait_result(action_id, timeout=10))

    def carry_to_machine(self, robot, package, machine):
        if self.client.StateClient.robot_battery(robot)<0.4:
            self.charge(robot)
        self.take_package(robot, package)
        self.deliver_package(robot, machine)

    def take_package(self, robot, package):

        belt = self.client.StateClient.package_location(package)
        self.position_robot_to_belt(robot, belt)
        action_id = self.client.ActionClientManager.run_command(['pick_package',robot, package])
        self.assertTrue(self.client.ActionClientManager.wait_result(action_id, timeout=10))

    def deliver_package(self, robot, machine):

        belt_in = self.client.StateClient.machine_input_belt(machine)
        self.position_robot_to_belt(robot, belt_in)
        action_id = self.client.ActionClientManager.run_command(['place',robot])
        self.assertTrue(self.client.ActionClientManager.wait_result(action_id, timeout=10))


if __name__ == '__main__':
    unittest.main()      