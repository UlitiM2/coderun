def solve():
    import sys
    m, n = map(int, input().split())
    
    if n == 1:
        print(1)
        return
    
    # Инициализация DP: dp[i][last][mask]
    dp = [[[0] * (1 << m) for _ in range(m + 2)] for __ in range(n + 2)]
    
    # Базовый случай: первая полоса (i=1)
    for subset in range(1, 1 << m):
        last = 0
        mask = 0
        for k in range(m):
            if subset & (1 << k):
                last = k + 1
                mask |= (1 << k)
        dp[1][last][mask] += 1
    
    # Заполнение DP для i от 2 до n
    for i in range(2, n + 1):
        for prev_last in range(1, m + 1):
            for prev_mask in range(1 << m):
                if dp[i-1][prev_last][prev_mask] == 0:
                    continue
                # Перебираем все возможные подмножества направлений для текущей полосы
                for subset in range(1, 1 << m):
                    current_last = 0
                    current_mask = 0
                    valid = True
                    # Проверяем, что все направления в subset >= prev_last
                    for k in range(m):
                        if subset & (1 << k):
                            if (k + 1) < prev_last:
                                valid = False
                                break
                            current_last = max(current_last, k + 1)
                            current_mask |= (1 << k)
                    if not valid:
                        continue
                    new_mask = prev_mask | current_mask
                    dp[i][current_last][new_mask] += dp[i-1][prev_last][prev_mask]
    
    # Суммируем все dp[n][last][mask], где mask покрывает все направления
    total = 0
    for last in range(1, m + 1):
        for mask in range(1 << m):
            if mask == (1 << m) - 1:
                total += dp[n][last][mask]
    
    print(total)

solve()
