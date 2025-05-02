from typing import List


def collatz(n: int) -> List[int]:
    """
    You're given a positive integer n. Write an algorithm that does the following:
        - If n is even, the algorithm divides n by 2. This is the new value of n
        - If n is odd, the algorithm multiplies it by 3 and adds 1. This is the new value of n.
        - The algorithm repeats this until n == 1.

    Implement this algorithm in this function and return a list of all the intermediate values of n.
    For example, if n = 3, the sequence of values is: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    So, your function would return: [3, 10, 5, 16, 8, 4, 2, 1]
    """
    # Make sure we're working with a positive number
    if n < 1:
        raise ValueError("Need a positive number to start with!")
    
    # Start with our initial number
    result = [n]
    
    # Keep going until we hit 1
    while n > 1:
        # Check if the number is even
        if n % 2 == 0:
            n = n // 2  # Divide by 2 for even numbers
        else:
            n = 3 * n + 1  # Multiply by 3 and add 1 for odd numbers
        result.append(n)  # Add the new number to our sequence
    
    return result


def distinct_numbers(numbers: List[int]) -> int:
    """
    You are given a list of integers (the list could be empty), calculate the number of distinct/unique values in the list.

    E.g if numbers = [2, 3, 2, 2, 3], then the answer is 2 since there are only 2 unique numbers: 2 and 3.
    """
    # Convert to set to remove duplicates, then count unique elements
    unique_nums = set(numbers)
    return len(unique_nums)
