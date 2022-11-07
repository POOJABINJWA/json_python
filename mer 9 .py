        
# a=(input("enter the alphabet"))
# if a>="A" and a<="Z" or a>="a" and a<="z":
#     b=int(input("enter the digit"))
#     if b>0 and b<=10:
#         c=(input("enter the special charector"))
#         if c=="@" or c=="#" or c=="&" or c=="$":
#             print(a+str(b)+c)
#             password=(a+str(b)+c)
#             if len(password)>=10:
#                 print("strong password")


import json
a=(input("enter the alphabet"))
if a>="A" and a<="Z" or a>="a" and a<="z":
    b=int(input("enter the digit"))
    if b>0 and b<=10:
        c=(input("enter the special charector"))
        if c=="@" or c=="#" or c=="&" or c=="$":
            print(a+str(b)+c)
            password=(a+str(b)+c)
            if len(password)>=10:
                print("strong password")