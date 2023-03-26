
import datetime

# Read default values from file
with open('OSICDef.dat', 'r') as f:
    policy_number, basic_premium, discount, extra_liability_cost, glass_coverage_cost, loaner_car_cost, hst_rate, processing_fee = f.readline().split()
    policy_number = int(policy_number)
    basic_premium = float(basic_premium)
    discount = float(discount)
    extra_liability_cost = float(extra_liability_cost)
    glass_coverage_cost = float(glass_coverage_cost)
    loaner_car_cost = float(loaner_car_cost)
    hst_rate = float(hst_rate)
    processing_fee = float(processing_fee)

# list of provinces
provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']

# Initialize policies list
policies = []

# Start input loop
while True:
    # Input customer information
    first_name = input("Enter customer's first name: ").title()
    last_name = input("Enter customer's last name: ").title()
    address = input("Enter customer's address: ")
    city = input("Enter customer's city: ").title()
    province = input("Enter customer's province (2 letter abbreviation): ").upper()
    while province not in provinces:
        print("Invalid province")
        province = input("Enter customer's province (2 letter abbreviation): ").upper()
    postal_code = input("Enter customer's postal code: ")
    phone_number = input("Enter customer's phone number: ")
    num_cars = int(input("Enter number of cars to be insured: "))
    extra_liability = input("Extra liability coverage (Y/N)? ").upper() == 'Y'
    glass_coverage = input("Glass coverage (Y/N)? ").upper() == 'Y'
    loaner_car = input("Loaner car coverage (Y/N)? ").upper() == 'Y'
    payment_method = input("Payment method (F for full or M for monthly): ").upper()

    # Calculate costs
    total_extra_costs = 0
    if extra_liability == "Y":
        total_extra_costs += num_cars * extra_liability_cost
    if glass_coverage == "Y":
        total_extra_costs += num_cars * glass_coverage_cost
    if loaner_car == "Y":
        total_extra_costs += num_cars * loaner_car_cost
    insurance_premium = basic_premium + ((num_cars - 1) * (basic_premium * discount))
    total_premium = insurance_premium + total_extra_costs
    total_hst = total_premium * hst_rate
    total_cost = total_premium + total_hst
    if payment_method == 'M':
        monthly_payment = (total_cost + processing_fee) / 8
        invoice_date = datetime.date.today()
        next_payment_date = invoice_date.replace(day=1)
        if invoice_date.month == 12:
            next_payment_date = next_payment_date.replace(year=invoice_date.year + 1, month=1)
        else:
            next_payment_date = next_payment_date.replace(month=invoice_date.month + 1)
    else:
        invoice_date = datetime.date.today()
        next_payment_date = None

    # Formated values
    basic_premium_f = "${:.2f}".format(basic_premium)
    total_extra_costs_f = "${:.2f}".format(total_extra_costs)
    total_premium_f = "${:.2f}".format(total_premium)
    total_hst_f = "${:.2f}".format(total_hst)
    total_cost_f = "${:.2f}".format(total_cost)
    if payment_method == 'M':
        monthly_payment_f = "${:.2f}".format(monthly_payment)

    # Display receipt

    print()
    print("-" * 70)
    print("One Stop Insurance Company", " " * 17, "Invoice Date: ", f"{invoice_date}")
    print("Policy information", " " * 25, "Policy number: ", f"{policy_number:>7}")
    print()
    print("Customer Information: ")
    print(" " * 32, "-" * 37)
    print(" " * 5, f"{first_name}.", f"{last_name:<23}")
    print(" " * 5, f"{address:<26}", f"{city:>24}")
    print(" " * 5, f"{province:<26}", f"{postal_code:>24}")
    print(" " * 5, f"{phone_number:<26}")
    print(" " * 32, "-" * 37)
    print(f"Number of cars: {num_cars}")
    print(f"Extra liability coverage: {'Yes' if extra_liability else 'No'}")
    print(f"Glass coverage: {'Yes' if glass_coverage else 'No'}")
    print(f"Loaner car coverage: {'Yes' if loaner_car else 'No'}")
    print("-" * 70)
    print("Premium Information:")
    print(f"Basic Premium: {basic_premium_f}", " " * 20, f"Total Extra Costs: {total_extra_costs_f:>7}")
    print(f"Total Premium: {total_premium_f}", " " * 33, f"HST: {total_hst_f:>5}")
    print(f"Total Cost: {total_cost_f}")
    if payment_method == 'M':
        print(f"Monthly Payment: {monthly_payment_f}")
        print(f"Invoice Date: {invoice_date}")
        print(f"Next Payment Date: {next_payment_date}")
    print()

    with open('Policies.dat', 'a') as f:
        f.write(f"{policy_number}, ")
        f.write(f"{first_name} {last_name}, ")
        f.write(f"{address}, ")
        f.write(f"{city}, ")
        f.write(f"{province}, ")
        f.write(f"{postal_code}, ")
        f.write(f"{phone_number}, ")
        f.write(f"{num_cars}, ")
        f.write(f"{'Y' if extra_liability else 'N'}")
        f.write(f"{'Y' if glass_coverage else 'N'}")
        f.write(f"{'Y' if loaner_car else 'N'}")
        f.write(f"{total_cost}, \n")

    print("Policy information processed and saved.")
    policy_number += 1

    with open('OSICDef.dat', 'w') as f:
        f.write(f"{policy_number} ")
        f.write(f"{basic_premium} ")
        f.write(f"{discount} ")
        f.write(f"{extra_liability_cost} ")
        f.write(f"{glass_coverage_cost} ")
        f.write(f"{loaner_car_cost} ")
        f.write(f"{hst_rate} ")
        f.write(f"{processing_fee} ")

    want_to_continue = input("Do you want to enter next policy? (Y/N)").upper()
    if want_to_continue == "N":
        exit()

