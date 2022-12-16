def practical4(n):
  assert n>=10,"n is less than 10"
  s = set()
  while(n>0):
   s.add(n%10)
   n = n//10
  return s

#Calling Part
num= int(input("ENter the number to get the digits of : "))
print(practical4(num))