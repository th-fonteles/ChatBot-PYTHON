# título 
# campo de mensagem (input) 
# quando o usuário enviar uma mensagem 
    # mostrar a mensagem na conversa
    # mandar a mensagem pra IA responder 
    # mostrar a resposta da IA

# pip install streamlit openai
# streamlit run codigo.py

import streamlit as st
from openai import OpenAI

st.write("## ChatBot de IA")

modelo_ia = OpenAI(api_key=st.secrets['GEMINI_API_KEY'], base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

# criar o histórico de mensagens
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]
    st.chat_message(quem_enviou).write(texto_mensagem)

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    mensagem1 = {"role" : "user", "content" : mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem1) 

# pegar a resposta da IA

    resposta_modelo = modelo_ia.chat.completions.create(
        messages = st.session_state["lista_mensagens"], 
        model = "gemini-flash-lite-latest" 
    ) 

    resposta_ia = resposta_modelo.choices[0].message.content

# enviar a mensagem de IA no chat 
    st.chat_message("assistant").write(resposta_ia) 
    mensagem2 = {"role" : "assistant", "content" : resposta_ia} 
    st.session_state["lista_mensagens" ].append(mensagem2) 



































