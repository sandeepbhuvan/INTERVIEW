colors = input("Enter comma-separated colors: ")
c = colors.split(",")
colors1 = input("Enter comma-separated colors: ")
c1 = colors.split(",")
uncommon_colors = set(c).symmetric_difference(set(c1))
print("Uncommon colors:", uncommon_colors)

# Example dictionary to sort
example_dict = {'red': 3, 'blue': 1, 'green': 2}

# Sorting the dictionary by keys
sorted_by_keys = dict(sorted(example_dict.items(), key=lambda item: item[0]))
print("Dictionary sorted by keys:", sorted_by_keys)

# Sorting the dictionary by values
sorted_by_values = dict(sorted(example_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by values:", sorted_by_values)


