# Arquivo: Home.py
import streamlit as st
import importlib
import os
import sys
import json

# Adiciona o diretório atual ao path do Python
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

st.set_page_config(page_title="WhatsApp Sender", page_icon="📱", layout="wide")

def load_users():
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
        st.write(f"Usuários carregados: {list(users.keys())}")  # Debug
        return users
    except Exception as e:
        st.error(f"Erro ao carregar usuários: {str(e)}")
        return {}

def check_credentials(username, password):
    users = load_users()
    is_valid = username in users and users[username] == password
    st.write(f"Tentativa de login para {username}: {'Sucesso' if is_valid else 'Falha'}")  # Debug
    return is_valid

def login_page():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state['authenticated'] = True
            st.session_state['username'] = username
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha incorretos")

def load_page(page_name):
    try:
        if page_name == "Página Inicial":
            show_home_page()
        else:
            module_name = page_name.lower().replace(" ", "_")
            module_name = module_name.replace("ç", "c").replace("ã", "a").replace("õ", "o")
            page_module = importlib.import_module(f"pages.{module_name}")
            page_module.main()
    except ImportError as e:
        st.error(f"Erro ao carregar a página {page_name}: {str(e)}")

def show_home_page():
    st.title("WhatsApp Sender - Página Inicial")
    st.write(f"""
    Bem-vindo ao WhatsApp Sender, {st.session_state.get('username', '')}!

    Use a barra lateral para navegar entre as páginas:
    - Enviar Mensagens: Para carregar seu arquivo Excel e enviar mensagens.
    - Configurações: Para ajustar os parâmetros da aplicação.
    - Manual: Para acessar o manual do usuário em PDF.
    """)

def main():
    if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
        login_page()
    else:
        st.sidebar.title("Navegação")
        page = st.sidebar.radio(
            "Escolha uma página",
            ["Página Inicial", "Enviar Mensagens", "Configurações", "Manual"]
        )

        if st.sidebar.button("Logout"):
            st.session_state['authenticated'] = False
            st.experimental_rerun()

        load_page(page)

    # Adicionar o rodapé personalizado
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1e4764;
        color: white;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
    }
    .footer a {
        color: #FCFCFD;
        text-decoration: none;
    }
    </style>
    <div class="footer">
        <p>Desenvolvido por Cleber Cardoso Pereira | Contato: cleber@analysisconsultoria.com | (64) 99989-5562 | <a href="https://br.linkedin.com/in/clebercardosopereira" target="_blank">LinkedIn</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()