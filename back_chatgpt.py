from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

# Crear una instancia del modelo
modelo = ChatOpenAI(model="gpt-4o-mini")

# Crear un parser de salida
formateador = StrOutputParser()

system_template = "Sos un asistente virtual, responder siempre en español y con un tono amigable."

plantilla_de_prompt = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

chatgpt = plantilla_de_prompt | modelo | formateador

def generar_respuesta(texto):
    respuesta = chatgpt.invoke({"text": texto})
    return respuesta