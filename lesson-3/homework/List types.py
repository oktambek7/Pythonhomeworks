#1.Count Occurrences: Given a list and an element, find how many times the element appears in the list.

import copy


my_list=['pen', 'pencil', 'ruler', 'textbook', 'pen', 'pencil']
counted_el=my_list[2]
count=my_list.count(counted_el)
print(count)

#2.Sum of Elements: Given a list of numbers, calculate the total of all the elements.

list=[1, 2, 3]
total=len(list)
print(total)

#3.Max Element: From a given list, determine the largest element.

a=[32, 13, 342, 52, 134]
largest_element=max(a)
print(largest_element)

#4.Min Element: From a given list, determine the smallest element.

b=[121,522,563,735,346]
min_el=min(b)
print(min_el)

#5.Check Element: Given a list and an element, check if the element is present in the list.

num=int(input('Enter number: '))
a=[1,2,3]

if num in a:
    print(f"{num} is in the list.")
else:
    print(f"{num} is NOT in the list.")

#6.First Element: Access the first element of a list, considering what to return if the list is empty.

my_list=[1,2,3,4,5]
if my_list:
    first_el=my_list[0]
    print("First element:", first_el)
else:
    print("List is empty.")

#7.Last Element: Access the last element of a list, considering what to return if the list is empty.

my_list=['a','b','c','d']
if my_list:
    last_el=my_list[3]
    print("Last element:", last_el)
else:
    print("List is empty.")


#8.Slice List: Create a new list that contains only the first three elements of the original list.

a=[21,32,534,65,2]
b=a[:3]
print("Sliced list: ", b)

#9.Reverse List: Create a new list that contains the elements of the original list in reverse order.

a=[123,2343,635,245]
b=a[::-1]
print("New list: ", b)

#10.Sort List: Create a new list that contains the elements of the original list in sorted order.

a=[142,25,964,96775]
sorted_list=sorted(a)
print("Sorted list:", sorted_list)


#11.Remove Duplicates: Given a list, create a new list that contains only unique elements from the original list.

a=[1,1,2,3,4,4]
uniqe_el=list(set(a))
print("Uniqe elements: ", uniqe_el)


#12.Insert Element: Given a list and an element, insert the element at a specified index.

a=['apple', 'orange', 'banana']
b=a[2]
print(b)

#13.Index of Element: Given a list and an element, find the index of the first occurrence of the element.

a=[21,32,52,84]
element=52
index=a.index(element)
print(f"Index of {element}:", index)


#14.Check for Empty List: Determine if a list is empty and return a boolean.

my_list=[32,42,62,73]
if my_list==(""):
    print("List is emtty.")
else:
    print("List is NOT empty.")

#15.Count Even Numbers: Given a list of integers, count how many of them are even.

a=[1,2,3,4,5,6]
even_count=sum(1 for num in a if num % 2 == 0)
print("Count of even numbers:", even_count)

#16.Count Odd Numbers: Given a list of integers, count how many of them are odd.

a=[1,2,3,4,5,6,7]
odd_count=sum(1 for num in a if num % 2 == 1)
print("Count of odd number:", odd_count)

#17.Concatenate Lists: Given two lists, create a new list that combines both lists.

a=[1,2,3,4,5]
b=[6,7,8]
new_list=[1,2,3,4,5]+[6,7,8]
print(new_list)


#18.Find Sublist: Given a list and a sublist, check if the sublist exists within the list.

a=[1,2,3,4,5]
b=[2,3,4]
if str(b)[1:-1] in str(a):
    print("Yes, sublist exists.")
else:
    print("No, sublist does not exist.")

#19.Replace Element: Given a list, replace the first occurrence of a specified element with another element.

a=[1,2,3,4]
old_value=2
new_value=30
if old_value in a:
    index=a.index(old_value)
    a[index]=new_value
print("Updated list:", a)

#20.Find Second Largest: From a given list, find the second largest element.

a=[1,2,3,4,5]
second_lar=a[3]
print(second_lar)

#21.Find Second Smallest: From a given list, find the second smallest element.

a=[1,2,3,4,5]
second_smal=a[1]
print(second_smal)


#22.Filter Even Numbers: Given a list of integers, create a new list that contains only the even numbers.

def filter_even_numbers(input_list):
    return [num for num in input_list if num %2==0]
