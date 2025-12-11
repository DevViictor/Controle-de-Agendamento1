import streamlit as st
from PIL import Image
from TarefasLojas import cadastrar_iguatemi1,cadastrar_iguatemi2

st.sidebar.image("image/Image (2).png")

icon = Image.open("image/vivo.png")

st.set_page_config(page_title="Login", page_icon=icon)

usuarios = st.secrets["usuarios"]


# -----------------------------------------
# SESSION STATE
# -----------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.role = None

# -----------------------------------------
# LOGIN
# -----------------------------------------
def login():
   
    st.title("Login")
    user = st.text_input("Usuário:")
    password = st.text_input("Senha:", type="password")

    if st.button("Entrar"):
        if user in usuarios and password == usuarios[user]["senha"]:
            st.session_state.logged_in = True
            st.session_state.user = user
            st.session_state.role = usuarios[user]["role"]
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos!")

# -----------------------------------------
# LOGOUT
# -----------------------------------------
def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.role = None
    st.rerun()

# -----------------------------------------
# NAVEGAÇÃO
# -----------------------------------------
def run_navigation():
    role = st.session_state.role

    # Criar objetos Page
    page_iguatemi1 = st.Page(cadastrar_iguatemi1, title="Loja Iguatemi 1", icon="🏬")
    page_iguatemi2 = st.Page(cadastrar_iguatemi2, title="Loja Iguatemi 2", icon="🏬")

    # Menus por role
    if role == "admin":
        menu = {
            "Painel Fibra": [
                page_iguatemi1,
                page_iguatemi2,
            ]
        }

    elif role == "loja1":
        menu = {
            "Loja Iguatemi 1": [
                page_iguatemi1,
            ]
        }

    elif role == "loja2":
        menu = {
            "Loja Iguatemi 2": [
                page_iguatemi2,
            ]
        }

    # Criar navegação
    nav = st.navigation(menu)

    # Sidebar com usuário
    st.sidebar.write(f"👤 Usuário: **{st.session_state.user}**")
    st.sidebar.button("Sair", on_click=logout)

    # Rodar página selecionada
    nav.run()

# -----------------------------------------
# EXECUÇÃO PRINCIPAL
# -----------------------------------------
if not st.session_state.logged_in:
    login()
else:
    run_navigation()
