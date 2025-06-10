n = int(input())
correct = {}
for _ in range(n):
    curr_word = input()
    if curr_word.lower() not in correct:
        correct[curr_word.lower()] = [curr_word]
    else:
        correct[curr_word.lower()].append(curr_word)

check_string = input()
errors = 0
for word in check_string.split():
    if word.lower() in correct:
        if word in correct[word.lower()]:
            continue
        else:
            errors += 1
    else:
        count_upper = 0
        for char in word:
            if char.isupper():
                count_upper += 1
        if count_upper != 1:
            errors += 1

print(errors)
