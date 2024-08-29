import itertools

def eval_expr(expr, values):
    """
    Evalúa una expresión lógica booleana con valores dados.

    Args:
        expr: La expresión lógica como string (e.g., "p ∧ q → r").
        values: Un diccionario que mapea variables a valores booleanos.

    Returns:
        El resultado booleano de la expresión o None si hay un error.
    """
    try:
        # Reemplazar los operadores lógicos con operadores Python
        expr = expr.replace('∧', ' and ').replace('∨', ' or ').replace('¬', ' not ')
        expr = expr.replace('→', ' <= ').replace('↔', ' == ')

        # Evaluar la expresión usando el diccionario de variables
        return eval(expr, {}, values)
    except (ValueError, SyntaxError, NameError) as e:
        print(f"Error al evaluar la expresión: {e}")
        return None

def generate_truth_table(expr):
    """
    Genera la tabla de verdad para una expresión lógica booleana.

    Args:
        expr: La expresión lógica como string (e.g., "p ∧ q → r").

    Returns:
        Una lista de tuplas, donde cada tupla contiene una combinación de 
        valores de verdad y el resultado correspondiente de la expresión.
        Devuelve None si hay un error en la expresión.
    """
    variables = sorted(set(c for c in expr if c.isalpha()))  # Obtener variables únicas
    num_vars = len(variables)
    combinaciones = list(itertools.product([False, True], repeat=num_vars))

    truth_table = []
    for combinacion in combinaciones:
        values = dict(zip(variables, combinacion))  # Crear diccionario de variables
        resultado = eval_expr(expr, values)
        if resultado is None:  # Manejar errores de eval_expr
            return None
        truth_table.append((combinacion, resultado))

    return truth_table

# Ejemplo de uso
expression = "p ∧ r" 
tabla_verdad = generate_truth_table(expression)

if tabla_verdad:
    print("Tabla de Verdad:")
    for combinacion, resultado in tabla_verdad:
        print(combinacion, resultado)
else:
    print("No se pudo generar la tabla de verdad debido a un error en la expresión.")