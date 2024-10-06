# All List Operations
# 1. Append an element to the list
c.append("new_color")
print("After append:", c)

# 2. Extend the list by appending elements from another list
c.extend(["color1", "color2"])
print("After extend:", c)

# 3. Insert an element at a specific position
c.insert(1, "inserted_color")
print("After insert:", c)

# 4. Remove the first occurrence of a value
c.remove("new_color")
print("After remove:", c)

# 5. Pop an element from the list
popped_color = c.pop()
print("After pop:", c)
print("Popped color:", popped_color)

# 6. Find the index of the first occurrence of a value
index = c.index("color1")
print("Index of 'color1':", index)

# 7. Count the occurrences of a value
count = c.count("color1")
print("Count of 'color1':", count)

# 8. Sort the list
c.sort()
print("After sort:", c)

# 9. Reverse the list
c.reverse()
print("After reverse:", c)

# 10. Copy the list
c_copy = c.copy()
print("Copy of list:", c_copy)

# 11. Clear the list
c.clear()
print("After clear:", c)

# ------------------------------------------------------------------

# All Tuple Operations
# 1. Access elements in a tuple
c = ("red", "green", "blue")

# 1. Access elements in a tuple
print("First element:", c[0])
print("Last element:", c[-1])

# 2. Count the occurrences of a value
count = c.count("red")
print("Count of 'red':", count)

# 3. Find the index of the first occurrence of a value
index = c.index("green")
print("Index of 'green':", index)

# 4. Unpack the tuple into variables
color1, color2, color3 = c
print("Unpacked:", color1, color2, color3)

# 5. Check if an element exists in the tuple
exists = "blue" in c
print("Does 'blue' exist in tuple?", exists)

# 6. Get the length of the tuple
length = len(c)
print("Length of tuple:", length)

# 7. Concatenate two tuples
c2 = ("yellow", "purple")
concatenated = c + c2
print("Concatenated tuple:", concatenated)

# 8. Repeat the tuple
repeated = c * 2
print("Repeated tuple:", repeated)

# 9. Convert a list to a tuple
list_colors = ["pink", "black"]
tuple_colors = tuple(list_colors)
print("Converted tuple:", tuple_colors)

# 10. Iterate through a tuple
for color in c:
    print("Color:", color)

# ------------------------------------------------------------------

# All Set Operations
# 1. Add an element to the set
s = {"red", "green", "blue"}
s.add("yellow")
print("After add:", s)

# 2. Update the set with elements from another set
s.update({"purple", "orange"})
print("After update:", s)

# 3. Remove an element from the set (raises KeyError if not found)
s.remove("red")
print("After remove:", s)

# 4. Discard an element from the set (does not raise an error if not found)
s.discard("blue")
print("After discard:", s)

# 5. Pop an element from the set
popped_element = s.pop()
print("After pop:", s)
print("Popped element:", popped_element)

# 6. Clear the set
s.clear()
print("After clear:", s)

# 7. Check if an element exists in the set
s = {"red", "green", "blue"}
exists = "green" in s
print("Does 'green' exist in set?", exists)

# 8. Get the length of the set
length = len(s)
print("Length of set:", length)

# 9. Perform union of two sets
s2 = {"yellow", "purple"}
union_set = s.union(s2)
print("Union of sets:", union_set)

# 10. Perform intersection of two sets
intersection_set = s.intersection(s2)
print("Intersection of sets:", intersection_set)

# 11. Perform difference of two sets
difference_set = s.difference(s2)
print("Difference of sets:", difference_set)

# 12. Perform symmetric difference of two sets
symmetric_difference_set = s.symmetric_difference(s2)
print("Symmetric difference of sets:", symmetric_difference_set)

# 13. Check if a set is a subset of another set
is_subset = s.issubset({"red", "green", "blue", "yellow"})
print("Is subset:", is_subset)

# 14. Check if a set is a superset of another set
is_superset = s.issuperset({"red", "green"})
print("Is superset:", is_superset)

# 15. Check if two sets are disjoint
are_disjoint = s.isdisjoint({"yellow", "purple"})
print("Are disjoint:", are_disjoint)


# ------------------------------------------------------------------

# All Dictionary Operations
# 1. Add or update an element in the dictionary
d = {"name": "Alice", "age": 25}
d["city"] = "New York"
print("After add/update:", d)

# 2. Remove an element from the dictionary
del d["age"]
print("After delete:", d)

# 3. Get a value for a key
name = d.get("name")
print("Get 'name':", name)

# 4. Get all keys in the dictionary
keys = d.keys()
print("Keys:", keys)

# 5. Get all values in the dictionary
values = d.values()
print("Values:", values)

# 6. Get all key-value pairs in the dictionary
items = d.items()
print("Items:", items)

# 7. Check if a key exists in the dictionary
exists = "city" in d
print("Does 'city' exist in dictionary?", exists)

# 8. Get the length of the dictionary
length = len(d)
print("Length of dictionary:", length)

# 9. Remove an element and return its value
city = d.pop("city")
print("After pop 'city':", d)
print("Popped value:", city)

# 10. Remove and return an arbitrary key-value pair
popped_item = d.popitem()
print("After popitem:", d)
print("Popped item:", popped_item)

# 11. Clear the dictionary
d.clear()
print("After clear:", d)

# 12. Copy the dictionary
d = {"name": "Alice", "age": 25}
d_copy = d.copy()
print("Copy of dictionary:", d_copy)

# 13. Update the dictionary with another dictionary
d.update({"city": "New York", "country": "USA"})
print("After update:", d)

# 14. Create a dictionary from keys with a default value
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "unknown")
print("Default dictionary:", default_dict)

# 15. Iterate through a dictionary
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")