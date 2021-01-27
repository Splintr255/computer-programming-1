# variables
from decimal import Decimal

taxRate = 0.08
numItems = int(input('Number of items '))
costPerItem = float(input('Cost Per item '))

# calculator
subTotal = numItems * costPerItem
taxAmmount = taxRate * subTotal
totalPrice = subTotal + taxAmmount

# reciept information
print('SALES RECIEPT')
print('\n')
print('Number of items:      ' + str(numItems))
print('Cost per item:       $' + str(costPerItem))
print('Tax Rate:            $' + str(taxRate))
print('Tax Ammount:         $' + str(round(Decimal(taxAmmount), 2)))
print('-------------------------------------')
print('TOTAL SALE PRICE     $' + str(round(Decimal(totalPrice), 2)))

