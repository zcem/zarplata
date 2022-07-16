from colorama import *
init()

print(Fore.YELLOW + Style.BRIGHT + 'Приветствую вас. Эта программа предназначена для расчета заработной платы работников нашего '
                     'завода.')
print(Fore.YELLOW + 'Внимание, незабывайте что ночные начинаются в 22:00 и заканчиваются в 06:00.')
print(Fore.YELLOW + 'Вводите только числа, если премии нет - значит 0')

oklad = float(input('Введите оклад: '))
hours = float(input('Введите количество часов по графику: '))
nighthours = float(input('Введите сколько из них ночных часов по графику: '))
rv = float(input('Введите количество часов РВ: '))
premia = float(input('Введите вашу премию: '))
nadbavka = float(input('Введите вашу надбавку: '))
drd = float(input('Введите ваше ДРД: '))
print('Теперь введите данные для расчета аванса: ')
avahour = float(input('Введите сколько часов до 15 числа включительно: '))
nightava = float(input('Введите сколько ночных часов до 15 числа включительно: '))
rvavans = float(input('Введите РВ часы до 15 числа включительно: '))

hour = oklad / hours # Оклад делим на количество часов по графику, для вычисления стоимости часа
night = hour * 0.2 # Часовую ставку умножаем на 20%, для вычисления добавки за ночные.

nightall = night * nighthours # Стоимость ночных
rvall = rv * hour * 2 # Стоимость РВ

pay = nightall + oklad + rvall + premia + nadbavka + drd # Месяц грязными
avans = hour * avahour + night * nightava + (hour*2*rvavans) # Аванс грязными

clear = pay - (pay / 100 * 13) # Зарплата на руки после вычета 13%
clearava = avans - (avans / 100 * 13) # Аванс чистыми после вычета 13%
cleartwo = clear - clearava # Остаток чистыми за вторую половину месяца

print(Fore.RED + 'Заработная платa за месяц равна: ' + str(pay))
print('Аванс: ' + str(avans))

print(Fore.GREEN + 'Чистыми аванс: ' + str(clearava))
print('Чистыми остаток за вторую половину: ' + str(cleartwo))
print('Всего чистыми за месяц: ' + str(clear))


end = input('Нажмите Enter для завершения')
