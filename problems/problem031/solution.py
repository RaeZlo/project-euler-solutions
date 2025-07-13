def coin_sums(target: int, coins: list[int]) -> int:
    if target < 0:
        raise ValueError("Target must be a non-negative integer")
    
    coins = sorted(set(coins))

    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]
