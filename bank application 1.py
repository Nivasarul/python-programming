
import re,random 
while True:
    email=input("enter mail")
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,email)):  
        break  
    else:  
        print("Invalid Email")
        continue
while True:
  mobno=input("enter mobno:")
  if len(mobno)!=10 or mobno[0]!="9":
    print("Sorry, enter 10 numbers")
    continue
  else:
     break
while True:
    pasword=input("enter pass:")
    if re.match(r'[A-Za-z0-9@#$%^&+=]{6,}', pasword):
        print("1.BALANCE \n 2.WITHDRAWL \n 3.MINISTATEMENT \n 4.DEPOSIT")
        break
    else:
        print("Password must be atleast length of 9 and should contain 1caps,1specialchar,1num")
        continue
x=random.randint(1000,2000)
print("Your Account number is:",x)
bal=30000
def balance():
    print("your balance is:",bal)


def deposit():
    new_depo=int(input("Amount to be deposited?"))
    """deposit+=new_depo
    depositlist=[]
    depositlist.append(new_depo)"""
    print("The amount has been added successfully")

def withdrawl():
    minbal=2000
    withamt=int(input("enter withdraw amount"))
    #temp=bal+minbal
    #if withamt>temp:
     #   bal=balance-withamt
    print("amount withdrawed successfully")

def ministatement():
    print("email:",email)
    print("acc no:",x)
    print("balance",bal)
choice=input("Enter your choice:")
if choice=="1":
    balance()
if choice=="2":
    withdrawl()
if choice=="3":
    ministatement()
if choice=="4":
    deposit()
