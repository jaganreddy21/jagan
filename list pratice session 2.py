# -*- coding: utf-8 -*-
"""Copy of Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w-9h5mZl_31-o_KF9wej1QCmPX24X2S8

second smallest element
"""

number=[1,50,1,7,8,9]
items=[]
for x in number:
  if x not in items:
    items.append(x)
    items.sort()
print("second element",items[1])
print("third element",items[2])

"""Write a Python program to find the second largest number in a list.

first largest
"""

number=[1,5,6,30,45,9]
number2=number[0]
for element in number:
  if element>number2:
    number2=element
print(number2)

"""second and third largest element in list

code not working you will be different comphiler work it properly
"""

number=[1,5,6,30,45,9]
number1=max(number)

number2=[x for x in number if x!=number1]
print("second largest element in our list",max(number2))
number3=max(number2)
number4=[x for x in number2 if x!=number3]
print("third largest element",max(number4))

"""first and second largest element"""

number=[2,0,55,45,780,568]
items1=[]
for x in number:
  if x not in items1:
    items1.append(x)
items1.sort()
print("first largest element ",items1[-1])
print("second largest element",items1[-2])
print("thrid largest element",items1[-3])

"""this code is not working here you will use different comphilers

second largest element
"""

number=[1,2,5,6,953,56]
number2=max(number)
for x in number:
    if x==number2:
        number.remove(x)
print("second element largest",max(number))

"""another apporach"""

number=[22,891,890,2563]
number.sort()
print("first largest element",number[-1])
print("second largest element ",number[-2])

""" Write a Python program to get unique values from a list."""

def unique_values(number):
  items2=[]
  for x in number:
    if x not in items2:
      items2.append(x)
  return items2
print(unique_values([10, 20, 30, 40, 20, 50, 60, 40]))

my_list = [10, 20, 30, 40, 20, 50, 60, 40]
my_list1=set(my_list)
print("to print the unique values are the ",(list(my_list1)))

my_list = [10, 20, 30, 40, 20, 50, 60, 40]
items2=[]
for x in my_list:
  if x not in items2:
    items2.append(x)
print("to the printed unique values ",items2)

my_list = [10, 20, 30, 40, 20, 50, 60, 40]
items7=[]
p=[x for x in my_list if x not in items7]
print("to print unique values",p)

def unique(values):
  value1=[]
  for x in values:
    if values.count(x)==1:
      value1.append(x)
  return value1
print(unique([10, 20, 30, 40, 20, 50, 60, 40]))

def unique(values):
  new_list=[]
  for value in values:
    if values.count(value) == 1:
      new_list.append(value)
  return new_list
print(unique([5, 4, 3, 4, 3]))

list_integers = [540, 986, 21, 540, 986, 21, 263, 556, 689, 908, 421, 469, 536]

print(list(i for i in list_integers if list_integers.count(i) == 1))

p=[x for x in list_integers if list_integers.count(x)==1]
print("to print unique values are",p)

""" Write a Python program to get the frequency of elements in a list"""

