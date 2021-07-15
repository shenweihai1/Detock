# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/transaction.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/transaction.proto',
  package='slog',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17proto/transaction.proto\x12\x04slog\"1\n\x0eMasterMetadata\x12\x0e\n\x06master\x18\x01 \x01(\r\x12\x0f\n\x07\x63ounter\x18\x02 \x01(\r\"\x81\x01\n\nValueEntry\x12\r\n\x05value\x18\x01 \x01(\x0c\x12\x11\n\tnew_value\x18\x02 \x01(\x0c\x12\x1b\n\x04type\x18\x03 \x01(\x0e\x32\r.slog.KeyType\x12(\n\x08metadata\x18\x04 \x01(\x0b\x32\x14.slog.MasterMetadataH\x00\x42\n\n\x08optional\"C\n\rKeyValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12%\n\x0bvalue_entry\x18\x02 \x01(\x0b\x32\x10.slog.ValueEntry\"j\n\x14TransactionEventInfo\x12%\n\x05\x65vent\x18\x01 \x01(\x0e\x32\x16.slog.TransactionEvent\x12\x0c\n\x04time\x18\x02 \x01(\x03\x12\x0f\n\x07machine\x18\x03 \x01(\x05\x12\x0c\n\x04home\x18\x04 \x01(\x05\"\x8d\x03\n\x13TransactionInternal\x12\n\n\x02id\x18\x01 \x01(\x04\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.slog.TransactionType\x12\x0c\n\x04home\x18\x03 \x01(\x05\x12\x1b\n\x13\x63oordinating_server\x18\x04 \x01(\r\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\x12\x1b\n\x13involved_partitions\x18\x06 \x03(\r\x12\x19\n\x11\x61\x63tive_partitions\x18\x07 \x03(\r\x12\x19\n\x11involved_replicas\x18\x08 \x03(\r\x12*\n\x06\x65vents\x18\t \x03(\x0b\x32\x1a.slog.TransactionEventInfo\x12\'\n\x1fmh_depart_from_coordinator_time\x18\n \x01(\x03\x12\x1e\n\x16mh_arrive_at_home_time\x18\x0b \x01(\x03\x12!\n\x19mh_enter_local_batch_time\x18\x0c \x01(\x03\x12\x1c\n\x14global_log_positions\x18\r \x03(\x03\"H\n\x11RemasterProcedure\x12\x12\n\nnew_master\x18\x01 \x01(\r\x12\x1f\n\x17is_new_master_lock_only\x18\x02 \x01(\x08\"\x19\n\tProcedure\x12\x0c\n\x04\x61rgs\x18\x01 \x03(\x0c\"1\n\nProcedures\x12#\n\nprocedures\x18\x01 \x03(\x0b\x32\x0f.slog.Procedure\"\x8c\x02\n\x0bTransaction\x12+\n\x08internal\x18\x01 \x01(\x0b\x32\x19.slog.TransactionInternal\x12 \n\x04\x63ode\x18\x02 \x01(\x0b\x32\x10.slog.ProceduresH\x00\x12+\n\x08remaster\x18\x03 \x01(\x0b\x32\x17.slog.RemasterProcedureH\x00\x12!\n\x04keys\x18\x04 \x03(\x0b\x32\x13.slog.KeyValueEntry\x12\x14\n\x0c\x64\x65leted_keys\x18\x05 \x03(\x0c\x12\'\n\x06status\x18\x06 \x01(\x0e\x32\x17.slog.TransactionStatus\x12\x14\n\x0c\x61\x62ort_reason\x18\x07 \x01(\tB\t\n\x07program*L\n\x0fTransactionType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bSINGLE_HOME\x10\x01\x12\x1b\n\x17MULTI_HOME_OR_LOCK_ONLY\x10\x02*@\n\x11TransactionStatus\x12\x0f\n\x0bNOT_STARTED\x10\x00\x12\r\n\tCOMMITTED\x10\x01\x12\x0b\n\x07\x41\x42ORTED\x10\x02*\x1e\n\x07KeyType\x12\x08\n\x04READ\x10\x00\x12\t\n\x05WRITE\x10\x01*\xc1\x06\n\x10TransactionEvent\x12\x07\n\x03\x41LL\x10\x00\x12\x10\n\x0c\x45NTER_SERVER\x10\x01\x12\x1c\n\x18\x45XIT_SERVER_TO_FORWARDER\x10\x02\x12\x13\n\x0f\x45NTER_FORWARDER\x10\x03\x12\x1f\n\x1b\x45XIT_FORWARDER_TO_SEQUENCER\x10\x04\x12(\n$EXIT_FORWARDER_TO_MULTI_HOME_ORDERER\x10\x05\x12\x1c\n\x18\x45NTER_MULTI_HOME_ORDERER\x10\x06\x12%\n!ENTER_MULTI_HOME_ORDERER_IN_BATCH\x10\x07\x12$\n EXIT_MULTI_HOME_ORDERER_IN_BATCH\x10\x08\x12\x1b\n\x17\x45XIT_MULTI_HOME_ORDERER\x10\t\x12\x13\n\x0f\x45NTER_SEQUENCER\x10\n\x12.\n*EXPECTED_WAIT_TIME_UNTIL_ENTER_LOCAL_BATCH\x10\x0b\x12\x15\n\x11\x45NTER_LOCAL_BATCH\x10\x0c\x12\x1c\n\x18\x45NTER_SEQUENCER_IN_BATCH\x10\r\x12\x1b\n\x17\x45XIT_SEQUENCER_IN_BATCH\x10\x0e\x12\x1e\n\x1a\x45NTER_INTERLEAVER_IN_BATCH\x10\x0f\x12\x14\n\x10\x45XIT_INTERLEAVER\x10\x10\x12\x13\n\x0f\x45NTER_SCHEDULER\x10\x11\x12\x16\n\x12\x45NTER_SCHEDULER_LO\x10\x12\x12\x16\n\x12\x45NTER_LOCK_MANAGER\x10\x13\x12\x15\n\x11\x44\x45\x41\x44LOCK_DETECTED\x10\x14\x12\x0e\n\nDISPATCHED\x10\x15\x12\x13\n\x0f\x44ISPATCHED_FAST\x10\x16\x12\x13\n\x0f\x44ISPATCHED_SLOW\x10\x17\x12\x1e\n\x1a\x44ISPATCHED_SLOW_DEADLOCKED\x10\x18\x12\x10\n\x0c\x45NTER_WORKER\x10\x19\x12\x14\n\x10GOT_REMOTE_READS\x10\x1a\x12\x1f\n\x1bGOT_REMOTE_READS_DEADLOCKED\x10\x1b\x12\x0f\n\x0b\x45XIT_WORKER\x10\x1c\x12\x14\n\x10RETURN_TO_SERVER\x10\x1d\x12\x19\n\x15\x45XIT_SERVER_TO_CLIENT\x10\x1e\x62\x06proto3'
)

