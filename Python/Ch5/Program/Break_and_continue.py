"""
Break :

    used to terminate the loop  when encountered.

Continue :-

    terminatets  execution in the current iteration & continues execution of the loop with the nest iteration.

"""


i = 1
j = 1

print("Break statement\n\n\n")
while(i <= 10):
    print(i)
    if(i == 7):
        break
    i += 1

print("\n\nContinue statement \n\n\n")
while(j <= 10):
    if(j == 7):
        j += 1
        continue
    print(j)
    j += 1

"""
Output 

Break statement



1
2
3
4
5
6
7


Continue statement



1
2
3
4
5
6
8
9
10
"""


