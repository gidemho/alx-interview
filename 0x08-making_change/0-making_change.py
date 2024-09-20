#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    Args:
        coins (list): The values of the coins in your possession.
        total (int): The total amount to meet.
    Returns:
        int: The fewest number of coins needed to meet the total,
             or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total <= 0:
            break
        # Determine how many of this coin can fit into the remaining total
        count += total // coin
        total %= coin

    # If total is not 0, it means it's not possible to meet the total
    if total != 0:
        return -1

    return count
