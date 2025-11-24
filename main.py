import streamlit as st
import gspread
from google.oauth2.service_account import Credentials


gcp_info = st.secrets["gcp"]
planilha_chave = st.secrets["planilha"]["chave"]

# Criar credenciais
creds = Credentials.from_service_account_info(
    dict(gcp_info),
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
)

client = gspread.authorize(creds)

pagina = client.open_by_key(planilha_chave).worksheet("dados")

st.set_page_config(page_title= "Acompanhamento das Fibras" , page_icon = "🌐" , layout= "wide")

lojas = [" ","LOJA IGUATEMI | BA" , "LOJA IGUATEMI || BA"]

consultores = ["" , "ANA" , "ANDERSON" , "AMANDA" , "DAVID" , "DEBORA" , "LENE" , "LORENA" , "RODRIGO"]

emalis =["","anapsantos@telefonica.com","anderson.scosta@telefonica.com",
         "amanda.dalmeida@telefonica.com","debora.sribeiro@telefonica.com",
         "david.brito@telefonica.com","lenilda.silva@telefonica.com",
         "lorena.rgomes@telefonica.com","marcos.reboucas@telefonica.com"]

emailgl = ["","max.silveira@telefonica.com"]

with st.form("Cadastro"):
    st.header("🌐 Agendamento da Fibra")
    Loja = st.selectbox("Loja:",lojas)
    nome = st.selectbox("Nome do consultor: ",consultores)
    ordem = st.text_input("SDR FIXA: ")
    data = st.date_input("Data do agendamento: ")
    hora = st.time_input("Hora de instalação: ")
    email = st.selectbox("Email do consultor: ",emalis)

    enviar = st.form_submit_button("Cadastrar")

if enviar:

    pagina.append_row([
        Loja,
        str(nome),
        ordem,
        data.strftime("%d/%m/%Y"),   
        hora.strftime("%H:%M"), 
        email,
    ])
    st.success("Agendamento realizado com sucesso!")
