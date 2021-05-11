# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='communication_commandes',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0emessages.proto\x12\x17\x63ommunication_commandes\"\xdd\x04\n\x07\x43ommand\x12\x44\n\x0c\x63ommand_name\x18\x01 \x01(\x0e\x32..communication_commandes.Command.Command_types\x12\x10\n\x08robot_id\x18\x05 \x01(\x05\x12Y\n\x16pickup_drop_parameters\x18\x02 \x01(\x0b\x32\x37.communication_commandes.Command.Pickup_Drop_ParametersH\x00\x12K\n\x0fgoto_parameters\x18\x03 \x01(\x0b\x32\x30.communication_commandes.Command.Goto_ParametersH\x00\x12U\n\x14goto_path_parameters\x18\x04 \x01(\x0b\x32\x35.communication_commandes.Command.Goto_Path_ParametersH\x00\x1a*\n\x16Pickup_Drop_Parameters\x12\x10\n\x08stand_id\x18\x01 \x01(\x05\x1a;\n\x0fGoto_Parameters\x12\x0b\n\x03\x64ir\x18\x01 \x01(\x02\x12\r\n\x05speed\x18\x02 \x01(\x02\x12\x0c\n\x04time\x18\x03 \x01(\x02\x1a\x44\n\x14Goto_Path_Parameters\x12\x15\n\rdestination_x\x18\x01 \x01(\x02\x12\x15\n\rdestination_y\x18\x02 \x01(\x02\">\n\rCommand_types\x12\x08\n\x04GOTO\x10\x00\x12\n\n\x06PICKUP\x10\x01\x12\r\n\tGOTO_PATH\x10\x02\x12\x08\n\x04\x44ROP\x10\x03\x42\x0c\n\nparameters\"\xe3\x04\n\x05State\x12\x34\n\x06robots\x18\x01 \x03(\x0b\x32$.communication_commandes.State.Robot\x12\x38\n\x08packages\x18\x02 \x03(\x0b\x32&.communication_commandes.State.Package\x1a\x41\n\x05Robot\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\x0f\n\x07\x62\x61ttery\x18\x03 \x01(\x02\x12\x11\n\tis_moving\x18\x04 \x01(\x08\x1a\x9b\x01\n\x07Package\x12\x39\n\x08location\x18\x01 \x01(\x0b\x32\'.communication_commandes.State.Location\x12>\n\x0eprocesses_list\x18\x02 \x03(\x0b\x32&.communication_commandes.State.Process\x12\x15\n\rdelivery_time\x18\x03 \x01(\x02\x1a\xcf\x01\n\x08Location\x12L\n\rlocation_type\x18\x01 \x01(\x0e\x32\x35.communication_commandes.State.Location.Location_Type\x12\x11\n\tparent_id\x18\x02 \x01(\x05\"b\n\rLocation_Type\x12\t\n\x05ROBOT\x10\x00\x12\x0b\n\x07\x41RRIVAL\x10\x01\x12\x11\n\rMACHINE_INPUT\x10\x02\x12\x12\n\x0eMACHINE_INSIDE\x10\x03\x12\x12\n\x0eMACHINE_OUTPUT\x10\x04\x1a\x37\n\x07Process\x12\x12\n\nprocess_id\x18\x01 \x01(\x05\x12\x18\n\x10process_duration\x18\x02 \x01(\x02\"\xdd\x04\n\x17\x45nvironment_Description\x12J\n\x08machines\x18\x01 \x03(\x0b\x32\x38.communication_commandes.Environment_Description.Machine\x12W\n\x0c\x61rrival_area\x18\x02 \x01(\x0b\x32\x41.communication_commandes.Environment_Description.Area_Description\x12X\n\rdelivery_area\x18\x03 \x01(\x0b\x32\x41.communication_commandes.Environment_Description.Area_Description\x1a\xf9\x01\n\x07Machine\x12U\n\ninput_area\x18\x01 \x01(\x0b\x32\x41.communication_commandes.Environment_Description.Area_Description\x12V\n\x0boutput_area\x18\x02 \x01(\x0b\x32\x41.communication_commandes.Environment_Description.Area_Description\x12\x12\n\ninput_size\x18\x03 \x01(\x05\x12\x13\n\x0boutput_size\x18\x04 \x01(\x05\x12\x16\n\x0eprocesses_list\x18\x05 \x03(\x05\x1aG\n\x10\x41rea_Description\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02'
)



