import grpc
from concurrent import futures
import time

import game_engine_pb2
import game_engine_pb2_grpc


class GameEngineServicer(game_engine_pb2_grpc.GameEngineServiceServicer):
    pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    game_engine_pb2_grpc.add_GameEngineServiceServicer_to_server(GameEngineServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
    print("Server is running on port 50051...")

if __name__ == "__main__":
    serve()