def fibonacci(num:int):
 num1=num
 n1=0
 n2=1
 sum=0
 while(num1>0):
    sum += n1
    n1=n2
    n2=sum
    num1 = num1-1
 return sum
def factorial(num:int):
  n3=1
  while(num>0):
   n3 *= num
   num = num-1
  return n3
def practical3():
 out = []
 n = int(input("Enter the n value to get the factorial and nth term"))
 nthfibo = fibonacci(n)
 itsfactorial = factorial(nthfibo)
 return [nthfibo,itsfactorial]
print("nth term of fibonacci & its factorial :",practical3())