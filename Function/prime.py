def prime_function(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main_function():
    print("I m checking the prime numbers")
    number=17
    if(prime_function(number)):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
main_function()
