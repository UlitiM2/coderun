n = int(input())
synonyms = {}
for _ in range(n):
    a = input().split()
    synonyms[a[0]] = a[1]

word = input()
if word in synonyms:
    print(synonyms[word])
else:
    for i in synonyms:
        if synonyms[i] == word:
            print(i)


