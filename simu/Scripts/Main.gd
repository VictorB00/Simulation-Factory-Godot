extends Node


onready var _Navigation = $Navigation2D

var _Robot
export (PackedScene) var RobotScene
export (PackedScene) var PackageScene
export (PackedScene) var MachineScene

var packages_list

var machines_list
#each element of the array is a Machine node

var robots_list

var packages_nb : int = 0

#var processes_list
#each element of the array is an array of integers 
#corresponding to the machines possible for the given process
#example : if process no.3 can be done by machines 4 or 5, 
#		   then the element at index 3 can be [4,5] (or [5,4])

var possible_tasks

func _ready():	
	#initialization
#	var test_templates = [ [[0,10],[1,5]], [[0,1],[1,8],[2,6]], [[2,3],[1,9]], [[2,7],[0,12],[5,4]] ]
#	var test_processes = [[Process.new(0,0), Process.new(1,0), Process.new(2,0)], [Process.new(2,0), Process.new(3,0), Process.new(4,0), Process.new(5,0)]]
#	var machine_nb := 0
#	for machine in get_tree().get_nodes_in_group("machines"):
#		if machine.is_in_group("input_machines"):
#			machine.packages_templates = test_templates
#			machine.create_time = 5.0
#		elif machine.is_in_group("output_machines"):
#			pass
#		else:
#			machine.processes.processes = test_processes[machine_nb]
#			machine_nb += 1


	#values of arguments
	
	var arguments : Array = Array(OS.get_cmdline_args ())
	
	var rng_seed = int(get_arg(arguments,"--seed",0 ))
	seed(rng_seed)
	
	var scenario_file = get_arg(arguments,"--scenario","res://scenarios/new_scenario.json" )
	load_scenario(scenario_file)
	
	var pickup_radius = float(get_arg(arguments,"--pickup-radius",100 ))
	_Robot.get_node("RayCast2D").set_cast_to(Vector2.RIGHT*pickup_radius)
	
	
	var log_name = get_arg(arguments,"--log", "")
	if log_name == "":
		var default_dir = OS.get_executable_path().get_base_dir()
		var default_log_name = "log"+str(OS.get_system_time_msecs())+".log"
		
		var dir = Directory.new()
		dir.open(default_dir)
		if not(dir.dir_exists("simu_logs")):
			dir.make_dir("simu_logs")
		log_name = default_dir + "/simu_logs/" + default_log_name
	Logger.set_log_location(log_name)

	
	#launch Communication Server
	var port = int(get_arg(arguments,"--port",10000 ))
	Communication.start_server(port)
	
	
func get_arg(args, arg_name, default):
	var index = args.find(arg_name)
	if index !=-1:
		return args[index+1]
	else:
		return default
	
func add_package(package : Node):
	packages_list.append(package)
	
func remove_package(package : Node):
	var package_index = packages_list.find(package)
	if package_index >= 0 :
		packages_list.remove(package_index)

	
	
func load_scenario(file_path : String):
	
	
	#load scenario file
	var file = File.new()
	var open_error = file.open(file_path, File.READ) 
	if open_error:
		Logger.log_error("Error opening the scenario file (Error code %s)" % open_error)
		return
		
	var content = JSON.parse(file.get_as_text())
	file.close()
	
	if content.get_error():
		Logger.log_error("Error parsing the scenario file (Error code %s)" % content.get_error())
		return	
		
	var scenario = content.get_result()
	
	
	#machines
	var all_machines_list = get_tree().get_nodes_in_group("machines")
	#filter to exclude intput and output machines
	
	var machines_list = []
	for machine in all_machines_list:
		if not(machine.is_in_group("input_machines")) and not(machine.is_in_group("output_machines")):
			machines_list.append(machine)
			
	if scenario.machines.size()!=machines_list.size():
		Logger.log_error("Wrong number of machines : processes specified for %s machines but there are %s machines in the simulation" 
						% [scenario.machines.size(),machines_list.size()])
	else:	
		for k in range(scenario.machines.size()):	
			var position = scenario.machines[k].position
			var x = position[0]
			var y = position[1]

		#find if there is a machine close enough to the position specified (for now search for distance <50)
			var closest_machine = null
			var closest_machine_x = 0
			var closest_machine_y = 0
			for machine in machines_list:
				var position_machine_pixels = ExportManager.pixels_to_meters(machine.position)
				var machine_x = floor(position_machine_pixels[0])
				var machine_y = floor(position_machine_pixels[1])
				if abs(machine_x-x)<=1 and abs(machine_y-y)<=1:
					closest_machine = machine
					closest_machine_x = machine_x
					closest_machine_y = machine_y
			if closest_machine == null:
				Logger.log_error("Cannot identify the machine for position specified (%s %s)" % [x,y])
			else:
				#a machine was found close enough but if position was not exact still register a warning
				if closest_machine_x != x or closest_machine_y != y:
					Logger.log_warning("No machine found at position specified (%s %s), so used instead the closest one at position (%s %s) " 
					% [x,y,closest_machine_x,closest_machine_y])
				
				var new_processes_list = []
				for process_id in scenario.machines[k].possible_processes:
					new_processes_list.append(Process.new(process_id))
					
				closest_machine.processes.processes = new_processes_list
			
	
	#robots		
	for k in range(scenario.robots.size()):
		var new_robot = RobotScene.instance()
		add_child(new_robot)
		var new_position = scenario.robots[k].position
		new_robot.position.x = new_position[0]
		new_robot.position.y = new_position[1]
		
		if k==0:
			_Robot = new_robot
		
	#packages
	for machine in get_tree().get_nodes_in_group("input_machines"):
			machine.packages_templates = scenario.packages
			machine.create_time = 5.0
		
	#$Arrival_Zone.set_next_packages(scenario.packages)
	print( scenario)

func _unhandled_input(event):
	if event.is_action_pressed("ui_up"):
		_Robot.pick()
	if event.is_action_pressed("ui_down"):
		_Robot.place()
		
	if event.is_action_pressed("ui_left"):
		_Robot.do_rotation(-PI/2, 2.0)
	if event.is_action_pressed("ui_right"):
		_Robot.do_rotation(PI/2, 2.0)

	if event is InputEventMouseButton and event.pressed:
		match event.button_index:
			BUTTON_LEFT:
				_Robot.navigate_to(event.position)
			BUTTON_RIGHT:
#				var temp_shape = PoolVector2Array([Vector2(-32,-32),Vector2(-32,32),Vector2(32,32),Vector2(32,-32)])
#				var temp_transform = Transform2D(0, event.position)
#				_Navigation.get_node("NavigationPolygonInstance").navpoly = _Navigation.cut_poly(temp_transform.xform(temp_shape))
				var angle = _Robot.get_angle_to(event.position)
				_Robot.do_rotation(angle, 2.0)
			BUTTON_MIDDLE:
#				_Navigation.get_node("NavigationPolygonInstance").navpoly = _Navigation.static_poly
				pass