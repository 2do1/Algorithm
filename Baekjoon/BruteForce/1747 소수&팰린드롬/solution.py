import sys

n = int(sys.stdin.readline())

def is_prime_number(num):
    if n == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    return False

while True:    
    if is_prime_number(n) and is_palindrome(n):
        break
    n += 1

print(n)