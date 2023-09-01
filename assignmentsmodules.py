"""Module 1"""
"""Exersice 1
firstname = input("Enter your firstname please")
secondname = input("Enter your secondname please")
print("Hello, " + firstname + " " + secondname + "!")"""
"""Exersice 2
I did it"""
"""Module 2"""
"""Exersice 1
firstname = input("Enter your firstname please")
print("Hello, " + firstname + "!")"""
"""Exersice 2
radius = float(input("Enter a radius of a circle"))
area = float(2 * radius * radius)
print(area)"""
"""Exersice 3
length = float(input("Enter length of a rectangle please"))
width = float(input("Enter width of a rectangle please"))
perimeter = float(length + width)
area = float(length * width)
print(perimeter)
print(area)"""
"""Exersice 4
a = int(input("Enter first number please"))
b = int(input("Enter second number please"))
c = int(input("Enter third number please"))
sum = int(a + b + c)
product = int(a * b * c)
average = float((a + b + c) / 3)
print(f"sum: {sum} product: {product} average: {average:.2f}")"""
"""Exersice 5
talents = float(input("Enter mass in talents please"))
pounds = float(input("Enter mass in pounds please"))
lots = float(input("Enter mass in lots please"))
talentsintopounds = float(talents * 20)
poundsintolots = float((talentsintopounds + pounds) * 32)
lotsintograms = float((poundsintolots + lots) * 13.3)
kilograms = float(lotsintograms // 1000 )
grams = float(lotsintograms - (kilograms * 1000))
print(f"The weight in modern units: \n{kilograms:.0f} kilograms and {grams:.2f} grams.")"""
"""Exersice 6
I honestly don't know how to do it. We didn’t seem to take it to class, or I missed it :(."""
"""Module 3"""
"""Exersice 1
length = float(input("Enter length of a zander please"))
if length < 42:
    size = float(42-length)
    print(f"Release the fish back into the lake please. \nThe zander does not fulfill the size limit. Your zander is below the size limit by {size:.2f} centimeters.")
else:
    print("The zander is true to size. You caught a fish, congratulations!")"""
"""Exersice 2
cabin = input("Enter the cabin class of cruise ship please")
if cabin == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin == "A":
    print("Above the car deck, equipped with a window.")
elif cabin == "B":
    print("Windowless cabin above the car deck.")
elif cabin == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")"""
"""Exersice 3
gender = input("What is your biological gender? Male or Female")
value = float(input("What is your hemoglobin value (g/l)?"))
if gender == "Male":
    print("You are male.")
    if value < 134:
        print("Your hemoglobin is below average.")
    elif value >= 134 and value <= 167:
        print("Your hemoglobin value is normal.")
    elif value > 167:
        print("Your hemoglobin is above average.")
    else:
        print("You are not a male.")
if gender == "Female":
    print("You are female.")
    if value < 117:
        print("Your hemoglobin is below average.")
    elif value >= 117 and value <= 155:
        print("Your hemoglobin value is normal.")
    elif value > 155:
        print("Your hemoglobin is above average.")
    else:
        print("You are not a Female.")
if gender != "Male" and gender != "Female":
    print("Please write gender again.")"""
"""Exersice 4
year = float(input("Please enter year."))
if year % 4 == 0 and year % 100 != 0:
    print("The year is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")"""
#this is just a test