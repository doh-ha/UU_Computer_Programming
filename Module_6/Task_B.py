def extend(x, n):
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

    new = new[n:len(r)-n]  # slice to the original size
    return new


def round_list(a_list, ndigits):
    for i in range(len(a_list)):

        # print(a_list[i])
        new_list = a_list.copy()
        new_list[i] = round(a_list[i], ndigits)
        # print(new_list[i])
    # print(new_list)
    return new_list


# main
x = [1, 2, 6, 4, 5, 0, 1, 2]
print('smooth_a(x, 1): ', smooth_a(x, 1))
print('smooth_a(x, 1) rounded: ', round_list(smooth_a(x, 1), 2))
