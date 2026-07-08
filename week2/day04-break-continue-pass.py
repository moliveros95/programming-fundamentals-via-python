# Lesson
# break exits a loop entirely. continue skips to the next iteration. pass does nothing (a placeholder for code you'll write later).

# Challenge — write this as a script
# Write a script with a list of server names. Loop through them: skip (continue) any named 'maintenance', and stop the loop entirely (break) if you hit 'db-primary'. Print each server you process.

servers = ["dev","prod","test","maintenance","db-primary"]
for x in servers:
    if x == "maintenance":
        continue
    elif x == "db-primary":
        break
    else:
        print(f"List of servers: {x}")