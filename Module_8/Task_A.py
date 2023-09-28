import csv
dic = {}


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
