# -*- coding: utf-8 -*-
"""Untitled81.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yGl5Xi36nJ3-iWG0vlKuPF8qzI779cQW
"""



"""[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

Move all zero digits to end of the said list of numbers:

[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

"""

number=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
number1=[]
number2=[]
for x in number:
  if x==0:
    number1.append(x)
  else:
    number2.append(x)
print(number2+number1)

number3=[x for x in number if x!=0]+[x for x in number if x==0]
print(f"here the zeroes will be the display itself only {number3}")

input = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
output = [x for x in input if x != 0] + [x for x in input if x == 0]
print(output)

arr = [3, 4, 0, 0, 0, 6, 2, 0, 6, 0]

for n in arr:
  if n == 0:
    arr.append(arr.pop(arr.index(0)))


print(arr)

a=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
b=[]
c=[]
for i in a:
  if i!=0:
    b.append(i)
  if i==0:
    c.append(i)

e=b+c
print(e)

"""Write a Python program to find the list in a list of lists whose sum of elements is the highest.

1+2+3=6
4+5+6=15
10+11+12=33
7+8+9=24  max sum of list3  [10,11,12]
"""

num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(max(num,key=sum))
print(max(num))
num1=sorted(num,key=sum)
print(num1)
print(num1[-1])

""". Write a Python program to find all the values in a list that are greater than a specified number."""

list1 = [220, 330, 500]

print(all(x>=240 for x in list1))
print(all(x>=200 for x in list1))

def value_greater(pylist, value):
  return [x for x in pylist if x>value]

pylist=[10,20,30,40,50,60]

print(pylist)
print(value_greater(pylist, 30))

"""Python: Extend a list without appen"""

# Define two lists, 'x' and 'y', containing integers
x = [10, 20, 30]
y = [40, 50, 60]
print(y+x)
x[:0]=y
print(x)
y.extend([10,20,30])
print(y)

def two_list_extend(x,y):
  s=y+x
  return s
x=[10,20,30]
y=[40,50,60]
print(two_list_extend(x,y))

one=[10,20,30]
two=[40,50,60]
for sa in two:
  one.insert(0,sa)
print(one)

lst1= [10,20,30]
lst2 = [40,50,60]
print(lst2+lst1)



"""69. Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

New List : [[10, 20], [30, 56, 25], [33], [40]]

"""

sample_list=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_list=[]
for x in sample_list:
  if  x not in new_list:
    new_list.append(x)
print(new_list)

l1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
l2 =[]
for i in l1:
  if i not in l2:
    l2.append(i)
print(l2)

arr = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]


new_arr = [list(t) for t in set(tuple(element) for element in arr)]


print(new_arr)

# Import the 'itertools' module for working with iterators and grouping
import itertools

# Define a list 'num' containing sublists with integers
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

# Print a message indicating the purpose of the following output
print("Original List", num)

# Sort the list 'num', which sorts the sublists lexicographically
num.sort()

# Use 'itertools.groupby' to group similar sublists and retain the first occurrence of each group
new_num = list(num for num, _ in itertools.groupby(num))

# Print a message indicating the purpose of the following output
print("New List", new_num)

"""
70. Write a Python program to find items starting with a specific character from a list.

Expected Output:
Original list:

['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

Items start with a from the said list:

['abcd', 'abc', 'acjd']
Items start with d from the said list:

['dagfa']
Items start with w from the said list:

[]
"""

def starting_characters(string1):
  return [x for x in string1 if x.startswith('a')]
print(starting_characters(['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']))
def starting_characters(string2):
  return [x for x in string2 if x.startswith('d')]



print(starting_characters(['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']))

def starting_characters(string3):
  return[x for x in string3 if x.startswith('w')]

print(starting_characters(['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']))

