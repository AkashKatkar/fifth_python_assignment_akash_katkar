# Task 1: Create a Dictionary of Student Marks
print("Task 1: Create a Dictionary of Student Marks")
stud_dict = {"Akash": 98.5, "Sky": 84.7, "Rahul": 79, "Alice": 85}
stud_name = input("Enter the student's name: ")
marks = stud_dict.get(stud_name, None)
if marks is None:
    print("Student not found.")
else:
    print(f"{stud_name}'s marks: {marks}")

# Task 2: Demonstrate List Slicing
print("\nTask 2: Demonstrate List Slicing: ")
num_list = [1,2,3,4,5,6,7,8,9,10]
extracted_first_five_ele = num_list[:5]
reversed_extracted_ele = extracted_first_five_ele[::-1]
print(f"Original list: {num_list}")
print(f"Extracted first five elements: {extracted_first_five_ele}")
print(f"Reversed Extracted elements: {reversed_extracted_ele}")