def mysumneg():
    nums = [2, 6, -2, -80]
    sumneg = 0
    for x in nums:
        if x < 0 :
            sumneg +=x
        else:
            continue
    return sumneg

print(" sum of neg numbers: ", mysumneg())
