def F(a, b):

    if b == 0:
        return 0

    elif a > b:
        return F(a - 1, b) + b

    elif b >= a and b > 0:
        return F(a, b - 1) + a


def div_finder(arr, a):

    for i in range(2, a + 1):

        if a % i == 0:
            arr.append(i)
            div_finder(arr, a // i)
            return(arr)

# Так как 2097152 = 2 ** 21, а функция F, по сути, представляет собой умножение натуральных чисел,
# то a и b могут быть различными степенями двойки от 0 до 21, дающими в произведени 2 ** 21.
# Значит, различных a 22 шт.: от 2 ** 0 до 2 ** 21.
