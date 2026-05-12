def is_prime(n):
    # Bug: This range skips the check for the number 2
    # and doesn't handle n=2 correctly.
    if n <= 1:
        return False
    
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    return True

# Testing the code
test_number = 2
if is_prime(test_number):
    print(f"{test_number} is prime")
else:
    print(f"{test_number} is not prime") # This will trigger incorrectly
