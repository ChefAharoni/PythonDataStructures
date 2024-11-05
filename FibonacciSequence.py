def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        # Store the result in memo to avoid duplicate work
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# Example usage:
print("\nFibonacci sequence up to 10:")
for i in range(10):
    print(fibonacci(i), end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34
