# Create a dictionary
veggies = {'carrot': 3, 'potato': 5, 'onion': 2}

   # Iterating over keys
for veggie in veggies:
      print(veggie)

   # Iterating over values
for count in veggies.values():
      print(count)

# Iterating over key-value pairs
for veggie, count in veggies.items():
      print(f"The count of {veggie} is {count}")
