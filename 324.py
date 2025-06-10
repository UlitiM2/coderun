N, M = input().split()
price = sorted(map(int, input().split()))
cost_for_customers = sorted(map(int, input().split()), reverse=True)
sum_of_profit = 0
for i in range(0, min(len(price), len(cost_for_customers))):
    if (cost_for_customers[i] - price[i]) > 0:
        sum_of_profit += (cost_for_customers[i] - price[i])
    else:
        break
print(sum_of_profit)
