import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

def enviar_solicitacao(email_contato, nome, data_nascimento, funcao, empresa, observacao):
    agora = datetime.datetime.now() - datetime.timedelta(hours=3)
    corpo_email = f"""
    <html>
      <body>
        <p>Teste solicitação adição usuario rede FACPE-Servicos<br></p>
        <p><strong>Nome:</strong> {nome} </p>
        <p><strong>Data de Nascimento:</strong> {data_nascimento} </p>
        <p><strong>Função:</strong> {funcao} </p>
        <p><strong>Empresa:</strong> {empresa} </p>
        <p><strong>Observação:</strong> {observacao} </p>
        <p style="text-align:center;"><strong>Solicitado por:</strong> {email_contato}</p>
      </body>
    </html>
    """
    mensagem = MIMEMultipart("alternative")
    mensagem['Subject'] = f"Solicitação: Rede serviços - {agora.strftime('%d%m%H%M%S%f')}"
    mensagem['From'] = st.secrets.SMTP.email
    mensagem['To'] = st.secrets.SMTP.destinatario
    mensagem['Cc'] = str(email_contato)
    destinatarios = [st.secrets.SMTP.destinatario, email_contato]
    mensagem.attach(
      MIMEText(
        corpo_email, 'html'
      )
    )

    with smtplib.SMTP('smtp.gmail.com', 587) as servidor_email:
      servidor_email.starttls()
      servidor_email.login(st.secrets.SMTP.email, st.secrets.SMTP.senha)
      servidor_email.sendmail(st.secrets.SMTP.email, destinatarios, mensagem.as_string())
