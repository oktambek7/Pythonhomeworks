# Append method

jobs=['teacher', 'baker']
jobs.append('YandexDriver')
print(jobs)

# Clear method

a=[5, 'True', 'Nimadir']
a.clear()
print(a)

# Copy method

b=['adaasd', 'daejdie']
b.copy()
print(b)

# Remove method

provinces=['Sirdaryo', 'Qashqadaryo', 'Jizzax']
provinces.remove('Qashqadaryo')
print(provinces)

# Count method

provinces=['Sirdaryo', 'Qashqadaryo', 'Jizzax', 'Qashqadaryo']
y=provinces.count('Qashqadaryo')
print(y)

# Extending lists or joining lists to make one big list in array usage.

names=["O'ktam", "Komil", "Odil"]
surnames=["Zulfqorov", "Baxtiyorov", "Botirov"]
names.extend(surnames)
print(names)

# lists with tuples

cities = ['Tashkent', 'Moscov', 'Washington']

rankings = (1,2,3)

cities.extend(rankings)

print(cities)

# Defining index of an element.

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)

# Inserting/adding a particular element to the list by their index.

brand=['Dior', 'Nike', 'Adidas']

brand.insert(0, "Zara")

print(brand)

# Returning popped element from the list

fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)

print(x)


# Reversing elements

fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)

# Sorting elements in a list by their year in an ascending order.

def myFunc(a):
	return a['year']
    
phones=[
    
	{'phone': 'Iphone', 'year':2006}, 
    {'phone': 'Nokia', 'year':1970}, 
    {'phone': 'Samsung', 'year':2010}   
]

phones.sort(key=myFunc)

print(phones)

# Lenghs of elements.

def something(d):
  return len(d)

cars = ['Chevrolet', 'Lada', 'Porsche', 'BMW']

cars.sort(reverse=True, key=something)

print(something(cars))
