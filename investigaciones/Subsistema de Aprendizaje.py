# Definición del subsistema de aprendizaje
def ajustar_reglas(hechos, resultado_esperado, reglas):
    """
    Ajusta las reglas del sistema experto en función del resultado esperado proporcionado por el usuario.
    """
    for regla in reglas:
        # Verificar si la regla se aplica a los hechos actuales
        condiciones_cumplidas = all(eval(condicion, {}, hechos) for condicion in regla["condiciones"])
        if condiciones_cumplidas:
            # Si la acción de la regla no coincide con el resultado esperado, ajustar la regla
            if regla["accion"](hechos) != resultado_esperado:
                print(f"Ajustando regla para {regla['accion'](hechos)} a {resultado_esperado}.")
                regla["accion"] = lambda hechos: resultado_esperado
                regla["explicacion"] = f"La regla fue ajustada automáticamente para mejorar la precisión basada en datos recientes."
                return f"Regla ajustada a {resultado_esperado}."
    return "No se encontró una regla para ajustar."

# Definición de hechos y reglas para la prueba
hechos = {'temperatura': 20, 'humedad': 50}  # Ejemplo de hechos
reglas = [
    {
        'condiciones': ['temperatura > 22'],
        'accion': lambda hechos: 'encender_calefaccion',
        'explicacion': 'Se enciende la calefacción si la temperatura es menor o igual a 22°C.'
    },
    {
        'condiciones': ['temperatura <= 22'],
        'accion': lambda hechos: 'apagar_calefaccion',
        'explicacion': 'Se apaga la calefacción si la temperatura es mayor a 22°C.'
    }
]

# Ejemplo de retroalimentación del usuario
resultado_esperado = 'apagar_calefaccion'  # Por ejemplo, el usuario esperaba que la calefacción se apague.

# Motor de inferencia con integración de aprendizaje
def motor_inferencia_aprendizaje(hechos, reglas, resultado_esperado=None):
    for regla in reglas:
        condiciones_cumplidas = all(eval(condicion, {}, hechos) for condicion in regla["condiciones"])
        if condiciones_cumplidas:
            resultado = regla["accion"](hechos)
            ejecutar_orden(resultado)  # Ejecuta la orden
            agregar_explicacion(regla["explicacion"])  # Agrega la explicación
            if resultado_esperado:
                # Ajustar las reglas basadas en la retroalimentación del usuario
                ajuste = ajustar_reglas(hechos, resultado_esperado, reglas)
                print(ajuste)
            return resultado
    return "No se encontró una regla aplicable."

# Funciones adicionales necesarias
def ejecutar_orden(orden):
    print(f"Orden ejecutada: {orden}")

def agregar_explicacion(explicacion):
    print(f"Explicación: {explicacion}")

def mostrar_explicaciones():
    print("Mostrando todas las explicaciones.")

# Ejecutar el sistema experto con aprendizaje
resultado = motor_inferencia_aprendizaje(hechos, reglas, resultado_esperado)
print(resultado)

# Mostrar explicaciones de las decisiones tomadas
mostrar_explicaciones()
