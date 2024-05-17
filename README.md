# MailSamStorm

MailSamStorm é uma ferramenta simples e eficiente para disparo automático de e-mails em massa utilizando uma planilha de e-mails e um arquivo de texto com a copy do e-mail.

## Funcionalidades

- Envio de e-mails em massa com base em uma lista de e-mails fornecida em uma planilha Excel.
- Personalização do corpo do e-mail a partir de um arquivo de texto.
- Configuração fácil de servidor SMTP para envio de e-mails.

## Requisitos

- Python 3.x
- Pandas
- openpyxl

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seuusuario/MailSamStorm.git
    cd MailSamStorm
    ```

2. Instale as dependências:
    ```bash
    pip install pandas openpyxl
    ```

## Configuração

1. Configure as informações do seu servidor SMTP no script `send_emails.py`:
    ```python
    smtp_server = 'smtp.seuservidoremail.com'
    smtp_port = 587
    smtp_user = 'seu_email@dominio.com'
    smtp_password = 'sua_senha'
    ```

2. Prepare seu arquivo Excel (`emails.xlsx`) com uma coluna chamada `Email` contendo os endereços de e-mail.

3. Crie um arquivo de texto (`copy_email.txt`) com a copy do e-mail que você deseja enviar.

## Uso

Para enviar os e-mails, execute o script `send_emails.py`:
```bash
python send_emails.py

Exemplo de Arquivo emails.xlsx
Email
exemplo1@dominio.com
exemplo2@dominio.com
exemplo3@dominio.com
Exemplo de Arquivo copy_email.txt
css
Copy code
Olá,

Este é um exemplo de e-mail enviado automaticamente pelo MailSamStorm.

Atenciosamente,
Sua Empresa
Contribuição
Sinta-se à vontade para contribuir com este projeto! Faça um fork do repositório, crie um branch com suas alterações e envie um pull request.

Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

Feito com ❤️ por SamDamazio