input_list=[13,15,19,20,45,60]
even_numbers=filter_even_numbers(input_list)
print(even_numbers)

#23.Filter Odd Numbers: Given a list of integers, create a new list that contains only the odd numbers.

def filter_odd_numbers(input_list):
    return[num for num in input_list if num %2!=0]
#example usage
input_list=[1,2,3,4,5,6,7,8,9]
odd_numbers=filter_odd_numbers(input_list)
print(odd_numbers)



#24.List Length: Determine the number of elements in the list.

list=[12,4,'apple','house',523]
num_of_elements=len(list)
print(num_of_elements)

#25.Create a Copy: Create a new list that is a copy of the original list.

or_list=[1,2,3]
cop_list=or_list.copy()
print(cop_list)

#26.Get Middle Element: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.

def get_middle_element(lst):
    if not lst:
        return None
    mid=len(lst)//2
    return lst[mid] if len(lst) % 2 != 0 else [lst[mid -1], lst[mid]]
print(get_middle_element([1,2,3,4,5,6,7]))
print(get_middle_element([1,2,3,4,5,6,7,8]))

#27.Find Maximum of Sublist: Given a list, find the maximum element of a specified sublist.

my_list=[1.2,32,4.1,12,5]
max_value=max(my_list)
print(max_value)

#28.Find Minimum of Sublist: Given a list, find the minimum element of a specified sublist.

list=[3,54,25,63,72,1]
min_value=min(list)
print(min_value)


#29.Remove Element by Index: Given a list and an index, remove the element at that index if it exists.

a=['apple', 'banana', 1, 'True']
removed_element=a.pop(0)
print(a)
print(removed_element)


#30.Check if List is Sorted: Determine if the list is sorted in ascending order and return a boolean.

def is_sorted(lst):
    return lst==sorted(lst)
a=[1,2,3,4]
print(is_sorted(a))

b=[34,1,53,66]
print(is_sorted(b))

#31.Repeat Elements: Given a list and a number, create a new list where each element is repeated that number of times.

old_list=[1,2,3]
new_list=[]
for item in old_list:
    new_list.extend([item] * 3)
print(new_list)


#32.Merge and Sort: Given two lists, create a new sorted list that merges both lists.

list1=[43,13,54,879]
list2=[9787,23,865,234]
new_sorted_list=sorted(list1+list2)
print(new_sorted_list)



#33.Find All Indices: Given a list and an element, find all the indices of that element in the list.

list=['cherry', 'apple','banana']
print(list[:])


#34.Rotate List: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).

a=[1,2,3,4]
print(a[::-1])

#35.Create Range List: Create a list of numbers in a specified range (e.g., from 1 to 10).

range_list=list(range(1,20))
print(range_list)

#36.Sum of Positive Numbers: Given a list of numbers, calculate the sum of all positive numbers.

def sum_of_pos_num(lst):
    return sum(num for num in lst if num>0)
my_list=[1,2,3,-4,5,-6]
print(sum_of_pos_num(my_list))


#37.Sum of Negative Numbers: Given a list of numbers, calculate the sum of all negative numbers.

def sum_of_neg_num(lst):
    return sum(num for num in lst if num<0)
my_list=[1,-2,-3,4,5,-26]
print(sum_of_neg_num(my_list))

#38.Check Palindrome: Given a list, check if the list is a palindrome (reads the same forwards and backwards).

def is_palindrome(lst):
    if lst==lst[::-1]:
        return True
    else:
        return False
my_list=[1,2,3,2,1]
print(is_palindrome(my_list))


#39.Create Nested List: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.

list1 = [["John", "Adam"], [123, 424], [4134], ["Oktam"], ["age:18"]]
list2 = []

for sublist in list1:
    if len(sublist) == 2:
        list2.append(sublist)

print(list2)

#40.Get Unique Elements in Order: Given a list, create a new list that contains unique elements while maintaining the original order.

def unique_elements(lst):
    seen = set()  # Create an empty set to track seen elements
    result = []   # Create an empty list to store the unique elements in order
    for item in lst:
        if item not in seen:  # If the item is not in the set, it's unique
            result.append(item)  # Add it to the result list
            seen.add(item)  # Mark the item as seen
    return result

# Test case
a = [1, 1, 2, 3, 3, 4, 5, 5]
print(unique_elements(a))  # Output: [1, 2, 3, 4, 5]
