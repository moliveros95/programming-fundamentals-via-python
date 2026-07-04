# Lesson
# for loops iterate over a sequence. range(start, stop, step) generates a sequence of numbers without storing them all in memory — very common for counted loops.

# Challenge — write this as a script
# Write a script that loops through numbers 1 to 10 using range() and prints only the even ones, labeled like 'Server-02 is even-numbered'.

for x in range (2, 11, 2):
    print(f"Server-{x:02d} is even-numbered.")