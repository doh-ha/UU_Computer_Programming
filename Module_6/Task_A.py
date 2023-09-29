def extend(x, n):
    # extend left side 000000000
    r = [0 for i in range(len(x)+n)]

    # add original list
    r[n:] = x

    # extend right side
    for i in range(n):
        r.append(0)

    return r


def smooth_a(x, n):
    r = extend(x, n)

    # extend the value of the side
    for i in range(n):
        r[i] = x[0]  # left
        r[-i-1] = x[-1]  # right

    new = r.copy()  # copy

    # calculate the value
    for i in range(len(x)):
        sum = r[i+n]  # itslef
        for j in range(n):
            sum += r[i+n-(j+1)]
            sum += r[i+n+(j+1)]
        new[i+n] = sum/(2*n+1)

    new2 = new[n:len(r)-n]  # slice to the original size
    return new2


def smooth_b(x, n):

    r = extend(x, n)
    new = r.copy()  # copy
    # print(r)
    # calculate the value
    for i in range(len(x)):
        sum = r[i+n]  # itslef
        num = 1
        for j in range(n):
            sum += r[i+n-(j+1)]  # left

            if (i+n-(j+1) >= n):
                num += 1
            sum += r[i+n+(j+1)]  # right
            if (i+n+(j+1) <= len(r)-n-1):
                num += 1

        new[i+n] = sum/num

    new2 = new[n:len(r)-n]  # slice to the original size
    return new2


# main
x = [1, 2, 6, 4, 5, 0, 1, 2]
print('smooth_a(x, 1): ', smooth_a(x, 1))
print('smooth_a(x, 8): ', smooth_a(x, 8))
print('smooth_b(x, 2): ', smooth_b(x, 2))
print('smooth_b(x, 2): ', smooth_b(x, 2))
