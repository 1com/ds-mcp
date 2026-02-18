# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b
        
        
print(f"First 10 Fibonacci numbers:")
fibonacci_iterative(10)