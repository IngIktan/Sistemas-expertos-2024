# Hechos iniciales
hechos = {
    "esta_lloviendo": False,
    "nubes_grises": True,
    "lleva_paraguas": False
}

# Reglas iniciales
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
# Funciones para gestionar la adquisición de conocimiento

def agregar_hecho(hechos, nombre, valor):
    """Añadir un nuevo hecho al sistema."""
    hechos[nombre] = valor
    print(f"Hecho añadido: {nombre} = {valor}")

def eliminar_hecho(hechos, nombre):
    """Eliminar un hecho del sistema."""
    if nombre in hechos:
        del hechos[nombre]
        print(f"Hecho eliminado: {nombre}")
    else:
        print(f"Hecho no encontrado: {nombre}")

def agregar_regla(reglas, condiciones, accion):
    """Añadir una nueva regla al sistema."""
    regla = {
        "condiciones": condiciones,
        "accion": accion
    }
    reglas.append(regla)
    print(f"Regla añadida: {condiciones} -> {accion}")

def eliminar_regla(reglas, indice):
    """Eliminar una regla del sistema por su índice."""
    if 0 <= indice < len(reglas):
        reglas.pop(indice)
        print(f"Regla eliminada en el índice: {indice}")
    else:
        print("Índice de regla no válido.")

def modificar_hecho(hechos, nombre, nuevo_valor):
    """Modificar un hecho existente en el sistema."""
    if nombre in hechos:
        hechos[nombre] = nuevo_valor
        print(f"Hecho modificado: {nombre} = {nuevo_valor}")
    else:
        print(f"Hecho no encontrado: {nombre}")

# Motor de inferencia (como antes)
def motor_inferencia(hechos, reglas):
    for regla in reglas:
        condiciones_cumplidas = all(eval(condicion, {}, hechos) for condicion in regla["condiciones"])
        if condiciones_cumplidas:
            resultado = regla["accion"](hechos)
            return resultado
    return "No se encontró una regla aplicable."

# Ejemplo de uso del subsistema de adquisición de conocimiento
agregar_hecho(hechos, "temperatura", "baja")
agregar_regla(reglas, ["temperatura == 'baja'", "nubes_grises == True"], lambda hechos: "Lleva abrigo y paraguas.")
modificar_hecho(hechos, "esta_lloviendo", True)

# Ejecutar el sistema experto con los nuevos hechos y reglas
resultado = motor_inferencia(hechos, reglas)
print(resultado)
