## Uses Fermatt's Little Theorem to calculate the denominator required, will only work given a prime modulo
mod = 10**9 + 7
factorial_size = 10 # Replace
fact = [1] * (2 * factorial_size + 5)

for i in range(2, factorial_size + 1):
  fact[i] = fact[i-1] * i % mod
  
fact[-factorial_size] = pow(fact[factorial_size], mod - 2, mod)
for i in reversed(range(2, factorial_size + 1)):
  fact[-i + 1] = fact[-i] * i % mod
  
def comb(n, k):
  if k < 0 or k > n:
    return 0
  return fact[n] * fact[-(n-k)] % mod * fact[-k] % mod
