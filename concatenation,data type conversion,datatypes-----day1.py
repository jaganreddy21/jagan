# -*- coding: utf-8 -*-
"""Untitled73.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vG2VN0lpX1T0jwQ-Ux4vzVnKdNSG-jHk

concatnation
"""

print("hello")

print("hello"+"world")

"""hello inside space"""

print("hello "+"world")

"""world befor some space"""

print("hello "+ "world")

print("hello"+""+"world")

"""here double quotes as a string"""

print("hello"+" new thing  "+"world")

print("hello"+" "+input("what is your name")+","+"how are you")

a=10
b=20
c=a+b
print(c)
print("value of c"+str(c))

type(c)

"""concatenation ++++ like this process every single or double quote string

> Indented block

> Indented block

actually values are intgers when to concatention str
"""

price=20
cake=30
toatl=price+cake
print("the total value of"+ str(toatl)+'$'+'concurrency')

price='raja'
raji='rani'
pizaa=price+raji
print("the value of"+str(pizaa)+"rupees")

"""double quotes or single treated as a string"""

a='jagan'
b='something'
print(a+b)
print(a+" "+b)

print(a+" ,"+"something")

print(a+" something1"+b)

"""datatype conversion"""

a1=10
b1=10.0
b2=10.9
c1='jagan'
d='1+2j'

e=a1+b1
f=b1+a1+b2
print(e,f)
print(type(f))
print(type(e))

"""int to float"""

name=10
name1=float(10)
print(name1)
print(type(name1))

"""float to int"""

name2=20.0
name3=int(name2)
print(name3)
print(type(name3))



"""add two number int,folat wee will datatype is int finnaly outout also be int"""

name4=int(name+name2)
print(name4)
print(type(name4))

name5=float(name1+name2)
print(name5);print(type(name5))

"""str values of variables"""

name6='6'
name7='3'
name8=name7+name6
print(name8);print(type(name8))

name6='6'
name7='3'
name9=int(name7+name6)
print(name9);print(type(name9))

name6='6'
name7='3'
name10=str(name7+name6)
print(name10);print(type(name10))

"""one var is string and another one is int just we perform add function not working"""

name10='8'
name11=9
print(name11+name10)

"""one var is string another one is float in snot working"""

name12='8'
name13=9
name14=float(name12+name13)
print(name14)

"""string"""

name14=input("enter the value")
print(name14)
name14='jagan'
print(name14)

"""str cant be coverted into the float and int"""

name15='venky'
name16=2
print(name15+name16)

"""if you try above codes refer it same as this code"""

name18='jagan'
name19='cse'
name20=name18+name19
print("we will printed values"+str(name20)+","
+"jagan")

"""every double quote treated as a string"""

name21=10
name22=90
name23=name21+name22
print("values are  "+str(name23))

print(name21+name22+10+20)

"""list"""

s="jagan mohan"
name25=list(s)
print(name25)

name26=input("enter the name")

name28=set(name26)
print(name28)
name29=list(name26)
print(name29)

# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Converting keys to a tuple
keys_tuple = tuple(my_dict.keys())

# Converting values to a tuple
values_tuple = tuple(my_dict.values())

# Converting items to a tuple of tuples
items_tuple = tuple(my_dict.items())

# Displaying the results
print(keys_tuple)
print(values_tuple)
print(items_tuple)

key_list=list(my_dict.keys())
print(key_list)
key_list=list(my_dict.values())
print(key_list)
key_list=list(my_dict.items())
print(key_list)

key_set=set(my_dict.keys())
print(key_set)
key1_set=set(my_dict.values())
print(key1_set)
key2_set=set(my_dict.items())
print(key2_set)

tuple1=(22,3,5,6,8)
list1=list(tuple1)
print(tuple1)
tuple2=set(tuple1)
print(tuple2)

list=[22,3,5]
list1=tuple(list)
print(list1)

"""tuple datatype conversion not working in google colab"""

x="33"
print(x*3)
type(x)

x='55'+11
print(x)

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(type(my_dict))

type(my_dict)==dict

"""cocatentation"""

y='10'+'10'
print(y)

user={"mario":1,'lugi':2}
print(user.get('apple'))

"""General Python Naming Conventions

Names are case-sensitive.

Names cannot start with a digit.

Names can contain letters, numbers, and underscores

Acceptable	var, var, var, var, var1, var2, var3

Not Acceptable	1var, var-name, var nam
"""

var=10
print(10)
var1_abc=10
print(var1_abc)
var_v=34
print(var_v)
var22_abc=30
print(var22_abc)

"""not acceptable"""

1var=10
print(1var)
var name=20
print(var name)
var -nmae=56
print(var-name)

"""MyClass,Pascal name conversion"""

MyClass=10
print(MyCLASS)

JaganMohan=100
print(JaganMohan)

"""datatypes

int
"""

a,b,c,d=10,20,-20,40
print(a,b,c,d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(0))
print(type(-0))
print(a)
print(b)

print(c)
print(d)

"""float"""

a,b,c=2.0,5.0,-0.0
print(a,b)
print(type(a))
print(type(b))
print(type(c))
print(type(-90.00))
print(a)
print(b)
print(c)

"""string"""

a,b,c="jagan",'raja','ramya'
d="""ab"""
print(type(d))
print(d)
print(a,b,c)
print(type(a))
print(type(b))
print(type(c))
print(type("jagan something"))

"""string in number"""

a,b,c='5','5','7'
print(a,b,c)
print(type(a))
print(type(b))
print(type(c))
print(type("123"))

"""list"""

list=[2,3,5,7]
print(list)
print(type(list))
print(type([22,4,5]))

tuple=(2,3,5,7)
print(tuple)
print(type(tuple))
print(type((22,4,5)))

tuple={2,3,5,7}
print(tuple)
print(type(tuple))
print(type({22,4,5}))