new_list1=[10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
p=[x for x in new_list1 if new_list1.count(x)>1]
print(p)

new_list1=[10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
items8=[]
count=0
for x in new_list1:
  if new_list1.count(x)>1:
    count+=1
    items8.append(count)
print(items8)

"""dict compreshions"""

new_list1=[10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
count_occurences_of_the_sentence={x:new_list1.count(x) for x in new_list1}
print("frequnecy alphbetic letter are",count_occurences_of_the_sentence)

def count_of_words_frequency(values):
  x={x:values.count(x) for x in values}
  return x
print("frequency of element are:",(count_of_words_frequency([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30])))

list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
count=0
for x in range(40,len(list1)):
  if x>=40 and x<=100:
    count+=1
    print(count)

list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
list2=[x for x in list1 if x in range(40,100)]
list3=len(list2)
print(list3)

def generate_sublists(input_list):
    all_sublists = []

    for i in range(len(input_list) + 1):
        for j in range(i + 1, len(input_list) + 1):
            sublist = input_list[i:j]
            all_sublists.append(sublist)

    return all_sublists

# Example usage
my_list = [1, 2, 3]
result = generate_sublists(my_list)

print(result)

def generate_sublists(input_list):
    all_sublists = []

    for i in range(len(input_list) + 1):
        for j in range(i + 1, len(input_list) + 1):
            sublist = input_list[i:j]
            all_sublists.append(sublist)

    return all_sublists

# Example usage
my_list = [10, 20, 30,40]
result = generate_sublists(my_list)

print(result)

# Import the 'combinations' function from the 'itertools' module, which is used to generate combinations

from itertools import combinations

# Define a function named 'sub_lists' that generates all possible sublists of a given list 'my_list'
def sub_lists(my_list):
    subs = []  # Create an empty list 'subs' to store the sublists

    # Iterate through the range of numbers from 0 to the length of 'my_list' + 1
    for i in range(0, len(my_list) + 1):
        # Use the 'combinations' function to generate all combinations of 'my_list' of length 'i'
        temp = [list(x) for x in combinations(my_list, i)]

        # Check if 'temp' contains any elements; if so, extend the 'subs' list with the generated sublists
        if len(temp) > 0:
            subs.extend(temp)

    return subs  # Return the list of generated sublists

# Define a list 'l1' containing numeric elements and another list 'l2' containing string elements
l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']

# Print the original list 'l1'
print("Original list:")
print(l1)

# Print a label indicating the start of sublist generation for 'l1'
print("Sublists of the said list:")

# Call the 'sub_lists' function with 'l1' and print the sublists of 'l1'
print(sub_lists(l1))

# Print a newline for separation
print("\nOriginal list:")
print(l2)

# Print a label indicating the start of sublist generation for 'l2'
print("Sublists of the said list:")

# Call the 'sub_lists' function with 'l2' and print the sublists of 'l2'
print(sub_lists(l2))

"""this taken by the defalut tuple"""

from itertools import combinations
def sublist(mylist):
  sub=[]
  for x in range(0,len(mylist)+1):
    temp=[y for y in combinations(mylist,x)]
    if len(temp)>0:
      sub.extend(temp)
  return sub
print(sublist(['x','y','z']))
print(sublist([10,20,30,40]))

"""we will mention the list that time output in the form list"""

from itertools import combinations
def sublist(mylist):
  sub=[]
  for x in range(0,len(mylist)+1):
    temp=[list(y) for y in combinations(mylist,x)]

    if len(temp)>0:
      sub.extend(temp)
  return sub
print(sublist(['x','y','z']))
print(sublist([10,20,30,40]))

""". Write a Python program to check whether a list contains a sublist."""

list1=[1,2,4]
list2=[1]
list3=[]
for x in list1:
  for x in list2:
    list2.append(x)



"""consecutively eleement is subset
ex =[1,3,5,6,7]=[6,7] is sublist
[1,6] is not sublist element are not a consecutively
"""

def is_subset(blist):
  alist = [2,4,3,5,7]
  if ''.join(map(str,blist)) in ''.join(map(str,alist)):
    return True

  return False

print(is_subset([4,3]))
print(is_subset([3,7]))
print(is_subset([5,7]))

list1 = [4, 3]
list2 = [2, 4, 3, 5, 7]
list3=[1,7]

list1 = ''.join([str(x) for x in list1])
list2 = ''.join([str(x) for x in list2])
list3=''.join([str(x) for x in list3])
print(list1 in list2)
print(list1 in list3)

print(list1)
print(list2)

"""The ''.join(map(str, blist)) and ''.join(map(str, alist)) are used to

convert the elements of the lists blist and alist to strings and

concatenate them into a single string. Here's a breakdown of why this is done:

map(str, blist) and map(str, alist):


map(str, blist) converts each element in blist to a string. Similarly,

 map(str, alist) converts each element in alist to a string.

''.join(...):


''.join(...) joins the elements obtained from the map(str, blist) and
 map(str, alist) into a single string.

The empty string '' is used as a separator, indicating that the

elements should be concatenated without any space or characters between
 them.
if ... in ...:

The if statement checks if the string representation of the elements in


blist is a substring of the string representation of the elements in alist.
"""

if ''.join(map(str,blist)) in ''.join(map(str,alist)):

"""35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""

list=['p','q']
s=5
c=[]
for x in list:
  for n in range(1,s+1):
    c.append(x+str(n))
print(c)

list=['p','q']
n=5

list1=[item+str(i) for i in range(1,n+1) for item in list]
print(list1)

list=['p','q']
n=5
c=[]
for x in range(1,n+1):
  for x1 in list:
    c.append(x1+str(x))
print(c)

"""def"""

def digit_char(list1,n):
  c=[]
  for x in list1:
    for i in range(1,n+1):
      ps=x+str(i)
      c.append(ps)
  return c
n=5
list=['p','q']
print(digit_char(list,5))

"""Write a Python program to get a variable with an identification number or string."""

n=100
print(n)
print(type(n))
print(id(n))
n='100'
print(n)
print(type(n))
print(id(n))

""" Write a Python program to find common items in two lists."""

num1=[1,3,4,5,6]
num2=[10,1,5]
num3=(set(num1)& set(num2))
print(f" common elements from the both the list {num3}")

L = [11, 33, 50,20,230,2]
for i in range(len(L)):
  if i%2==0:
    L[i],L[i+1]=L[i+1],L[i]
print(L)

"""
 Write a Python program to convert a list of multiple integers into a

 single integer.
Sample list: [11, 33, 50]

Expected Output: 113350
"""

L1 = [11, 33, 50]
B=int(''.join(map(str,L1)))
print(B)

# Import the 'groupby' function from the 'itertools' module and the 'itemgetter' function from the 'operator' module
from itertools import groupby
from operator import itemgetter

# Define a list 'word_list' containing words
word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

# Use 'groupby' to group and sort the words in 'word_list' based on the first letter of each word
# Iterate through the groups and print the first letter and the words starting with that letter
for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)

def spl(a):
  b = sorted(a)
  for i in b:
    print(i[0])
    print(i)
# Define a list 'word_list' containing words
a = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']
print(spl(a))

bank = []
n = 5
for i in range(1,n+1):
  bank.append([i])
print(bank)

# Define two lists 'list1' and 'list2' containing elements
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']
new_set1=set(list1).difference(list2)
print("missing letter between the list1 nd list2",','.join(new_set1))
print(new_set1)
new_list2=set(list2).difference(list1)
print("missing letter between the list2 nd list1",','.join(new_list2))
print(new_list2)

Write Python 3 code in this online editor and run it.
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']
new_set1=set(list1).difference(list2)
print("missing elements between the list1 and list2 ",list(new_set1))
print(new_set1)
new_Set2=set(list2).difference(list1)
print("missing elements between the list1 and list2 ",new_Set2)
print(list(new_Set2))

"""43. Write a Python program to split a list into different variables."""

my_list=[2,10,4]
var1,var2,var3=my_list
print(var1,var2,var3)
print(var1)
print(var2)
print(var3)

def list_of_elements(elements):
  if len(elements)>=5:
    var1,var2,var3,var4,var5=elements
    return var1,var2,var3,var4,var5

def split_list(my_list):
    if len(my_list) >= 5:
        var1, var2, var3, var4, var5 = my_list[:5]
        return var1, var2, var3, var4, var5
    else:
        print("Error: List should have at least 5 elements.")

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = split_list(my_list)
if result:
    print("Variable 1:", var1)
    print("Variable 2:", var2)
    print("Variable 3:", var3)
    print("Variable 4:", var4)
    print("Variable 5:", var5)

if result:
    var1, var2, var3, var4, var5 = result
    print("Variable 1:", var1)
    print("Variable 2:", var2)
    print("Variable 3:", var3)
    print("Variable 4:", var4)
    print("Variable 5:", var5)



"""Write a Python program to generate groups of five consecutive numbers in a list."""

lsit=[1,2,3,4,5,6,7,8,9,10,11,12,13,1,4,15]
list=[lsit[i:i+5] for i in range(1,len(lsit),5)]
print(list)

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
c=[]
d=[]
e=[]
f=[]
for x in list:
  if x<=5:
    c.append(x)
  elif x>=5 and x<=10:
    d.append(x)
  else:
    e.append(x)
    f=c,d,e
print(f)

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=[]
c=[]
d=[]
f=[]
for i in a:
  if i<=5:
    b.append(i)
  elif i>=5 and i<=10:
    c.append(i)
  else:
    d.append(i)
    e=b,c,d
print(e)

# Create a nested list 'l' using a list comprehension
# This list comprehension generates a 5x5 matrix with elements calculated using the formula 5*i + j
l = [[5*i + j for j in range(1, 6)] for i in range(5)]

# Print the resulting 5x5 matrix 'l'
print(l)

"""45. Write a Python program to convert a pair of values into a sorted unique array.

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)
"""

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
(7, 8), (9, 10)]
BS=[]
for x in L:
  for y in x:
    BS.append(y)
print(BS)
A=sorted(BS)
b=set(A)
print(b)

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]

J = []
for i in L:
    for j in i:
        J.append(j)

print(J)

A = sorted(J)
B = set(A)
print(B)

"""list compreshion"""

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
sort_pair=[j for x in L for j in x]
print(sort_pair)
sort_pair1=sorted(sort_pair)
print("sort the pair based uon ascending order ",set(sort_pair1))

"""Write a Python program to select the odd items from a list.

here will printe
"""

list=[1,2,3,4,5,6,7,8,9,10]
print("odd space values will be printed",list[1::2])
print(list[0::2])

color = ['Red', 'Green', 'Black']
number=[]
for x in color:
  number.append("c")
  number.append(x)
print(number)

color = ['Red', 'Green', 'Black']
name='c'
count=0
for x in color:
  color.insert(x+name,count)

color = ['Red', 'Green', 'Black']
ch='ali'
check=0
for i in range(len(color)):
  color.insert(i+check,ch)
  check +=1
print(color)

color = ['Red', 'Green', 'Black']
b=[]
for x in color:
  for y in ('c',x):
    b.append(y)
print(b)

color = ['Red', 'Green', 'Black']
b=[]
for x in color:
  b.append('c')
  b.append(x)
print(b)

color = ['Red', 'Green', 'Black']
c1=[]
for x in color:
  for y in 'c':
    c1.extend((y,x))
print(c1)

colors = [['Red'], ['Green'], ['Black']]
for x in color:
  print(x,'\n')

"""code will not work in this platfrom try to use the different comphilers"""

colors = [['Red'], ['Green'], ['Black']]
 for x in colors:

  print(list(x))

"""Write a Python program to print nested lists (each list on a new line) using the print() function."""

colors = [['Red'], ['Green'], ['Black']]
p=[print(x) for x in color]

colors = [['Red'], ['Green'], ['Black']]
print('\n'.join([str(lst) for lst in colors]))

color = [['Red'], ['Green'], ['Black']]
n=[print(i) for i in color]

"""51. Write a Python program to split a list every Nth element.
Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""

list= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

[list[x::3]for x in range(3)]

list= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n=5
b=[]
for x in range(n):
  b.append(list[x::n])
print(b)

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
ls = []
n = 3
for x in range(n):
  ls.append(lst[x::n])
print(ls)

def characters(lst,n):
  return [lst[x:x+n] for x in range(0,len(lst),n)]
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

n = 5
print(characters(lst,n))

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def test(m, n):
  return [m[i:i+5] for i in range(0, len(a), n)]
print(test(a, 5))

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
list1= []
new_list= []
for j in range(3):
  for i in range(j,len(list),3):
    new_list.append(list[i])
    list1.append(new_list)
print(list1)

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
ts=[]
bs=[]
cs=[]
ps=[]
for x in list:
  if list.index(x)%3==0:
    ts.append(x)
  if list.index(x)%3==1:
    bs.append(x)

  if list.index(x)%3==2:
    cs.append(x)

print([ts,bs,cs])

""" Write a Python program to compute the difference between two lists.

Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]

Expected Output:

Color1-Color2: ['white', 'orange', 'red']

Color2-Color1: ['black', 'yellow']
Click me to see the sample solution
"""

data1=["red", "orange", "green", "blue", "white"]
data2=["black", "yellow", "green", "blue"]
new_data1=set(data1).difference(data2)
print(new_data1)

new_data2=set(data2).difference(data1)
print(new_data2)

data1=["red", "orange", "green", "blue", "white"]
data2=["black", "yellow", "green", "blue"]


xn=[]
for x in data1:
  if x not in data2:
    xn.append(x)
print("difference between the data1 and data2",xn)
bn=[]
for x in data2:
  if x not in data1:
    bn.append(x)
print("difference between the daat2 and data1",bn)

"""Write a Python program to create a list with infinite elements"""

colors=['jagan','mohan']
print(''.join(colors))