# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только
# арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
# делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.





numb = 1
final = 0

while numb < 1000:
    sum = 0
    numb += 1
    result = numb
    if result % 2:
        result = result ** 3
        numb_remember = result
        while (result != 0):
            sum = sum + result % 10
            result = result // 10
            if result == 0 and sum % 7 == 0:
                final += numb_remember
print(final)

numb = 1
final = 0

while numb < 1000:
    sum = 0
    numb += 1
    result = numb
    if result % 2:
        result = result ** 3
        result += 17
        numb_remember = result
        while (result != 0):
            sum = sum + result % 10
            result = result // 10
            if result == 0 and sum % 7 == 0:
                final += numb_remember
print(final)