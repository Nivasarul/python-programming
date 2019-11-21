n=int(input("enter the first range : "))
s=int(input("enter the second range : "))
for a in range (n,s):
  if(a%2==0):
    print("even:",a)
  if(a%2!=0):
      print("odd:",a)