def main():
    num = int(input())
    a = list(input().split())
    uniq = {}
    for i in range(num):
        if a[i] not in uniq:
            uniq[a[i]] = 1
        elif a[i] in uniq:
            uniq[a[i]] += 1

    maxi_count = 0
    num_often = None
    for p in uniq:
        curr_count = uniq[p]
        curr_num = int(p)
        if (curr_count > maxi_count) or (curr_count == maxi_count and curr_num > num_often):
            maxi_count = curr_count
            num_often = curr_num
    print(num_often)


if __name__ == '__main__':
    main()
