# -*- coding: utf-8 -*-
"""Untitled86.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18hqz5YrPy8D0Hhq0W4fNRyQPdi5e-0Qf

Certainly! The abs() function in Python is a built-in function that stands for
"absolute value." It is used to obtain the absolute value of a number, which is


the distance of the number from zero on the number line, regardless of its sign.

Here's the basic syntax of the abs() function:

never get negative number
"""

abs(-5)

abs(-5 - 3)  #this complrx number just we will square

abs(-5+3)

abs(2-5)

value=int(input("enter the value"))
positive_number=value
print("the positive number are ",positive_number)

def two_numbers(num1,num2):
  return abs(num1-num2)
num1=10
num2=3
print(two_numbers(num1,num2))

def absolute_difference(x, y):
    return abs(x - y)

result = absolute_difference(10, 5)
print(result)  # Output: 5

number=[1,2,-5,-6,10]
new_numbers=[abs(x) for x in number]
print(new_numbers)

"""Ensure a Value is Within a Certain Range:


"""

temperature = -5
min_temperature = 0
adjusted_temperature = max(abs(temperature), min_temperature)
print(adjusted_temperature)  # Output: 5

"""Complex Numbers:"""

complex_num = complex(-2, 3)
magnitude = abs(complex_num)
print(magnitude)  # Output: 3.605551275463989

def three_numbers_to_find_max_value(num1,num2,num3):
  max_value=max(abs(num1),abs(num2),abs(num3))
  return max_value
num1,num2,num3=10,2,20
print(three_numbers_to_find_max_value(num1,num2,num3))

"""all"""

number=[22,4,5,6]
even_number=all(x%2==0 for x in number)
print("where all the number even numebr or not",even_number)

number=[22,3,4,5,67]
zero_greater_than=all(x>0 for x in number)
print("all the elements are zero greater than or not",zero_greater_than)

"""
The reason you are getting False is that all(word.isalpha() for word in
non_numeric_char) is iterating over each character in the string 'hello world',
not over words. The isalpha() method is checking if each character is an
 alphabetic character, and since there is a space between 'hello' and 'world',
 the condition evaluates to False.
"""

non_numeric_char='hello world'
print(non_numeric_char)
verify=all(word.isalpha() for word in non_numeric_char)
print(verify)

"""


If you want to check if all words in the string consist only of alphabetic characters, you should split the string into words first. Here's the corrected code:

"""

non_numeric_char='hello world'
new_split=non_numeric_char.split()
#because ther is no space that the here we will get ouptut as the true
print(new_split)
verfit_karo=all(x for x in new_split)
print(verfit_karo)

words = ["apple", "banana", "cherry"]
result = all(word for word in words)
print(result)  # Output: True

empty_list = []
result = all(empty_list)
print(result)  # Output: True

numbers = [3, -5, 8, 12]
result = all(num > 0 for num in numbers)
print(result)  # Output: False

def all_number_in_another_list(num1,num2):
  check_all_elements_into_the_another_list=all(x in num2 for x in num1 )
  return check_all_elements_into_the_another_list

num1=[1,2,4,5]
num2=[1,2,4]
print(all_number_in_another_list(num1,num2))

mixed_data = [True, 42, "hello", [1, 2, 3]]
result = all(isinstance(item, (int, str)) for item in mixed_data)
print(result)  # Output: False

"""any is the anyone value in list,tuple,set,dict..etc it gives true if otherwise gave the false condition"""

number=[1,2,4]
new_numbers=any(x>2 for x in number)
print(new_numbers)

number=['jagan','ciet','cse']
new_number=any(len(x)>3 for x in number)
print(f"here the length is 3 greater than {new_number}")

number=['jagan','ciet','cse']
new_number=any(x=='jagan' for x in number)
print(f"here the length is 3 greater than {new_number}")

"""tuple compreshions"""

tuple_result = tuple(expression for item in iterable if condition)

number=[1,1,3,4]
number=any(x%2==0 for x in number)
print(number)

number=[1,1,3,4]
number=any(x%2==0 for x in number if x)
print(number)

new_number=[1,'jagan',""]
new_line=any(x for x in new_number if x)
print(new_line)

