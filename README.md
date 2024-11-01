# Tutorial: Primera Aplicación LLM

Este tutorial te guiará a través de los pasos necesarios para configurar y ejecutar una aplicación en Python que consta de un chatbot desarrollado con LangChain.

# Links

- [Tutorial Oficial LangChain](https://python.langchain.com/docs/tutorials/llm_chain/)
- [OpenAI API key](https://platform.openai.com/)

## Pasos

1. **Crear un entorno virtual (venv)**:

```bash
python -m venv venv
```

2. **Activar el entorno virtual**:

- En Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- En macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

3. **Instalar las dependencias desde `requirements.txt`**:

```bash
pip install -r requirements.txt
```

4. **Crear un archivo `.env`**:
   Crea un archivo llamado `.env` en el directorio raíz del proyecto y añade las variables de entorno necesarias:

```env
OPENAI_API_KEY=your_api_key
```

5. **Ejecutar la aplicación**:

```bash
python frontend.py
```

¡Y eso es todo! Ahora deberías tener tu aplicación en funcionamiento.
