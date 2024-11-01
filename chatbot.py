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

# Crear un mensaje humano
messages = [
    HumanMessage(content="Decime un chiste!"),
]

# Chatbot en cadena
chatbot = modelo | formateador 

# # Invocar el modelo
# respuesta = modelo.invoke(messages)


# # Formatear la respuesta
# respuesta_formateada = formateador.invoke(respuesta)

respuesta = chatbot.invoke(messages)

#Imprimir la respuesta
print(respuesta)



