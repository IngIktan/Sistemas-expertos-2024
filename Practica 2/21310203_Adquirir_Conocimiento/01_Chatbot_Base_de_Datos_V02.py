import tkinter as tk
from tkinter import simpledialog, scrolledtext
import time

# Función para leer las respuestas de la base de datos
def leer_respuestas():
    try:
        with open('base_de_datos_2.txt', 'r') as file:
            datos = file.readlines()
        return {linea.strip().split(" - ")[0]: linea.strip().split(" - ")[1] for linea in datos}
    except FileNotFoundError:
        return {}

# Función para agregar una nueva respuesta a la base de datos
def agregar_respuesta(pregunta, respuesta):
    with open('base_de_datos_2).txt', 'a') as file:
        file.write(f"{pregunta} - {respuesta}\n")
    mostrar_mensaje(f"Nueva respuesta guardada: {pregunta} - {respuesta}")

# Mostrar mensaje en el área de texto
def mostrar_mensaje(mensaje):
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, mensaje + "\n")
    chat_area.configure(state='disabled')
    chat_area.see(tk.END)

# Función para procesar el mensaje del usuario
def enviar_mensaje(event=None):
    pregunta = entry.get()
    entry.delete(0, tk.END)

    mostrar_mensaje(f"Tú: {pregunta}")

    # Respuestas predefinidas
    if pregunta in respuestas_predefinidas:
        mostrar_mensaje(f"Danbot: {respuestas_predefinidas[pregunta]}")
    elif pregunta in respuestas:
        mostrar_mensaje(f"Danbot: {respuestas[pregunta]}")
    elif pregunta.lower() == "bye":
        mostrar_mensaje("Danbot: ¡Hasta luego!")
        ventana.after(3000, ventana.destroy)  # Cerrar ventana después de 3 segundos
    else:
        nueva_respuesta = simpledialog.askstring("Respuesta desconocida", "No tengo una respuesta para eso. ¿Cuál debería ser mi respuesta?")
        if nueva_respuesta:
            agregar_respuesta(pregunta, nueva_respuesta)
            mostrar_mensaje(f"Danbot: {nueva_respuesta}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Chatbot Danbot")

# Crear el área de texto para mostrar el chat
chat_area = scrolledtext.ScrolledText(ventana, state='disabled', width=50, height=15)
chat_area.pack(pady=10)

# Crear la entrada de texto para el usuario
entry = tk.Entry(ventana, width=50)
entry.pack(pady=10)

# Bind para enviar mensaje al presionar Enter
entry.bind("<Return>", enviar_mensaje)

# Botón para enviar el mensaje
send_button = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
send_button.pack()

# Cargar respuestas
respuestas = leer_respuestas()
respuestas_predefinidas = {
    "Hola": "¡Hola! ¿Cómo estás?",
    "Cómo estás?": "Estoy bien, gracias. ¿Y tú?",
    "De qué te gustaría hablar?": "Podemos hablar de lo que quieras. Pregúntame algo."
}

# Iniciar el bucle principal de la ventana
ventana.mainloop()
