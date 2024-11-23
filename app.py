import streamlit as st
import openai

# Configurar la página
st.set_page_config(page_title="Chat Inteligente", page_icon="💬", layout="centered")

# Estilizar la aplicación
st.markdown(
    """
    <style>
    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .user-message {
        background-color: #d0f0c0; /* Verde claro */
        border: 1px solid #a2d9a2;
        text-align: left;
    }
    .assistant-message {
        background-color: #f0f0f0; /* Gris claro */
        border: 1px solid #cfcfcf;
        text-align: left;
    }
    .header {
        text-align: center;
        font-size: 1.5rem;
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: #888888;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Mostrar el encabezado
st.title("💬 Chat Inteligente")
st.write(
    "Bienvenido a tu asistente virtual creado con OpenAI. Haz tus preguntas y recibe respuestas inteligentes."
)

# Obtener la clave de la API
openai_api_key = st.secrets.get("api_key")
if not openai_api_key:
    st.error("La clave de la API no está configurada en los secretos.")
    st.stop()

# Configurar cliente de OpenAI
openai.api_key = openai_api_key

# Entrada del usuario
prompt = st.chat_input("Escribe algo para comenzar:")
if not prompt:
    st.stop()

# Mostrar el mensaje del usuario
with st.chat_message("user"):
    st.markdown(f"<div class='stChatMessage user-message'>{prompt}</div>", unsafe_allow_html=True)

# Generar respuesta del asistente
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente amigable y útil."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=800,
        temperature=0.7,
    )
    respuesta = response["choices"][0]["message"]["content"]

    # Mostrar el mensaje del asistente
    with st.chat_message("assistant"):
        st.markdown(f"<div class='stChatMessage assistant-message'>{respuesta}</div>", unsafe_allow_html=True)
except Exception as e:
    st.error(f"Error al generar la respuesta: {str(e)}")

# Pie de página
st.markdown(
    """
    <div class="footer">
        Aplicación desarrollada por <b>Inteligencia Artificial</b>. 🌟
    </div>
    """,
    unsafe_allow_html=True,
)

