name = input("what is your name: ")
total = int(input("what is your total marks: "))
eng = int(input("what is your english obtain marks: "))
math = int(input("what is your math obtain marks: "))
urdu = int(input("what is your urdu obtain marks: "))

obt = eng + math + urdu
if(obt> total):
    print(name, "your total of obtain marks is greater than total please Enter the valid marks.")
    exit()
per = obt / total * 100

if(per>= 80 and per <100):
    print(f"{name} your total is {obt} and your percentage is {per} and grade is A")

elif(per>= 70 and per <80):
    print(f"{name} your total is {obt} and your percentage is {per} and grade is B")

elif(per>= 60 and per <70):
    print(f"{name} your total is {obt} and your percentage is {per} and grade is C")

elif(per>= 0 and per <60):
    print(f"{name} your total is {obt} and your percentage is {per} and grade is fail")