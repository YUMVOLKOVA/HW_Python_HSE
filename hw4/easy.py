def fibonacci(n):
    list_with_numbers = [0, 1]
    if n == 1:
        return list_with_numbers[0]
    elif n == 2:
        return list_with_numbers[1]
    else:
        for i in range(1, n):
            list_with_numbers.append(list_with_numbers[i] + list_with_numbers[i - 1])
        return list_with_numb