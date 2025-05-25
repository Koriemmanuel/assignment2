item = input('what item would you like to buy?: ')
price = float(input('what is the price of the item?: '))
quantity = int(input('how many quantity is the item?: '))
total = price * quantity
print(f'you have bought {quantity} x {item}/s.')
print(f'your total is: {total}')

