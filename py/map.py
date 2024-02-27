# Define a function to square a number
def square(x):
    return x ** 2

# Use map to square each element in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(squared_numbers)
# Convert the result to a list (as map returns an iterator)
result_list = list(squared_numbers)
print(result_list)
# Get a space-separated list of numbers from the user
input_numbers = input("Enter numbers separated by space: ")
# Use map to convert the input string to a list of integers
numbers_list = list(map(int, input_numbers.split()))
# Print the resulting list
print("List of numbers:", numbers_list)
