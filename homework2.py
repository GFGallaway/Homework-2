# author is Gabby Gallaway
#Problem 1
def print_name(name):
    print("The name is", name)

print_name("Gabby")

#Problem 2
import math
def ninety(a,b,c):
    d=360-(a+b+c)
    return d

print(ninety(24, 75, 34))

#Problem 3
def miles_per_hour(miles,hours,minutes,second):
    total_hours=hours+(minutes/60)+(second/3600)
    mph=miles/total_hours
    return mph

print(miles_per_hour(69, 4, 55, 27))

#Problem 4
def name(x):
    if x=="Gabby":
        print("Hello,", x)
    else:
        print("Goodbye")

name("Gabby")
name("Faye")

#Problem 5
def convert_temperature(temp,units):
    if units=="celsius":
        f_temp=(temp*(9/5))+32
        return f_temp
    if units=="farenheit":
        c_temp=(temp-32)*5/9
        return c_temp

print(convert_temperature(69,"celsius"), "degrees farenheit")
print(convert_temperature(69,"farenheit"), "degrees celsius")

#Problem 6
def calculate_grade(score):
    if score>90:
        print("Your grade is an A")
    if 80<score<90:
        print("Your grade is a B")
    if 70<score<80:
        print("Your grade is a C")
    if 60<score<70:
        print("Your grade is a D")
    if score<60:
        print("Your grade is an F")

calculate_grade(69)
calculate_grade(98)
