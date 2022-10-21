salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
while months != 9:
    need_money = spend
    months -= 1

for i in range(9):
    spend = spend * increase + spend
    need_money += spend
    months -= 1

need_money -= salary * 10
# TODO Оформить решение

print(round(need_money))
