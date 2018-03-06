# Assignment: Product
#Create a product class to fill the following requirements.
class Product(object):
#Attributes: Price, Item Name, Weight, Brand
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
    #  Status: default "for sale"
        status = "for sale"
        self.status = status

# Methods:
# Every method that doesn't have to return something should return self so methods can be chained.
#  Sell: changes status to "sold"
    def sell(self):
        self.status = "sold"
        return(self)

#  Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    def add_tax(self, tax):
        if type(tax) != float:
            print 'tax must be entered as a decimal amount'
        else:
            amount = self.price * (1 + tax)
            return amount

    #  Return: takes reason for return as a parameter and changes status accordingly.
    def Return(self, state):
    # returned because it is defective, change status to "defective" and change price to 0.
        if state == 'deffective':
            self.status = 'deffective'
            self.price = 0
            return self

    #  If it is being returned in the box, like new, mark it "for sale".     
        elif state == 'unopened':
            self.status = 'for sale'
            return self

    #  If the box has been, opened, set the status to "used" and apply a 20% discount.
        elif state == 'opened':
            self.status = "used"
            self.price = round(self.price * .80, 2)
            return self
        else:
            print "'state' parameter must be either 'deffective', 'unopened', or 'opened'."
            return self

#  Display Info: show all product details.
    def Display_info(self):
        print ('Price: $' + str(self.price) )
        print ('Item Name: ' + self.item_name)
        print ('Weight: ' + str(self.weight)+'lbs.')
        print ('Brand: ' + self.brand)
        print ('Status: ' + self.status)
        print (' ')
        return(self)




# test_item = Product(2.99, 'ink pen', .08, 'Bic')

# test_item.Display_info()

# test_item.Return('opened').Display_info().Return('deffective').Display_info()