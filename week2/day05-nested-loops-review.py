# Lesson
# Loops can contain other loops (e.g. looping over regions, and for each region, looping over instance types). Keep nested blocks shallow and readable.

# Challenge — write this as a script
# Write a script with a list of 2 regions and a list of 3 instance types. Use nested for loops to print every region/instance-type combination, e.g. 'ap-southeast-1 — t2.micro'.

aws_regions     = ["ap-northeast-1","ap-northeast-3"]
ec2_instances   = ["t3.micro","t3.medium","m5.large"]

for x in aws_regions:
    for y in ec2_instances:
        print(f"{x} - {y}")