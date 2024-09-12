# Definimos las acciones del sistema
def encender_dispositivo(nombre_dispositivo):
    print(f"{nombre_dispositivo} ha sido encendido.")

def apagar_dispositivo(nombre_dispositivo):
    print(f"{nombre_dispositivo} ha sido apagado.")

def enviar_notificacion(mensaje):
    print(f"Notificación enviada: {mensaje}")

# Acciones específicas para diferentes dispositivos
acciones = {
    "encender_luz": lambda: encender_dispositivo("Luz del salón"),
    "apagar_luz": lambda: apagar_dispositivo("Luz del salón"),
    "encender_calefaccion": lambda: encender_dispositivo("Calefacción"),
    "apagar_calefaccion": lambda: apagar_dispositivo("Calefacción"),
    "enviar_alerta_clima": lambda: enviar_notificacion("Alerta de clima adverso detectado."),
}

# Definimos la función ejecutar_orden
def ejecutar_orden(orden):
    """Ejecuta la orden proporcionada por el motor de inferencia."""
    if orden in acciones:
        acciones[orden]()
        print(f"Orden '{orden}' ejecutada con éxito.")
    else:
        print(f"Orden '{orden}' no reconocida o no disponible.")

# Subsistema de explicación
explicaciones = []

def agregar_explicacion(explicacion):
    """Añade una explicación a la lista de explicaciones."""
    explicaciones.append(explicacion)

def mostrar_explicaciones():
    """Muestra todas las explicaciones de las decisiones tomadas."""
    if explicaciones:
        print("Explicaciones de las decisiones:")
        for explicacion in explicaciones:
            print(f"- {explicacion}")
    else:
        print("No hay explicaciones disponibles. No se tomaron decisiones.")

# Motor de inferencia actualizado con explicación
def motor_inferencia(hechos, reglas):
    for regla in reglas:
        condiciones_cumplidas = all(eval(condicion, {}, hechos) for condicion in regla["condiciones"])
        if condiciones_cumplidas:
            resultado = regla["accion"](hechos)
            ejecutar_orden(resultado)  # Ejecuta la orden
            agregar_explicacion(regla["explicacion"])  # Agrega la explicación
            return resultado
    return "No se encontró una regla aplicable."

# Hechos iniciales
hechos = {
    "temperatura": "baja",
    "esta_lloviendo": True,
    "viento_fuerte": False
}

# Reglas con explicaciones
reglas = [
    {
        "condiciones": ["temperatura == 'baja'", "esta_lloviendo == True"],
        "accion": lambda hechos: "encender_calefaccion",
        "explicacion": "La temperatura es baja y está lloviendo, por lo que es recomendable encender la calefacción."
    },
    {
        "condiciones": ["temperatura == 'alta'", "esta_lloviendo == False"],
        "accion": lambda hechos: "apagar_calefaccion",
        "explicacion": "La temperatura es alta y no está lloviendo, por lo que no se necesita la calefacción."
    },
    {
        "condiciones": ["viento_fuerte == True"],
        "accion": lambda hechos: "enviar_alerta_clima",
        "explicacion": "El viento es fuerte, se envía una alerta de clima adverso."
    }
]

# Ejecutar el sistema experto con los hechos y reglas actuales
resultado = motor_inferencia(hechos, reglas)
print(resultado)

# Mostrar explicaciones de las decisiones tomadas
mostrar_explicaciones()