string1=['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
num6=[x for x in string1 if x.startswith('a')]
print(num6)
num7=[x for x in string1 if x.startswith('d')]
print(num7)
num8=[x for x in string1 if x.startswith('w')]
print(num8)

"""1. Write a Python program to check whether all dictionaries in a list are empty or not.

Sample list : [{},{},{}]

Return value : True

Sample list : [{1,2},{},{}]

Return value : False

*   List item
*   List item


"""

mylist1 =[{},{},{}]
mylist2 =[{1,2},{},{}]
print(all([i == {} for i in mylist1]))
print(all([i == {} for i in mylist2]))

""". Write a Python program to flatten a given nested list structure.

Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

Flatten list:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

"""

orginal_list=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
new_lst=[]
for i in orginal_list:
  if type(i)==int:
    new_lst.append(i)
  else:
    new_lst.extend(i)
print(new_lst)

orginal_list=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
m=[]
n=[]
for i in orginal_list:
  if type(i)==int:
    m.append(i)
  else:
    n.extend(i)

print(m+n)

orginal_list=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
m=[]
n=[]
for i in orginal_list:
  if isinstance(i,int):

    m.append(i)
  else:
    n.extend(i)

print(m+n)

"""73. Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.

Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

After removing consecutive duplicates:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

"""

def remove_consecutive_duplicates(input_list):
    return [x for x, y in zip(input_list, input_list[1:]+[None]) if x != y]

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]
result_list = remove_consecutive_duplicates(original_list)

print("Original list:", original_list)
print("List with consecutive duplicates removed:", result_list)

from itertools import groupby
def consecutive_duplicates(orginal_list):
  return [key for key ,group in groupby(orginal_list)]
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]
print(consecutive_duplicates(original_list))

a =[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
print(sorted(set(a)))
print(sorted(set(original_list)))

l1 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l2 = []
for i in range(len(l1)-1):
  if l1[i]!=l1[i+1]:
    l2.append(l1[i])
l2.append(l1[len(l1)-1]) # adding last element to the l2
print(l2)



l1 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l2 = []

for i in range(len(l1)):
    if i == len(l1) - 1 or l1[i] != l1[i+1]:
        l2.append(l1[i])

print(l2)

""". Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
Original list:

[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

After packing consecutive duplicates of the said list elements into sublists:

[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""

l2=[list(group) for key,group in groupby(l1)]
print(l2)



from itertools import groupby
def consecutive_duplicates(orginal_list):
  return [list(group) for key ,group in groupby(l1)]
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]
print(consecutive_duplicates(original_list))

"""Write a Python program to split a given list into two parts where the length of
 the first part of the list is given.


Original list:

[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3

Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])

"""

def split_wise(number,n):
  return number[:n],number[n:]
print(split_wise([1,2,2,3,4,4,5,1],3))

"""79. Write a Python program to remove the K'th element from a given list, and

 print the updated list.

Original list:

[1, 1, 2, 3, 4, 4, 5, 1]

After removing an element at the kth position of the said list:

[1, 1, 3, 4, 4, 5, 1]

"""

def remove_kth_position(number,position):

  number.remove(position)
  return number

print(remove_kth_position([1,1,3,4,4,5,1],3))

"""Write a Python program to insert an element at a specified position into a given list.
Original list:

[1, 1, 2, 3, 4, 4, 5, 1]

After inserting an element at kth position in the said list:

[1, 1, 12, 2, 3, 4, 4, 5, 1]

"""

def insert_position(number,position,n):
  number.insert(position,n)
  return number
print(insert_position([1,1,2,3,4,4,5,1],2,12))

number=[1, 1, 2, 3, 4, 4, 5, 1]
position=2
n=12
number.insert(position,n)
print(number)

"""81. Write a Python program to extract a given number of randomly selected elements from a given list.

Original list:

[1, 1, 2, 3, 4, 4, 5, 1]

Selected 3 random numbers of the above list:

[4, 4, 1]
"""

import random

def random_number(number,n):
  return random.sample(number,3)
print(random_number([1,1,2,3,4,4,5,1],3))

# Import the 'random' module to generate random numbers
import random

# Define a function 'random_select_nums' that takes a list 'n_list' and an integer 'n' as input
def random_select_nums(n_list, n):
    # Use 'random.sample' to select 'n' random elements from the input list 'n_list'
    return random.sample(n_list, n)

# Create a list 'n_list' containing integers
n_list = [1, 1, 2, 3, 4, 4, 5, 1]

# Print a message indicating the original list
print("Original list:")
# Print the original list
print(n_list)

# Assign an integer 'selec_nums' with the value 3
selec_nums = 3

# Call the 'random_select_nums' function with 'n_list' and 'selec_nums'
# and store the result in the 'result' variable
result = random_select_nums(n_list, selec_nums)

# Print a message indicating the selection of 3 random numbers from the above list
print("\nSelected 3 random numbers of the above list:")
# Print the 'result' list containing the randomly selected numbers
print(result)

from itertools import combinations
number=combinations([1, 2, 3, 4, 5, 6, 7, 8, 9],2)
for i in number:
  print(i)

"""Write a Python program to round every number in a given list of numbers and

