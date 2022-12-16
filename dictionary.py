def maxpercent(d1):
  opd={}
  for i in d1:
    sum = 0
    for j in range(0,4,1):
      sum += d1[i][j]
      opd[sum]=i
    return opd[max(opd)]
di = {}
n = int(input("Enter the number of students in class : "))
for i in range(0,n,1):
  l = []
  st = input("Enter name of"+(str)(i+1)+" student :")
  for j in range(0,4,1):
    l.append(float(input("Enter the marks of "+(str)(j+1)+"Subject :")))
    di[st]= l
print("Name of the Student Scoring highest marks: ",maxpercent(di))