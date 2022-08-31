'''4. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.'''

first_let = ord(input('Введите букву (латинский алф): ').lower())
scnd_let = ord(input('Введите вторую букву (латинский алф): ').lower())
first_let = first_let - ord('a') + 1
scnd_let = scnd_let - ord('a') + 1
let_betw = abs(scnd_let - first_let) - 1
print(f'Позиция первой буквы в алфавите: {first_let}, второй буквы: {scnd_let}, \nМежду ними {let_betw} букв(ы).')