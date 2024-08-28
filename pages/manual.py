# Arquivo: pages/manual.py
import streamlit as st

def main():
    st.title("Manual do Usuário")

    st.write("""
    O manual do usuário está disponível para download no link abaixo.
    """)

    # Substitua esta URL pela URL real do seu PDF hospedado na nuvem
    pdf_url = "https://drive.google.com/file/d/1gyG3qUke_RO4hRcIzZb-6bW9yMKT60fn/view"

    st.markdown(f"[Clique aqui para baixar o Manual do Usuário (PDF)]({pdf_url})")

    st.write("""
    Instruções:
    1. Clique no link acima para baixar o manual.
    2. Abra o arquivo PDF baixado com seu leitor de PDF preferido.
    3. Se tiver problemas para abrir o arquivo, certifique-se de ter um leitor de PDF instalado em seu dispositivo.
    """)



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