def practical10():
  s = input("Enter the string :")
  op= dict()
  for i in s:
    if(i not in " ."):
      op[i] =0;
  for i in s:
    if(i not in " ."):
      op[i] += 1;

  return op
print("Frequency of Each Letter : ",practical10(),end="\n")