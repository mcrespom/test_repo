from datetime import date, timedelta

def days_between_ufs(last_uf_known_date: date) -> int:
    # Calcular la fecha actual
    current_date = date.today()

    # Calcular la diferencia en días entre las dos fechas
    days_difference = (current_date - last_uf_known_date).days

    return days_difference

def get_ufs(last_uf_known_date: date, last_uf_value: float, new_ipc: float) -> dict[date, float]:
    # Obtener la cantidad de días entre dos UF consecutivas
    days_between_ufs_value = days_between_ufs(last_uf_known_date)

    # Inicializar el diccionario para almacenar los resultados
    uf_values = {}

    # Calcular UF para cada día entre last_uf_known_date y la fecha actual
    while last_uf_known_date < date.today():
        # Calcular la UF usando la fórmula proporcionada
        uf_value = last_uf_value * pow(1 + new_ipc / 100, days_between_ufs_value)

        # Almacenar la UF calculada en el diccionario
        uf_values[last_uf_known_date] = uf_value

        # Actualizar la fecha y el valor de la UF para la próxima iteración
        last_uf_known_date += timedelta(days=1)
        last_uf_value = uf_value

        # Actualizar la cantidad de días entre dos UF consecutivas
        days_between_ufs_value = days_between_ufs(last_uf_known_date)

    return uf_values

# Ejemplo de uso:
last_uf_known_date = date(2023, 1, 1)
last_uf_value = 28000.0
new_ipc = 0.5

result = get_ufs(last_uf_known_date, last_uf_value, new_ipc)

# Imprimir los resultados
for date_key, uf_value in result.items():
    print(f"{date_key}: {uf_value}")
