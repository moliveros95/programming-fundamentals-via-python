# Lesson
# A set is an unordered collection of unique values — great for deduplication and comparing groups (union, intersection, difference).

# Challenge — write this as a script
# Write a script with two lists of tag names used across two S3 buckets. Convert both to sets and print which tags are shared (intersection) and which are unique to each bucket.

bucket_a_tags = ["prod", "backup", "ap-northeast-1", "logs", "encrypted"]
bucket_b_tags = ["prod", "staging", "ap-northeast-1", "public", "encrypted"]

set_a = set(bucket_a_tags)
set_b = set(bucket_b_tags)

shared = set_a & set_b
only_a = set_a - set_b
only_b = set_b - set_a

print(f"Shared tags: {shared}")
print(f"Only in bucket A: {only_a}")
print(F"Only in bucket B: {only_b}")

