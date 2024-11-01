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

system_template = "Traducir lo siguie a {language}:"

plantilla_de_prompt = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

chatbot = plantilla_de_prompt | modelo | formateador

respuesta = chatbot.invoke({"language": "german", "text": "hola cómo estás?"})

print(respuesta)