_TRANSACTIONTYPE = _descriptor.EnumDescriptor(
  name='TransactionType',
  full_name='slog.TransactionType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SINGLE_HOME', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTI_HOME_OR_LOCK_ONLY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1216,
  serialized_end=1292,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONTYPE)

TransactionType = enum_type_wrapper.EnumTypeWrapper(_TRANSACTIONTYPE)
_TRANSACTIONSTATUS = _descriptor.EnumDescriptor(
  name='TransactionStatus',
  full_name='slog.TransactionStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_STARTED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMMITTED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ABORTED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1294,
  serialized_end=1358,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONSTATUS)

TransactionStatus = enum_type_wrapper.EnumTypeWrapper(_TRANSACTIONSTATUS)
_KEYTYPE = _descriptor.EnumDescriptor(
  name='KeyType',
  full_name='slog.KeyType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READ', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WRITE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1360,
  serialized_end=1390,
)
_sym_db.RegisterEnumDescriptor(_KEYTYPE)

KeyType = enum_type_wrapper.EnumTypeWrapper(_KEYTYPE)
_TRANSACTIONEVENT = _descriptor.EnumDescriptor(
  name='TransactionEvent',
  full_name='slog.TransactionEvent',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTER_SERVER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXIT_SERVER_TO_FORWARDER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTER_FORWARDER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXIT_FORWARDER_TO_SEQUENCER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXIT_FORWARDER_TO_MULTI_HOME_ORDERER', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTER_MULTI_HOME_ORDERER', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTER_MULTI_HOME_ORDERER_IN_BATCH', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXIT_MULTI_HOME_ORDERER_IN_BATCH', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXIT_MULTI_HOME_ORDERER', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTER_SEQUENCER', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXPECTED_WAIT_TIME_UNTIL_ENTER_LOCAL_BATCH', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTER_LOCAL_BATCH', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTER_SEQUENCER_IN_BATCH', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXIT_SEQUENCER_IN_BATCH', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTER_INTERLEAVER_IN_BATCH', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXIT_INTERLEAVER', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTER_SCHEDULER', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTER_SCHEDULER_LO', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTER_LOCK_MANAGER', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEADLOCK_DETECTED', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISPATCHED', index=21, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISPATCHED_FAST', index=22, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISPATCHED_SLOW', index=23, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISPATCHED_SLOW_DEADLOCKED', index=24, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTER_WORKER', index=25, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOT_REMOTE_READS', index=26, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOT_REMOTE_READS_DEADLOCKED', index=27, number=27,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXIT_WORKER', index=28, number=28,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RETURN_TO_SERVER', index=29, number=29,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXIT_SERVER_TO_CLIENT', index=30, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1393,
  serialized_end=2226,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONEVENT)

