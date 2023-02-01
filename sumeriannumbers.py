#Sumerian Character Unicodes
AS = 0x12038
AS2 = 0x12400
U = 0x1230B
U2 = 0x12399
U3 = 0x1230D
U4 = 0x1240F

# returns i where num >= 60^i
def PWR60(num):
  i = 0
  j = num
  while j > 60:
    i += 1
    #j = num is integer-divided by 60
    j = (j // 60)
  # num >= 60^i, so the first sumerian digit represents 60^i
  return i

#returns a sumerian number between 1, 10
def SAS(num):
  if num and num > 1 and num < 10:
    return chr(AS2 + (num - 2))
  elif num == 1:
    return chr(AS)
  else:
    return ""

#returns num in SU(10s)
def SU(num):
  if num == 1:
    return chr(U)
  elif num == 2:
    return chr(U2)
  elif num == 3:
    return chr(U3)
  elif num and num > 3 and num < 6:
    return chr(U4 + num - 4)
  else:
    return ""

#returns a sumerian num
def SUAS(num):
  if num:
    return SU(num // 10) +  SAS(num % 10)
  else:
    return ""

#prints all sumerian num < 60
def SUASs():
  for i in range(1, 59):
    print((SUAS(i)))


def SumerianDig(num):
  #i is the exponent of 60 represented by the first digit
  i = PWR60(num)
  #j is an empty array
  j = []
  #k is a new num equal to num
  k = num
  while i >= 1:
    #k is integer-divided by l = 60^i ,which forms the first sumerian digit because a single sumerian digit represents a power of 60, the first digit is written and the exponent is reduced for the nrxt operation, which is to repeat until i = 1, 60^1 = 1
     l = 60 ** i
     # 
     m = (k//l)
     j.append(SUAS(m))
     print (l)
     print (m)
     print(k)

    #k = k - (60^i) * (k//60^i)
     k -= l * m
     i -= 1
     print(k, " = ", l, "*", m)
     print(j)
  j.append(SUAS(num % 60))
  print(j)
  return j

#returns a sumerian number from arabic num
def SumerianNum(num):
  return "   ".join(SumerianDig(num))

#prints arabic num : sumerian num from num a to num b (not inclusive)
def SumerianNums(a, b):
  for i in range(a, b):
    print(str(i) + ' : ' + SumerianNum(i))


print(SumerianNum(1558237297)) 
 

