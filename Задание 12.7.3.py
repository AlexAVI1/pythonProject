money = int(input('Введите сумму, которую планируете положить под процент на год '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for item in per_cent:
    deposit.append(per_cent[item] * money/100)
print('Максимальная сумма, которую вы можете заработать -', max(deposit))