_COMMAND_COMMAND_TYPES = _descriptor.EnumDescriptor(
  name='Command_types',
  full_name='communication_commandes.Command.Command_types',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GOTO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PICKUP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOTO_PATH', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DROP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=573,
  serialized_end=635,
)
_sym_db.RegisterEnumDescriptor(_COMMAND_COMMAND_TYPES)

_STATE_LOCATION_LOCATION_TYPE = _descriptor.EnumDescriptor(
  name='Location_Type',
  full_name='communication_commandes.State.Location.Location_Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROBOT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ARRIVAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MACHINE_INPUT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MACHINE_INSIDE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MACHINE_OUTPUT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1108,
  serialized_end=1206,
)
_sym_db.RegisterEnumDescriptor(_STATE_LOCATION_LOCATION_TYPE)


_COMMAND_PICKUP_DROP_PARAMETERS = _descriptor.Descriptor(
  name='Pickup_Drop_Parameters',
  full_name='communication_commandes.Command.Pickup_Drop_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stand_id', full_name='communication_commandes.Command.Pickup_Drop_Parameters.stand_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=398,
  serialized_end=440,
)

_COMMAND_GOTO_PARAMETERS = _descriptor.Descriptor(
  name='Goto_Parameters',
  full_name='communication_commandes.Command.Goto_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dir', full_name='communication_commandes.Command.Goto_Parameters.dir', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='communication_commandes.Command.Goto_Parameters.speed', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='communication_commandes.Command.Goto_Parameters.time', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=442,
  serialized_end=501,
)

_COMMAND_GOTO_PATH_PARAMETERS = _descriptor.Descriptor(
  name='Goto_Path_Parameters',
  full_name='communication_commandes.Command.Goto_Path_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='destination_x', full_name='communication_commandes.Command.Goto_Path_Parameters.destination_x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination_y', full_name='communication_commandes.Command.Goto_Path_Parameters.destination_y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=571,
)

_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='communication_commandes.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_name', full_name='communication_commandes.Command.command_name', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='communication_commandes.Command.robot_id', index=1,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pickup_drop_parameters', full_name='communication_commandes.Command.pickup_drop_parameters', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='goto_parameters', full_name='communication_commandes.Command.goto_parameters', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='goto_path_parameters', full_name='communication_commandes.Command.goto_path_parameters', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COMMAND_PICKUP_DROP_PARAMETERS, _COMMAND_GOTO_PARAMETERS, _COMMAND_GOTO_PATH_PARAMETERS, ],
  enum_types=[
    _COMMAND_COMMAND_TYPES,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='parameters', full_name='communication_commandes.Command.parameters',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=44,
  serialized_end=649,
)


_STATE_ROBOT = _descriptor.Descriptor(
  name='Robot',
  full_name='communication_commandes.State.Robot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='communication_commandes.State.Robot.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='communication_commandes.State.Robot.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery', full_name='communication_commandes.State.Robot.battery', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_moving', full_name='communication_commandes.State.Robot.is_moving', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=773,
  serialized_end=838,
)

_STATE_PACKAGE = _descriptor.Descriptor(
  name='Package',
  full_name='communication_commandes.State.Package',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='communication_commandes.State.Package.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='processes_list', full_name='communication_commandes.State.Package.processes_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delivery_time', full_name='communication_commandes.State.Package.delivery_time', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=841,
  serialized_end=996,
)

_STATE_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='communication_commandes.State.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='location_type', full_name='communication_commandes.State.Location.location_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='communication_commandes.State.Location.parent_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATE_LOCATION_LOCATION_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=999,
  serialized_end=1206,
)

_STATE_PROCESS = _descriptor.Descriptor(
  name='Process',
  full_name='communication_commandes.State.Process',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='process_id', full_name='communication_commandes.State.Process.process_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='process_duration', full_name='communication_commandes.State.Process.process_duration', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1208,
  serialized_end=1263,
)

_STATE = _descriptor.Descriptor(
  name='State',
  full_name='communication_commandes.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='robots', full_name='communication_commandes.State.robots', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='packages', full_name='communication_commandes.State.packages', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STATE_ROBOT, _STATE_PACKAGE, _STATE_LOCATION, _STATE_PROCESS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=652,
  serialized_end=1263,
)


