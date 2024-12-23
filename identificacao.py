
import boto3
from botocore.exceptions import BotoCoreError, NoCredentialsError

def detect_celebrities(image_path):
    """Detect celebrities in an image using Amazon Rekognition."""
    try:
        # Inicializa o cliente Rekognition
        rekognition = boto3.client('rekognition')

        # Lê o arquivo de imagem
        with open(image_path, 'rb') as image_file:
            image_bytes = image_file.read()

        # Faz a chamada para o Rekognition
        response = rekognition.recognize_celebrities(Image={'Bytes': image_bytes})

        # Processa a resposta
        celebrities = response.get('CelebrityFaces', [])
        if not celebrities:
            print("Nenhum famoso identificado na imagem.")
        else:
            print("Famosos identificados:")
            for celebrity in celebrities:
                print(f"- Nome: {celebrity['Name']}")
                print(f"  Confiança: {celebrity['MatchConfidence']:.2f}%")
                print(f"  URLs de informações: {celebrity.get('Urls', [])}")

    except FileNotFoundError:
        print("Erro: Arquivo de imagem não encontrado.")
    except NoCredentialsError:
        print("Erro: Credenciais da AWS não configuradas.")
    except BotoCoreError as error:
        print(f"Erro ao chamar o Rekognition: {error}")

if __name__ == "__main__":
    # Caminho da imagem para análise
    image_path = input("Digite o caminho da imagem: ")
    detect_celebrities(image_path)
