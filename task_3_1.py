def sqrt_num(n):
    if n<0:
        raise ValueError("n should be non-negative")
    l = 0
    r = n
    while l <= r:
        mid = (l + r) // 2
        sqrt = mid * mid
        if sqrt == n:
            return mid
        if sqrt > n:
            r = mid - 1
        else:
            l = mid + 1
    return r

        
