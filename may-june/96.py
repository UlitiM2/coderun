n, k = map(int, input().split())
string = input()

count_letters = {}
max_length = 0
best_left = 0
left = 0

for right in range(n):
    char = string[right]
    count_letters[char] = count_letters.get(char, 0) + 1

    while count_letters[char] > k:
        left_char = string[left]
        count_letters[left_char] -= 1
        left += 1

    current_length = right - left + 1
    if current_length > max_length:
        max_length = current_length
        best_left = left

print(max_length, best_left + 1)
