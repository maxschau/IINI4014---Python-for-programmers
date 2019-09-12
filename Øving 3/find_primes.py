#Method to find wether an input n is a prime or not
def find_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
#Variable to count how many primes we have found
counter = 0
#Variable to keep track of the number we are checking
input = 2
while counter < 1000:
    if find_prime(input):
        print(input)
        counter += 1 #Updating the counter variable
    input += 1 #Updating the index