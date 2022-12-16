import matplotlib.pyplot as plt
#Called UDF
def histogramplotter(lis:list):
  plt.hist(lis,lis,histtype='bar',rwidth=0.9)
  plt.xlabel('X Axis')
  plt.ylabel("Y Axis")
  plt.title("User Entered Data")
  plt.legend
  plt.show()
#Calling UDF
lis=[]
N = int(input("ENter the number of elements of list:"))
for i in range(0,N,1):
  lis.append(input())
  histogramplotter(lis)