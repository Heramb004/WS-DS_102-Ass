

# 1. Check whether a number is positive, negative, or zero
print("\n1. Positive, Negative, or Zero")
n = float(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# 2. Check whether a number is even or odd
print("\n2. Even or Odd")
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Find the greater of two numbers
print("\n3. Greater of Two Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greater number:", a)
elif b > a:
    print("Greater number:", b)
else:
    print("Both numbers are equal")


# 4. Find the greatest of three numbers
print("\n4. Greatest of Three Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Greatest number:", a)
elif b >= a and b >= c:
    print("Greatest number:", b)
else:
    print("Greatest number:", c)


# 5. Check voting eligibility
print("\n5. Voting Eligibility")
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 6. Check whether a year is a leap year
print("\n6. Leap Year")
year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")


# 7. Check whether a character is a vowel or consonant
print("\n7. Vowel or Consonant")
ch = input("Enter one alphabet: ").lower()
if ch in "aeiou" and len(ch) == 1:
    print("Vowel")
elif len(ch) == 1 and ch.isalpha():
    print("Consonant")
else:
    print("Please enter one alphabet")


# 8. Check divisibility by both 5 and 11
print("\n8. Divisible by 5 and 11")
n = int(input("Enter a number: "))
if n % 5 == 0 and n % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# 9. Check whether a number is a multiple of both 3 and 7
print("\n9. Multiple of 3 and 7")
n = int(input("Enter a number: "))
if n % 3 == 0 and n % 7 == 0:
    print("It is a multiple of both 3 and 7")
else:
    print("It is not a multiple of both 3 and 7")


# 10. Assign grade based on marks
print("\n10. Grade")
marks = int(input("Enter marks out of 100: "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")


# 11. Check uppercase or lowercase
print("\n11. Uppercase or Lowercase")
ch = input("Enter one character: ")
if len(ch) == 1 and ch.isupper():
    print("Uppercase")
elif len(ch) == 1 and ch.islower():
    print("Lowercase")
else:
    print("Please enter one alphabet character")


# 12. Check vowel using if-elif
print("\n12. Vowel using if-elif")
ch = input("Enter one alphabet: ").lower()
if ch == "a":
    print("Vowel")
elif ch == "e":
    print("Vowel")
elif ch == "i":
    print("Vowel")
elif ch == "o":
    print("Vowel")
elif ch == "u":
    print("Vowel")
elif len(ch) == 1 and ch.isalpha():
    print("Consonant")
else:
    print("Please enter one alphabet")


# 13. Check whether three sides can form a triangle
print("\n13. Triangle Check")
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("The sides can form a triangle")
else:
    print("The sides cannot form a triangle")


# 14. Find the type of triangle
print("\n14. Type of Triangle")
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


# 15. Find the greatest among four numbers
print("\n15. Greatest of Four Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
greatest = a
if b > greatest:
    greatest = b
if c > greatest:
    greatest = c
if d > greatest:
    greatest = d
print("Greatest number:", greatest)


# 16. Check whether a number is a three-digit number
print("\n16. Three-Digit Number")
n = int(input("Enter a number: "))
if 100 <= abs(n) <= 999:
    print("It is a three-digit number")
else:
    print("It is not a three-digit number")


# 17. Calculate electricity bill using example rates
print("\n17. Electricity Bill")
units = int(input("Enter units consumed: "))
if units < 0:
    print("Units cannot be negative")
elif units <= 100:
    bill = units * 1.50
    print("Electricity bill: Rs.", bill)
elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50
    print("Electricity bill: Rs.", bill)
elif units <= 300:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4
    print("Electricity bill: Rs.", bill)
else:
    bill = 100 * 1.50 + 100 * 2.50 + 100 * 4 + (units - 300) * 6
    print("Electricity bill: Rs.", bill)


# 18. Calculate income tax using example slabs
print("\n18. Income Tax")
income = int(input("Enter annual income in rupees: "))
if income < 0:
    print("Income cannot be negative")
elif income <= 300000:
    tax = 0
    print("Tax:", tax)
elif income <= 600000:
    tax = (income - 300000) * 0.05
    print("Tax:", tax)
elif income <= 900000:
    tax = 15000 + (income - 600000) * 0.10
    print("Tax:", tax)
else:
    tax = 15000 + 30000 + (income - 900000) * 0.15
    print("Tax:", tax)


# 19. Check whether a student passes (minimum 35 in each subject)
print("\n19. Student Pass or Fail")
m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Student passes")
else:
    print("Student fails")


# 20. Check whether a number is within a given range
print("\n20. Number in Range")
n = int(input("Enter a number: "))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))
if low > high:
    print("Invalid range")
elif n >= low and n <= high:
    print("Number is within the range")
else:
    print("Number is outside the range")


# 21. Simple calculator
print("\n21. Simple Calculator")
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))
if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)
else:
    print("Invalid operator")


