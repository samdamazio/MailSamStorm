import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do servidor de e-mail
smtp_server = 'smtp.seuservidoremail.com'  # Substitua pelo seu servidor SMTP
smtp_port = 587  # Porta do servidor SMTP
smtp_user = 'seu_email@dominio.com'  # Substitua pelo seu e-mail
smtp_password = 'sua_senha'  # Substitua pela sua senha

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
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())

# Loop para enviar o e-mail para todos os destinatários na planilha
subject = 'Assunto do seu e-mail'  # Substitua pelo assunto do seu e-mail

for index, row in df.iterrows():
    email = row['Email']  # Certifique-se de que a coluna na planilha se chama 'Email'
    send_email(email, subject, email_body)
    print(f'E-mail enviado para {email}')

print('Todos os e-mails foram enviados com sucesso!')