new_character="'this is jagan belongs to the chalapathi istitute of engineeinga and technology"
new_line=tuple(y for x in new_character for y in x)
print(new_line)

"""ascii

ord() Function: This function takes a character as an argument and returns its ASCII value.

chr() Function: This function takes an ASCII value as an argument and returns the corresponding character.
"""

for x in 'ABCDEFGHIJK':
  print(f"the ascill of the char {x} is value of {ord(x)}")

number='abcbdebfgjhnvnminl'
for x in number:
  print(f"the ascill of the char {x} is value of {ord(x)}")

"""print("""

print(f"to space value is the {ord(x)}")
a='c'
print(ord(a))
b='d'
print(ord(b))
c=' '
print(ord(c))
s='&'
print(ord(s))
p='^'
print(ord(p))

for x in '@#$%^&*(())|}{::}*.,/?~!.':
  print(f"ascii value the sepcial characters {ord(x)}")

num='1'
print(ord(num))
a='10'

b='a'
c=ord(b)
print(c)

number=97
number1=chr(number)
print(number1)

number=222
number1=chr(number)
print(number1)

number='^'
number1=ord(number)
print(number1)

number=94
number1=chr(number)
print(number1)

char=input("enter the characters")
print(type(char))
if ord('A')<=ord(char) or ord('a')<=ord(char):
  print("somEthing")

number=10
binary_number_rep=bin(number)
print(binary_number_rep)

binary_values=34
new_binary_values=bin(binary_values)
print(new_binary_values)

print(new_binary_values[2:])

binary_values=63
new_binary_values=bin(binary_values)
print(new_binary_values[2:])

binary_values=0
new_binary_values=bin(binary_values)
print(new_binary_values[2:])

"""bool"""

number=[1,23]
number1=bool(number)
print(number1)
new_number=''
new_set=bool(new_number)
print(new_set)
extra=None
new_none=bool(extra)
print(new_none)

values='HELLO WORDLF'
new_values=bool(values)
print(type(new_values))
print(new_values)

new_list=[]
new_list1=bool(new_list)
print(type(new_list1))
print(new_list1)

new_list=[1,2,]
new_list2=bool(new_list1)
print(new_list2)

new_list=(1,2,)
new_list2=bool(new_list1)
print(new_list2)

new_list=(1,2,3)
new_list2=bool(new_list1)
print(new_list2)

values=0
new_values=bool(values)
print(new_values)

values=23
new_values=bool(values)
print(new_values)

new_list=[1,2,None]
new_list2=bool(new_list1)
print(new_list2)

"""if anyone value is true within your list,tuple,set like this"""

ones=[1,2,3,4,True]
two=bool(ones)
print(two)

new_list = [1, 2, True,True]
new_list2 = bool(new_list)
print(new_list2)

new_list = [1, 2, True,True,False,False]
new_list2 = bool(new_list)
print(new_list2)

new_list = [1, 2, False,False,True]
new_list2 = bool(new_list)
print(new_list2)

"""even the list false have it gave the True"""

new_list = [1, 2, False,False]
new_list2 = bool(new_list)
print(new_list2)

def add(n1,n2):
  z=n1+n2
  breakpoint()


  return z
n1=2
n2=5
print(add(n1,n2))

def example_function(x, y):
    z = x + y
    breakpoint()  # This will pause the execution here
    return z

result = example_function(3, 4)
print(result)

def add(a, b):
  return a + b

def main():
  a = 5
  b = 10
  c = add(a, b)
  print(c)

if __name__ == "__main__":
  breakpoint(10)
  main()

a=complex(6,9)
print(a)
b=3+3j
print(type(b))
print(b)



"""a-> quotient
b->remainder
"""

a=9
b=4
new_line=divmod(a,b)
print(new_line)

c,d=9,0
new_line1=divmod(a,b)
print(new_line1)

e,f=10,5
quotient,reaminder=divmod(e,f)
print("quotient",quotient)
print("reaminder",reaminder)

"""enumerate"""

number=[1,4,5,6]
list(enumerate(number))

number=[1,4,5,6]
for x,value in enumerate(number):
  print(f"index of the start from the {x} and the value of the based whatevver assign of the list {value}")

"""eval


The eval() function in Python is a built-in function that evaluates a Python

expression as a string and returns the result. Its syntax is:
"""

