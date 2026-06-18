# Insurance Premium Calculator
age = int(input("Enter age: "))
coverage_amount = float(input("Enter coverage amount: "))
# Determine premium rate based on age
if age < 25:
    rate = 0.05
elif age <= 40:
    rate = 0.04
elif age <= 60:
    rate = 0.03
else:
    rate = 0.06
# Calculate premium
premium = coverage_amount * rate
# Display result
print("\nInsurance Premium Details")
print(f"Age: {age}")
print(f"Coverage Amount: ₹{coverage_amount:,.2f}")
print(f"Premium Rate: {rate * 100}%")
print(f"Estimated Premium: ₹{premium:,.2f}")
