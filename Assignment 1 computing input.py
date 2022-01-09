# ASSIGNMENT 1 #


# Ans1. Average of three numbers #
# Input from user #

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))

print("The average of given numbers is ", (n1+n2+n3)/3)
print("\n")

# Ans2. Program for calculating income tax #
# Input from user #

income=float(input("Enter your total income:"))
members=int(input("Enter no. of dependents:"))

taxable_income=float(income-10000-members*3000)

income_tax=taxable_income*0.2

if income_tax<0:
    print("No income tax to be paid.")

else:    
   print("Income tax to be paid is ", income_tax)
   print("\n")
   
# Ans 3. Storing data in form of list #
# Input from user #

SID=int(input("Enter your SID-"))
name=input("Enter your name-")
gender=input("Enter your Gender-(M,F,U) -  ")
course=input("Enter the course name-")
cgpa=float(input("Enter the CGPA-"))

Student=[SID,name,gender,course,cgpa]

print(Student)
print("\n")

# Ans4. Sorting marks of 5 students #
# Input from user #

M1=float(input("Enter your marks:"))
M2=float(input("Enter your marks:"))
M3=float(input("Enter your marks:"))
M4=float(input("Enter your marks:"))
M5=float(input("Enter your marks:"))

Marks=[M1,M2,M3,M4,M5]
Marks.sort()
print(Marks)
print("\n")

# Ans 5.1 Removing certain element from a list #
# Input from user #

colour=['Red','Green','White','Black','Pink','Yellow']
colour.remove('Black')
print(colour)
print("\n")

# Ans5.2 Overwriting elements of a list #
# Input from user #

print("(b)")
colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colour[3:5] = ["Purple"]
print("Output second is: \n",colour)
