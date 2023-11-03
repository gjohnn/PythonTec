def fibonacci_sequence(n):
    fib = [0, 1]
    for i in range(2, n):
        next_fib = fib[i - 1] + fib[i - 2]
        fib.append(next_fib)
    return fib

n = 10
fibonacci_numbers = fibonacci_sequence(n)
print("Los primeros 10 números de la sucesión de Fibonacci son: ")
for num in fibonacci_numbers:
    print(num)