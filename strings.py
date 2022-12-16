def length(st:str):
 return len(st)
def maxofthree(st1,st2,st3):
 return max(st1,st2,st3)
def replacevowel(st:str):
 l = list(st)
 for i in range(0,len(st),1):
   if l[i] in "aeiou":
     l[i] = '#'

   op = ""
   for i in l:
      op+= i
   return op
def noofwords(st:str):
      l= list(st)
      cnt = 1
      if(st==""):
         return 0
      for i in l:
          if i==' ' or i=='\n':
            cnt += 1
      return cnt
def checkpali(st:str):
  l = list(st)
  l.reverse()
  ops=""
  for i in l:
    ops += i
    if (ops==st):
       return True
    else:
      return False

while(True):

  choice = int(input("1.Length of a String\n2.Maximum of 3strings\n3.Replace all vowels with #\n4.Number of words in a given string\n5.Check Palindrome\nEnter Choice:"))
  if(choice==1):
    str1 = input("Enter the string : ")
    print("Length:",length(str1))
  elif(choice==2):
    str1 = input("Enter the string: ")
    str2 = input("Enter the string: ")
    str3 = input("Enter the string: ")
    print("Maximum of these 3strings:",maxofthree(str1,str2,str3))
  elif(choice==3):
    str1 = input("Enter the string: ")
    print(replacevowel(str1))
  elif(choice==4):
    str1 = input("Enter the string: ")
    print(noofwords(str1))
  elif(choice==5):
    str1 = input("Enter the string :")
    if(checkpali(str1)):
      print("Yes! Its a palindrome")
    else:
      print("No! Its a non-palindrome")

  else:
   break