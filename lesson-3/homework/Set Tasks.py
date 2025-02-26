#1.Union of Sets: Given two sets, create a new set that contains all unique elements from both sets.
set1={1,2,3,4,5}
set2={3,4,5,6,7}
union_set=set1|set2
print(union_set)

#2.Intersection of Sets: Given two sets, create a new set that contains elements common to both sets.

set1={1,2,3,6}
set2={1,3,4,5}
intersection_set=set1&set2
print(intersection_set)

#3.Difference of Sets: Given two sets, create a new set with elements from the first set that are not in the second.

set1={1,2,3,6}
set2={1,3,4,5}
difference_set=set1-set2
print(difference_set)

#4.Check Subset: Given two sets, check if one set is a subset of the other.

set1={1,2,3}
set2={1,2,3,4,5}
is_subset=set1<=set2
print(is_subset)

#5.Check Element: Given a set and an element, check if the element exists in the set.

set={1,2,3,4}
element_presence=3
if element_presence in set:
    print("true")
else:
    print("false")

#6.Set Length: Determine the number of unique elements in a set.

set={1,1,2,3,4,4,4,5,6,7}
unique_el=len(set)
print(unique_el)

#7.Convert List to Set: Given a list, create a new set that contains only the unique elements from that list.

list=[1,1,2,2,3,543,536,652]
unique_set=set(list)
print(unique_set)

#8.Remove Element: Given a set and an element, r emove the element if itexists.

def remove_element_discard(s, element):
    s.discard(element)
    return s

set={1,1,2,3,4,4,4,5,6,7}
print(remove_element_discard(set, 4))

#9.Clear Set: Create a new empty set from an existing set.

my_set={1,2,3,4,5}
clear_set={}
print(clear_set)

#10.Check if Set is Empty: Determine if a set has any elements.

input("Enter which set to check: ")
set1={1,2,3,4}
if set1=={}:
    print("Set is empty.")
else:
    print("Set is NOT empty.")
set2={}
if set2=={}:
    print("Set2 is empty.")
else:
    print("Set is NOT empty.")

#11.Symmetric Difference: Given two sets, create a new set that contains elements that are in either set but not in both.

def symmetric_difference_method(set1, set2):
    return set1.symmetric_difference(set2)
A={1,2,3,4}
B={3,4,5,6}
print(symmetric_difference_method(A,B))

#12.Add Element: Given a set and an element, add the element to the set if it is not already present.

def add_element(s, element):
    s.add(element)
    return s
my_set={1,2,3,4,5}
added_element=6
new_set=add_element(my_set,added_element)
print("Updated set:", new_set)


#13.Pop Element: Given a set, remove and return an arbitrary element from the set.

def pop_element(s):
    if s:
        return s.pop()
    else:
        return None
my_set={1,2,3,4}
removed_element=pop_element(my_set)
print("Removed elment:",removed_element)
print("Updated set:", my_set)


#14.Find Maximum: From a given set of numbers, find the maximum element.

a={435,675,234,786,834,126}
if a:
    max_element=max(a)
    print("Maximum element:",max_element)
else:
    print("The set is empty.")

#15.Find Minimum: From a given set of numbers, find the minimum element.

a={435,675,234,786,834,126}
if a:
    min_element=min(a)
    print("Minimum element:",min_element)
else:
    print("The set is empty.")

#16.Filter Even Numbers: Given a set of integers, create a new set that contains only the even numbers.

a={1,2,3,4,5,6,7,8}
even_numbers={num for num in a if num % 2 ==0}
print("Even numbers:", even_numbers)

#17.Filter Odd Numbers: Given a set of integers, create a new set that contains only the odd numbers.

b={234,6456,678,324,97,829,1247,876}
odd_numbers={x for x in b if x % 2 ==1}
print("Odd numbers:", odd_numbers)

#18.Create a Set of a Range: Create a set of numbers in a specified range (e.g., from 1 to 10).

range_set=set(range(1,11))
print("Range Set:", range_set)

#19.Merge and Deduplicate: Given two lists, create a new set that merges both lists and removes duplicates.

list1=[1,2,3,4,4,5,5]
list2=[6,6,7,8,9,10]
merged_set=set(list1).union(set(list2))
print("Merged Set:", merged_set)

#20.Check Disjoint Sets: Given two sets, check if they have no elements in common.

set1={1,2,3,4}
set2={5,6,7,1}
if set1.isdisjoint(set2):
    print("The sets are disjoint.")
else:
    print("The sets are NOT disjoint.")

#21.Remove Duplicates from a List: Given a list, create a set from it to remove duplicates, then convert back to a list.

a=[1,1,1,2,3,4,4,5]
unique_list=list(set(a))
print("List without duplicates:", unique_list)

#22.Count Unique Elements: Given a list, determine the count of unique elements using a set.

g=[1,2,3,3,4,5,5]
unique_list=list(set(g))
number_of_unique_elments=len(unique_list)
print("Number of unique elments:", number_of_unique_elments)

#23.Generate Random Set: Create a set with a specified number of random integers within a certain range.

a={1,2,3,4,5}
q=set(range(2,5))
print("Range set:", q)


