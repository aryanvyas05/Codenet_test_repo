def factorial(n):
    """Compute factorial of n recursively."""
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    """Return first n Fibonacci numbers."""
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]