TransactionEvent = enum_type_wrapper.EnumTypeWrapper(_TRANSACTIONEVENT)
UNKNOWN = 0
SINGLE_HOME = 1
MULTI_HOME_OR_LOCK_ONLY = 2
NOT_STARTED = 0
COMMITTED = 1
ABORTED = 2
READ = 0
WRITE = 1
ALL = 0
ENTER_SERVER = 1
EXIT_SERVER_TO_FORWARDER = 2
ENTER_FORWARDER = 3
EXIT_FORWARDER_TO_SEQUENCER = 4
EXIT_FORWARDER_TO_MULTI_HOME_ORDERER = 5
ENTER_MULTI_HOME_ORDERER = 6
ENTER_MULTI_HOME_ORDERER_IN_BATCH = 7
EXIT_MULTI_HOME_ORDERER_IN_BATCH = 8
EXIT_MULTI_HOME_ORDERER = 9
ENTER_SEQUENCER = 10
EXPECTED_WAIT_TIME_UNTIL_ENTER_LOCAL_BATCH = 11
ENTER_LOCAL_BATCH = 12
ENTER_SEQUENCER_IN_BATCH = 13
EXIT_SEQUENCER_IN_BATCH = 14
ENTER_INTERLEAVER_IN_BATCH = 15
EXIT_INTERLEAVER = 16
ENTER_SCHEDULER = 17
ENTER_SCHEDULER_LO = 18
ENTER_LOCK_MANAGER = 19
DEADLOCK_DETECTED = 20
DISPATCHED = 21
DISPATCHED_FAST = 22
DISPATCHED_SLOW = 23
DISPATCHED_SLOW_DEADLOCKED = 24
ENTER_WORKER = 25
GOT_REMOTE_READS = 26
GOT_REMOTE_READS_DEADLOCKED = 27
EXIT_WORKER = 28
RETURN_TO_SERVER = 29
EXIT_SERVER_TO_CLIENT = 30



_MASTERMETADATA = _descriptor.Descriptor(
  name='MasterMetadata',
  full_name='slog.MasterMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='master', full_name='slog.MasterMetadata.master', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counter', full_name='slog.MasterMetadata.counter', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=82,
)


_VALUEENTRY = _descriptor.Descriptor(
  name='ValueEntry',
  full_name='slog.ValueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='slog.ValueEntry.value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_value', full_name='slog.ValueEntry.new_value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='slog.ValueEntry.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='slog.ValueEntry.metadata', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='optional', full_name='slog.ValueEntry.optional',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=85,
  serialized_end=214,
)


_KEYVALUEENTRY = _descriptor.Descriptor(
  name='KeyValueEntry',
  full_name='slog.KeyValueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='slog.KeyValueEntry.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value_entry', full_name='slog.KeyValueEntry.value_entry', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=283,
)


_TRANSACTIONEVENTINFO = _descriptor.Descriptor(
  name='TransactionEventInfo',
  full_name='slog.TransactionEventInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='slog.TransactionEventInfo.event', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='slog.TransactionEventInfo.time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='machine', full_name='slog.TransactionEventInfo.machine', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='home', full_name='slog.TransactionEventInfo.home', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=391,
)


