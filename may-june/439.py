text = input()
uniq_pairs = {}

for i in range(len(text) - 1):
    if text[i] != ' ' and text[i+1] != ' ':
        uniq_pairs[text[i]+text[i+1]] = uniq_pairs.get(text[i]+text[i+1], 0) + 1

max_freq = max(uniq_pairs.values())
candidates = [pair for pair, count in uniq_pairs.items() if count == max_freq]
result = max(candidates)

print(result)
