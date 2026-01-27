######################################################################
#   Function name : ChkPrime
#   Description   : return the prime number from the list 
#   Input         : List[]
#   Output        : List[]
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 23/01/2026
#######################################################################

def ChkPrime(numbers):

    primes = []
    is_prime = True

    for No in numbers:
        if No <= 1:
            continue  
        
        for i in range(2,No):
            if No % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(No)
    return primes

