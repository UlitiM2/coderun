word = input().strip()
count = {}

n = len(word)
for i in range(n):
    char = word[i]
    cnt = (i + 1) * (n - i)
    if char in count:
        count[char] += cnt
    else:
        count[char] = cnt

for char in sorted(count.keys()):
    print(f"{char}: {count[char]}")
