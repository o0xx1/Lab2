salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0  # подушка безопасности
for i in range(months):
    d = spend - salary  # долг
    spend *= 1 + increase
    money_capital += d
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))