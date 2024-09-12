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
def ejecutar_orden(orden):
    """Ejecuta la orden proporcionada por el motor de inferencia."""
    if orden in acciones:
        acciones[orden]()
        print(f"Orden '{orden}' ejecutada con éxito.")
    else:
        print(f"Orden '{orden}' no reconocida o no disponible.")

# Motor de inferencia actualizado
def motor_inferencia(hechos, reglas):
    for regla in reglas:
        condiciones_cumplidas = all(eval(condicion, {}, hechos) for condicion in regla["condiciones"])
        if condiciones_cumplidas:
            resultado = regla["accion"](hechos)
            ejecutar_orden(resultado)  # Integración con el subsistema de ejecución
            return resultado
    return "No se encontró una regla aplicable."
def ejecutar_orden(orden):
    """Ejecuta la orden proporcionada por el motor de inferencia."""
    if orden in acciones:
        acciones[orden]()
        print(f"Orden '{orden}' ejecutada con éxito.")
    else:
        print(f"Orden '{orden}' no reconocida o no disponible.")

# Motor de inferencia actualizado
def motor_inferencia(hechos, reglas):
    for regla in reglas:
        condiciones_cumplidas = all(eval(condicion, {}, hechos) for condicion in regla["condiciones"])
        if condiciones_cumplidas:
            resultado = regla["accion"](hechos)
            ejecutar_orden(resultado)  # Integración con el subsistema de ejecución
            return resultado
    return "No se encontró una regla aplicable."
# Hechos iniciales
hechos = {
    "temperatura": "baja",
    "esta_lloviendo": True,
    "viento_fuerte": False
}

# Reglas actualizadas con órdenes
reglas = [
    {
        "condiciones": ["temperatura == 'baja'", "esta_lloviendo == True"],
        "accion": lambda hechos: "encender_calefaccion"  # Orden a ejecutar
    },
    {
        "condiciones": ["temperatura == 'alta'", "esta_lloviendo == False"],
        "accion": lambda hechos: "apagar_calefaccion"
    },
    {
        "condiciones": ["viento_fuerte == True"],
        "accion": lambda hechos: "enviar_alerta_clima"
    }
]
# Ejecutar el sistema experto con los hechos y reglas actuales
resultado = motor_inferencia(hechos, reglas)
print(resultado)
