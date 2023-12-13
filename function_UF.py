from datetime import date, timedelta
import calendar

class UFCalculator:
    def __init__(self, last_uf_known_date: date, last_uf_value: float, new_ipc: float):
        self.last_uf_known_date = last_uf_known_date
        self.last_uf_value = last_uf_value
        self.new_ipc = new_ipc

    def days_between_ufs(self, end_date: date) -> int:
        days_difference = (end_date - self.last_uf_known_date).days
        return days_difference

    def calculate_ufs(self) -> dict[date, float]:
        uf_values = {}
        current_date = date.today()
        days_between_ufs_value = self.days_between_ufs(current_date)

        while self.last_uf_known_date < current_date:
            uf_value = self.last_uf_value * pow(1 + self.new_ipc / 100, days_between_ufs_value)
            uf_values[self.last_uf_known_date] = uf_value

            self.last_uf_known_date += timedelta(days=1)
            self.last_uf_value = uf_value
            days_between_ufs_value = self.days_between_ufs(self.last_uf_known_date)

        return uf_values

    def get_ufs(self, date_last_uf: date, last_uf_day_9: float, ipc_day_9: float) -> dict[date, float]:
        # Validador de la fecha objetivo sea 9
        if date_last_uf.day != 9:
            raise ValueError("Error: La función solo admite el día 9 del mes.")

        # Obtener el último día del mes actual
        ultimo_dia_mes_actual = date_last_uf.replace(day=1) + timedelta(days=calendar.monthrange(date_last_uf.year, date_last_uf.month)[1])

        # Calcular la cantidad total de días en el mes de la última UF conocida
        dias_en_mes = calendar.monthrange(date_last_uf.year, date_last_uf.month)[1]

        # Calcular la diferencia de días entre el 9 de diciembre y el último día del mes actual
        diferencia_dias = (ultimo_dia_mes_actual.replace(day=9) - date_last_uf.replace(day=9)).days

        # Inicializar el diccionario de resultados
        uf_values_result = {}

        # Calcular el valor de la UF para cada día desde la fecha inicial hasta el 9 del siguiente mes
        for i in range(0, diferencia_dias + 1):
            fecha_actual = date_last_uf + timedelta(days=i)
            valor_uf_objetivo = round(last_uf_day_9 * (1 + ipc_day_9) ** (i / dias_en_mes), 2)
            uf_values_result[fecha_actual] = valor_uf_objetivo

        return uf_values_result

# Ejemplo de uso:
last_uf_known_date = date(2023, 1, 1)
last_uf_value = 28000.0
new_ipc = 0.5

uf_calculator = UFCalculator(last_uf_known_date, last_uf_value, new_ipc)
result = uf_calculator.calculate_ufs()

# Imprimir los resultados de la calculadora original
for date_key, uf_value in result.items():
    print(f"{date_key}: {uf_value}")

# Ejemplo de uso de la nueva función get_ufs
date_last_uf = date(2023, 1, 9)
last_uf_day_9 = 28000