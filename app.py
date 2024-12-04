import time
import streamlit as st
import datetime
from solicitacao import enviar_solicitacao

logo_facape, texto_nti = st.columns([1, 3], vertical_alignment="center")
with logo_facape:
    st.image("logo-facape.png", width=100)
with texto_nti:
    st.header("NTI - Redes e Internet", anchor="titulo_pagina_inicial")


@st.dialog("Confirmar informações o formulario", width='large')
def confirmar(email_contato, nome, data_nascimento, funcao, empresa, observacao):
    st.markdown(
        f"""
        **Email da empresa:** {email_contato}\n
        | Nome | Data Nascimento | Função | Empresa | Observação |
        | :---: | :---: | :---: | :---: | :---: |
        | {nome.upper()} | {data_nascimento.strftime('%d/%m/%Y')} | {funcao.upper()} | {empresa.upper()} | {observacao} |
        """
)
    st.subheader("", divider=True)
    confirmacao, sim = st.columns(2)
    with confirmacao:
        st.markdown("**Confirmar e enviar?**")
    if sim.button("Sim"):
        with st.spinner("Enviando Solicitação..."):
            enviar_solicitacao(
                email_contato,
                nome.upper(),
                data_nascimento.strftime('%d/%m/%Y'),
                funcao.upper(),
                empresa.upper(),
                observacao
            )
            time.sleep(2)
        st.success("Solicitação enviada com sucesso!")
        time.sleep(1)
        st.rerun()
    st.warning("Endereços de Email não reconhecidos serão descartados!")


with st.form(key="formulario_ususarios_terceirizados", border=True):
    st.subheader("**:material/badge: Solicitar acesso de internet para o funcionario**")
    st.html(
        f"""<html>
          <body>
            <p style="text-align:center;"><strong>Preencha as informações abaixo para realizar a sua solicitação</strong></p>
          </body>
        </html>"""
    )
    email_contato = st.text_input(
        label=":material/email: **:orange[Email de contato da empresa]** :red[*]",
        help=":orange[EX:] verdeservico@gmail.com",
        max_chars=40,
        placeholder="Email da empresa solicitante para resposta da solicitação",
    )
    nome = st.text_input(
        label=":material/badge: **:orange[Nome Funcionario]** :red[*]",
        help=":orange[EX:] Alexandre Silva Nascimento",
        max_chars=40,
        placeholder="Nome do funcionario",
    )
    data_nascimento = st.date_input(
        label=":material/calendar_month: **:orange[Data de Nascimento]** :red[*]",
        help=":orange[EX:] 01/01/2001",
        format="DD/MM/YYYY",
        min_value=datetime.date(datetime.datetime.now().year - 100,1,1),
        max_value=datetime.date(datetime.datetime.now().year - 14,1,1),
    )
    funcao = st.text_input(
        label=":material/handyman: **:orange[Função exercida]** :red[*]",
        help=":orange[EX:] Jardineiro :orange[,] Serviços Gerais",
        max_chars=30,
        placeholder="Função principal exercida pelo funcionario",
    )
    empresa = st.text_input(
        label=":material/enterprise: **:orange[Empresa do funcionario]** :red[*]",
        help=":orange[EX:] FACAPE",
        max_chars=40,
        placeholder="Empresa a qual o funcionario faz parte",
    )
    observacao = st.text_input(
        label=":material/abc: **:orange[Observação]**",
        max_chars=60,
        placeholder="Caso deseje adicionar uma informação extra necessaria",
    )

    if st.form_submit_button("Solicitar Acesso"):
        if email_contato == "":
            st.toast(":warning: *:orange[Email de Contato]* não pode ser vazio!")
        elif nome == "":
            st.toast(":warning: *:orange[Nome do Funcionario]* não pode ser vazio!")
        elif data_nascimento == "":
            st.toast(":warning: *:orange[Data de Nascimento]* não pode ser vazio!")
        elif funcao == "":
            st.toast(":warning: *:orange[Função]* não pode ser vazio!")
        elif empresa == "":
            st.toast(":warning: *:orange[Empresa]* não pode ser vazio!")
        else:
            confirmar(email_contato, nome, data_nascimento, funcao, empresa, observacao)
