import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import csv
dic = {}


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


def read_csv_to_list(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in reader:

            if line_count == 0:
                line_count += 1
            else:

                country_code = row[1].lower()
                strList = row[3:]
                floatList = list(map(float, strList))
                dic[country_code] = floatList

            # rows.append(row)


row = read_csv_to_list("Module_8/CO2Emissions_filtered.csv")
print(dic)

# get values with key
dnk_list = dic.get("dnk")
fin_list = dic.get("fin")
isl_list = dic.get("isl")
nor_list = dic.get("nor")
swe_list = dic.get("swe")

# create the frame of the figure
fig, ax = plt.subplots()
time = list(range(1960, 2015))

# original
ax.plot(time, dnk_list, linestyle='dotted', color="blue")
ax.plot(time, fin_list,  linestyle='dotted', color="orange")
ax.plot(time, isl_list, linestyle='dotted', color="green")
ax.plot(time, nor_list, linestyle='dotted', color="red")
ax.plot(time, swe_list, linestyle='dotted', color="purple")

# smooth_a
ax.plot(time, smooth_a(dnk_list, 5), label='dnk',
        linestyle="solid", color="blue")
ax.plot(time, smooth_a(fin_list, 5), label="fin",
        linestyle='solid', color="orange")
ax.plot(time, smooth_a(isl_list, 5), label='isl',
        linestyle='solid', color="green")
ax.plot(time, smooth_a(nor_list, 5), label='nor',
        linestyle='solid', color="red")
ax.plot(time, smooth_a(swe_list, 5), label='swe',
        linestyle='solid', color="purple")

# smooth_b
ax.plot(time, smooth_b(dnk_list, 5),
        linestyle="dashed", color="blue")
ax.plot(time, smooth_b(fin_list, 5),
        linestyle="dashed", color="orange")
ax.plot(time, smooth_b(isl_list, 5),
        linestyle="dashed", color="green")
ax.plot(time, smooth_b(nor_list, 5),
        linestyle="dashed", color="red")
ax.plot(time, smooth_b(swe_list, 5),
        linestyle="dashed", color="purple")

# UI
ax.set_xlabel('Year')
ax.set_ylabel('CO2 Emmissions (kt)')
ax.set_title("Yearly Emmissions of CO2 in the Nordic Countries")


ax.legend()
plt.show()