_ENVIRONMENT_DESCRIPTION_MACHINE = _descriptor.Descriptor(
  name='Machine',
  full_name='communication_commandes.Environment_Description.Machine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_area', full_name='communication_commandes.Environment_Description.Machine.input_area', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_area', full_name='communication_commandes.Environment_Description.Machine.output_area', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input_size', full_name='communication_commandes.Environment_Description.Machine.input_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_size', full_name='communication_commandes.Environment_Description.Machine.output_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='processes_list', full_name='communication_commandes.Environment_Description.Machine.processes_list', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1549,
  serialized_end=1798,
)

_ENVIRONMENT_DESCRIPTION_AREA_DESCRIPTION = _descriptor.Descriptor(
  name='Area_Description',
  full_name='communication_commandes.Environment_Description.Area_Description',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='communication_commandes.Environment_Description.Area_Description.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='communication_commandes.Environment_Description.Area_Description.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='communication_commandes.Environment_Description.Area_Description.width', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='communication_commandes.Environment_Description.Area_Description.height', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1800,
  serialized_end=1871,
)

_ENVIRONMENT_DESCRIPTION = _descriptor.Descriptor(
  name='Environment_Description',
  full_name='communication_commandes.Environment_Description',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machines', full_name='communication_commandes.Environment_Description.machines', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arrival_area', full_name='communication_commandes.Environment_Description.arrival_area', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delivery_area', full_name='communication_commandes.Environment_Description.delivery_area', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ENVIRONMENT_DESCRIPTION_MACHINE, _ENVIRONMENT_DESCRIPTION_AREA_DESCRIPTION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1266,
  serialized_end=1871,
)

_COMMAND_PICKUP_DROP_PARAMETERS.containing_type = _COMMAND
_COMMAND_GOTO_PARAMETERS.containing_type = _COMMAND
_COMMAND_GOTO_PATH_PARAMETERS.containing_type = _COMMAND
_COMMAND.fields_by_name['command_name'].enum_type = _COMMAND_COMMAND_TYPES
_COMMAND.fields_by_name['pickup_drop_parameters'].message_type = _COMMAND_PICKUP_DROP_PARAMETERS
_COMMAND.fields_by_name['goto_parameters'].message_type = _COMMAND_GOTO_PARAMETERS
_COMMAND.fields_by_name['goto_path_parameters'].message_type = _COMMAND_GOTO_PATH_PARAMETERS
_COMMAND_COMMAND_TYPES.containing_type = _COMMAND
_COMMAND.oneofs_by_name['parameters'].fields.append(
  _COMMAND.fields_by_name['pickup_drop_parameters'])
_COMMAND.fields_by_name['pickup_drop_parameters'].containing_oneof = _COMMAND.oneofs_by_name['parameters']
_COMMAND.oneofs_by_name['parameters'].fields.append(
  _COMMAND.fields_by_name['goto_parameters'])
_COMMAND.fields_by_name['goto_parameters'].containing_oneof = _COMMAND.oneofs_by_name['parameters']
_COMMAND.oneofs_by_name['parameters'].fields.append(
  _COMMAND.fields_by_name['goto_path_parameters'])