# 22. Check century leap year
print("\n22. Century Leap Year")
year = int(input("Enter year: "))
if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
elif year % 100 == 0:
    print("Century year, but not a leap year")
elif year % 4 == 0:
    print("Leap year, but not a century year")
else:
    print("Not a leap year and not a century year")


# 23. Determine season based on month number (India)
print("\n23. Season")
month = int(input("Enter month number (1-12): "))
if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month >= 3 and month <= 5:
    print("Summer")
elif month >= 6 and month <= 9:
    print("Monsoon")
elif month >= 10 and month <= 11:
    print("Post-monsoon / Autumn")
else:
    print("Invalid month")


# 24. Find the number of days in a month
print("\n24. Days in a Month")
month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))
if month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Number of days: 29")
    else:
        print("Number of days: 28")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("Number of days: 30")
elif month >= 1 and month <= 12:
    print("Number of days: 31")
else:
    print("Invalid month")


# 25. Check basic password conditions
print("\n25. Password Check")
password = input("Enter password: ")
if len(password) < 8:
    print("Password must have at least 8 characters")
elif not any(ch.isdigit() for ch in password):
    print("Password must contain at least one digit")
elif not any(ch.isupper() for ch in password):
    print("Password must contain at least one uppercase letter")
elif not any(ch.islower() for ch in password):
    print("Password must contain at least one lowercase letter")
else:
    print("Password is valid")


# 26. Ticket price based on age
print("\n26. Ticket Price")
age = int(input("Enter age: "))
if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket is free")
elif age <= 12:
    print("Ticket price: Rs. 50")
elif age <= 59:
    print("Ticket price: Rs. 100")
else:
    print("Ticket price: Rs. 60")


# 27. Calculate discount based on purchase amount
print("\n27. Purchase Discount")
amount = float(input("Enter purchase amount: "))
if amount < 0:
    print("Amount cannot be negative")
elif amount >= 10000:
    discount = amount * 0.20
    print("Discount: Rs.", discount)
    print("Final amount: Rs.", amount - discount)
elif amount >= 5000:
    discount = amount * 0.10
    print("Discount: Rs.", discount)
    print("Final amount: Rs.", amount - discount)
elif amount >= 1000:
    discount = amount * 0.05
    print("Discount: Rs.", discount)
    print("Final amount: Rs.", amount - discount)
else:
    print("No discount")
    print("Final amount: Rs.", amount)


# 28. Check driving licence eligibility
print("\n28. Driving Licence Eligibility")
age = int(input("Enter age: "))
eyesight = input("Is your eyesight acceptable? (yes/no): ").lower()
if age >= 18 and eyesight == "yes":
    print("Eligible to apply for a driving licence")
else:
    print("Not eligible based on the given conditions")


# 29. Simple login system
print("\n29. Login System")
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "Python123":
    print("Login successful")
elif username != "admin":
    print("Invalid username")
else:
    print("Invalid password")


# 30. Menu-driven calculator
print("\n30. Menu-Driven Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
choice = input("Choose an option (1-5): ")
if choice == "1":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a + b)
elif choice == "2":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a - b)
elif choice == "3":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a * b)
elif choice == "4":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)
elif choice == "5":
    print("Exit")
else:
    print("Invalid choice")
