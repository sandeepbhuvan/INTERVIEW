dict={'b': "Name", 'a' : "My" , 'c' : "is", 'd' : "Sandeep", 'e': "B"}
print("Hello")
print(sorted(dict.items()))
print(sorted(dict.items(),key=lambda x:x[1]))
print(sorted(dict.items(),reverse=True))