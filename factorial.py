def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i

    print(f"Factorial of {n} is {result}")
    return result
