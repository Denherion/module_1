numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
not_Primes = []
for i in range(0, len(numbers)):
    is_prime = True
    if numbers[i] > 1:
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            Primes.append(numbers[i])
        elif not is_prime:
            not_Primes.append(numbers[i])
print(Primes)
print(not_Primes)