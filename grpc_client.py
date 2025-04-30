import grpc
import game_engine_pb2_grpc


def main():
    try:
        channel = grpc.insecure_channel("localhost:50051")
        stub = game_engine_pb2_grpc.GameEngineServiceStub(channel)
        print("Connected to the gRPC server.")
    except Exception as e:
        print("Failed to connect:", e)


if __name__ == "__main__":
    main()
