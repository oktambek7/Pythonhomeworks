#1.Count Occurrences: Given a tuple and an element, find how many times the element appears in the tuple.

t=('apple','orange', 'potato', 'apple')
count=t.count('apple')
print(count)

#2.Max Element: From a given tuple, determine the largest element.

a=(12,3324,13,45,11,45234)
max_value=max(a)
print(max_value)

#3.Min Element: From a given tuple, determine the smallest element.

a=(12,3324,13,45,11,45234)
min_value=min(a)
print(min_value)

#4.Check Element: Given a tuple and an element, check if the element is present in the tuple.

a=int(input("Enter number: "))
tuple=(12,32,14,42,453)
if a in tuple:
    print(f"{a} is present in the tuple.")
else:
    print(f"{a} is NOT present in the tuple.")

#5.First Element: Access the first element of a tuple, considering what to return if the tuple is empty.

tuple=(1,2,3,4,5,'house','True')
first_element=tuple[0]
print(first_element)

#6.Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.

tuple=(1,2,3,4,5,'house','True')
last_element=tuple[6]
print(last_element)

#7.Tuple Length: Determine the number of elements in the tuple.

tuple=(2132,1344,1425,7476)
num_of_elements=len(tuple)
print(num_of_elements)

#8.Slice Tuple: Create a new tuple that contains only the first three elements of the original tuple.

or_tuple=(1,2,3,4,5,6)
new_tuple=or_tuple[:3]
print(new_tuple)

#9.Concatenate Tuples: Given two tuples, create a new tuple that combines both.

t1=(1,2,3)
t2=(4,5,6)
new_t=(t1)+(t2)
print(new_t)

#10.Check if Tuple is Empty: Determine if a tuple has any elements.

tuple=(1,2,3,4)
if tuple=={}:
    print("Tuple is empty!")
else:
    print("Tuple is NOT empty!")

#11.Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.

fruits=('apple','orange','banana')
for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")

#12.Find Second Largest: From a given tuple, find the second largest element.

given_tuple=(1,2,3,4,5,6)
second_largest_t=given_tuple[-2]
print(second_largest_t)

#13.Find Second Smallest: From a given tuple, find the second smallest element.

given_tuple=(1,2,3,4,5,6)
second_smallest_t=given_tuple[1]
print(second_smallest_t)

#14.Create a Single Element Tuple: Create a tuple that contains a single specified element.

single_el_t=('wassup')
print(single_el_t)

#15.Convert List to Tuple: Given a list, create a tuple containing the same elements.

list=['mike','john','sam']
list_to_tuple=tuple(list)
print(list_to_tuple)

#16.Check if Tuple is Sorted: Determine if the tuple is sorted in ascending order and return a boolean.

t=(12,22,546,75,34)
if t is sorted:
    print("True")
else:
    print("False")

#17.Find Maximum of Subtuple: Given a tuple, find the maximum element of a specified subtuple.

a=(123,745,856,456,637)
subtuple=a[1:5]
max_subtuple=max(a)
print(max_subtuple)

#18.Find Minimum of Subtuple: Given a tuple, find the minimum element of a specified subtuple.

a=(123,745,856,456,637)
subtuple=a[1:5]
min_subtuple=min(a)
print(min_subtuple)

#19.Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.

given_tuple=(1,2,3,4,5,6,7)
el_to_rem=1
temp_list=list(given_tuple)
temp_list.remove(el_to_rem)
new_tuple=tuple(temp_list)
print(new_tuple)

#20.Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple

original_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
nested_tuple = ((original_tuple[0], original_tuple[1]), 
                (original_tuple[2], original_tuple[3]), 
                (original_tuple[4], original_tuple[5]), 
                (original_tuple[6], original_tuple[7]))

print(nested_tuple)




