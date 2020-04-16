#Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_number = int(input('Введите номер буквы латинского алфавита: '))

letter = chr(96 + letter_number)

print(letter)

