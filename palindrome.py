import math

min = input('Input min number: ')
max = input('Input max number: ')
a = [i for i in range(min, max+1)]
b = []
pals = []
maxPal = 0
firstMaxNumber = 0
secondMaxNumber = 0
l=0

#choose only primes from array "a" and store them to the array "b"
for i in xrange(min, max+1):
  for j in xrange(2, int(math.sqrt(i))):
    if i%j == 0:
      break
  else: 
    b.append(i)

#check items for being palindromes in array "b"
for x in b:
  p = l
  for y in b:
    result = str(b[l]*b[p])
    revResult = ''.join(reversed(result))
    if result == revResult:
      #choose the maximal palindrome among others
      if int(result) > maxPal:
        maxPal = int(result)
        firstMaxNumber = b[l]
        secondMaxNumber = b[p]
    p += 1
    if p > len(b)-1:
      break
  l += 1

print ('Maximal palindrome: '+str(maxPal)+'. Multiplicand: '+str(firstMaxNumber)+'. Multiplier: '+str(secondMaxNumber)+'.')
