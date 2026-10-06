import random
rice_quantity = 3
sugar_quantity = 2.5
oil_quantity = 1.8

rice_price = 45
sugar_price = 40
oil_price = 130

rice_total = rice_price * rice_quantity
sugar_total = sugar_price * sugar_quantity
oil_total = oil_price * oil_quantity
total_bill = rice_total + sugar_total + oil_total
total_bill_int = int(total_bill)
total_bill_str = str(total_bill)
delivery_charge = random.randint(5, 10)
final_bill = total_bill_int + delivery_charge

print(rice_total)
print("total oil price:", oil_total)
print("sugar total price:", sugar_total)
print("total bill in int:", total_bill_int)
print("total bill in string:", total_bill_str)
print("deliver charge:", delivery_charge)
print ("final bill:", final_bill)