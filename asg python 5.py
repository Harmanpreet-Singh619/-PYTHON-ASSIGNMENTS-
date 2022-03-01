
# ASSIGNMENT 4  #
print("\n")



#      ** QUESTION-1 **
#      TOWER OF HANOI

print("\t \t \t Question-1 \n")
def Tower_of_Hanoi(n, source, destination, auxillary):
    if n==1:
        print("Move disc 1 from", source, "to", destination)         # only 1 move is required for n=1
    else:
        Tower_of_Hanoi(n-1, source, auxillary, destination)          # moves first (n-1) discs from source peg to auxillary peg
        print("Move disc", n, "from", source, "to", destination)     # moves the largest peg from source peg to destination peg
        Tower_of_Hanoi(n-1, auxillary, destination, source)          # moves the (n-1) pegs in auxillary peg to destination peg
n=int(input("Enter the number of discs: "))
Tower_of_Hanoi(n, 'A', 'B', 'C')                                     # A is peg-1 (source peg), B is peg-2 (destination peg), C is peg-3 (auxillary peg)
print("\n")



#         ** QUESTION-2 **
#         PASCAL'S TRIANGLE
print("\t \t \t Question-2 \n")
num=int(input("Enter number of rows: "))
def factorial(n):                   # gives factorial of a number
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
# ITERATIVE METHOD
for i in range(0, num):             # two for loops are applied to give nCr
    for j in range(0, num-i):
        print(" ", end="")
    for j in range (0, i+1):
        print(int(factorial(i)/(factorial(j)*factorial(i-j))), end=" ")               # prints formula of nCr according to Pascal's Triangle
    print()
# RECURSIVE METHOD
def pascal(n, k):
    if(n<0):
        return
    else:
        pascal(n-1, k)                  # recursion gives previous lines of Pascal's triangle
        for i in range(0, k-n):
            print(" ", end="")
        for i in range(0, n):
            print(int(factorial(n-1)/(factorial(i)*factorial(n-1-i))), end=" ")                # give current line of Pascal's Triangle
        print()
pascal(num, num)
print("\n")



#     ** QUESTION-3 **
print("\n\t Question 3 \n")

# Asking for two numbers from the user.
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter second number(number must not be zero): "))
print()

# Using inbuilt function to calculate quotient and reminder.
quotient_reminder = divmod(num_1, num_2)
print(f"The quotient and reminder of the values are {quotient_reminder}")

print("\n\tPart A\n")
# Checking whether the object is callable or not.
check = callable(divmod)
if check == True:
    print("It is callable.")
elif check == False:
    print("It is not callable.")

print("\n\t Part B\n")

# Checking whether the values are non zero or not.
if quotient_reminder == (0,0):
    print("Both values are zero.")
elif quotient_reminder[0] == 0:
    print("Only quotient is zero")
elif quotient_reminder[1] == 0:
    print("Only reminder is zero.")
else:
    print("Both are non zero.")
print("\n\t Part C \n")

# Adding values to the previous set.
new_result = quotient_reminder.__add__((4,5,6))
print(f"Result after adding values: {new_result} \n")

# Filtering out the values greater than 4 in a list.
value_greater_than_4 = []
for counter in range(len(new_result)):
    if new_result[counter] > 4:
        value_greater_than_4.append(new_result[counter])
print(f"Values greater than 4: {value_greater_than_4}")
print()


print("\n\t Part D \n")

# Converting list of values greater than 4 into a set.
converting_to_set = set(new_result)
print(f"After converting the above result into set {converting_to_set} \n")


print("\n\t Part E \n")

# Making the set immutable.
converting_to_immutable = frozenset(converting_to_set)
print("Now set is immutable")

print("\n\t Part f \n")

# Calculating the max value and hash value.
print(f"Max value in the set is {max(converting_to_immutable)}")
print(f"Hash value is: {hash(converting_to_immutable)}")

#      ** QUESTION-4 **
#      CLASS STUDENT

print("\t \t \t Question-4 \n")

class Student():                # Creating class named student.

    def __init__(self,name,rollno):         # initilizing name and roll number
        self.name = name
        self.rollno = rollno
        print(f"Object created for {self.name}")

    def show_info(self):                    # Details of student
        print(f'The name of the student is {self.name}')
        print(f'The roll number of {self.name} is {self.rollno}')

    def __del__(self):                      # Destructor
        print(f"Destructor deleted {self.name}'s record.")
# Creating objects 
student_1 = Student("Harmanpreet Singh", 21105053)
student_2 = Student("Ayush kher", 21105001)
student_3 = Student("Akshat Dutta", 21105093)
print()
# Details of students
student_1.show_info()
print("\n")
student_2.show_info()
print("\n")
student_3.show_info()
print('\n')
# Calling destructor.
del student_1
del student_2
del student_3
print("\n")



#       ** QUESTION-5 **
#       CLASS EMPLOYEE

print("\t \t \t Question-5 \n")

class factory():                        # Creating a class names factory.

    def __init__(self,name,salary):     # Storing data of employees
        self.name = name
        self.salary = salary
        print(f"Object created named {self.name}.")

    def show_info(self):                # Data of employees
        print("\tShowing info of the employee.")
        print(f"Name of the employee working in this factory is {self.name}")
        print(f"Salary of {self.name} is {self.salary}.")

    def update_salary(self,new_salary): # Update the salary of employee
        self.salary = new_salary
        print(f"Updated salary of the employee {self.name} is {self.salary}\n")

    def __del__(self):                  # Deleting data of employee
        print(f"Record of the employee {self.name} is deleted.")
    
# Employees
Mehak = factory('Mehak', 40000)
Ashok = factory("Ashok", 50000)
Viren = factory('Viren', 60000)
print()

# DATA of employees
Mehak.show_info()
print()
Ashok.show_info()
print()
Viren.show_info()
print()

# Updating salary of employee
print("Updating mehak's salary.")
Mehak.update_salary(70000)

# Removing data of employee
print("Calling destructor to delete viren's record.")
del Viren

print("\n")



#       ** QUESTION-6 **
#       ANAGRAM TEST

print("\t \t \t Question-6 \n")

george_word=input("Enter George's word: ")
barbie_word=input("Enter Barbie's word: ")

def anagrams(s):                            # function to find list of anagrams
    if s=="":
        return [s]
    else:
        ans=[]                              # list of anagrams
        for w in anagrams(s[1:]):           # iterates over anagrams of tail of the string
            for pos in range(len(w)+1):     # puts first letter in different positions in the anagrams of the remaining letters
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans

correct_words=anagrams(george_word)
if barbie_word in correct_words:            # checks if Barbie's word is an anagram of George's word
    print("Friendship is True.")
else:
    print("Friendship is Fake.")
