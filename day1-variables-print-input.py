# Day 1 - variables, print, and input

# Lesson
# Variables are names bound to values — Python figures out the type for you (no need to declare 'int x' like in some languages). 
# Use print() to display output and input() to read a line of text from the user (always returns a string).

# Challenge — write this as a script
# Write a script that asks the user for an AWS region code (e.g. ap-southeast-1) and their instance count, then prints a sentence like: 'Provisioning 3 instance(s) in ap-southeast-1.'

# Get user input for AWS region code.
region_code = input("Enter AWS region code: ")

# Get user instance for AWS.
instance_count = int(input("Enter number of instance: "))

# Print region_code + instance_count by creating variable using f string.
message = f"Provisioning {instance_count} instance(s) in {region_code}."
print(message)