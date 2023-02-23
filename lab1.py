def task1():
    number = int(input('Введите натуральное число: '))
    s = 1
    x = 1
    for n in range(1, number + 1):
        x = ((-1) ** n) / (2 ** n)
        s = x + s
    print('Член ряда ', x, 'сумма ряда ', s)




def task2():
    title = 'Python In Easy Steps'
    try:
        print(titel)
    except (NameError, IndexError) as msg:
        print(msg)
    day = 32
    try:
        if day > 31:
            raise ValueError('Invalid Day Number')
    except ValueError as msg:
        print( 'The Program found An' , msg )
    finally:
        print('But Today Is Beautiful Anyway.')

def complex_calc():
    str = input('Введите пример: ')
    result = complex(eval(str))
    print(f'Результат: {result}')

def task4():
    message1 = 'Улетел на луну'
    message2 = 'Ты попал в лужу'
    message3 = 'Улетел на Бали'
    message4 = 'Улетел в космос'
    message5 = 'Тебя сьел тиранозавр'
    message6 = 'Ты попал в бассейн'


    str = input('Введите число: ')
    if (str == '4'):
        print(message5)

    elif (str == '33'):
        str = input('Введите число: ')
        if (str == '1'):
            str = input('Введите число: ')
            if (str == '11'):
                print(message6)
            elif (str == '12'):
                print(message5)
            else:
                print('Вы ошиблись с вводом')



    elif (str == '3'):
        print('Вы никуда не попали')


    elif (str == '2'):
        str = input('Введите число: ')
        if (str == '21'):
            print(message5)
        elif (str == '22'):
            str = input('Введите число: ')
            if (str == '221'):
                print(message4)
            elif (str == '222'):
                print(message3)
            else:
                print('Вы ошиблись с вводом')

    elif (str == '32'):
        str = input('Введите число: ')
        if (str == '311'):
            print(message2)
        else:
            print('Вы ошиблись с вводом')

    elif (str == '31'):
        str = input('Введите число: ')
        if (str == '311'):
            print(message1)
        elif (str == '222'):
            print(message3)
        else:
            print('Вы ошиблись с вводом')
    else:
        print('Вы ошиблись с вводом')





if __name__ == '__main__':
   complex_calc()


