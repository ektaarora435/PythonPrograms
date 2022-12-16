def factorial(num:int):
  n3=1
  while(num>0):
    n3 *= num
    num = num-1
  return n3
#Called Function
def sumofser(n,x): #To get the serie o/p
  assert n%2==0
  sum=0
  j=0
  for i in range(0,n+1,2):
    sum += (((-1)**j)*(x**i))/factorial(i);
    j += 1
  return sum
# Calling Function
n = int(input("Enter the value of n in the serie :"));
k = sumofser(n,2)
print(k)
