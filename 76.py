N, K, M = map(int, input().split())

total_details = 0

while N >= K:
    blanks = N // K
    remainder_blanks = N % K
    details_per_blank = K // M
    if details_per_blank == 0:
        break
    total_details += blanks * details_per_blank
    remainder_details = blanks * (K % M)
    N = remainder_blanks + remainder_details

print(total_details)
