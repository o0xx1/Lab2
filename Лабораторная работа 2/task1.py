money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0  # месяц
d = spend - salary  # долг
while money_capital > d:
    spend *= (1 + increase)
    d = spend - salary
    money_capital -= d
    months += 1
print("Количество месяцев, которое можно протянуть без долгов:", months)
