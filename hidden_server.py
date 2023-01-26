import logging
import asyncio

import grpc

from definitions_pb2 import HiddenResponse
from definitions_pb2_grpc import HiddenServiceServicer, add_HiddenServiceServicer_to_server

class HiddenService(HiddenServiceServicer):
    async def DoHiddenRequest(self, request, context):
        return HiddenResponse(message="Hello from hidden.")


async def serve():
    server = grpc.aio.server()
    add_HiddenServiceServicer_to_server(HiddenService(), server)
    server.add_insecure_port("[::]:50052")
    logging.info("Starting hidden service.")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())