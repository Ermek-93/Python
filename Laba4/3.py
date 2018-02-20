numLength = 10
alphabetLength = 26
n = int(input("Длина пароля: "))

casesAmount = (numLength + alphabetLength) ** n
print("Варианты паролей: %s" % casesAmount)
print("Шанс угадать пароль с первой попытки: %s%%" % (1 / casesAmount * 100))
