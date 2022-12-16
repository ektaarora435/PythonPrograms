def sales():
 name=input("Enter the name: ")
 week1=int(input("Enter the sales in first week: "))
 week2=int(input("Enter the sales in second week: "))
 week3=int(input("Enter the sales in third week: "))
 week4=int(input("Enter the sales in forth week: "))
 Sales=week1+week2+week3+week4
 remarks=""
 if(Sales>=80000):
     remarks="Excellent"
     commission=5
     t=(name,Sales,commission,remarks)
 elif(Sales>=60000 and Sales<80000):
     remarks="Good"
     commission=5
     t=(name,Sales,commission,remarks)
 elif(Sales>=40000 and Sales<60000):
     remarks="Average"
     commission=5
     t=(name,Sales,commission,remarks)
 elif(Sales<40000):
     remarks="Work Hard"
     commission=0
     t=(name,Sales,commission,remarks)
 return t

#Main Function Calling the UDF
if __name__=="__main__":
  n=int(input("Enter the number of workers: "))
  for i in range(0,n,1):
      print(sales())