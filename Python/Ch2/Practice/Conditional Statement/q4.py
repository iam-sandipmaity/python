# WAP for school grade system

mark = int(input("Enter mark : "))

if(mark >= 90):
    print("A+")
elif(mark < 90 and mark >= 80):
    print("A")
elif(mark < 80 and mark >= 70):
    print("B")
elif(mark < 70 and mark >= 60):
    print("C")
elif(mark < 60 and mark >= 50):
    print("D")
elif(mark < 50 and mark >= 40):
    print("E")
elif(mark < 40 and mark >= 0):
    print("FAIL")
else:
    print("Please enter a valid mark")