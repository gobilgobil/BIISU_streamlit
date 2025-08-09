import streamlit as st
import base64
from PIL import Image
from pathlib import Path

# Define o layout da página como 'wide' (largo)
st.set_page_config(layout="wide")

def scrollable_image(image_path):
    """
    Exibe uma imagem em um contêiner rolável.

    Argumentos:
    image_path (str ou Path): O caminho para o arquivo de imagem.
    """
    try:
        # Lê o arquivo de imagem e o codifica em base64
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        
        encoded_image = base64.b64encode(image_bytes).decode()
        image_ext = Path(image_path).suffix.lstrip('.')

        # Cria o HTML para o contêiner rolável e a imagem.
        # 'overflow: auto' adiciona barras de rolagem horizontal e vertical conforme necessário.
        # A imagem é exibida com 100% da largura do contêiner.
        html_content = f"""
        <div style="overflow: auto; height: 600px; border: 1px solid #ddd;">
            <img src="data:image/{image_ext};base64,{encoded_image}" 
             style="width: 200%; height: 200%; display: block;">
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error(f"Arquivo de imagem não encontrado em {image_path}")
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")

# --- Layout do App ---

# Cria um layout de duas colunas: 1/3 para controles, 2/3 para a imagem
col1, col2 = st.columns([1, 2])

# Conteúdo para a coluna da esquerda
with col1:
    st.title("🎈 Meu novo app")
    st.write(
        "Esta é a área do painel de controle. Todos os textos e widgets vão aqui."
    )
    st.write(
        "A imagem à direita está colocada em uma janela rolável."
    )
    st.write(
        "Para ajuda e inspiração, acesse [docs.streamlit.io](https://docs.streamlit.io/)."
    )

# Conteúdo para a coluna da direita
with col2:
    st.subheader("Visualizador de Imagem Rolável")
    # Você pode substituir 'teste.png' pelo seu arquivo de imagem.
    # Certifique-se de que a imagem esteja na mesma pasta que o seu script.
    image_file = 'teste.png'
    scrollable_image(image_file)

