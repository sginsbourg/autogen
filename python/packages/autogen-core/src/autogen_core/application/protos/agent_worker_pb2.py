# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent_worker.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import cloudevent_pb2 as cloudevent__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61gent_worker.proto\x12\x06\x61gents\x1a\x10\x63loudevent.proto\x1a\x19google/protobuf/any.proto\"$\n\x07\x41gentId\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"<\n\x18RegisterAgentTypeRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"^\n\x19RegisterAgentTypeResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x12\n\x05\x65rror\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_error\":\n\x10TypeSubscription\x12\x12\n\ntopic_type\x18\x01 \x01(\t\x12\x12\n\nagent_type\x18\x02 \x01(\t\"G\n\x16TypePrefixSubscription\x12\x19\n\x11topic_type_prefix\x18\x01 \x01(\t\x12\x12\n\nagent_type\x18\x02 \x01(\t\"\x96\x01\n\x0cSubscription\x12\x34\n\x10typeSubscription\x18\x01 \x01(\x0b\x32\x18.agents.TypeSubscriptionH\x00\x12@\n\x16typePrefixSubscription\x18\x02 \x01(\x0b\x32\x1e.agents.TypePrefixSubscriptionH\x00\x42\x0e\n\x0csubscription\"X\n\x16\x41\x64\x64SubscriptionRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12*\n\x0csubscription\x18\x02 \x01(\x0b\x32\x14.agents.Subscription\"\\\n\x17\x41\x64\x64SubscriptionResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x12\n\x05\x65rror\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_error\"\x9d\x01\n\nAgentState\x12!\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x0f.agents.AgentId\x12\x0c\n\x04\x65Tag\x18\x02 \x01(\t\x12\x15\n\x0b\x62inary_data\x18\x03 \x01(\x0cH\x00\x12\x13\n\ttext_data\x18\x04 \x01(\tH\x00\x12*\n\nproto_data\x18\x05 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x06\n\x04\x64\x61ta\"j\n\x10GetStateResponse\x12\'\n\x0b\x61gent_state\x18\x01 \x01(\x0b\x32\x12.agents.AgentState\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x12\n\x05\x65rror\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_error\"B\n\x11SaveStateResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_error\"\xd6\x02\n\x07Message\x12,\n\ncloudEvent\x18\x01 \x01(\x0b\x32\x16.cloudevent.CloudEventH\x00\x12\x44\n\x18registerAgentTypeRequest\x18\x02 \x01(\x0b\x32 .agents.RegisterAgentTypeRequestH\x00\x12\x46\n\x19registerAgentTypeResponse\x18\x03 \x01(\x0b\x32!.agents.RegisterAgentTypeResponseH\x00\x12@\n\x16\x61\x64\x64SubscriptionRequest\x18\x04 \x01(\x0b\x32\x1e.agents.AddSubscriptionRequestH\x00\x12\x42\n\x17\x61\x64\x64SubscriptionResponse\x18\x05 \x01(\x0b\x32\x1f.agents.AddSubscriptionResponseH\x00\x42\t\n\x07message2\xb2\x01\n\x08\x41gentRpc\x12\x33\n\x0bOpenChannel\x12\x0f.agents.Message\x1a\x0f.agents.Message(\x01\x30\x01\x12\x35\n\x08GetState\x12\x0f.agents.AgentId\x1a\x18.agents.GetStateResponse\x12:\n\tSaveState\x12\x12.agents.AgentState\x1a\x19.agents.SaveStateResponseB!\xaa\x02\x1eMicrosoft.AutoGen.Abstractionsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'agent_worker_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\036Microsoft.AutoGen.Abstractions'
  _globals['_AGENTID']._serialized_start=75
  _globals['_AGENTID']._serialized_end=111
  _globals['_REGISTERAGENTTYPEREQUEST']._serialized_start=113
  _globals['_REGISTERAGENTTYPEREQUEST']._serialized_end=173
  _globals['_REGISTERAGENTTYPERESPONSE']._serialized_start=175
  _globals['_REGISTERAGENTTYPERESPONSE']._serialized_end=269
  _globals['_TYPESUBSCRIPTION']._serialized_start=271
  _globals['_TYPESUBSCRIPTION']._serialized_end=329
  _globals['_TYPEPREFIXSUBSCRIPTION']._serialized_start=331
  _globals['_TYPEPREFIXSUBSCRIPTION']._serialized_end=402
  _globals['_SUBSCRIPTION']._serialized_start=405
  _globals['_SUBSCRIPTION']._serialized_end=555
  _globals['_ADDSUBSCRIPTIONREQUEST']._serialized_start=557
  _globals['_ADDSUBSCRIPTIONREQUEST']._serialized_end=645
  _globals['_ADDSUBSCRIPTIONRESPONSE']._serialized_start=647
  _globals['_ADDSUBSCRIPTIONRESPONSE']._serialized_end=739
  _globals['_AGENTSTATE']._serialized_start=742
  _globals['_AGENTSTATE']._serialized_end=899
  _globals['_GETSTATERESPONSE']._serialized_start=901
  _globals['_GETSTATERESPONSE']._serialized_end=1007
  _globals['_SAVESTATERESPONSE']._serialized_start=1009
  _globals['_SAVESTATERESPONSE']._serialized_end=1075
  _globals['_MESSAGE']._serialized_start=1078
  _globals['_MESSAGE']._serialized_end=1420
  _globals['_AGENTRPC']._serialized_start=1423
  _globals['_AGENTRPC']._serialized_end=1601
# @@protoc_insertion_point(module_scope)
