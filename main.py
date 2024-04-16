from dials import dials
from itertools import product


def calcSum(dials):
  current = [0] * 4
  for dial in dials:  # Checks for overlapping
    current = map(lambda x, y: y if y else x, current, dial)

  current = list(current)
  return sum(current)  # Returns the sum of the column


def check(rot): # Checks if all columns add up to 42
  for i in range(12):
    total = calcSum(dial[(i + rot[num]) % 12] for num, dial in enumerate(dials))
    if total != 42:
      return False
  return True
    

for perm in product(range(12), repeat=4): # Bruteforce
  solution = [0] + list(perm)
  if check(solution):
    print(solution) # Prints solution
