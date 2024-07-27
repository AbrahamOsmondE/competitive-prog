h, w, A, B = list(map(int, input().split()))

mod = 10**9 + 7
factorial_size = h + w - 2
fact = [1] * (2 * factorial_size + 5)

for i in range(2, factorial_size + 1):
  fact[i] = fact[i-1] * i % mod
  
## Fermatt's Little Theorem: a^(p-2) ≡ a^(-1) mod p where p is a prime
fact[-factorial_size] = pow(fact[factorial_size], mod - 2, mod)
for i in reversed(range(2, factorial_size + 1)):
  fact[-i + 1] = fact[-i] * i % mod
  
def comb(n, k):
  if k < 0 or k > n:
    return 0
  return fact[n] * fact[-(n-k)] % mod * fact[-k] % mod

total_number_of_unique_paths = comb(h + w - 2, h - 1)
ans = total_number_of_unique_paths
for b in range(B):
  number_of_ways_to_reach_forbidden_cells_entrance = comb(h - A - 1 + b, b) 
  number_of_ways_from_forbidden_cell_entrance_to_exit = comb(w + A - b - 2, w - b - 1)
  ans -= number_of_ways_to_reach_forbidden_cells_entrance * number_of_ways_from_forbidden_cell_entrance_to_exit
  ans %= mod

print(ans)