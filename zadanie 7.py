N, K, M = map(int,input().split())
distance = (M - K) if M > K else (M + N - K)
print(distance - 1)