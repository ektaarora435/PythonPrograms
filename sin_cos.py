import matplotlib.pyplot as plt
import numpy as np
def plotting(x,y,deg,a,b,diff): #UDF for plotting
z=[0 for i in range(0,360,1)]
Angles=[i for i in range(0,360,1)]
angles=[i*(np.pi/180) for i in range(0,360,1)]
plt.plot(Angles,z,color="black")
plt.plot(Angles,np.sin(angles),label="Sine Curve")
plt.plot(Angles,np.cos(angles),label="Cosine curve")
plt.xlabel("Angles in degree")
plt.ylabel("Trigonometric values")
plt.legend()
plt.show()
curve=np.polyfit(x,y,deg)
graph=np.poly1d(curve)
new_x=list()
new_y=list()
for i in range(len(x)):
new_x.append(x[i])
curl=graph(x[i])
new_y.append(curl)
plt.plot(new_x,new_y,label="y = "+str(graph))
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.legend()
plt.show()
val=np.arange(a,b,diff)
plt.plot(val,np.exp(val),label="Exponential")
plt.xlabel("Range values")
plt.ylabel("Exponential values")
plt.legend()
plt.show()

# Calling Function
n=int(input("Enter the number of plottings values: "))
x=[]
y=[]
for i in range(n):
x1=int(input("Enter the value of x coordinate for polynomial: "))
x.append(x1)
y1=int(input("Enter the value of y coordinate for polynomial: "))
y.append(y1)
degree=int(input("Enter the degree of the polynomial: "))

a=int(input("Enter the starting range for exponential graph: "))
b=int(input("Enter the ending range for exponential graph: "))
diff=int(input("Enter the difference in values for exponential graph:"))
print("Plotting all the graphs..........")
print("..........")
plotting(x=x,y=y,deg=degree,b=b,a=a,diff=diff)