print the total sum multiplied by the length of the list.


"""

nums = [22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]
print(nums)
nums1=len(nums)
print(nums1)
print(sum(list(map(round,nums))*nums1))

nums2=[round(x) for x in nums]
print(nums2)
nums3=len(nums2)
sum_of_elements=sum(nums2*nums3)
print(sum_of_elements)

"""Write a Python program to round the numbers in a given list, print the minimum


and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.



"""

num3=[22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
num5=list(map(round,num3))
num5.sort()
print("smallest element ",num5[0])
print("largets element",num5[-1])


print(num5)
num6=[x*5 for x in num5]
for x in num6:
  print(x,end=' ')

"""[[1, 3], [5, 7], [9, 11]]

[[2, 4], [6, 8], [10, 12, 14]]

Zipped list:

[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
"""

l1=[[1, 3], [5, 7], [9, 11]]
l2=[[2, 4], [6, 8], [10, 12, 14]]
g=[]
for a,b in zip(l1,l2):

  g.append(a+b)
print(g)

a=[[1, 3], [5, 7], [9, 11]]
b=[[2, 4], [6, 8], [10, 12, 14]]
d=[]
print(len(a))
for i,j in zip(a,b):
  d.append(i+j)
print(d)

a=[[1, 3], [5, 7], [9, 11]]
b=[[2, 4], [6, 8], [10, 12, 14]]
new_list=[]
n=len(a)
print(n)
for x in range(n):
  lst=[a[x]+b[x]]
  #if you use the append function three list we get it
  new_list.extend(lst)
  #new_list.append(lst)

print(new_list)

def compreshion(lst1,lst2):
  return [a+b for a,b in zip(lst1,lst2)]
print(compreshion([[1, 3], [5, 7], [9, 11]],[[2, 4], [6, 8], [10, 12, 14]]))

""" Write a Python program to count the number of lists in a given list of lists.
Original list:

[[1, 3], [5, 7], [9, 11], [13, 15, 17]]

Number of lists in said list of lists:

4
Original list:

[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]

Number of lists in said list of lists:
3
"""

l1=[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
count=0
for x in l1:
  if type(x)==list:
    count+=1
print("number of lists in said list of lists",count)

l2=[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
count=0
for x in l2:
  if type(x)==list:
    count+=1
print("number of lists in said list of list",count)

"""Click me to see the sample solution

91. Write a Python program to find a list with maximum and minimum lengths.
Original list:

[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

List with maximum length of lists:

(3, [13, 15, 17])

List with minimum length of lists:

(1, [0])
Original list:

[[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]

List with maximum length of lists:

(3, [3, 5, 7])
List with minimum length of lists:

(1, [0])

Original list:

[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
List with maximum length of lists:
(4, [1, 34, 5, 7])
List with minimum length of lists:
(1, [12])
"""

l1=[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]

def maximum_value(input_list):
  n1=max([len(x) for x in input_list])
  n2=max(l2,key=len)
  return n1,n2
def min_value(input_list):
  n1=min([len(x) for x in input_list])
  n2=min(l2,key=len)
  return n1,n2
print(maximum_value([[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]))
print(min_value([[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]))
print(maximum_value([[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]))

print(min_value([[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]))
print(maximum_value([[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]))
print(min_value([[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]))

def min_and_max_lists(l):
  min_list = min(l,key=len)
  print((len(min_list), min_list))
  max_list = max(l,key=len)
  print((len(max_list), max_list))
min_and_max_lists(l2)
min_and_max_lists([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])
min_and_max_lists([[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]])

"""Python: Check if a nested list is a subset of another nested list
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[1, 3], [13, 15, 17]]
# New Section

this will be simplify from the above the code
"""

def check(a,b):
  for i in a:
    for j in b:
      if j in a:
        flag=True
      else:
        return False
  return True
a=[[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
b=[[[3, 4], [5, 7]]]
print(check(a,b))

def is_subset(list1,list2):
  num1={tuple(element) for element in list1}
  num2={tuple(element) for element in list2}
  return num2.issubset(num1)
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[1, 3], [13, 15, 17]]
print(is_subset(list1,list2))

def is_subset(list1,list2):
  num1={tuple(element) for element in list1}
  num2={tuple(element) for element in list2}
  return num2.issubset(num1)
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[1, 3], [13, 14, 17]]
print(is_subset(list1,list2))

list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[1, 3], [13, 14, 17]]

def is_subset(list1, list2):
    set1 = {tuple(sublist) for sublist in list1}
    set2 = {tuple(sublist) for sublist in list2}
    return set2.issubset(set1)

# Example usage
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[1, 3], [13, 15, 14]]

result = is_subset(list1, list2)

print("Is list2 a subset of list1?", result)

def is_subset(list1, list2):
    return all(any(sublist == sub for sublist in list1) for sub in list2)

# Example usage
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[1, 3], [13, 15, 17]]

result = is_subset(list1, list2)

print("Is list2 a subset of list1?", result)

"""93. Write a Python program to count the number of sublists that contain a particular element.
Original list:

[[1, 3], [5, 7], [1, 11], [1, 15, 7]]

Count 1 in the said list:

3
Count 7 in the said list:

2
Original list:

[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]

Count 'A' in the said list:

3
Count 'E' in the said list:
1
"""

def nested_list1(nested_list,target_number):
  new_list=[element for x in nested_list for element in x]
  return new_list.count(target_number)
list1=[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
print("count of the 1 value",nested_list1(list1,1))
print("count of the 7 value",nested_list1(list1,7))
list2=[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
print("count of the value A",nested_list1(list2,'A'))
print("count of the value E",nested_list1(list2,'E'))

"""94. Write a Python program to count the number of unique sublists within a given list.
Original list:

[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]

Number of unique lists of the said list:

{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}

Original list:

[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]

Number of unique lists of the said list:

{('green', 'orange'): 2, ('black',): 1, ('white',): 1}

"""

from collections import counter
l1=[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
for x in l1:
  print(l1.index(x),x)

from collections import Counter

l1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]

# Use Counter to count occurrences of each sublist
count_dict = Counter(tuple(sublist) for sublist in l1)
print(count_dict)

from collections import Counter

l1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
for i in l1:
  print((l1.count(i),i))

"""Write a Python program to sort each sublist of strings in a given list of lists.
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

Sort the list of lists by length and value:

[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
"""

l1=[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
l1=sorted(l1,key=min)
l1=sorted(l1,key=len)
print("Sort the list of lists by length and value",l1)

"""color1 = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]"""

def color(number):
  number1=sorted(number,key=len)
  return number1
print(color([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))

"""97. Write a Python program to remove sublists from a given list of lists that contain an element outside a given range.
Original list:
[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
After removing sublists from a given list of lists, which contains an element outside the given range:
[[13, 14, 15, 17]]

"""

def remove_sublist(numbers):
  new_ones=[x for x in numbers if (min(x)>=left_value and max(x)<=right_value)]
  return new_ones
left_value=13
right_value=17
print(remove_sublist([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]))

""" Write a Python program to scramble the letters of a string in a given list.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']

After scrambling the letters of the strings of the said list:

['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']
"""

import random
list1=['Python', 'list', 'exercises', 'practice', 'solution']
n2=[''.join(random.sample(word,len(word))) for word in list1]
print(n2)
for word in list1:
  print(''.join(random.sample(word,len(word))))

"""99. Write a Python program to find the maximum and minimum values in a given heterogeneous list.
Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum and Minimum values in the said list:
(5, 2)
"""

list1=['Python', 3, 2, 4, 5, 'version']
n1=max(x for x in list1 if isinstance(x,int))
n2=min(x for x in list1 if isinstance(x,int))
print((n1,n2))

"""100. Write a Python program to extract common index elements from more than one given list.
Original lists:

[1, 1, 3, 4, 5, 6, 7]

[0, 1, 2, 3, 4, 5, 7]

[0, 1, 2, 3, 4, 5, 7]

Common index elements of the said lists:
[1, 7]

"""

li1 = [1, 1, 3, 4, 5, 6, 7]
li2 = [0, 1, 2, 3, 4, 5, 7]
li3 = [0, 1, 2, 3, 4, 5, 7]

common_li = []

for i in range(len(li1)):
  if li1[i] == li2[i] == li3[i]:
    common_li.append(li1[i])

print(common_li)

def common_elements(li1,li2,li3):
  result=[]
  for x,y,z in zip(li1,li2,li3):
    if(x==y==z):
      result.append(x) #any value values finally output are same x.y,z

  return result

li1 = [1, 1, 3, 4, 5, 6, 7]
li2 = [0, 1, 2, 3, 4, 5, 7]
li3 = [0, 1, 2, 3, 4, 5, 7]

print(common_elements([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]))

"""Original Matrix:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]

Sort the said matrix in ascending order according to the sum of its rows
[[1, 1, 1], [1, 2, 3], [2, 4, 5]]

Original Matrix:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

Sort the said matrix in ascending order according to the sum of its rows
[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]

"""

def sort_matrix(m):
  number=sorted(m)
  return number

print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))



print(sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]]))

"""Write a Python program to extract specified size of strings from a give list of string values.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']

length of the string to extract:

8
After extracting strings of specified length from the said list:

['practice', 'solution']
"""

numbers=[['Python', 'list', 'exercises', 'practice', 'solution']]
def length_of_the_string(numbers,n):
  result=[x for x in numbers if len(x)==n]
  return result
numbers=['Python', 'list', 'exercises', 'practice', 'solution']
n=8
print(length_of_the_string(numbers,n))

""". Write a Python program to extract specified number of elements from a given list, which follows each other continuously.
Original list:
[1, 1, 3, 4, 4, 5, 6, 7]


Extract 2 number of elements from the said list which follows each other continuously:
[1, 4]

Original lists:
[0, 1, 2, 3, 4, 4, 4, 4, 5, 7]

Extract 4 number of elements from the said list which follows each other continuously:

[4]
"""

from itertools import groupby
def extract_elements(number,n):
   result = [i for i, j in groupby(number) if len(list(j)) == n]
   return result
#n=2
##list1=[1, 1, 3, 4, 4, 5, 6, 7]
#print(extract_elements(list1,n))
n=1
list2=[0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
print(extract_elements(list2,n))

# Import the 'groupby' function from the 'itertools' module
from itertools import groupby

# Define a function 'extract_elements' that extracts elements from a list that follow each other continuously and occur 'n' times
def extract_elements(nums, n):
    # Use a list comprehension and 'groupby' to filter elements in 'nums' that occur 'n' times in a row
    result = [i for i, j in groupby(nums) if len(list(j)) == n]
    return result

# Create a list 'nums1' containing numbers
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]

# Set the value of 'n' to 2
n = 2

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'nums1'
print(nums1)

# Print a message indicating the number of elements to extract and the criteria for extraction
print("Extract 2 number of elements from the said list which follows each other continuously:")

# Call the 'extract_elements' function with 'nums1' and 'n', then print the result
print(extract_elements(nums1, n))

# Create a list 'nums2' containing numbers
nums2 = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]

# Set the value of 'n' to 4
n = 4

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'nums2'
print(nums2)

# Print a message indicating the number of elements to extract and the criteria for extraction
print("Extract 4 number of elements from the said list which follows each other continuously:")

# Call the 'extract_elements' function with 'nums2' and 'n', then print the result
print(extract_elements(nums2, n))

"""Write a Python program to find the difference between consecutive numbers in a given list.
Original list:
[1, 1, 3, 4, 4, 5, 6, 7]

Difference between consecutive numbers of the said list:
[0, 2, 1, 0, 1, 1, 1]

Original list:
[4, 5, 8, 9, 6, 10]

Difference between consecutive numbers of the said list:
[1, 3, 1, -3, 4]

"""

a=[1, 1, 3, 4, 4, 5, 6, 7]
print([a[i+1]-a[i] for i in range(len(a)-1)])
b=[4, 5, 8, 9, 6, 10]
print([b[i+1]-b[i] for i in range(len(b)-1)])