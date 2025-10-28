from src.utils import math_utils, data_utils

print("starting app")

x = input("Enter your name: ")
print("Hello " + x)

result = math_utils.add(5, 3)
print("Result:", result)

data = data_utils.get_data()
print("Data:", data)
