def p_to_k(weight):
    return float(weight) * 0.45359237

def k_to_p(weight):
    return float(weight) * 2.20462

print("""Welcome to the Weight Converter App ***
        Conversion Options
        (1) Pounds to kilograms
        (2) Kilograms to pounds""")

option = input("What do you want to do? ")
input_temp = input("How many pounds/kilograms? ")

if option == '1':
    converted_weight = p_to_k(input_temp)
    output = f"{input_temp} Pounds is {converted_weight:.2f} kilograms."
elif option == '2':
    converted_weight = k_to_p(input_temp)
    output = f"{input_temp} Kilograms is {converted_weight:.2f} pounds."
else:
    output = "Invalid option. Please choose 1 or 2."

print(output)