y=eval("2+5")

print(y)

z=eval("0+3")
print(z)
x=eval("2+3")
print(x)

print("22+8")

number=[1,2,3,4]
new_number=filter(lambda x:x%2==0,number)
new_line=list(new_number)
print(new_line)

def is_even(number):
  return number%2==0
number=[2,4,17]
new_assign=filter(is_even,number)
new_number=list(new_assign)
print(new_number)

"""float"""

a=9.0
print(type(a))
b=8+9.0
print(type(b))
c=6.0+9+9
print(c)
print(type(c))

"""format"""

age=10
name='jagan'
print("here the {} and the {} of the".format(age,name))

age=10
name='jagan'
print("here the {} and the {} of the".format(name,age))

dir("dict")

help('list')

"""id means address of the memory locations"""

a=10
b=10
print(id(a))
print(id(b))
c=10
d='10'
print(id(c),id(d))
e=10.0
f=10
print(id(e),id(f))
g='10'
h=10
print(id(g),id(h))

input_value=input("enter the value ")
print(input_value)
input_value1=input("enter customized value ")

print(input_value1)

new_value=int(input("enter the value "))
print(new_value)
new_life=input("enter the string ")
print(new_life)

number=['jagan',1,23,'something',12.0]
num1=[]
num2=[]
num3=[]
for x in number:
  if isinstance(x,str):
     num1.append(x)

  elif isinstance(x,int):
    num2.append(x)
  elif isinstance(x,float):
    num3.append(x)

print(num1)
print(num2)
print(num3)

my_list = [1, 2, 3, 4]

# Create an iterator from the list
my_iterator = iter(my_list)

# Access elements using the iterator
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2

for x in my_iterator:
  print(x)

number=[1,2,3,4,6,7,'mahesh babu']
print(len(number))

jagan='this is jagan'
list_of_values=list(jagan)
print(list_of_values)

jagan='jagan is jagan'
split_actual_string=jagan.split()
print(split_actual_string)

new=('jagan mohan reddy')
new_line=list(new)
print(new_line)
print(type(new_line))

def square(number):
  return number%2==0
number=[1,2,3,4,5,10]
number3=list(filter(square,number))

print(number3)

def new_number(x):
  return x if x>5 else None
number=[10,2,45,5,7,8,0]
number2=map(new_number,number)
square_values=list(number2)
print(square_values)

new_numbers=[1,45,6,789,34]
new_line=max(new_numbers)
print(new_line)

new_numbers=[1,45,6,789,34]
new_line=min(new_numbers)
print(new_line)

numbers=iter([1,256,78,9,0])
print(next(numbers))
print(next(numbers))

numbers=iter([1,34,5,6,8])
for x in numbers:
  print(x)

list2=[2,4,5,6]
list3=iter(list2)
print(list3)
print(next(list3))
print(next(list3))
print(next(list3))

"""octal"""

number='56'
new_number=int(number,8)
print(new_number)
binary_conversion=bin(new_number)
print(binary_conversion)
print(binary_conversion[2:])

number='567'
new_number=int(number,8)
print(new_number)
binary_conversion=bin(new_number)
print(binary_conversion)
print(binary_conversion[2:])

a=bin(101110111)
print(a)

octal_number1 = '22'
octal_number2 = '70'

# Convert octal numbers to decimal
decimal_number1 = int(octal_number1, 8)
decimal_number2 = int(octal_number2, 8)
print(decimal_number1)
print(decimal_number2)
print()

# Using bin() to convert decimal numbers to binary
binary_representation1 = bin(decimal_number1)
binary_representation2 = bin(decimal_number2)

print(binary_representation1)
print(binary_representation2)

new_number='27.375'
first,second=new_number.split('.')
print(first)
print(second)
one=int(first,8)
print(one)
two=bin(one)

print("binary conversion",two)
print("binary conversion",two[2:])
three=int(second,8)
print(three)
four=bin(three)
print("binary conversion",four)

"""oct to decimal"""

new_number='675'
decimal_number=int(new_number,8)
print(decimal_number)

new_number='56'
decimal_number=int(new_number,8)
print(decimal_number)

new_number='74'
decimal_number=int(new_number,8)
print(decimal_number)

