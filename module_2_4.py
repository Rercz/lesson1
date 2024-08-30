numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
n = 2
for i in range(2, 16):
    if i % n == 0:
        primes.append(i)
for j in range(2, 16):
     if j % n != 0:
      not_primes.append(j)
print(f'''Primes: {primes}''')
print(f'''Not primers: {not_primes}''')