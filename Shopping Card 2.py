class ItemToPurchase:

    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = 'none'
    def print_item_cost(self):
        return '{} {} @ ${} = ${}'.format(self.item_name,self.item_quantity, self.item_price, (self.item_quantity * self.item_price))
if __name__ == "__main__":
    item1 = ItemToPurchase()
    print("Enter customer's name:")
    name = input("Enter today's date:\n")
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n\n'))
    item1.item_name = name
    item1.item_price = price
    item1.item_quantity = quantity

    item2 = ItemToPurchase()
    print('Item 2')
    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n\n'))
    item2.item_name = name
    item2.item_price = price
    item2.item_quantity = quantity

    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print('TOTAL COST')
    print(item1.print_item_cost())
    print(item2.print_item_cost())
    print()
    print ('Total: ${}'.format(total_cost))
