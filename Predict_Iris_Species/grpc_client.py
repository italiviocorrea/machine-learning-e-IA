# Cria o cliente gRPC

# Imports
import grpc
import argparse

# Import do módulo gerado a partir da compilação do arquivo proto
import iris_pb2

# Import to grcp_server
import grpc_server


# Executa o cliente
def run(host, port):
    # Define a classe de previsão
    stub = grpc_server.IrisPredictor()

    # Prepara uma request
    request = iris_pb2.IrisPredictRequest(
        sepal_length=5.0,
        sepal_width=4.6,
        petal_length=5.3,
        petal_width=1.25
    )

    # Envia a request e obtém a previsão
    response = stub.PredictIrisSpecies(request)
    print("Número da previsão da classe prevista para a flor: " + str(response.species))


# Executa
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='Nome da máquina', default='localhost', type=str)
    parser.add_argument('--port', help='Porta', default=50052, type=int)
    args = parser.parse_args()
    run(args.host, args.port)
