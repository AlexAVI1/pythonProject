price = 0
while True:
    try:
        tickets = input('Укажите, пожалуйста, количество билетов, которое Вы хотите приобрести на онлайн-конференцию? ')
        tickets = int(tickets)
        if type(tickets) == int:
            break
    except ValueError:
        print('Введено некорректное значение. Введите количество билетов, которое необходимо пробрести')
for item in range(tickets):
    item += 1
    while True:
        try:
            age = input(f'Возраст посетителя по {item} билету? ')
            age = int(age)
            if age < 18:
                print('Проход бесплатный')
            elif 25 > age >= 18:
                price += 990
                print('Стоимость билета: 990 руб.')
            else:
                price += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Введено некорректное значение. Укажите полное количество лет')
if tickets > 3:
    price = price - ((price / 100) * 10)
    print(f'Сумма к оплате {price} руб. '
          f'с учётом дополнительной скидки в 10% на полную стоимость заказа за регистрацию больше 3-х человек')
else:
    print(f'Сумма к оплате {price} руб.')