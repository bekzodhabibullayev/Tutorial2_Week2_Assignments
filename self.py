# Name , price , quantity for each
# Calculate subtotal and discount eligibility
# Discount rules with boolen arithmetic
# Tax and shipping
# itemized receipt
# Github

item = "Banana"
original_price = 785.575
discount_percent = 20.25
tax_percent = 11.55
discount_amount = original_price * discount_percent / 100
quantity = input("how many bananas would you like to buy")
print(f'\n\n{"=" * 50}')
print('Receipt for: {}'.format(item))
print(f'{"=" * 50}')
print(f'Original Price: { original_price:.2f} som')  
print(f'Discount Percent: ({discount_percent:.2f}%); - {discount_amount}')
print(f'Price after discount:  {price_after_discount:.2f} som')
price_after_discount = original_price - discount_amount
print("Number of Bananas in the cart: {quantity}")

