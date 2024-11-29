name = 'John'
s = f'Hello, {name}!'
print(s)
first_name = 'John'
last_name = 'Doe'
s = F'Hello, {first_name} {last_name}!'
print(s)
first_name = 'John'
last_name = 'Doe'
s = F'Hello, {" ".join((first_name, last_name))}!'

print(s)

name = 'John'
website = 'PythonTutorial.net'

message = (
    f'Hello {name}. '
    f"You're learning Python at {website}." 
)

print(message)