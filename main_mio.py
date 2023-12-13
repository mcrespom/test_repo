from datetime import date
from  import UFCalculator

    # Definir parámetros iniciales
last_uf_known_date = date(2023, 1, 1)
last_uf_value = 28000.0
new_ipc = 0.5

    # Crear una instancia de UFCalculator
uf_calculator = UFCalculator(last_uf_known_date, last_uf_value, new_ipc)

    # Calcular UF con la función calculate_ufs
result_calculate_ufs = uf_calculator.calculate_ufs()

    # Imprimir los resultados de la función calculate_ufs
print("Resultados de calculate_ufs:")
for date_key, uf_value in result_calculate_ufs.items():
    print(f"{date_key}: {uf_value}")

    # Definir parámetros para la función get_ufs
date_last_uf = date(2023, 1, 9)
last_uf_day_9 = 28000
ipc_day_9 = 0.5

    # Calcular UF con la función get_ufs
result_get_ufs = uf_calculator.get_ufs(date_last_uf, last_uf_day_9, ipc_day_9)

    # Imprimir los resultados de la función get_ufs
print("\nResultados de get_ufs:")
for date_key, uf_value in result_get_ufs.items():
    print(f"{date_key}: {uf_value}")
