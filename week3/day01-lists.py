# Lesson
# A list is an ordered, mutable collection: my_list = [1, 2, 3]. Access items by index (starting at 0), and use append() to add items.

# Challenge — write this as a script
# Write a script that builds a list of 4 server hostnames, appends one more, then prints the total count and the first and last hostname in the list.

server_hostnames = ["test.alpha", "test.beta", "test.charlie", "test.delta"]
server_hostnames.append("test.echo")
print(f"Total count of server hostnames: {len(server_hostnames)}")
print(f"First hostname: {server_hostnames[0]}")
print(f"Last hostname: {server_hostnames[-1]}")


