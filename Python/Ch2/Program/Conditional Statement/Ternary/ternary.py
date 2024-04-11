"""
Single line IF or Ternary Operator

    <var> = <val1> if <condition> else <val2>
"""


food = input("Enter food : ")

eat = "YES" if food == "cake" or "byriyani" else "NO"

print(eat)