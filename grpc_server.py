import grpc
from concurrent import futures
import time
import sqlite3

import game_engine_pb2
import game_engine_pb2_grpc


class GameEngineServicer(game_engine_pb2_grpc.GameEngineServiceServicer):
    def __init__(self):
        self.conn = sqlite3.connect("", check_same_thread=False)
        self.cursor = self.conn.cursor()
        print("Database connection established.")

    def Move(self, request, context):
        return game_engine_pb2.MoveResponse(
            success=False,
            message="Move not implemented",
            new_x=0,
            new_y=0
        )

    def GetView(self, request, context):
        return game_engine_pb2.ViewResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    game_engine_pb2_grpc.add_GameEngineServiceServicer_to_server(GameEngineServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
    print("Server is running on port 50051...")

if __name__ == "__main__":
    serve()