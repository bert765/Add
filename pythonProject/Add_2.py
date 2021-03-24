from Open import lstData
# Словарь для обработки массива - сравнение значений и передача в функцию
testDict = {'Hlv1': ['=01', '=1', '= 1'], 'dels': ['=', '(', 'ЭЭЭ'],
            'HLv7': ['=7', '=07', '= 7'], 'HLv8': ['=8', '=08', '= 8'],
            'HLv9': ['=9', '=09', '= 9'], 'Sha': ['-', '/', 'Щ']}
AddN = 5    # Значение вводимой поправки


# Функция для добавления поправки в массив
def add_num(lst, pos, r1, r2, r3):
    for x in range(r1, r2, r3):
        if str(lst[pos + x]) not in testDict['Sha']:
            lst[pos + x] = lst[pos + x] + AddN


# Обработка массива из файла
for i in range(0, len(lstData), 1):
    for n, m in testDict.items():
        if lstData[i] in m:
            if n == 'Hlv1':
                add_num(lstData, i, 7, 8, 1)
            elif n == 'HLv7':
                add_num(lstData, i, 1, 25, 1)
                lstData[i + 18] = '\n' + str(lstData[i + 18])
            elif n == 'HLv8':
                add_num(lstData, i, 2, 5, 2)
            elif n == 'HLv9':
                add_num(lstData, i, 2, 9, 2)
