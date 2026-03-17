N = int(input())

count_zero = 0

for _ in range(N):
    if int(input()) == 0:
        count_zero += 1

print(count_zero)