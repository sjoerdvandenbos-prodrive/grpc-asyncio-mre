import logging
import asyncio

import grpc

from definitions_pb2 import HiddenRequest, PublicResponse
from definitions_pb2_grpc import (
    PublicServiceServicer,
    add_PublicServiceServicer_to_server,
    HiddenServiceStub,
)


class PublicService(PublicServiceServicer):
    async def DoPublicRequest(self, request, context):
        logging.info("Sending request to hidden.")
        async with grpc.aio.insecure_channel("localhost:50052") as channel:
            stub = HiddenServiceStub(channel)
            request = HiddenRequest(message="The client sends their regards.")
            response = await stub.DoHiddenRequest(request)
            logging.info(response)
        return  PublicResponse(message="Hello from public.")


async def serve():
    server = grpc.aio.server()
    add_PublicServiceServicer_to_server(PublicService(), server)
    server.add_insecure_port("[::]:50051")
    logging.info("Starting public service.")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve(), debug=False)
