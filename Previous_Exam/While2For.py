# # 8 Parallelltrapets Arean
# def Trapezoid(h, a, b):
#     area = (a+b)/2*h
#     return area


# print("# 8 area is ", Trapezoid(2, 3, 6))

# # 9 While2For
# f = 1
# j = 1
# for i in range(4):
#     f *= j
#     j += 1

# print('# 9 f = ', f)

# # 10 reflecList


# def reflectList(lst):
#     newList = []
#     j = -1
#     for i in range(len(lst)):
#         newList.append(lst[-i-1])

#         # j -= 1

#     return newList


# lst = [1, 3, 4, 2]
# print("# 10 ", reflectList(lst))

# # 11 평균 구하기

# numbers = input("input numbers:")
# num_lst = [float(number) for number in numbers.split()]

# sum = 0
# for number in num_lst:
#     sum += number

# print("#11: average is ", sum/len(num_lst))


# # 12 피보나치
# def Fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)


# n = int(input("# 12 input n:"))

# print(Fibonacci(n))


# 13 합 함수

def addera(string):
    sum = 0
    lst = [int(number) for number in string.split()]

    for n in lst:
        sum += n
    return sum


# numbers = input("input numbers:")
# num_lst = [int(number) for number in numbers.split()]
# print(addera(num_lst))
print(addera('10 15 7 4'))
print(addera('6'))
print(addera('3 2 -10'))
