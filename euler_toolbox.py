# A toolbox for functions shared between multiple solutions.


from math import sqrt  # for proper_divisor_sum, is_prime, prime_sieve, count_unique_prime_factors


def fibonacci():
    """Calculates the fibonacci numbers, then returns them via generator."""
    a, b = 1, 1
    while 1:  # Always true. Not problematic due to how generators work.
        yield a
        # By simultaneously assigning multiple variables, I can skip the temporary variable "z" from the initial solution:
        a, b = b, a+b


def proper_divisor_sum(n):
    """Returns the sum of proper divisors of n, i.e. of divisors < n."""

    # Special case for zero. Perhaps never used.
    if n == 0:
        return 0

    # Special case for the divisor 1:
    div_sum = 1

    # Otherwise, test all numbers between 2 and the square root, rounded down to the nearest integer.
    # If there's a divisor <root, there's also a divisor >root.
    root = int(sqrt(n))
    for i in range(2, root + 1):
        if n % i == 0:
            div_sum += i + n // i  # Add both the divisor i and the divisor n // i.

    # Special case for squares. Otherwise, we get wrong results for e.g. 128*128=16384.
    if n == root ** 2:
        div_sum -= root

    return div_sum


def is_prime(x):
	"""Returns True if the given number is prime, False otherwise."""
	assert x >= 1

	if x == 1:  # Special case for 1: 1 is not prime.
		return False
	if x > 2 and x % 2 == 0:
		return False

	root = int(sqrt(x))
	for i in range(3, root + 1, 2):  # No need to consider even numbers.
		if x % i == 0:
			return False
	return True


def prime_sieve(limit = 1_000_000): 
	"""Returns a boolean list with all primes set to False.
    The list ranges from 0 to limit - 1."""
    # Based on an implementation on the web.

	assert limit > 1
	
	# Initialize the sieve. 
	sieve = [False] * limit  # sieve = [False, ...]. Alternative: sieve = [False for _ in range(limit)]
    
    # Special cases: 0, 1, and even numbers > 2 are not prime.
	sieve[0] = True
	sieve[1] = True
	for n in range(4, limit, 2):
		sieve[n] = True

	# Apply the actual sieve algorithm to all odd numbers >=3.
    # Only consider odd divisors below the square root of limit.
	crosslimit = int(sqrt(limit))
	for n in range(3, crosslimit, 2):  
		if not sieve[n]: # Only consider n if it's prime.
			# If n is prime, then it's multiples are not prime.
            # And because we apply this algorithm to each prime,
            # there's no need to consider any multiples ilke n*2, n*3 etc.,
            # but just odd multiples of n*n (i.e. cases which just involve the prime itself.
            # Because we're interested in odd multiples of n*n, we jump ahead by 2*n,
            # not just by n. Otherwise we'd land on an even number that's already been sieved out.
			for m in range(n * n, limit, 2*n):  
			    sieve[m] = True

	return sieve


def count_unique_prime_factors(n, sieve):
	"""Returns the number of unique prime factors of n.
	The function must be provided with a prime sieve."""

    # Instead of the following implementation which repeatedly calculates the square root,
    # an alternative would be to repeatedly divide by each prime, then go on to the next larger one
    # without "looking back".
	factors = set()
	while True:
		root = int(sqrt(n))
		# Small optimization potential: I could adapt the following to make a special case 
		# for 2 as a prime factor, so I only need to cycle through odd primes afterwards.
		for i in range(2, root + 1):  
			if not sieve[i] and n % i == 0:  # Checks that i is prime, and if it's a factor of n
				n = n // i
				factors.add(i)
				break  # Jump back to the top of the while loop.
		else:  # Escape the while loop if no further prime factor can be found - presumably because n is now prime. Or 1?
			factors.add(n)
			break
	return len(factors)