_TRANSACTIONINTERNAL = _descriptor.Descriptor(
  name='TransactionInternal',
  full_name='slog.TransactionInternal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='slog.TransactionInternal.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='slog.TransactionInternal.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='home', full_name='slog.TransactionInternal.home', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coordinating_server', full_name='slog.TransactionInternal.coordinating_server', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='slog.TransactionInternal.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='involved_partitions', full_name='slog.TransactionInternal.involved_partitions', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active_partitions', full_name='slog.TransactionInternal.active_partitions', index=6,
      number=7, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='involved_replicas', full_name='slog.TransactionInternal.involved_replicas', index=7,
      number=8, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='events', full_name='slog.TransactionInternal.events', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mh_depart_from_coordinator_time', full_name='slog.TransactionInternal.mh_depart_from_coordinator_time', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mh_arrive_at_home_time', full_name='slog.TransactionInternal.mh_arrive_at_home_time', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mh_enter_local_batch_time', full_name='slog.TransactionInternal.mh_enter_local_batch_time', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='global_log_positions', full_name='slog.TransactionInternal.global_log_positions', index=12,
      number=13, type=3, cpp_type=2, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=791,
)


_REMASTERPROCEDURE = _descriptor.Descriptor(
  name='RemasterProcedure',
  full_name='slog.RemasterProcedure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_master', full_name='slog.RemasterProcedure.new_master', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_new_master_lock_only', full_name='slog.RemasterProcedure.is_new_master_lock_only', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=793,
  serialized_end=865,
)


_PROCEDURE = _descriptor.Descriptor(
  name='Procedure',
  full_name='slog.Procedure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='args', full_name='slog.Procedure.args', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=867,
  serialized_end=892,
)


_PROCEDURES = _descriptor.Descriptor(
  name='Procedures',
  full_name='slog.Procedures',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='procedures', full_name='slog.Procedures.procedures', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=894,
  serialized_end=943,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='slog.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='internal', full_name='slog.Transaction.internal', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='slog.Transaction.code', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remaster', full_name='slog.Transaction.remaster', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keys', full_name='slog.Transaction.keys', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted_keys', full_name='slog.Transaction.deleted_keys', index=4,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='slog.Transaction.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='abort_reason', full_name='slog.Transaction.abort_reason', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='program', full_name='slog.Transaction.program',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=946,
  serialized_end=1214,
)

_VALUEENTRY.fields_by_name['type'].enum_type = _KEYTYPE
_VALUEENTRY.fields_by_name['metadata'].message_type = _MASTERMETADATA
_VALUEENTRY.oneofs_by_name['optional'].fields.append(
  _VALUEENTRY.fields_by_name['metadata'])
_VALUEENTRY.fields_by_name['metadata'].containing_oneof = _VALUEENTRY.oneofs_by_name['optional']
_KEYVALUEENTRY.fields_by_name['value_entry'].message_type = _VALUEENTRY
_TRANSACTIONEVENTINFO.fields_by_name['event'].enum_type = _TRANSACTIONEVENT
_TRANSACTIONINTERNAL.fields_by_name['type'].enum_type = _TRANSACTIONTYPE
_TRANSACTIONINTERNAL.fields_by_name['events'].message_type = _TRANSACTIONEVENTINFO
_PROCEDURES.fields_by_name['procedures'].message_type = _PROCEDURE
_TRANSACTION.fields_by_name['internal'].message_type = _TRANSACTIONINTERNAL
_TRANSACTION.fields_by_name['code'].message_type = _PROCEDURES
_TRANSACTION.fields_by_name['remaster'].message_type = _REMASTERPROCEDURE
_TRANSACTION.fields_by_name['keys'].message_type = _KEYVALUEENTRY
_TRANSACTION.fields_by_name['status'].enum_type = _TRANSACTIONSTATUS
_TRANSACTION.oneofs_by_name['program'].fields.append(
  _TRANSACTION.fields_by_name['code'])
_TRANSACTION.fields_by_name['code'].containing_oneof = _TRANSACTION.oneofs_by_name['program']
_TRANSACTION.oneofs_by_name['program'].fields.append(
  _TRANSACTION.fields_by_name['remaster'])
