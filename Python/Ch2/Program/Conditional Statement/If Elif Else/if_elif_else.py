"""
IF ELIF ELSE Statement

Syntax 
    if (condition):
        statement1
    elif (condition):
        statement2
    else:
        statementN
    
"""

# Trafic light code in python using if else statement

light = input("Enter light in coloum : ")

if( light == "red") :
    print("STOP")
elif(light == "green"):
    print("GO")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")