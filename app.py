import streamlit as st
from openai import OpenAI

st.set_page_config()
# Show title and description.
st.title("💬 Mi Chat inteligente ")
st.write(
   "Bienvenido a tu asistente virtual creado con OpenAI. Haz tus preguntas y recibe respuestas inteligentes."
)
openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

prompt = st.chat_input("What is up?")
if prompt==None:
   st.stop()

with st.chat_message("user"):
   st.markdown(prompt)

# Generate a response using the OpenAI API.

stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0,
    )
respuesta = stream.choices[0].message.content
with st.chat_message("assistant"):
   st.write(respuesta)
   st.markdown(
    """
    <div class="footer">
        Aplicación desarrollada por <b>Inteligencia Artificial</b>. 🌟
    </div>
    """,
    unsafe_allow_html=True,
)
