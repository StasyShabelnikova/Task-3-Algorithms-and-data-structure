def two_sum(data, target):
    cache = {}

    for i, num in enumerate(data):
        diff = target - num

        if diff in cache:
            return [cache[diff], i]

        cache[num] = i

    return []