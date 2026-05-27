def find_fewest_coins(coins, target):
    coins.sort()
    if target == 0:
        return []
    elif target < 0:
        raise ValueError("target can't be negative")
    elif target < coins[0]:
        raise ValueError("can't make target with given coins")
    n_coins = len(coins)
    length_indexes = 1
    indexes = [0]
    result = [coins[0]]
    check = 0
    while sum(result) != target and check < 1000: #bruteforce
        check += 1
        cursor = length_indexes - 1
        complete = False
        while not complete:
            indexes[cursor] += 1
            if indexes[cursor] == n_coins:
                if cursor > 0:
                    indexes[cursor] = 0
                    cursor -= 1
                else:
                    length_indexes += 1
                    indexes = [0] * length_indexes
                    complete = True
            else:
                complete = True
        result = [coins[index] for index in indexes]
    if sum(result) != target and check >= 1000:
        rest = target
        result = []
        while rest != 0: #greedy fallback
            for i in range(len(coins)-1, -1, -1):
                if coins[i] <= rest:
                    rest -= coins[i]
                    result.append(coins[i])
                    break
            if rest < coins[0]:
                break
        result.reverse()
    if sum(result) != target:
        raise ValueError("can't make target with given coins")
    return result