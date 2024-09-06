# Type code for classes here...
def main():
    class ItemToPurchase:

        def __init__(self):
            self.item_name = ''
            self.item_price = 0
            self.item_quantity = 0
            self.item_description = ''

        def cust_info(self):
            self.customer_name = ''
            self.current_date = 'January 1, 2016'
            self.cart_items = []

        def print_item_description(self):
            print ('{}"s Shopping Cart - {}'.format(customer_name, current_date))

        def print_total(self):
            print('{}"s Shopping Cart - {}'.format(customer_name, current_date))
            print('Number of items: {}'.format(len(self.cart_items)))

    #def print_item_cost(self):
       #print(self.item_name, end = ' ')
        #print(self.item_quantity, '@ $', self.item_price, '= $', (self.item_quantity * self.item_price))

#if __name__ == "__main__":

# Type main section of code here
# Item 1
   #print('Item 1')
    #item1_name = input('Enter the item name:\n')
    #item1_price = int(input('Enter the item price:\n'))
    #item1_quantity = int(input('Enter the item quantity:\n\n'))

#Item 2
    #print('Item 2')
    #item2_name = input('Enter the item name:\n')
    #item2_price = int(input('Enter the item price:\n'))
    #item2_quantity = int(input('Enter the item quantity:\n\n'))

#Combined Total
    #combined_total = (item1_price * item1_quantity) + (item2_price * item2_quantity)

#Outputs
    #print ('TOTAL COST')
    #print ('{} {} @ ${} = ${}'.format(item1_name, item1_quantity, item1_price, item1_price * item1_quantity))
    #print ('{} {} @ ${} = ${}\n'.format(item2_name,item2_quantity , item2_price, item2_price * item2_quantity))
    #print ('Total: ${}'.format(combined_total))
