def knapsack(capacity, weights, values, n):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.

    Parameters:
    capacity (int): The maximum weight capacity of the knapsack.
    weights (list of int): A list of weights of the items.
    values (list of int): A list of values of the items.
    n (int): The number of items.

    Returns:
    int: The maximum value that can be put in a knapsack of given capacity.
    """
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][capacity]


# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)
print(
    "Maximum value in Knapsack =", knapsack(capacity, weights, values, n)
)  # Output: 220
