with open("D:\Python\Ch7\Program\demo.txt","r") as f:
    data = f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("new data")