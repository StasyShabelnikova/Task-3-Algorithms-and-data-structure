def copy_time (n, x, y):
    
    if n < 0:
        raise ValueError("N should be non-negative")
    
    if n == 0:
        return n
    
    l = 0
    r = (n - 1) * max(x, y)

    while l < r:
        mid = (r + l) // 2
        if mid // x + mid // y >= n - 1 :
            r = mid
        else:
            l = mid + 1
    return l + min(x,y)