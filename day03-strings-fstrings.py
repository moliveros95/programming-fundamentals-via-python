# Lesson
# Strings are sequences of characters. f-strings (f"text {variable}") let you embed variables directly into text — the standard way to build readable output in modern Python.

# Challenge — write this as a script
# Write a script with variables for an EC2 instance_id, instance_type, and region. Use an f-string to print a one-line summary, e.g. 'i-0abc123 (t2.micro) is running in ap-southeast-1'.

ec2_instance_id   = "ami-xyz081624"
ec2_instance_type = "t2.micro"
ec2_region        = "ap-northeast-1"
region            = "Tokyo"

# If user input is preferred, uncomment the following lines and comment out the above variables.
# input_ec2_instance_id   = input("Enter EC2 instance ID: ")
# input_ec2_instance_type = input("Enter EC2 instance type: ")
# input_ec2_region        = input("Enter EC2 region: ")
# input_region            = input("Enter region name: ")

print(f"{ec2_instance_id} ({ec2_instance_type}) is running in {ec2_region} ({region}).")