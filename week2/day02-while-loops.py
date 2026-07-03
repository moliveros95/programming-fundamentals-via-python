# Lesson
# while repeats a block as long as a condition is True. Always make sure something inside the loop can eventually make the condition False, or you'll get an infinite loop.

# Challenge — write this as a script
# Write a script that simulates retrying a failed API call: start with retries=0, and while retries < 5, print 'Retry attempt {n}' and increment retries. After the loop, print 'Max retries reached.'

retries = 0
while retries < 5:
    print(f"Retry attempt {retries}.")
    retries += 1
else:
    print("Max retries reached.")