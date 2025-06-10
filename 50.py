import sys

sys.stdin = open('50.txt')
string = sys.stdin.read().split()

uniq_words = {}
for word in string:
    uniq_words[word] = uniq_words.get(word, 0) + 1

count_max = max(uniq_words.values()) if uniq_words else 0
all_maximums = []
for j in uniq_words.keys():
    if uniq_words[j] == count_max:
        all_maximums.append(j)

print(sorted(all_maximums)[0])
