#Why is handling string data importent?
# Text is everywhere 
    #1.filename 
    #2. user input
    #3.webdata 
    #4. logs

#String category
print("-------------type function----------")
#1.types = 1.type(), 2.str()
#type(): returns the data type of a value so we know what kind of object it is
name="Anuj" 
print(type(name))

age=22
print(type(age))

# print("my age is"+age)   #cant combine a string with an integer using +operator

print("my Age is: "+str(age))
age+age+5
age=str(age)
print(type(age))
# age=age+5 #python is flexible with data types- but watch out! we can change a values type but python will treat it dfferently
  
print("--------------Math function----------")
#Math 
#  Use case: check password Quality
#  make sue the password meets minimum length requirements
password="123a567"
len(password)       #len(): returns the number of items in a value returns the number of charecters in a string
print("len():",len(password))     # it counts everything even spaces
if(len(password)>8):    
    print("valid password")
else:
    print("invalid Password")


#count: returns how often a word appears in the String 

text= """"
Python is easy to learn .
Python is Powerful.
Many  people love python.
"""
print("count(Python):",text.count("Python")) # Python is case-sensitive :means uppercase and lower case letters are treated as different
 #use Case: detect Quality Issues -count how many unwanted characters in my data

print("--------------Transformation function----------")
#Transformations
print("-------#1.replace()---------")
#1.replace()
#use case: replace commas with dots in European- style decimal number
price="1234,46"
print(price.replace(",","."))


phone="857-8046-720"
print(phone.replace("-"," "))

price="$1,299.99"

#Chained methods are executed in order from left to right.
        # Each replace() runs on result of the one before it.
print("chained method:",price.replace("$","").replace(",","")) 

#CHALLENGEs !. convert the messy phone number into a clean number format with only digits
phone1="+49 (176) 123-4567"
print(phone1.replace("+","").replace(" ","").replace(")","").replace("(","").replace("-",""))

print("------------#2.joins(concatinates)------------")
#2.joins(concatinates)
#plus(+) operator : joins(concatinates) two String into one
first_namme="Anuj Kumar"
last_name="Yadav"
full_name=first_namme+" "+last_name
print(full_name)

# use case: build file paths
#         build dynamic paths using folder and file variables
folder="C:/users/anuj/"
file="report.csv"
full_file_path=folder+file
print(full_file_path)

print("---------f-String-------")
#f-String:modern, super-easy way to format and build strings 
#       "f" stands for "formated"
#   lets we easily put variables and expressions directly inside string value

name="Anuj"
age=21;
is_student=False
print("My name is"+name+", I am "+str(age)+" yerars old, and students Status is "+str(is_student)+".") #hard to read- There are lots of plus signs and we have to worry about spaces and types

print(f"My Name is {name}, I am {age}, Year Old, and student status is {is_student}")
print(f"2+3={2+3}")

print("---------slit()--------")

#split()
stamp="2026-09-20"
print(stamp.split(" "))
print(stamp.split("-"))

#use case
csv_file="1234,Anuj,India,2005-04-02,Male"
print(csv_file.split(",")) # break comma-seperated values into individual items

print("--------String repetition---------")
#string *numbers : repeats the string multiple items
print("ha"*3)
# use case: style our logs- use repeated characters to create clear sections in output
print("="*30)
print("@"*30)
print("#"*30)

print("-" *10 +"Data EWxtraction"+"-"*10)
#Indexing 
text="Python"

#extract the first charecter
print(text[0])
print(text[-6]) #indexing : extracts one character by position

#extract the last Charecter
print(text[-1])
print(text[5])

#extract h
print(text[3])


#  Slicing
date="2026-09-20"

#Extract the year
print(date[0:4])
print(date[:4]) # open-end Slicing : if we leave the start index empty, Python starts from index 0


#extract  the months
print(date[5:7])

#extract the day
print(date[8:])

#Q-> When to use positive or negative indexes?
#Ans- whenever we need to acees the data from left side then we use positive indexes and whenever we need to acees the data from end then we use negative indexes

print("-" *10 +"Data Cleaning"+"-"*10)
#Remove Spaces
text=" Engineering".lstrip()
print(text)

text="Engineering  ".rstrip()
print(text)

text="  Engineering  ".strip() #strip(): removes spaces from both ends
print(text)

#Best Practice - Trim Spaces from User Input
        #we never know whereb users might add spaces use strip() remove all extra spaces from both ends
    # it removes tabs and multiple spaces
text="  Data Engineering  ".strip()
print(text) #only removes spaces at the starts or end, not in the middle

#it removes any characters you want from the start and end - not just spaces
text="###Abc####".strip("#")
print(text)

#Use Case: Detect Extra Spaces- check the length before and after strip() to find unwanted spaces
text="Engineering"
print(len(text))
print(len(text.strip()))
no_of_spaces=len(text)-len(text.strip())
is_clean=len(text)==len(text.strip())
print("no_of_spaces:",no_of_spaces)
print("is_clean:",is_clean)

# Case conversion
text="python PROGRAMMING "
print(text.upper()) #upper():makes all letters uppercase
print(text.lower()) # lower(): makes all letters in lowercase

#use Case:clean Data -lowercase all text to prevent case-based mismatches during search or comparison
#Best Practices: Clean Before Search-always trimm spaces and lowercase our data and search term before matching

search="    Email".lower().strip()
data=" email".lower().strip()
print(search==data)

#CHALLENGES 
#Q. turn the messy string into a single clean summary with name ,role and age
text="968-Maria, (  D@t@ Engineer  );;  27y  "
print(text.replace("968-","name: ").replace(","," |").replace("(","role:").replace("@","a").replace(")","|").replace(";;"," age:").strip())


print("-" *10 +"Searching"+"-"*10)
#searching 
phone="+91-85780-46720"
print(phone.startswith("+91")) #startswith(""xyz): checks if the strings begins with a specific word

email="anujkryadav02042005@gmail.com"
print(email.endswith("gmail.com")) #endswith: checks if the string ends with a specific word\

#use case: 1. check the extension 
file="data_backup.csv"
print(file.endswith(".csv"))

#Use case:2. is this a valid emails? Check for(@)
print("@" in email) #in: Checks if a word exists in the string 

url= "https://com.google.in/anuj"
print("com" in url) # check if url is an API endpoint

#find() is great when combined with other methods to add dynamics
phone1="91-85780-46720"
phone2="+91-99311-18625"

#handcoding the start position doesn't work when the country code length changes
print(phone1[3:])
print(phone2[4:])
 
#find() : returns the starting position of a word in the string
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])

print(phone1.find("-"))

#find() is great when combined with other methods to add dynamics

print("-" *10 +"Validation"+"-"*10)
#validation: 
#check if the country name contains only letters
country="IND"
print(country.isalpha()) #osalpha(): checks if the string has only letters
state="jh12"
print(state.isalpha())

phone="8678046720"
print(phone.isnumeric()) # isnumeric(): checks if the string has only numbers
phone="86780-46720"
print(phone.isnumeric())


#Prevent invalid or "Garbage" data from entering your System