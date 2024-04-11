# Write a program to ask user to enter names of their 3 favorites movies and store them in a list

movies = []    # creating a empty list

# Now take input and append them in the list

"""

# Method 1
x = input("Enter Your movie name : ")
movies.append(x)
x = input("Enter Your movie name : ")
movies.append(x)
x = input("Enter Your movie name : ")
movies.append(x)
print(movies)

"""

# Method 2

movies.append(input("Enter your 1st movie : "))
movies.append(input("Enter your 2nd movie : "))
movies.append(input("Enter your 3rd movie : "))
print(movies)