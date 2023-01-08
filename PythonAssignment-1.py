# Ans1. We call python as general purpose and HLL because it can be used to create a variety of different programs utilizing different
#libraries and HLL because its written in human understandable format which is easy to read and write

# Ans2. Python is called dynamically typed language because the data-type is automatically asigned in run-time

# Ans3. Pros- Flexible, Extensive Libraries
# Cons - Slower in comparison to compiled langauge

# Ans4. Python can be used in multiple domain such as machine learning, artificial intelligence, deep and neural networks

# Ans5. Variables are name given to a memory location
# variables can not start with numbers, can not have any special character excluding _ underscore
# variables should start with alphabet or underscore

# Ans6. Using Input() function

# Ans7. String

# Ans8. Type-casting is when we want to certain variable to be interpreted in different form
# for eg. typecast float a variable into int -> a=int(a)

# Ans9. Yes, more no. of inputs can be taken using input() function along with different inbuilt functions such as split(), map()

# Ans10. Keywords are reserved words which are there to serve different purpose

# Ans11. No, we can not use keywords as variables. e.g. 'and' its a logical operator so can't be used as variable otherwise it will throw error

# Ans12. Indentation are spaces in beginning of the code line. Python indentation is a way of telling a Python interpreter that the group of statements belongs to a particular block of code.

# Ans13. using print() function

# Ans14. In Python, operators are special symbols that designate that some sort of computation should be performed

# Ans15. / - float division and // -> integer division

# Ans16.

print("iNeuron"*3)

# Ans17.

x=int(input("Enter a number"))
if x%2 == 0:
    print("No. is even")
else:
    print("No. is odd")


# Ans18. The operators such as not, and, or that are used to 
# perform logical operations in Python, with results of the 
# operations involving them being returned in TRUE or FALSE


# Ans19.
print(1 or 0) # ans -> 1
print(0 and 0) # and -> 0
print(True and False and True) # and -> False
print (1 or 0 or 0) # ans -> 1

# Ans 20. Python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# Ans 21. An else statement can be combined with an if statement. An else statement contains the block of code that executes if the conditional expression in the if statement resolves to 0 or a FALSE value.
# The else statement is an optional statement and there could be at most only one else statement following if.

# Ans 22.
age=int(input("enter your age:"))
if age >= 18:
    print("I can vote")
else:
    print("I can't vote")

# Ans 23.
numbers = [12, 75, 150, 180, 145, 525, 50]
sum=0
for num in numbers:
    if num%2== 0:
        sum=sum+num
print("sum of even no. from the list is: ",sum)

# Ans 24.
num1 = int(input("Enter first no."))
num2 = int(input("Enter second no."))
num3 = int(input("Enter third no."))
if (num1 > num2 and num1 > num3):
    print("The Largest number is", num1)
elif (num2 > num1 and num2 > num3):
    print ("The Largest number is", num2)
else:
    print ("The Largest number is", num3)

# Ans 25.
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 ==0 and num <= 150:
        print(num)
    elif num >500 :
        break
    else:
        continue

        
    
    
