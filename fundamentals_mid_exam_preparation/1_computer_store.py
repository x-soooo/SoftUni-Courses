price_without_taxes = 0
tax = 0
total_price = 0
type_of_customer = ('special', 'regular')

while True:
    command = input()
    if command in type_of_customer:
        if price_without_taxes == 0:
            print("Invalid order!")
            break
        else:
            tax = 0.2 * price_without_taxes
            total_price = price_without_taxes + tax
            if command == 'special':
                total_price -= 0.1 * total_price
        print(f"Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {price_without_taxes:.2f}$\n"
              f"Taxes: {tax:.2f}$\n"
              f"-----------\n"
              f"Total price: {total_price:.2f}$")
        break
    part_price = float(command)
    if part_price > 0:
        price_without_taxes += part_price
    else:
        print("Invalid price!")