# a)Check if all elements in list are numbers or not
def checknum(l:list):
  for i in l:
    if(type(i)!=int):
      return False

  return True
# b)If it is a numeric list,then count number of odd values in it
def oddvalno(l):
   if(checknum(l)):
     cnt=0
     for i in l:
         if(i%2!=0):
            cnt += 1
            return cnt
         else:
            return -1

# c)If list contains all Strings,then display largest String in the list
def largeststr(l:list):
   if(~checknum(l)):
      return max(l)

# d)Display list in reverse form
def displayrev(l:list):
   for i in range(len(l)-1,-1,-1):
     print(l[i]," ")

# e)Find a specified element in list.
def linearsearch(l:list,ele):
   for i in range(0,len(l),1):
     if(ele==l[i]):
        return i
     else:
        return -1

# f)Remove the specified element from the list.
def removespecified(l:list,ele):
  l.remove(ele)
# g)Sort the list in descending order
def sortindesc(l:list):
  for i in range(1,len(l),1) :
    key = l[i]
    j = i-1
    while(j>=0 and key<l[j]):
      l[j+1]=l[j]
      j -= 1
      l[j+1]=key
      l.reverse()
      print(l)
# h)accept 2 lists and find the common members in them.
def findcommon(l1,l2):
  opl = []
  for i in l1:
    for j in l2:
      if(i==j):
         opl.append(i)

  return opl