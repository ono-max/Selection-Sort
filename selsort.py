def SelSort(num):
    steps = 0
    n = len(num)
    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1, n):
            if num[mp] > num[i]:
                mp = i
        if mp != bottom:
            num[mp], num[bottom] = num[bottom], num[mp]
            steps += 1
    return num
