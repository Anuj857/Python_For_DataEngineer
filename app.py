# this is a single-line comment 


# store the final exam score
x=10

x=80 #store the final exam score

# function
print("hi python")
print('hi python')
# print("hello') # syntax errorerror

print("---------------------")
print("     LEARN PYTHON    ")
print("---------------------")

# Escape sequence
#1. \
print("hi \"Anuj kumar\"")
print('hello "anuj Yadav"')
print('hello \'anuj Yadav\'')


#2.\\
print("Path: \"C:\\Users\\acer\\Desktop\"")

#3. \n
print("Anuj Kumar Yadav\n\nbablu kumar saw")

#4.\t
print("Anuj\tKumar\tYadav\n\n")

#Q1. Print 
# your learning path:
#       -Python Basics
#       -Data Engineer
#       -AI       
#using only one print() function
print("Your Learning Path:\n\t-Python Basics\n\t-Data Engineering\n\t-AI")

print("""Your Learning Path:
      \t-Python Basics
      \t-Data Engineering
      \t-AI""")

#Why do we need print()? when should we use it?
price_shirt=25.00
price_jeans=45.50

qty_shirt=2
qty_jeans=1

total_shirt=price_shirt*qty_shirt
total_jeans=price_jeans*qty_jeans
subtotal=total_jeans*total_shirt
print("sub Total:",subtotal)
discount=subtotal*0.10
print("discount:",discount)
final_total=subtotal-discount
print("final total:",final_total)