def calculate(price,vat):
    return price + price * vat

print()
print()
print(" WITH THIS PROGRAM YOU CAN CALCULATE THE TOTAL PRICE OF THE PRODUCTS YOU BOUGHT")
print("----------------------------------------------------------------------------------------------------")
print()
print("     1) Enter the title of the product you bought")
print()
print("     2) Enter the price of the product")
print()
print("     3) Enter the VAT (value added tax) of the product")
print()

# Create a dictionary
dictionary = {'product': 'title', 'price': 0, 'vat': '0'}

# Create an empty list for each product's total price
list = []

# Set a flag to terminate the process
flag = "Y"

while flag == "Y" or flag == "y":
    print()
    print("----------------------------------------------------------------------------------------------------")
    print()
    product = input("     Enter the title of the product:  ")
    price = input("     Enter the price of the product:  ")
    vat = input("     Enter the VAT of the product:  ")
    dictionary['product'] = product
    dictionary['price'] = price
    dictionary['vat'] = vat
    x = calculate(float(dictionary['price']), float(dictionary['vat']))
    list.append(x)
    print()
    print()
    total_price = 0
    for values in list:
        total_price += values
    print("     TOTAL PRICE: ", total_price, "€")
    print()
    print("----------------------------------------------------------------------------------------------------")
    print()
    print("     Would you like to add more products? ")
    flag = input("     Press [Y]es to agree, [N]o to quit: ")
