# Создать калькулятор — программу, в которой мы вводим 2 числа, и с ними производятся
# сразу все математические действия, рассмотренные в уроке.

a = int(input("введите первое число: "))
b = int(input("введите второе число: "))

plus = a + b
minus = a - b
mult = a * b
devide = a / b
devide_int = a // b
dev_residue = a % b
power = a ** b

print("сложение: ",plus)
print("вычитание: ", minus)
print("умножение: ", mult)
print("деление: ", devide)
print("целая часть от деления: ", devide_int)
print("остаток от деления: ", dev_residue)
print("возведение в степень: ", power)