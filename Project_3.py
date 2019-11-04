# Программа кодирует символы в азбуку морзе.

message=input('Сообщение для передачи:')
i=len(message)
print('Результат:')
for i in message:
    if i == 'а':
        symbol = ('• —')
        print(symbol)
    elif i == 'б':
        symbol = ('— • • •')
        print(symbol)
    elif i == 'в':
        symbol = ('• — —')
        print(symbol)

    elif i == 'г':
        symbol = ('— — •')
        print(symbol)

    elif i == 'д':
        symbol = ('— • •')
        print(symbol)

    elif i == 'е':
        symbol = ('• ')
        print(symbol)

    elif i == 'ё':
        symbol = ('• ')
        print(symbol)

    elif i == 'ж':
        symbol = ('• • • —')
        print(symbol)

    elif i == 'з':
        symbol = ('— — • •')
        print(symbol)

    elif i == 'и':
        symbol = ('• •')
        print(symbol)

    elif i == 'к':
        symbol = ('— • —')
        print(symbol)

    elif i == 'л':
        symbol = ('• — • •')
        print(symbol)

    elif i == 'м':
        symbol = ('— —')
        print(symbol)

    elif i == 'н':
        symbol = ('— •')
        print(symbol)

    elif i == 'о':
        symbol = ('— — —')
        print(symbol)

    elif i == 'п':
        symbol = ('• — — •')
        print(symbol)

    elif i == 'р':
        symbol = ('• — •')
        print(symbol)

    elif i == 'с':
        symbol = ('• • •')
        print(symbol)

    elif i == 'т':
        symbol = ('—')
        print(symbol)

    elif i == 'у':
        symbol = ('• • —')
        print(symbol)

    elif i == 'ф':
        symbol = ('• • — •')
        print(symbol)

    elif i == 'х':
        symbol = ('• • • •')
        print(symbol)

    elif i == 'ц':
        symbol = ('— • — •')
        print(symbol)

    elif i == 'ч':
        symbol = ('— — — ')
        print(symbol)

    elif i == 'ш':
        symbol = ('— — — —')
        print(symbol)

    elif i == 'щ':
        symbol = ('— — • —')
        print(symbol)

    elif i == 'ъ':
        symbol = ('— — • — —')
        print(symbol)

    elif i == 'ы':
        symbol = ('— • — —')
        print(symbol)

    elif i == 'ь':
        symbol = ('— • • —')
        print(symbol)

    elif i == 'ю':
        symbol = ('• • — —')
        print(symbol)

    elif i == 'я':
        symbol = ('• — • —')
        print(symbol)

    elif i == '.':
        symbol = ('• • • • • •')
        print(symbol)

    elif i == ',':
        symbol = ('• — • — • —')
        print(symbol)

    elif i == ':':
        symbol = ('— — — • • •')
        print(symbol)

    elif i == ';':
        symbol = ('— • — • —')
        print(symbol)

    elif i == '(':
        symbol = ('— • — — • —')
        print(symbol)

    elif i == ')':
        symbol = ('— • — — • —')
        print(symbol)

    elif i == '"':
        symbol = ('• — • • — •')
        print(symbol)

    elif i == '?':
        symbol = ('• • — — • •')
        print(symbol)

    elif i == '!':
        symbol = ('— — • • — —')
        print(symbol)

    elif i == '-':
        symbol = ('— • • • • —')
        print(symbol)

    elif i == ' ':
        symbol = ('.......')
        print( symbol)
