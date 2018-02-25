# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import api_pb2 as api__pb2


class ApiStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetMinerInfo = channel.unary_unary(
        '/api.Api/GetMinerInfo',
        request_serializer=api__pb2.MinerRequest.SerializeToString,
        response_deserializer=api__pb2.MinerInfo.FromString,
        )
    self.GetPoolStatsInfo = channel.unary_unary(
        '/api.Api/GetPoolStatsInfo',
        request_serializer=api__pb2.Void.SerializeToString,
        response_deserializer=api__pb2.PoolStatsInfo.FromString,
        )
    self.GetBlockInfo = channel.unary_unary(
        '/api.Api/GetBlockInfo',
        request_serializer=api__pb2.Void.SerializeToString,
        response_deserializer=api__pb2.BlockInfo.FromString,
        )


class ApiServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetMinerInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPoolStatsInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlockInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetMinerInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetMinerInfo,
          request_deserializer=api__pb2.MinerRequest.FromString,
          response_serializer=api__pb2.MinerInfo.SerializeToString,
      ),
      'GetPoolStatsInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetPoolStatsInfo,
          request_deserializer=api__pb2.Void.FromString,
          response_serializer=api__pb2.PoolStatsInfo.SerializeToString,
      ),
      'GetBlockInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlockInfo,
          request_deserializer=api__pb2.Void.FromString,
          response_serializer=api__pb2.BlockInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.Api', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
