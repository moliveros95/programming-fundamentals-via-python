# Lesson
# int(), float(), str(), bool() convert between types. input() always gives you a string, so numeric input needs explicit conversion before doing math on it.

# Challenge — write this as a script
# Write a script that reads a disk usage value as text input (e.g. '73.5'), converts it to a float, and prints a warning message only if usage is over 70%. This ties together input, conversion, and conditionals from this week.

disk_usage   = input('Enter disk usage: ')
f_disk_usage = float(disk_usage)

if f_disk_usage > 70:
    print(f'INFO: Disk usage is at {f_disk_usage}%. You are running out of disk space.')
else:
    print(f'INFO: Disk usage is at {f_disk_usage}.')