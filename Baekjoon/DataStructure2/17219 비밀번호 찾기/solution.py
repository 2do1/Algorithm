import sys
n, m = map(int, input().split())

login = {}

for _ in range(n):
    ip, password = sys.stdin.readline().split()

    login[ip] = password

for _ in range(m):
    ip = sys.stdin.readline().rstrip()

    print(login[ip])