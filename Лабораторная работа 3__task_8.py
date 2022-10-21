money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
while money_capital > spend:
    money_capital -= spend
    spend = spend * increase + spend
    month += 1

budget = money_capital + salary

while budget > spend:
    budget -= spend
    spend = spend * increase + spend
    month += 1
    budget += salary

# TODO Оформить решение

print(month)
