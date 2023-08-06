name = input("Enter your name: ")
age = input("Enter your age: ")
street = input("Enter your street: ")
city = input("Enter your city: ")
country = input("Enter your country: ")

print("\n")
print(f"\"Name: {name}\"")
print(f"\"Age: {age}\"")
print(f"\"Address: {street}, {city}, {country}\"")

print("\n")
print(f"\"Hello {name}\" Your age is {int(age)-5} Years Old, Your Address is {street}, {city}, {country}.")
print("\n")
print(type(name), type(age), type(street), type(city), type(country))

print("\n")
print(f"\"Hello '{name}', How Are You? \\ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: {country}")

print("\n")
print(f"\"Hello '{name}', How Are You? \\\n\"\"\" Your Age Is \"{age}\"\" + And\n Your City Is: {city}")

print("\n")
name = 'Doaa Reem'
print(f"First Letter Is \"{name[0]}\"")
print(f"Third Letter Is \"{name[2]}\"")
print(f"Last Letter Is \"{name[-1]}\"")

print("\n")
print(name[-3:])
print(name[:4])
print(name[2].upper() + name[3:7])
print(name[-4:][::-1])
print(name[:4:2] + name[4:7])

print("\n")
name = "$&$&Mohammed$&$&"
cleaned_name = name.strip("$&")
print(cleaned_name)

print("\n")
msg = "I %7 Python And Although I %7 GSG with Zakaria"
new_msg = msg.replace("%7", "Love")
print(new_msg)

print("\n")
#The title method capitalizes the first letter of each word in a string.
text = "hello world"
print(text.title())
#The capitalize method capitalizes only the first letter of the entire string.
text = "hello world"
print(text.capitalize())

print("\n")
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"

print(f"{num1:0>5}")
print(f"{num2:0>5}")
print(f"{num3:0>5}")
print(f"{num4:0>5}")
print(f"{num5:0>5}")
print(f"{num6:0>5}")

print("\n")
first_name = "Hadeel"

print("*" * 11 + first_name)
print("*" * 11 + first_name + "*" * 11)
print(first_name + "*" * 11)

print("\n")
name_one = "HaLA"
name_two = "shaHD"

print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
print("\n")
print(name_one.isupper())
print(name_two.islower())
print("\n")
print(name_one.startswith("S"))
print(name_two.endswith("HD"))

print("\n")
msg = "I Love Python And Although I Love GSG with Zakaria"

print("Number of <Love> is:", msg.count("Love"))
print("Number of <t> is:", msg.count("t"))

print("\n")
name = "Zakaria"
print(name.index("r"))

print("\n")
msg = "I %7 Python And Although I %7 GSG with Zakaria"

new_msg = msg.replace("%7", "Love", 1)
print(new_msg)
