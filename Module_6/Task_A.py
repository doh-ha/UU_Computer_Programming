def smooth_a(a, n):

    r = [0 for i in range(len(x)+2*n)]

    for i in range(n):

        r.insert(i, a[0])  # extend left side
        r.insert(i-n, a[-1])  # extend right side

    print(r)

    for i in range(len(a)):
        sum = r[i+n]
        for j in range(n):

            sum += r[i+n-(j+1)]
            print("index is ", i+n-(j+1))
            sum += r[i+n+(j+1)]

        # print("sum is ", sum)
        r[i+n] = sum/(2*n+1)

    r = r[n:len(r)-n]  # slice to the original size
    return r


# def smooth_b(a, n):
#     print(n)


x = [1, 2, 6, 4, 5, 0, 1, 2]
# print('smooth_a(x, 1): ', smooth_a(x, 1))
print('smooth_a(x, 2): ', smooth_a(x, 2))
# print('smooth_b(x, 1): ', smooth_b(x, 1))
# print('smooth_b(x, 2): ', smooth_b(x, 2))
