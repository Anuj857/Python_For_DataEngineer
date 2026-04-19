#Data Types behind the seen
    #1.Python autometicaly detect Data Types 
    #2.Dynamic: data types- can change any time
    #3.Data in Different Types and Size

#Q. Why Data Types?
    #1.prevent Problem
    #2. know how to operate Data

#DATA TYPES Categories
#1. No Values-- none/nothing
#2. single Value --primitive Data Types --> n=50,f=3.14,str="anuj",anuj=true;
#3.Multi Values -- Data STsructures/collections/containers --> arr=[1,2,3,4], set, list,dics,tupple

a=90 #int: integer whole numbers without decimals

b=3.15 # float: numbers with decimal point

c="Hello Anuj" # String: -String represent text or a sequence of charecters
                    #    -written inside single or double quotes

f=True #boolean :can be either True or false
g=False        #-used to handle logic and decision- making


h=None #None :- means "no value","nothing" or"unknown"
            #:- it is used to show the absence of any data

i="" # Blank "" is string value with no charecters iside,it is not same as None
j=" " # White Space " " is a string values with 1 or more spaces, it is note same as None


#DATA TYPES, FUNCTIONS, METHODS

#Built-in-functions
text="anuj"
number=10
print(type(text)) #types() :- returns the data types of value so we know what kind of object it is
print(type(number))
print("----------------------------------------------")
print(len(text)) #len() :- gives the total count of items inside a value.helping you measure its length.
# print(len(number)) ## means no applicables for integers

print("--------------------upper(),lower()------------------------")
print(text.upper()) #upper():- converts all letters in a string in upper case
print(text.lower()) #upper():- converts all letters in a string in lower case

print("-------------------bit_length()------------")
print(number.bit_length()) #bit_lengths():- returns the length of a number in binary

print("-------------------------------------------")
print("""Q. create 5 variables-each with a different data types " \
1.your age
2.your height(with.decimals)
3.your Name
4.are you a student
5.somthing with no valuesn yet

    then print the values data types lengths of all variables
""")

age=21
hieght=5.9
name ="anujYadav"
AreYouStudent= True
fav=None

print("age:",age,type(age),age.bit_length() )
print("hieght:",hieght,type(hieght) )
print("name:",name,type(name),len(name) )
print("Are u student:",AreYouStudent,type(AreYouStudent) )
print("your Fav.. num:",fav,type(fav))