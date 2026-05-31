"""
Calculate cost of electricity bill
"""
print("Electricity bill estimator")
price_per_kwh = (float(input("Enter cents per kWh: "))) / 100
daily_use_kwh = float(input("Enter daily use in kWh: "))
number_billing_day = int(input("Enter number of billing days: "))
daily_cost = price_per_kwh * daily_use_kwh
total_bill_cost = daily_cost * number_billing_day
print(f"Estimated bill: {total_bill_cost:0.2f}")

