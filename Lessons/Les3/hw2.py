def data(name, surname, birth_date, city, email, phone):
    print("Данные пользователя:")
    print(f"{name}, {surname}, {birth_date}, {city}, {email}, {phone}")



data(      name = input('Введите имя\n'),
           surname = input('Введите фамилию\n'),
           birth_date = input('Введите год рождения\n'),
           city = input('Введите город\n'),
           email = input('Введите Email\n'),
           phone = input('Введите номер телефона\n'))

