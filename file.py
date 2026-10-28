# file=open("data.txt","x")
# file=(file.py)
# file=open("data.txt","w")
# file.write("hello python")
# file=file.close()

# file=open("data.txt","a")
# file.write("\n hello cd")
# file=file.close()

# with open("data.txt","r")as file:
#     print(file.read())

# lines=["Apple\n","Banana\n","Mango\n"]
# with open ("fruits.txt","w")as file:
#     file.writelines(lines)

# with open("data.txt","r+")as file:
#     print(file.read())
#     file.write("\n Learninmg file Hnadling")


# with open("data.txt","r+")as file:
#         file.write("\n737867437")
# print(file.read())


# with open("data.txt","a+")as file:
#     file.write("java")
#     file.seek(4)
#     print(file.read())

# with open("data.txt","r+")as file:
#     file.seek(4)
#     print(file.tell())

# with open("data.txt","r+")as file: 
#     file.write("\namit jaiswal")
#     file.seek(0)
#     print(file.read())



# with open("img.png","rb")as file:
#     print(file.read())

# with open("photo.png","rb")as file:
#     print(file.read())

# with open("photo.png","wb")as file:
#         file.write(b"nhello")        

# with open("photo.png","rb+")as file:
#     print(file.read())


# with open("photo.png","wb+")as file:
#     file.write(b"nhello")        

# with open("data.txt","r")as file:
#     print(file.readline(),end="")
#     print(file.readline(),end="")
#     print(file.readline(),end="")


# with open("data.txt","r")as file:
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())


# with open("data.txt","r")as file:
#     lines=file.readlines()
#     print(lines)

# with open("data.txt","r") as file:
#     lines=file.readlines()
#     for i in lines:
#         print(i.strip())


# with open("data.txt","r")as file:
#     lines= file.readlines()
#     print(lines[:2])

# with open("data.txt","r")as file:
#     lines=file.readlines()
#     print(len(lines))

# with open("data.txt","r") as file:
#     for line in file:
#         if "banana" in line:
#             print(line.strip())


# with open("fruits.txt","r") as file:
#     line=file.readline()
#     for i in range(2):
#         print(i,line)

# with open("data.txt","r")as file:
#     lines=file.readlines()
#     file.seek(5)
#     print(file.tell())


# with open("note.txt","r")as file:
#     print(file.readline(),end="")
#     print(file.readline(),end="")
#     print(file.readline(),end="")
# with open("note.txt","r")as file:
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
    

# with open("note.txt","r")as file:
#     lines=file.readlines()
#     print(lines)


# with open("note.txt","r") as file:
#     lines=file.readlines()
#     for i in lines:
#         print(i.strip())



# with open("note.txt","r") as file:
#     line=file.readline()
#     for i in range(9):
#         print(i,line)


# with open("note.txt","r")as file:
#     lines= file.readlines()
#     print(lines[:7])

# with open("note.txt","r")as file:
#     lines=file.readlines()
#     print(len(lines))

# with open("note.txt","r") as file:
#     for line in file:
#         if "kashmir" in line:
#             print(line.strip())


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Line chart

# x=[1,2,3,4,5]
# y=[10,20,15,25,30]
# plt.plot(x,y)
# plt.title("LineChart")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# Bar chart

# x=['A','B','C','D']
# y=[5,7,3,8]
# plt.bar(x,y)
# plt.title("BarChart")
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.show()

# Pie chart

# labels=['A','B','C','D']
# sizes=[30,25,20,25]
# plt.pie(sizes,labels=labels,autopct='%1.1f%%')
# plt.title("PieChart")
# plt.show()

# Scatter Plot

# x=[1,2,3,4,5]
# y=[5,15,10,20,25]
# plt.scatter(x,y)
# plt.title("ScatterPlot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()