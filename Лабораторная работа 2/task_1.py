salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
podushka = 0
for i in range(months):
    a= spend - salary
    if a > 0:
        podushka += a
    spend = spend + spend * increase
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(podushka))