_TRANSACTION.fields_by_name['remaster'].containing_oneof = _TRANSACTION.oneofs_by_name['program']
DESCRIPTOR.message_types_by_name['MasterMetadata'] = _MASTERMETADATA
DESCRIPTOR.message_types_by_name['ValueEntry'] = _VALUEENTRY
DESCRIPTOR.message_types_by_name['KeyValueEntry'] = _KEYVALUEENTRY
DESCRIPTOR.message_types_by_name['TransactionEventInfo'] = _TRANSACTIONEVENTINFO
DESCRIPTOR.message_types_by_name['TransactionInternal'] = _TRANSACTIONINTERNAL
DESCRIPTOR.message_types_by_name['RemasterProcedure'] = _REMASTERPROCEDURE
DESCRIPTOR.message_types_by_name['Procedure'] = _PROCEDURE
DESCRIPTOR.message_types_by_name['Procedures'] = _PROCEDURES
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.enum_types_by_name['TransactionType'] = _TRANSACTIONTYPE
DESCRIPTOR.enum_types_by_name['TransactionStatus'] = _TRANSACTIONSTATUS
DESCRIPTOR.enum_types_by_name['KeyType'] = _KEYTYPE
DESCRIPTOR.enum_types_by_name['TransactionEvent'] = _TRANSACTIONEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MasterMetadata = _reflection.GeneratedProtocolMessageType('MasterMetadata', (_message.Message,), {
  'DESCRIPTOR' : _MASTERMETADATA,
  '__module__' : 'proto.transaction_pb2'
  # @@protoc_insertion_point(class_scope:slog.MasterMetadata)
  })
_sym_db.RegisterMessage(MasterMetadata)

ValueEntry = _reflection.GeneratedProtocolMessageType('ValueEntry', (_message.Message,), {
  'DESCRIPTOR' : _VALUEENTRY,
  '__module__' : 'proto.transaction_pb2'
  # @@protoc_insertion_point(class_scope:slog.ValueEntry)
  })
_sym_db.RegisterMessage(ValueEntry)

KeyValueEntry = _reflection.GeneratedProtocolMessageType('KeyValueEntry', (_message.Message,), {
  'DESCRIPTOR' : _KEYVALUEENTRY,
  '__module__' : 'proto.transaction_pb2'
  # @@protoc_insertion_point(class_scope:slog.KeyValueEntry)
  })
_sym_db.RegisterMessage(KeyValueEntry)

TransactionEventInfo = _reflection.GeneratedProtocolMessageType('TransactionEventInfo', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONEVENTINFO,
  '__module__' : 'proto.transaction_pb2'
  # @@protoc_insertion_point(class_scope:slog.TransactionEventInfo)
  })
_sym_db.RegisterMessage(TransactionEventInfo)

TransactionInternal = _reflection.GeneratedProtocolMessageType('TransactionInternal', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONINTERNAL,
  '__module__' : 'proto.transaction_pb2'
  # @@protoc_insertion_point(class_scope:slog.TransactionInternal)
  })
_sym_db.RegisterMessage(TransactionInternal)

RemasterProcedure = _reflection.GeneratedProtocolMessageType('RemasterProcedure', (_message.Message,), {
  'DESCRIPTOR' : _REMASTERPROCEDURE,
  '__module__' : 'proto.transaction_pb2'
  # @@protoc_insertion_point(class_scope:slog.RemasterProcedure)
  })
_sym_db.RegisterMessage(RemasterProcedure)

Procedure = _reflection.GeneratedProtocolMessageType('Procedure', (_message.Message,), {
  'DESCRIPTOR' : _PROCEDURE,
  '__module__' : 'proto.transaction_pb2'
  # @@protoc_insertion_point(class_scope:slog.Procedure)
  })
_sym_db.RegisterMessage(Procedure)

Procedures = _reflection.GeneratedProtocolMessageType('Procedures', (_message.Message,), {
  'DESCRIPTOR' : _PROCEDURES,
  '__module__' : 'proto.transaction_pb2'
  # @@protoc_insertion_point(class_scope:slog.Procedures)
  })
_sym_db.RegisterMessage(Procedures)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'proto.transaction_pb2'
  # @@protoc_insertion_point(class_scope:slog.Transaction)
  })
_sym_db.RegisterMessage(Transaction)


# @@protoc_insertion_point(module_scope)
