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
    print("Server is running on port 50051...")
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print("Shutting down server...")
        server.stop(0)


if __name__ == "__main__":
    serve()