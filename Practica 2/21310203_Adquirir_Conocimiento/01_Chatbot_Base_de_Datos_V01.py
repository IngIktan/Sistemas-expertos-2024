# Función para leer las respuestas de la base de datos
def leer_respuestas():
    try:
        with open('base_de_datos.txt', 'r') as file:
            datos = file.readlines()
        # Convertimos el archivo en un diccionario: {pregunta: respuesta}
        return {linea.strip().split(" - ")[0]: linea.strip().split(" - ")[1] for linea in datos}
    except FileNotFoundError:
        # Si no existe el archivo, devolvemos un diccionario vacío
        return {}

# Función para agregar una nueva respuesta a la base de datos
def agregar_respuesta(pregunta, respuesta):
    with open('base_de_datos.txt', 'a') as file:
        file.write(f"{pregunta} - {respuesta}\n")
    print(f"Nueva respuesta guardada: {pregunta} - {respuesta}")

# Función del chatbot para interactuar con el usuario
def chatbot():
    respuestas = leer_respuestas()
    
    # Respuestas predefinidas
    respuestas_predefinidas = {
        "Hola": "¡Hola! ¿Cómo estás?",
        "Cómo estás?": "Estoy bien, gracias. ¿Y tú?",
        "De qué te gustaría hablar?": "Podemos hablar de lo que quieras. Pregúntame algo."
    }
    
    while True:
        pregunta = input("Tú: ")

        # Primero, buscamos en las respuestas predefinidas
        if pregunta in respuestas_predefinidas:
            print(f"Chatbot: {respuestas_predefinidas[pregunta]}")
        # Luego, si no está en predefinidas, buscamos en la base de datos
        elif pregunta in respuestas:
            print(f"Chatbot: {respuestas[pregunta]}")
        else:
            # Si no se encuentra la pregunta en la base de datos, pedimos una nueva respuesta
            nueva_respuesta = input("Chatbot: No tengo una respuesta para eso. ¿Cuál debería ser mi respuesta? ")
            agregar_respuesta(pregunta, nueva_respuesta)
            # Actualizamos las respuestas cargadas en el chatbot
            respuestas = leer_respuestas()

# Iniciar el chatbot
chatbot()
