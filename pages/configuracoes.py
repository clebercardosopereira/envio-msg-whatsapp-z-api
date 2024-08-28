# Arquivo: pages/2_Configuracoes.py
import streamlit as st
import json
import os


if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
    st.error("Por favor, faça login para acessar esta página.")
    st.stop()

def check_authentication():
    if not st.session_state.get('authenticated', False):
        st.error("Por favor, faça login para acessar esta página.")
        st.stop()

def main():
    check_authentication()

def load_config():
    default_config = {
        "message_template": "",
        "api_token": "",
        "instance_url": "",
        "image_url": "",
        "link_url": "",
        "title": "",
        "link_description": ""
    }
    if os.path.exists('config.json'):
        with open('config.json', 'r', encoding='utf-8') as f:
            loaded_config = json.load(f)
            # Atualiza o default_config com os valores carregados
            default_config.update(loaded_config)
    return default_config

def save_config(config):
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

def main():
    st.title("Configurações")

    config = load_config()

    config['message_template'] = st.text_area("Template da Mensagem", config.get('message_template', ''), height=200)
    config['api_token'] = st.text_input("Token da API Z-API", config.get('api_token', ''))
    config['instance_url'] = st.text_input("URL da Instância Z-API", config.get('instance_url', ''))
    
    st.subheader("Configurações do Payload")
    config['image_url'] = st.text_input("URL da Imagem", config.get('image_url', ''))
    config['link_url'] = st.text_input("URL do Link", config.get('link_url', ''))
    config['title'] = st.text_input("Título", config.get('title', ''))
    config['link_description'] = st.text_input("Descrição do Link", config.get('link_description', ''))

    if st.button("Salvar Configurações"):
        save_config(config)
        st.success("Configurações salvas com sucesso!")



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