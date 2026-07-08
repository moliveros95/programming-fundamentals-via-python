# Lesson
# Useful list methods: .append(), .remove(), .sort(), .pop(). Slicing my_list[start:stop] grabs a sub-section without modifying the original list.

# Challenge — write this as a script
# Write a script with a list of 6 CPU usage readings (floats). Sort them, then print the 3 highest readings using slicing (no manual looping).

cpu_usage = [4.3, 10.9, 21.33, 50.1, 70.89, 89.99]
cpu_usage.sort(reverse=True)
print(f"3 highest CPU usage readings: {cpu_usage[0:3]}")