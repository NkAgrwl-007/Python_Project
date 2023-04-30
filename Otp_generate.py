from random import random
n = input("Type 'Y' to generate O.T.P :\n")
if n.lower() == "y":
    otp = str(random())[-6:]
    print(otp)
    print("Verified") if input("Verify the O.T.P :\n")==otp else print("NOT VERIFIED")
else:
    print("O.T.P not generated.")
input("Enter to exit program.")