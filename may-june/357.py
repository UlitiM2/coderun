from collections import defaultdict

n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)

vertices = set()
edges = defaultdict(int)

for word in words:
    n = len(word)
    if n < 3:
        continue
    trigrams = []
    for i in range(n - 2):
        trigram = word[i:i+3]
        trigrams.append(trigram)
        vertices.add(trigram)
    for i in range(len(trigrams) - 1):
        src = trigrams[i]
        dest = trigrams[i+1]
        edges[(src, dest)] += 1

v = len(vertices)
e = len(edges)
print(v)
print(e)
for (src, dest), weight in edges.items():
    print(src, dest, weight)
