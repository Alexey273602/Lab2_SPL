def func(argument):
    if type(argument) == list:
        print(f'Изначальный список: {argument}')
        my_list = argument[::-1]
        summa = 0
        is_last_positive = 0
        for i in my_list:
            if i <= 0 and not is_last_positive:
                summa += i
            else:
                is_last_positive = 1
        for j in range(argument.count(0)):
            argument.remove(0)
        print(f'Сумма всех элементов после последнего положительного = {summa}')
        print(f'Измененный список: {argument}')
    elif type(argument) == dict:
        print(f'Изначальный словарь: {argument}')
        print(f'Ключ с минимальным значением: {min(argument, key=argument.get)}')
    elif type(argument) == float or type(argument) == int:
        print(f'Изначальное число: {argument}')
        print(f'Число в обратном порядке: {str(argument)[::-1]}')
    elif type(argument) == str:
        print(f'Изначальная строка: {argument}')
        argument = argument.split()
        print(f'Количество слов в строке = {len(argument)}')


while 1:
    print('1. Cписок\n'
          '2. Cловарь\n'
          '3. Число\n'
          '4. Строка\n')
    choice = input('Выберите пункт меню:')
    if choice == '1':
        a = [1, 0, 2, 0, -2, -3]
        func(a)
    elif choice == '2':
        a = {'a': 1, 'b': 4, 'c': 0, 'd': 5}
        func(a)
    elif choice == '3':
        a = 123.456
        func(a)
    elif choice == '4':
        a = 'Один два три четыре пять'
        func(a)
    else:
        print('Неверно выбран пункт меню')
