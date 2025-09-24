import math

def comparacion():
  variable = 0
  for n in range(2, 1000000):
    if (0.01*(n**3) < 1.5**n):
      variable = n
      break
  return variable

print(comparacion())

def comparacion2():
  variable = 0
  for n in range(2, 1000000):
    if (((6*n) / math.log2(n)) + 300 < 5*(n**2) + 10*n):
      variable = n
      break
  return variable

print(comparacion2())