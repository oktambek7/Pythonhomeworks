#1.Get Value: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.

my_dict={"name":"Oktam","age":"18"}
print(my_dict.get("name"))

#2.Check Key: Given a dictionary and a key, check if the key is present in the dictionary.
my_dict={"height":175,"width":120}
if "height" and "width" in my_dict:
    print("Key exists")
else:
    print("Key doesnt exists")



#3.Count Keys: Determine the number of keys in the dictionary.
my_dict={"height":175,"width":120}
num_of_keys=len(my_dict)
print(num_of_keys)


#4.Get All Keys: Create a list that contains all the keys in the dictionary.
my_dict={"name":"Oktam","age":"18"}
keys_list=list(my_dict.keys())
print(keys_list)

#5.Get All Values: Create a list that contains all the values in the dictionary.
my_dict={"name":"Oktam","age":"18"}
values_list=list(my_dict.values())
print(values_list)


#6.Merge Dictionaries: Given two dictionaries, create a new dictionary that combines both.
my_dict1={"name":"Oktam","age":"18"}
my_dict2={"height":175,"width":120}
combined_version=my_dict1|my_dict2
print(combined_version)

#7.Remove Key: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
my_dict1={"name":"Oktam","age":"18"}
del my_dict1["age"]
print(my_dict1)


#8.Clear Dictionary: Create a new empty dictionary.
my_dict1={"name":"Oktam","age":"18"}
b={}
print(b)

#9.Check if Dictionary is Empty: Determine if a dictionary has any elements.
my_dict1={"name":"Oktam","age":"18"}
if my_dict1=={}:
    print("Dictionary is empty.")
else:
    print("Dictionary is NOT empty.")


#10.Get Key-Value Pair: Given a dictionary and a key, retrieve the key-value pair if the key exists.
my_dict1={"name":"Oktam","age":"18"}
if "name" in my_dict1:
    print("Key exists.")
else:
    print("Key does not exist.")
print(my_dict1["name"])



#11.Update Value: Given a dictionary, update the value for a specified key.
my_dict1={"name":"Oktam","age":"18"}
my_dict1["name"]="Mirziyod"
print(my_dict1)

#12.Count Value Occurrences: Given a dictionary, count how many times a specific value appears across the keys.
my_dict1={"name":"John","age":18}
value_to_count=18
count_val=list(my_dict1.values()).count(value_to_count)
print(count_val)
