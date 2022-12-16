def insertionsort(l:list):
  for i in range(1,len(l),1) :
    key = l[i]
    j = i-1
    while(j>=0 and key<l[j]):
       l[j+1]=l[j]
       j -= 1
       l[j+1]=key

def linearsearch(l:list,element):
   for i in range(0,len(stuname),1):
     if(element==l[i]):
       return i

   return -1
def binarysearch(l:list,element,start,end):
  if(start==end):
    return start
  mid = int((start+end)/2)
  if(element==l[mid]):
     return mid
  elif(element<l[mid]):
     return binarysearch(l,element,start,mid-1)
  elif(element>l[mid]):
     return binarysearch(l,element,mid+1,end)

def selectionsort(l:list):
  for i in range(0,len(l),1):
    min_idx = i
  for j in range(i+1,len(l),1):
    if(l[min_idx]<l[j]):
        min_idx=j
        temp = l[min_idx]
        l[min_idx]= l[i]
        l[i]=temp

def bubblesort(l:list):
  swapped = False
  for n in range(len(l)-1, 0, -1):
      for i in range(n):
        if l[i] > l[i + 1]:
          swapped = True
          l[i], l[i + 1] = l[i + 1], l[i]

  if not swapped:
     return
stuname = []
n = int(input("Enter the number of students :"))
for i in range(0,n,1):
     k = input("Enter the name of student :" )
     stuname.append(k)
while(True):
    print("1.Search using Linear Search\n2.Search using BinarySearch\n3.Bubble Sort\n4.Insertion Sort\n5.Selection Sort\n6.ToDisplay the current List\n")
    choice = int(input("\nEnter Your Choice : "))
    if(choice==1):
      ele =input("Enter the name of the student to be searched :")
      idx = linearsearch(stuname,ele)
      print("ELement found at :",idx)
    elif(choice==2):
      ele =input("Enter the name of the student to be searched :")
      start = 0
      end = len(stuname)
      insertionsort(stuname)
      idx = binarysearch(stuname,ele,start,end)
      print("Student found at position :",idx)
    elif(choice==3):
      bubblesort(stuname)
    elif(choice==4):
      insertionsort(stuname)

    elif(choice==5):
      selectionsort(stuname)
    elif(choice==6):
      print(stuname)
    else:
      break