def print_sequence(n):
    for i in range(1, n+1):
        numbers = ""
        for j in range(0, i):
            numbers = numbers + str(i)
        print(numbers)

print_sequence(5)