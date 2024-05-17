import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do servidor SMTP do Hotmail/Outlook
smtp_server = 'smtp.office365.com'
smtp_port = 587
smtp_user = 'seu_email@hotmail.com'  # Substitua pelo seu endereço de e-mail do Hotmail/Outlook
smtp_password = 'sua_senha'  # Substitua pela sua senha de e-mail do Hotmail/Outlook

# Carregar a planilha com os e-mails
df = pd.read_excel('emails.xlsx')  # Substitua pelo caminho do seu arquivo Excel

# Carregar o arquivo com a copy do e-mail
with open('copy_email.txt', 'r') as file:
    email_body = file.read()

# Função para enviar e-mail
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to_email, msg.as_string())
        print(f'E-mail enviado para {to_email}')
    except Exception as e:
        print(f'Falha ao enviar e-mail para {to_email}: {e}')

# Loop para enviar o e-mail para todos os destinatários na planilha
subject = 'Assunto do seu e-mail'  # Substitua pelo assunto do seu e-mail

for index, row in df.iterrows():
    email = row['Email']  # Certifique-se de que a coluna na planilha se chama 'Email'
    send_email(email, subject, email_body)

print('Tentativa de envio de todos os e-mails concluída!')
