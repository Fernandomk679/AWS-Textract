# Inicialize o cliente do Textract
textract = boto3.client('textract')

# Defina o nome do seu bucket e o nome do arquivo
bucket_name = 'seu-bucket'
file_name = 'imagem.jpg'

# Chame o Textract para detectar o texto na imagem
response = textract.detect_text(
    Document={'S3Object': {'Bucket': bucket_name, 'Name': file_name}}
)

# Exiba o texto extraído
for block in response['Blocks']:
    if block['BlockType'] == 'LINE':
        print(block['Text'])