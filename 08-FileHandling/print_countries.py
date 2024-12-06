
###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    content = file.read()
    print(content)
