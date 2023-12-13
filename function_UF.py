from datetime import date, timedelta

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

# Ejemplo de uso:
last_uf_known_date = date(2023, 1, 1)
last_uf_value = 28000.0
new_ipc = 0.5

uf_calculator = UFCalculator(last_uf_known_date, last_uf_value, new_ipc)
result = uf_calculator.calculate_ufs()

# Imprimir los resultados
for date_key, uf_value in result.items():
    print(f"{date_key}: {uf_value}")
