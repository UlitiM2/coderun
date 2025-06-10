from collections import defaultdict

with open('input.txt', 'r') as file:
    text = file.read()

words = text.split()

uniq_words = defaultdict(int)
count_words = []

for word in words:
    count_words.append(str(uniq_words[word]))
    uniq_words[word] += 1

print(' '.join(count_words))
