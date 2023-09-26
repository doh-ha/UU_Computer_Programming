
import re
words_cnt = 0


with open(r"/Users/Doh/Developer/UU_Computer_Programming/Module_7/TextFile.rtf", 'r') as file:
    text_with_symbols = file.read().lower()
    text = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]',
                  " ", text_with_symbols)
    counts = dict()

    words = text.split()

    counts = dict()
    for word in words:
        words_cnt += 1  # for total words
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    sorted_counts = sorted(
        counts.items(), key=lambda x: x[1], reverse=True)
    print(sorted_counts)

    def most_common(n):
        return (sorted_counts[:n])

    def least_common(m):
        return (sorted_counts[-m:])


print('1. Total number of words: ', words_cnt)
print('2. Number of different words: ', len(counts))
n = int(input("input n:"))
print('3. n most common words: ', most_common(n))
m = int(input("input m:"))
print('4. m least words: ', least_common(m))
