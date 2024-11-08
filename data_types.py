# Variable declarations and operations

num1 = 7
num2 = 3
print(f"Sum of integers {num1} and {num2}: {num1 + num2}")

flt1 = 5.67
flt2 = 4.33
print(f"Sum of floats {flt1} and {flt2}: {flt1 + flt2}")

str1 = "Hello"
str2 = " World"
print(f"Concatenation of strings: {str1 + str2}")

bool1 = True
bool2 = False

and_operation = bool1 and bool2
or_operation = bool1 or bool2

# Store variables in a dictionary by type
variables_dict = {
    "int": [num1, num2],
    "float": [flt1, flt2],
    "str": [str1, str2],
    "bool": [bool1, bool2, and_operation, or_operation]
}

print("\nData stored in the dictionary:")
for data_type, values in variables_dict.items():
    print(f"{data_type}: {values}")
