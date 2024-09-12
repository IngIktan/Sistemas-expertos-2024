# Hechos iniciales
hechos = {
    "temperatura": "moderada",
    "esta_lloviendo": False,
    "viento_fuerte": False
}

# Reglas iniciales
reglas = [
    {
        "condiciones": ["temperatura == 'alta'", "esta_lloviendo == False"],
        "accion": lambda hechos: "Recomendamos nadar."
    },
    {
        "condiciones": ["temperatura == 'baja'", "esta_lloviendo == True"],
        "accion": lambda hechos: "Recomendamos quedarse en casa y leer un libro."
    },
    {
        "condiciones": ["temperatura == 'moderada'", "viento_fuerte == False"],
        "accion": lambda hechos: "Recomendamos ir a caminar."
    }
]
def agregar_hecho(hechos, nombre, valor):
    """Añadir un nuevo hecho al sistema."""
    if nombre in hechos:
        print(f"Hecho ya existente: {nombre} = {hechos[nombre]}. Modifícalo si es necesario.")
    else:
        hechos[nombre] = valor
        print(f"Hecho añadido: {nombre} = {valor}")

def modificar_hecho(hechos, nombre, nuevo_valor):
    """Modificar un hecho existente en el sistema."""
    if nombre in hechos:
        hechos[nombre] = nuevo_valor
        print(f"Hecho modificado: {nombre} = {nuevo_valor}")
    else:
        print(f"Hecho no encontrado: {nombre}. Añádelo primero.")

def eliminar_hecho(hechos, nombre):
    """Eliminar un hecho del sistema."""
    if nombre in hechos:
        del hechos[nombre]
        print(f"Hecho eliminado: {nombre}")
    else:
        print(f"Hecho no encontrado: {nombre}.")

def agregar_regla(reglas, condiciones, accion):
    """Añadir una nueva regla al sistema."""
    nueva_regla = {"condiciones": condiciones, "accion": accion}
    if not es_coherente_regla(reglas, nueva_regla):
        print("Conflicto detectado: Una regla con condiciones similares ya existe.")
    else:
        reglas.append(nueva_regla)
        print(f"Regla añadida: {condiciones} -> {accion}")

def modificar_regla(reglas, indice, nuevas_condiciones, nueva_accion):
    """Modificar una regla existente en el sistema."""
    if 0 <= indice < len(reglas):
        reglas[indice]["condiciones"] = nuevas_condiciones
        reglas[indice]["accion"] = nueva_accion
        print(f"Regla modificada en el índice {indice}.")
    else:
        print("Índice de regla no válido.")

def eliminar_regla(reglas, indice):
    """Eliminar una regla del sistema por su índice."""
    if 0 <= indice < len(reglas):
        reglas.pop(indice)
        print(f"Regla eliminada en el índice: {indice}")
    else:
        print("Índice de regla no válido.")

def es_coherente_regla(reglas, nueva_regla):
    """Verifica si la nueva regla es coherente con las reglas existentes."""
    for regla in reglas:
        if set(regla["condiciones"]) == set(nueva_regla["condiciones"]):
            return False
    return True

# Motor de inferencia
def motor_inferencia(hechos, reglas):
    for regla in reglas:
        condiciones_cumplidas = all(eval(condicion, {}, hechos) for condicion in regla["condiciones"])
        if condiciones_cumplidas:
            resultado = regla["accion"](hechos)
            return resultado
    return "No se encontró una regla aplicable."
# Agregar un nuevo hecho
agregar_hecho(hechos, "humedad_alta", True)

# Modificar un hecho existente
modificar_hecho(hechos, "temperatura", "alta")

# Eliminar un hecho
eliminar_hecho(hechos, "viento_fuerte")

# Agregar una nueva regla
agregar_regla(reglas, ["temperatura == 'alta'", "humedad_alta == True"], lambda hechos: "Recomendamos beber mucha agua y descansar en sombra.")

# Modificar una regla existente
modificar_regla(reglas, 1, ["temperatura == 'baja'", "esta_lloviendo == True"], lambda hechos: "Recomendamos preparar una bebida caliente y ver una película.")

# Ejecutar el sistema experto con los hechos y reglas actuales
resultado = motor_inferencia(hechos, reglas)
print(resultado)
