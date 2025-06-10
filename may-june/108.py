def find_median(all_seq, num_of_seq, num_of_seq_2, L):
    i = 0
    j = 0
    total_sequence = []
    while i < L and j < L:
        if all_seq[num_of_seq][i] <= all_seq[num_of_seq_2][j]:
            total_sequence.append(all_seq[num_of_seq][i])
            i += 1
        else:
            total_sequence.append(all_seq[num_of_seq_2][j])
            j += 1

    if i != L:
        total_sequence.extend(all_seq[num_of_seq][i:])
    elif j != L:
        total_sequence.extend(all_seq[num_of_seq_2][j:])
    return total_sequence[L - 1]


N, K = map(int, input().split())
all_sequences = []
for _ in range(N):
    sequence = list(map(int, input().split()))
    all_sequences.append(sequence)

for obj in range(N-1):
    for second_obj in range(obj+1, N):
        print(find_median(all_sequences, obj, second_obj, K))
