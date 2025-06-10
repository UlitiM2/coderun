import sys

input_string = sys.stdin.read()
input_string = input_string.replace('\n', '')
input_string = input_string.replace(' ', '')

dict_for_letters = {}
for i in input_string:
    if i not in dict_for_letters:
        dict_for_letters[i] = 1
    else:
        dict_for_letters[i] += 1

dict_sort = sorted(dict_for_letters)
curr_max = max(dict_for_letters.values())

for level in range(curr_max, 0, -1):
    line = []
    for char in dict_sort:
        if dict_for_letters[char] >= level:
            line.append('#')
        else:
            line.append(' ')
    print(''.join(line))

print(''.join(dict_sort))


