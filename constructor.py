class Student:
  max=0
  def __init__(self,name:str,marks:list): #Constructor
    self.name=name
    self.marks=marks
    sum=0
    for i in self.marks:
     sum+=i
     sum=sum/len(self.marks)
     if(sum>=Student.max):
       Student.max=sum

  def maxavgmarks(): #Function returning Maximum Average marks
    print("Maximum average marks are: "+str(Student.max))
  def __del__(self): #Destroyer
   pass

n=int(input("Enter the number of students :"))
students=[]
for k in range(n):
 students.append(0)
 for i in range(n):
    name=input("Enter name of"+str(i+1)+" student: ")
    l=[]
    for j in range(3):
         print("Enter the marks in ",i+1," subject: ",end="")
         x=int(input())
         l.append(x)
students[i]=Student(name,l)
Student.maxavgmarks()