#ввод переменных

years = int(input('Введите год рождения: '))

month = int(input('Введите месяц рождения: '))

years_now = int(input('Введите сейчашний год: '))

month_now = int(input('Введите сейчашний месяц: '))

#сколько лет (без расчета месяцев)

s = years_now - years

#сколько полных месяцев

month_age = month + month_now

if month_age >= 12:

   s -= 1

print(s)
