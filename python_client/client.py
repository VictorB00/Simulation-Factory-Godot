import socket
import sys

import math

import socket
import sys

import json
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
	
def goto_path_stand(stand_x,stand_y):
	#given robot position and position of stand to go to computes and sends instructions to move it to objective
	#then issue goto command
	Command = messages_pb2.Command()
	Command.command_name = messages_pb2.Command.Command_types.Value('GOTO_PATH')
	Command.goto_path_parameters.destination_x = stand_x
	Command.goto_path_parameters.destination_y = stand_y
	
	message = Command.SerializeToString()
	length = len(message).to_bytes(4,'little') #4bytes because sending as int32 
	sock.sendall(length + message)
	
	return	
	

try:

	message = json.dumps({'timestamp' : time.time(), 'robot_command': ['navigate_to', 505, 400]})
	
	message = json.dumps({'timestamp' : time.time(), 'robot_command': ['pickup', '0']})
	length = len(message).to_bytes(4,'little') #4bytes because sending as int32 
	sock.sendall(length + bytes(message,encoding="utf-8"))

	data = ""
	while True:
		data = sock.recv(4)
		if len(data)>0:
			size = int.from_bytes(data,'little')
			print(size) 
			data = sock.recv(size)
			state = json.loads(data)
			print(state) 

	# #first save environment
	
	# environment = messages_pb2.Environment_Description()
	# length = 0
	# while length == 0:
	# 	data = sock.recv(4)#because int32
	# 	length = len(data)
	# 	if len(data)>0:
	# 		size = int.from_bytes(data,'little')
	# 		data = sock.recv(size)
	# 		environment.ParseFromString(data)
	# 		print(environment) 
			
	# 		liste_machines = environment.machines
			
	
	
	# destination_stand = None

	# while True:
	# 	data = sock.recv(4)
	# 	if len(data)>0:
	# 		size = int.from_bytes(data,'little')
	# 		data = sock.recv(size)
	# 		state = messages_pb2.State()
	# 		state.ParseFromString(data)
	# 		#print(state) 
			
	# 		# if destination_stand == None:
	# 			# #then we will fix the destination_stand to the farthest stand 
	# 			# stands_x = state.stands_x
	# 			# stands_y = state.stands_y
	# 			# dist_max=0
	# 			# pos_x = state.robots_x[0]
	# 			# pos_y = state.robots_y[0]
	# 			# for k in range(len(stands_x)):
	# 				# x = stands_x[k]
	# 				# y = stands_y[k]
	# 				# dist = (x-pos_x)**2 + (y-pos_y)**2
	# 				# if dist >= dist_max:
	# 					# dist_max = dist
	# 					# destination_stand = k #index of corresponding stand
						
	# 		for k in range(2):
	# 		#for now we will try a program making each robot take care of a corresponding package
	# 			package = state.packages[k]
	# 			robot = state.robots[k]					
							
	# 			if not(robot.is_moving):
	# 				#send a command only if robot not already moving
					
	# 				possible_types = messages_pb2.State.Location.Location_Type
					
	# 				if package.location.location_type == possible_types.Value('ARRIVAL') or package.location.location_type == possible_types.Value('MACHINE_OUTPUT'):
						
	# 					#case where the package is on an output stand so needs to be picked up
	# 					if package.location_id != destination_stand:
	# 						pos_x = robot.x
	# 						pos_y = robot.y
							
	# 						#then need to get coordinates of stand where package is located, will depend on if arrival zone or machine output
	# 						stand_x = 0
	# 						stand_y = 0
	# 						if package.location.location_type == possible_types.Value('ARRIVAL'):
	# 							area = environment.arrival_area
	# 							stand_x = area.x
	# 							stand_y = area.y
	# 						else:
	# 							machine_id = package.location.parent_id
	# 							machine = environment.machines[machine_id]
	# 							area = machine.output_area
	# 							stand_x = area.x
	# 							stand_y = area.y
							
							
	# 						distance = (stand_x-pos_x)**2 + (stand_y-pos_y)**2
	# 						print(distance)
							
	# 						if distance > 100**2: #compare to pickup radius, will need to take the right value later

	# 							goto_path_stand(stand_x,stand_y)
								
	# 						else:
	# 							#already close enough so send pickup command
	# 							Command = messages_pb2.Command()
	# 							Command.command = messages_pb2.Command.Command_types.Value('PICKUP')
	# 							#pas besoin de specifier d'autres parametres pour une commande de type pickup
	# 							message = Command.SerializeToString()

	# 							length = len(message).to_bytes(4,'little') #4bytes because sending as int32 
	# 							sock.sendall(length + message)
		
	# 				elif package.location.location_type == possible_types.Value('ROBOT'):
	# 					#case where the robot already picked up the package so needs to deliver it to the objective
	# 					pos_x = state.robots_x[0]
	# 					pos_y = state.robots_y[0]
	# 					stand_x = state.stands_x[destination_stand]
	# 					stand_y = state.stands_y[destination_stand]
	# 					distance = (stand_x-pos_x)**2 + (stand_y-pos_y)**2
						
	# 					if distance > 100**2: #compare to pickup radius, will need to take the right value later
								
	# 						direction_x = stand_x - pos_x
	# 						direction_y = stand_y - pos_y
	# 						goto_stand(direction_x,direction_y)
							
	# 					else:
	# 						#already close enough so send pickup command (this time it will have the effect to drop and not pick up)
	# 						Command = messages_pb2.Command()
	# 						Command.command = messages_pb2.Command.Command_types.Value('PICKUP')
	# 						#pas besoin de specifier d'autres parametres pour une commande de type pickup
	# 						message = Command.SerializeToString()

	# 						length = len(message).to_bytes(4,'little') #4bytes because sending as int32	 
	# 						sock.sendall(length + message)

finally:
	print('closing socket')
	sock.close()
	


