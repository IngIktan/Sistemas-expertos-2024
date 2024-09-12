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
def es_coherente_hecho(hechos, nuevo_hecho, nuevo_valor):
    """Verifica si el nuevo hecho es coherente con los hechos existentes."""
    if nuevo_hecho in hechos:
        if hechos[nuevo_hecho] != nuevo_valor:
            print(f"Conflicto detectado: El hecho '{nuevo_hecho}' ya existe con un valor diferente.")
            return False
    return True

def es_coherente_regla(reglas, nueva_regla):
    """Verifica si la nueva regla es coherente con las reglas existentes."""
    for regla in reglas:
        if set(regla["condiciones"]) == set(nueva_regla["condiciones"]):
            print("Conflicto detectado: Una regla con las mismas condiciones ya existe.")
            return False
    return True

def agregar_hecho(hechos, nombre, valor):
    """Añadir un nuevo hecho al sistema con control de coherencia."""
    if es_coherente_hecho(hechos, nombre, valor):
        hechos[nombre] = valor
        print(f"Hecho añadido: {nombre} = {valor}")
    else:
        print(f"No se pudo añadir el hecho: {nombre} = {valor}")

def agregar_regla(reglas, condiciones, accion):
    """Añadir una nueva regla al sistema con control de coherencia."""
    nueva_regla = {"condiciones": condiciones, "accion": accion}
    if es_coherente_regla(reglas, nueva_regla):
        reglas.append(nueva_regla)
        print(f"Regla añadida: {condiciones} -> {accion}")
    else:
        print("No se pudo añadir la regla debido a un conflicto de coherencia.")

# Motor de inferencia (sin cambios)
def motor_inferencia(hechos, reglas):
    for regla in reglas:
        condiciones_cumplidas = all(eval(condicion, {}, hechos) for condicion in regla["condiciones"])
        if condiciones_cumplidas:
            resultado = regla["accion"](hechos)
            return resultado
    return "No se encontró una regla aplicable."
# Ejemplo de uso del subsistema de adquisición de conocimiento con control de coherencia

agregar_hecho(hechos, "esta_lloviendo", True)  # Este hecho es coherente
agregar_hecho(hechos, "esta_lloviendo", False)  # Este hecho genera un conflicto

agregar_regla(reglas, ["esta_lloviendo == True"], lambda hechos: "Deberías llevar un paraguas.")  # Esta regla genera un conflicto
agregar_regla(reglas, ["temperatura == 'baja'", "nubes_grises == True"], lambda hechos: "Lleva abrigo y paraguas.")  # Esta regla es coherente

# Ejecutar el sistema experto con los hechos y reglas actuales
resultado = motor_inferencia(hechos, reglas)
print(resultado)