new_number='44'
decimal_number=int(new_number,8)
print(decimal_number)

"""oct number to hexa decimal"""

octal_number='331'
new_number=int(octal_number,8)
print(new_number)
#hexa
hexa_decimal_number=hex(new_number)
print(hexa_decimal_number)

octal_number='1657'
new_number=int(octal_number,8)
print(new_number)
#hexa
hexa_decimal_number=hex(new_number)
print(hexa_decimal_number)

binary_number='100111011'
new_number=int(binary_number,2)
print(new_number)
octal_conversion=oct(new_number)
print(octal_conversion)

binary_number='11100111011'
new_number=int(binary_number,2)
print(new_number)
octal_conversion=oct(new_number)
print(octal_conversion[2:])

binary_number='1100111011'
new_number=int(binary_number,2)
print(new_number)
octal_conversion=oct(new_number)
print(octal_conversion[2:])

"""binary to decimal"""

binary_number='10010'
decimal_number=int(binary_number,2)
print(new_number)

binary_number='11011'
decimal_number=int(binary_number,2)
print(decimal_number)

binary_number='1100011'
decimal_number=int(binary_number,2)
print(decimal_number)

binary_number='1100.101'
first,second=binary_number.split('.')
print(first,second)
decimal_number1=int(first,2)
decimal_number2=int(second,2)
print(decimal_number1)
print(decimal_number2)

"""binary to hexa decimalx"""

binary_number='101011001111'
new_number=int(binary_number,2)
hexa_decimal_number=hex(new_number)
print(f"hexa decimal number is {hexa_decimal_number[2:]}")
print(f"hexa decimal number is {hexa_decimal_number}")

binary_number='1011101010'
new_number=int(binary_number,2)
hexa_decimal_number=hex(new_number)
print(f"hexa decimal number is {hexa_decimal_number[2:]}")
print(f"hexa decimal number is {hexa_decimal_number}")

binary_number='101110101010101000100'
new_number=int(binary_number,2)
hexa_decimal_number=hex(new_number)
print(f"hexa decimal number is {hexa_decimal_number[2:]}")
print(f"hexa decimal number is {hexa_decimal_number}")

"""decimal to binary"""

n='10'
n=int(n,10)
nbinary_number=bin(n)
print(nbinary_number)
print(nbinary_number[2:])

n='20'
n=int(n,10)
nbinary_number=bin(n)
print(nbinary_number)
print(nbinary_number[2:])

n='75'
n=int(n,10)
nbinary_number=bin(n)
print(nbinary_number)
print(nbinary_number[2:])

n='75'
n=int(n,10)
nbinary_number=oct(n)
print(nbinary_number)
print(nbinary_number[2:])

"""decimal to octal"""

n='394'
n=int(n,10)
nbinary_number=oct(n)
print(nbinary_number)
print(nbinary_number[2:])

n='22'
n=int(n,10)
nbinary_number=oct(n)
print(nbinary_number)
print(nbinary_number[2:])

n='35'
n=int(n,10)
nbinary_number=oct(n)
print(nbinary_number)
print(nbinary_number[2:])

n='124'
n=int(n,10)
nbinary_number=oct(n)
print(nbinary_number)
print(nbinary_number[2:])

"""binary to hexa decimal"""

n='312'
n=int(n,10)
nbinary_number=hex(n)
print(nbinary_number)
print(nbinary_number[2:])

number='345'
new_number=int(number,10)
print(new_number)
binary=hex(new_number)
print(binary)

number='A98E'
new_number=int(number,16)
print(new_number)
binary=bin(new_number)
print(binary)

number='A89f'
new_number=int(number,16)
print(new_number)
binary=bin(new_number)
print(binary)

number='A89f'
new_number=int(number,16)
print(new_number)
binary=oct(new_number)
print(binary)

number='c'
new_number=ord(number)
print(new_number)

"""pow()"""

new_line=pow(2,3)
print(f"power of the 2 and  3 three numbers are {new_line}")

"""three arguments a^b=some value and the some value%c="""

new_line=pow(2,3,5)
print(f"power of the 2 and  3 three numbers are {new_line}")

new_line=pow(2,3,20)
print(f"power of the 2 and  3 three numbers are {new_line}")

"""print"""

print("'chala pathi ' ")

