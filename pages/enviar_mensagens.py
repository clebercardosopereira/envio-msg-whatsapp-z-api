# Arquivo: pages/enviar_mensagens.py
import streamlit as st
import pandas as pd
import http.client
import json
import time


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
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def read_data_from_excel(file):
    df = pd.read_excel(file)
    
    phone_column = next((col for col in df.columns if 'telefone' in col.lower()), None)
    name_column = next((col for col in df.columns if 'nome' in col.lower()), None)
    
    if not phone_column or not name_column:
        st.error(f"Colunas necessárias não encontradas. Encontradas: {df.columns.tolist()}")
        return None, None, None
    
    data = df[[phone_column, name_column]].to_dict('records')
    return data, phone_column, name_column

def send_message(phone_number, client_name):
    config = load_config()
    conn = http.client.HTTPSConnection("api.z-api.io")

    message = config['message_template'].format(client_name=client_name)

    payload = {
        "phone": phone_number,
        "message": message,
        "image": config['image_url'],
        "linkUrl": config['link_url'],
        "title": config['title'],
        "linkDescription": config['link_description']
    }

    headers = {
        'Content-Type': "application/json; charset=utf-8",
        'User-Agent': "insomnia/2023.5.8",
        'Client-Token': config['api_token']
    }

    try:
        conn.request("POST", config['instance_url'], json.dumps(payload, ensure_ascii=False).encode('utf-8'), headers)
        res = conn.getresponse()
        data = res.read()
        return f"Mensagem enviada para {client_name} ({phone_number}). Resposta: {data.decode('utf-8')}"
    finally:
        conn.close()

def main():
    st.title("Envio de Mensagens WhatsApp")

    uploaded_file = st.file_uploader("Escolha o arquivo Excel", type="xlsx")
    
    if uploaded_file is not None:
        client_data, phone_column, name_column = read_data_from_excel(uploaded_file)
        
        if client_data:
            st.success(f"Arquivo carregado com sucesso. {len(client_data)} clientes encontrados.")
            
            if st.button("Enviar Mensagens"):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for i, client in enumerate(client_data):
                    result = send_message(client[phone_column], client[name_column])
                    status_text.text(result)
                    progress_bar.progress((i + 1) / len(client_data))
                    
                    if (i + 1) % 3 == 0 and i < len(client_data) - 1:
                        time.sleep(60)
                        status_text.text("Aguardando 1 minuto antes do próximo lote...")
                
                st.success("Todas as mensagens foram enviadas!")


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