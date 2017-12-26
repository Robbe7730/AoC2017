# HARDCODED, rewritten and optimized input
h = 0

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f += 6
  return True

# for b in range(108100, 125100, 17):
b = 108100
while b != 125100:
    if(not is_prime(b)):
        h += 1
        # print(b, h)
    b += 17

if(not is_prime(b)): # I FUCKING LOVE OFF BY ONE ERRORS
    h += 1
print(h)
