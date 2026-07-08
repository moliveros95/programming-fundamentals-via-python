# Lesson
# A tuple is like a list but immutable (can't be changed after creation) — good for fixed data like coordinates or a (region, zone) pair.

# Challenge — write this as a script
# Write a script that stores 3 (region, availability_zone) tuples in a list, then loops through and prints each pair using unpacking, e.g. 'for region, az in zones:'.

zones = [
    ("ap-northeast-1","ap-northeast-1a"),
    ("ap-northeast-3","ap-northeast-3a"),
    ("ap-southeast-1","ap-southeast-1a")
]

for region, az in zones:
    print(f"{region}, {az}")