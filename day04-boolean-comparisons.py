# Lesson
# bool is True or False. Comparison operators (== != > < >= <=) produce booleans. These are the building blocks for every decision your scripts will make.

# Challenge — write this as a script
# Write a script that stores a server's CPU usage percentage in a variable, then prints True/False for: is_healthy (below 80%), needs_scaling (above 90%).

cpu_usage     = float(input('Enter server CPU usage: '))
is_healthy    = float(80)
needs_scaling = float(90)

if cpu_usage <= is_healthy:
    print('True: CPU usage is healthy.')
elif cpu_usage >= needs_scaling:
    print('False: CPU usage needs scaling.')
else:
    print('True: CPU usage is healthy.')