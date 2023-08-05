#Assumptions made:
#The user will enter valid integer numbers between 1 and 100.
#If the user enters a number that is out of the specified range, they will be prompted to enter a valid number.
#The code will only remove exact duplicates, not similar numbers (e.g., 5 and 05 are considered distinct).
#If the user enters more than 4 duplicate numbers, the code will remove all duplicates, leaving only the non-duplicate numbers.
#This code does not include extensive error handling. 

import heapq
from collections import Counter

# Solution 1
# A set is used to efficiently track unique numbers while iterating through the input array. 
# The heapq.nlargest function is then used to extract the largest unique numbers in descending order from the set.

def remove_duplicates_and_sort(arr):
    unique_numbers = set()
    
    for num in arr:
        if num not in unique_numbers:
            unique_numbers.add(num)
    
    sorted_numbers = heapq.nlargest(len(unique_numbers), unique_numbers)
    
    return sorted_numbers


# Solution 2
# Counter class is used to efficiently count the occurrences of each number in the input array. 
# This avoids creating unnecessary intermediate lists during the duplicate removal process. The sorted function is then used to sort the unique

def remove_duplicates_and_sort_1(arr):
    # Count the occurrences of each number
    num_counter = Counter(arr)
    
    # Create a list of unique numbers
    unique_numbers = list(num_counter.keys())
    
    # Sort the unique numbers in descending order
    unique_numbers.sort(reverse=True)
    
    return unique_numbers


# Solution 3
def remove_duplicates_and_sort_2(arr):
    # Remove duplicates and sort in descending order
    unique_numbers = list(set(arr))  # Removes duplicates by converting to a set and back to a list
    unique_numbers.sort(reverse=True)  # Sorts the list in descending order
    return unique_numbers

# Read a list of numbers from the user
numbers = []
for _ in range(10):
    num = int(input("Enter a number between 1 and 100: "))
    if 1 <= num <= 100:
        numbers.append(num)
    else:
        print("Number out of range. Please enter a valid number between 1 and 100.")

# Call the function to remove duplicates and sort
sorted_numbers = remove_duplicates_and_sort(numbers)

# Print the sorted list without duplicates
print("Sorted list without duplicates:", sorted_numbers)