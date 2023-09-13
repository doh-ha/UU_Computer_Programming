def smooth_a(a, n):
    # extend left side
    r = [0 for i in range(len(x)+n)]

    # add original list
    r[n:] = a

    # extend right side
    for i in range(n):
        r.append(0)

    # extend the value of the side
    for i in range(n):
        r[i] = a[0]  # left
        r[-i-1] = a[-1]  # right

    new = r.copy()  # copy

    # calculate the value
    for i in range(len(a)):
        sum = r[i+n]  # itslef
        for j in range(n):
            sum += r[i+n-(j+1)]
            # print("index is ", i+n-(j+1))
            sum += r[i+n+(j+1)]

        # print("sum is ", sum)
        new[i+n] = sum/(2*n+1)
        # print("r is ", r)
        # print("new is ", new)

    new = new[n:len(r)-n]  # slice to the original size
    return new


# def smooth_b(a, n):
#     print(n)


x = [1, 2, 6, 4, 5, 0, 1, 2]
print('smooth_a(x, 1): ', smooth_a(x, 1))
print('smooth_a(x, 2): ', smooth_a(x, 2))
# print('smooth_b(x, 1): ', smooth_b(x, 1))
# print('smooth_b(x, 2): ', smooth_b(x, 2))
