import logging
import asyncio

import grpc

from definitions_pb2 import PublicRequest
from definitions_pb2_grpc import PublicServiceStub


async def do_request():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = PublicServiceStub(channel)
        request = PublicRequest(message="Hi.")
        response = await stub.DoPublicRequest(request)
        logging.info("response")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(do_request())