_COMMAND.fields_by_name['goto_path_parameters'].containing_oneof = _COMMAND.oneofs_by_name['parameters']
_STATE_ROBOT.containing_type = _STATE
_STATE_PACKAGE.fields_by_name['location'].message_type = _STATE_LOCATION
_STATE_PACKAGE.fields_by_name['processes_list'].message_type = _STATE_PROCESS
_STATE_PACKAGE.containing_type = _STATE
_STATE_LOCATION.fields_by_name['location_type'].enum_type = _STATE_LOCATION_LOCATION_TYPE
_STATE_LOCATION.containing_type = _STATE
_STATE_LOCATION_LOCATION_TYPE.containing_type = _STATE_LOCATION
_STATE_PROCESS.containing_type = _STATE
_STATE.fields_by_name['robots'].message_type = _STATE_ROBOT
_STATE.fields_by_name['packages'].message_type = _STATE_PACKAGE
_ENVIRONMENT_DESCRIPTION_MACHINE.fields_by_name['input_area'].message_type = _ENVIRONMENT_DESCRIPTION_AREA_DESCRIPTION
_ENVIRONMENT_DESCRIPTION_MACHINE.fields_by_name['output_area'].message_type = _ENVIRONMENT_DESCRIPTION_AREA_DESCRIPTION
_ENVIRONMENT_DESCRIPTION_MACHINE.containing_type = _ENVIRONMENT_DESCRIPTION
_ENVIRONMENT_DESCRIPTION_AREA_DESCRIPTION.containing_type = _ENVIRONMENT_DESCRIPTION
_ENVIRONMENT_DESCRIPTION.fields_by_name['machines'].message_type = _ENVIRONMENT_DESCRIPTION_MACHINE
_ENVIRONMENT_DESCRIPTION.fields_by_name['arrival_area'].message_type = _ENVIRONMENT_DESCRIPTION_AREA_DESCRIPTION
_ENVIRONMENT_DESCRIPTION.fields_by_name['delivery_area'].message_type = _ENVIRONMENT_DESCRIPTION_AREA_DESCRIPTION
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['Environment_Description'] = _ENVIRONMENT_DESCRIPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {

  'Pickup_Drop_Parameters' : _reflection.GeneratedProtocolMessageType('Pickup_Drop_Parameters', (_message.Message,), {
    'DESCRIPTOR' : _COMMAND_PICKUP_DROP_PARAMETERS,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:communication_commandes.Command.Pickup_Drop_Parameters)
    })
  ,

  'Goto_Parameters' : _reflection.GeneratedProtocolMessageType('Goto_Parameters', (_message.Message,), {
    'DESCRIPTOR' : _COMMAND_GOTO_PARAMETERS,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:communication_commandes.Command.Goto_Parameters)
    })
  ,

  'Goto_Path_Parameters' : _reflection.GeneratedProtocolMessageType('Goto_Path_Parameters', (_message.Message,), {
    'DESCRIPTOR' : _COMMAND_GOTO_PATH_PARAMETERS,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:communication_commandes.Command.Goto_Path_Parameters)
    })
  ,
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:communication_commandes.Command)
  })
_sym_db.RegisterMessage(Command)
_sym_db.RegisterMessage(Command.Pickup_Drop_Parameters)
_sym_db.RegisterMessage(Command.Goto_Parameters)
_sym_db.RegisterMessage(Command.Goto_Path_Parameters)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {

  'Robot' : _reflection.GeneratedProtocolMessageType('Robot', (_message.Message,), {
    'DESCRIPTOR' : _STATE_ROBOT,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:communication_commandes.State.Robot)
    })
  ,

  'Package' : _reflection.GeneratedProtocolMessageType('Package', (_message.Message,), {
    'DESCRIPTOR' : _STATE_PACKAGE,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:communication_commandes.State.Package)
    })
  ,

  'Location' : _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
    'DESCRIPTOR' : _STATE_LOCATION,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:communication_commandes.State.Location)
    })
  ,

  'Process' : _reflection.GeneratedProtocolMessageType('Process', (_message.Message,), {
    'DESCRIPTOR' : _STATE_PROCESS,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:communication_commandes.State.Process)
    })
  ,
  'DESCRIPTOR' : _STATE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:communication_commandes.State)
  })
_sym_db.RegisterMessage(State)
_sym_db.RegisterMessage(State.Robot)
_sym_db.RegisterMessage(State.Package)
_sym_db.RegisterMessage(State.Location)
_sym_db.RegisterMessage(State.Process)

Environment_Description = _reflection.GeneratedProtocolMessageType('Environment_Description', (_message.Message,), {

  'Machine' : _reflection.GeneratedProtocolMessageType('Machine', (_message.Message,), {
    'DESCRIPTOR' : _ENVIRONMENT_DESCRIPTION_MACHINE,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:communication_commandes.Environment_Description.Machine)
    })
  ,

  'Area_Description' : _reflection.GeneratedProtocolMessageType('Area_Description', (_message.Message,), {
    'DESCRIPTOR' : _ENVIRONMENT_DESCRIPTION_AREA_DESCRIPTION,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:communication_commandes.Environment_Description.Area_Description)
    })
  ,
  'DESCRIPTOR' : _ENVIRONMENT_DESCRIPTION,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:communication_commandes.Environment_Description)
  })
_sym_db.RegisterMessage(Environment_Description)
_sym_db.RegisterMessage(Environment_Description.Machine)
_sym_db.RegisterMessage(Environment_Description.Area_Description)


# @@protoc_insertion_point(module_scope)
