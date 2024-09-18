def enterProducts ():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input('Press A to add product or Q to quit: ')
        if details == 'A':
            product = input('Enter Product: ')
            quantity = int(input('Enter Quantity: '))
            buyingData.update(product: quantity)
        elif details == 'Q':
            enterDetails = False
        else:
            print('Please select a correct option')
            

