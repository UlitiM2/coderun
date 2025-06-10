def main():
    num = int(input())
    mass = []
    mass_multi = []
    for _ in range(num):
        a, b = list(input().split())
        mass.append([a, b])
    for i in mass:
        mass_multi.append(int(i[0])*int(i[1]))
    suma = sum(mass_multi[:])
    for j in range(num):
        p = mass_multi[j] / suma
        print(round(p, 12))


if __name__ == '__main__':
    main()
