

infil = open(
    "/Users/Doh/Developer/UU_Computer_Programming/Module_7/TextFile.rtf", 'r')
print(infil.read())

word = infil.split()
print(word)
# print('1. Total number of words: ', word_cnt)

infil.close()
