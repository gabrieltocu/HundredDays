def is_prime(num):
    if num > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (num//2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

print(is_prime(73))