new_value=[]
for x in range(0,20,2):
  new_value.append(x)
print(f"to display the even number are",new_value)

for x in range(0,20,-2):
  new_value.append(x)
print(f"to display the even number are",new_value)

"""**repr** it gaves the string format"""

number=45
new_number=repr(number)
print(new_number)
print(type(new_number))

char='jagan'
new_number1=repr(char)
print(new_number1)
print(type(new_number1))

new_char='jaagn'+'mohan'
new_line=repr(new_char)
print(new_line)
print(type(new_line))

number=[1,4,9]
for x,words in enumerate(reversed(number)):
  print(x,words)

number=[1,4,5,6]
for x in reversed(number):
  print(x)

"""
In Python, the round() function is a built-in function used to round a floating-point number to a specified number of digits. The general syntax of round() is as follows:"""

round(number[, ndigits])

"""round figure"""

number=round(3.578)
print(number)

number=round(3.45)
print("round number is the",number)
number1=round(3.4545,2)
print("round number is the",number1)
number2=round(3.454)
print("round number is the",number2)
number3=round(3.654)
print("round number is the",number3)
number3=round(37,-1)
print("round number is the",number3)
# Round to the nearest integer
result1 = round(3.14159)
print(result1)  # Output: 3

# Round to two decimal places
result2 = round(3.14159, 2)
print(result2)  # Output: 3.14

# Round to the nearest multiple of 5
result3 = round(27, -1)
print(result3)  # Output: 30

# Round to the nearest multiple of 100
result4 = round(678, -2)
print(result4)  # Output: 700

# Rounding with ties (round half to even)
result5 = round(0.5)
print(result5)  # Output: 0
result6 = round(1.5)
print(result6)  # Output: 2

"""slice"""

name='jagan mohan '
new_line=name[::-1]
print(new_line)

name='jagan mohan '
new_line=name[0::2]
print(new_line)

"""sorted"""

number=[10,34,2,4,0,-7,-6]
new_line=sorted(number,reverse=True)
print(new_line)

"""str"""

number=22
new_number=str(number)
print(new_number)
print(type(new_number))

"""sum"""

numbers=[19,2,3,-0-8-9]
new_numbers=sum(numbers)
print("sum of the numbers of the list",new_numbers)
print(type(new_numbers))

"""type"""

a=10
print(type(a))

"""tuple"""

new_names=20,30,50,
print(type(new_names))

new_names=20,30,50,
print(type(new_names))

new_assign=20,30,50,
print(type(new_assign))

new_numbers = [1, 2, 4, 5]
new_line = [10, 2, 3, 10]

for x, y in zip(new_numbers, new_line):
    # Perform some operation with x and y
    result = x + y
    print(f"Sum of {x} and {y} is {result}")

numbers = [1, 23, 4]
new_lesson = [10, 25, 3, 55]

for x, y in zip(numbers, new_lesson):
    # Perform some operation with x and y
    result = x + y
    print(f"Sum of {x} and {y} is {result}")

new_line=[1,2,4,56]
new_Sector=[10,20,30]
new_life=new_line+new_Sector
print(new_life)

x = [1, 2, 3]
y = [4, 5, 6]
print(list(zip(x, y)))

x2, y2 = zip(*zip(x, y))
print(x2)
print(y2)

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]

# using zip() to map values
mapped = zip(name, roll_no)

print(set(mapped))

names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)

name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]

for x, (new_name, age) in enumerate(zip(name, roll_no)):
    print(f"Person {x+1}: Name: {new_name}, Roll No: {age}")

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']
zipped = zip(list1, list2, list3)
print(list(zipped))

x=['jagan','sai','sap']
y=[20,30,40]

new_lines={new:n_news for new,n_news in zip(x,y)}
print(new_lines)

stocks = ['GEEKS', 'For', 'geeks']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
            prices in zip(stocks, prices)}
print(new_dict)

number=[123,245,78]
new_value=[]
for x in number:
  new=str(x)[0]

  new_value.append(int(new))
print(new_value)

n1=[1,2,3,4,5]
n2=[2,3,4,5,7]
new=zip(n1,n2)
new_life=list(new)
print(new_life)
#whenever iterate the list eliminate insidee the tuple gave
for x in new_life:
  print(x)