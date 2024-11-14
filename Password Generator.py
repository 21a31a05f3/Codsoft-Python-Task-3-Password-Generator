import random
print("Welcome to the Password Generator !")
length=int(input("Enter the password length : "))
c=0
alphabet=list("abcdefghijklmnopqrstuvwxyz")
number=list("0123456789")
symbols=list("!@#$%^&*()+-")
total=list("abcdefghijklmnopqrstuvwxyz012345678!@#$%^&*()+-")
while length<8 and c<3:
    print("Please select a minimum length of 8 characters for strong password")
    length=int(input("Enter the password length again : "))
    c=c+1
if c==3:
    print("Sorry, Please try after sometime !!")
else:
    password=""
    for i in range(1,length+1):
        if i<4:
            password+=random.choice(alphabet)
        else:
            password+=random.choice(total)
    print("The passsword generated is : ",password)