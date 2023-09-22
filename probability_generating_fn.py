# adapted from https://math.stackexchange.com/questions/970523/how-many-ways-can-the-sum-of-n-dice-be-s
from math import comb, floor
import sys

def generate_probability(n, k, d):
    """
    Calculate the probability of obtaining a specified sum when throwing n fair dice with d sides each.

    Args:
        n (int): The number of fair dice thrown.
        k (int): The specified sum of the dice thrown.
        d (int): The number of sides each die has.

    Returns:
        float: The probability of obtaining the specified sum.

    Raises:
        ValueError: If any of the input values (n, k, d) are less than 1.
    """
    
    if n < 1 or k < 1 or d < 1:
        raise ValueError("All input values (n, k, d) must be greater than or equal to 1.")

    denominator = d ** n
    i_max = floor((k - n) / d)
    numerator = sum([(-1) ** i * comb(n, i) * comb(k - d * i - 1, k - d * i - n) for i in range(0, i_max + 1)])

    return numerator, denominator, numerator / denominator

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python probability_generating_fn.py <number_of_dice> <specified_sum> <number_of_sides>")
        sys.exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2])
    d = int(sys.argv[3])

    for i in range(1, k+1):
        numerator, denominator, probability = generate_probability(n, i, d)
        print(f"P(Sum of {i:^3} when throwing {n} dice with {d} sides each) = {probability:.6f}, {numerator:^3} ways out of a total of {denominator} ways")
