t1 = (1,2,5,7,9,2,4,6,8,10)
a = tuple()
#Part-(a)
for i in t1:
  if(i%2==0):
    a = a+(i,)

print("a.Even Integers :",a)
#Part-(b)
t2 = (11,13,15)
t1 += t2
print("b.After Concatenation : ",t1)
#Part-(c)
print("c. Minimum:",min(t1),"\nMaximum: ",max(t1))