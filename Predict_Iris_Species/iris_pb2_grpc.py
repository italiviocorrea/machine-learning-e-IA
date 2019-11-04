# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import iris_pb2 as iris__pb2


class IrisPredictorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PredictIrisSpecies = channel.unary_unary(
        '/ml.IrisPredictor/PredictIrisSpecies',
        request_serializer=iris__pb2.IrisPredictRequest.SerializeToString,
        response_deserializer=iris__pb2.IrisPredictReply.FromString,
        )


class IrisPredictorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def PredictIrisSpecies(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IrisPredictorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PredictIrisSpecies': grpc.unary_unary_rpc_method_handler(
          servicer.PredictIrisSpecies,
          request_deserializer=iris__pb2.IrisPredictRequest.FromString,
          response_serializer=iris__pb2.IrisPredictReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ml.IrisPredictor', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
