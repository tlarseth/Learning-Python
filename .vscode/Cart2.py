class Item:
    def __init__(self):
        self.item_name = str('')
        self.item_price = float(0)
        self.item_quantity = int(0)

    def print_item_cost(self):
        print(self.item_name, end=' ')
        print(self.item_quantity, '@ $', self.item_price, '= $', (self.item_quantity * self.item_price))


if __name__ == "__main__":
    print('Item 1')
    name = input('Enter the item name:\n')
    price = float(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    item1 = Item()  # Calls Class
    item1.item_name = name
    item1.item_price = price
    item1.item_quantity = quantity

    print('Item 2')
    name = input('Enter the item name:\n')
    price = float(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    item2 = Item()
    item2.item_name = name
    item2.item_price = price
    item2.item_quantity = quantity


total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

print('TOTAL COST')
print(item1.print_item_cost(), '\n')
print(item2.print_item_cost(), '\n')
print('Total:', f'{total_cost:.2f}')