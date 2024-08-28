# Arquivo: pages/manual.py
import streamlit as st
import base64
import os

def main():
    st.title("Manual do Usuário")

    # Caminho para o arquivo PDF
    pdf_file = "manual.pdf"  # Certifique-se de que este é o nome correto do seu arquivo

    # Verifica se o arquivo existe
    if not os.path.isfile(pdf_file):
        st.error(f"O arquivo {pdf_file} não foi encontrado.")
        return

    # Lê o arquivo PDF
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Incorpora o PDF na página
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

    # Adiciona um botão para download
    st.download_button(
        label="Baixar Manual PDF",
        data=base64_pdf,
        file_name="manual.pdf",
        mime="application/pdf"
    )


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