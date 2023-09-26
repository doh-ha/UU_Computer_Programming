
from collections import Counter

words_cnt = 0
diff_cnt = 0
dic = {}
n = int(input("input n:"))
# m = int(input("input m:"))
with open(r"/Users/Doh/Developer/UU_Computer_Programming/Module_7/TextFile.rtf", 'r') as file:
    text = file.read().lower()
    words = text.split()
    words_cnt = len(words)

    # store multiple items in a single variable
    diff_cnt = len(set(text.split()))

    # for character in text:
    #     if character.isalpha():
    #         character = character.lower()
    print(text.split())

    Counter = Counter(words)
    most_words = Counter.most_common(n)

    print(words)


print('1. Total number of words: ', words_cnt)
print('2. Number of different words: ', diff_cnt)
print('3. n most common words: ', most_words)

# print('4. m least words: ', least_words)
