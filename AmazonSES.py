import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Configurações do Amazon SES
AWS_REGION = "us-east-1"  # Substitua pela sua região AWS
SENDER = "seu_email@dominio.com"
SUBJECT = "Assunto do seu e-mail"

# Carregar a planilha com os e-mails
df = pd.read_excel('emails.xlsx')  # Substitua pelo caminho do seu arquivo Excel

# Carregar o arquivo com a copy do e-mail
with open('copy_email.txt', 'r') as file:
    email_body = file.read()

# Inicializar o cliente SES
client = boto3.client('ses', region_name=AWS_REGION)

# Função para enviar e-mail
def send_email(to_email, subject, body):
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [to_email],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': body,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': subject,
                },
            },
            Source=SENDER,
        )
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f'Erro ao enviar e-mail: {e}')
        return False
    return True

# Loop para enviar o e-mail para todos os destinatários na planilha
for index, row in df.iterrows():
    email = row['Email']  # Certifique-se de que a coluna na planilha se chama 'Email'
    if send_email(email, SUBJECT, email_body):
        print(f'E-mail enviado para {email}')
    else:
        print(f'Falha ao enviar e-mail para {email}')

print('Todos os e-mails foram enviados (ou tentativa feita).')
