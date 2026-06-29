def primes(limit):
    primes = []
    if limit < 2:
        return primes
    for i in range(2,limit+1):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes