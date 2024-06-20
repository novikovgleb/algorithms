def min_cost(N, A, B, C, D):
    max_cost = N
    dp = [max_cost] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + 1
        if i >= A:
            dp[i] = min(dp[i], dp[i - A] + B)
        else:
            dp[i] = min(dp[i], B)
        if i >= C:
            dp[i] = min(dp[i], dp[i - C] + D)
        else:
            dp[i] = min(dp[i], D)
    return dp[N]
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
print(min_cost(N, A, B, C, D))