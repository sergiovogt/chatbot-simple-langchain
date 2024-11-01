import gradio as gr
from back_chatgpt import generar_respuesta

def chatbot(texto, history):
    return generar_respuesta(texto)

gr.ChatInterface(chatbot, type="messages").launch()