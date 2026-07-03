# Lesson
# int for whole numbers, float for decimals. Standard operators: + - * / (always returns float) // (floor division) % (modulo) ** (power).

# Challenge — write this as a script
# Write a script that takes a monthly AWS bill (float) and calculates: cost per day (assume 30 days), and whether the bill exceeds a $50 budget threshold — print both results.

monthly_aws_bill = float(input('Enter AWS bill per month: '))
cost_per_day = monthly_aws_bill / 30
exceeds_budget = monthly_aws_bill > 50

print(f"Cost per day: ${cost_per_day:.2f}")
print(f"Exceeds $50 budget: {exceeds_budget}")