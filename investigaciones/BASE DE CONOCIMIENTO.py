# Definimos los hechos (estado inicial del conocimiento)
hechos = {
    "esta_lloviendo": False,
    "nubes_grises": True,
    "lleva_paraguas": False
}

# Definimos las reglas (condiciones y acciones)
reglas = [
    {
        "condiciones": ["esta_lloviendo == True"],
        "accion": lambda hechos: "Deberías llevar un paraguas."
    },
    {
        "condiciones": ["nubes_grises == True", "esta_lloviendo == False"],
        "accion": lambda hechos: "Parece que podría llover. Mejor lleva un paraguas por si acaso."
    },
    {
        "condiciones": ["nubes_grises == False", "esta_lloviendo == False"],
        "accion": lambda hechos: "No necesitas un paraguas."
    }
]
def motor_inferencia(hechos, reglas):
    for regla in reglas:
        # Evaluar todas las condiciones en la regla
        condiciones_cumplidas = all(eval(condicion, {}, hechos) for condicion in regla["condiciones"])
        
        if condiciones_cumplidas:
            # Si todas las condiciones son ciertas, ejecuta la acción de la regla
            resultado = regla["accion"](hechos)
            return resultado

    return "No se encontró una regla aplicable."

# Ejecutar el sistema experto
resultado = motor_inferencia(hechos, reglas)
print(resultado)
