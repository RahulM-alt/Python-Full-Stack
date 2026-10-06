receipt_header = """\
\tBOOKSTORE RECEIPT
\t-----------------"""

book1 = "\tBook Title: {}\tPrice: ₹{}".format("Python Basics", 450)
book2 = "\tBook Title: {}\tPrice: ₹{}".format("Data Science Intro", 600)

total_price = 450 + 600
total_line = "\tTotal Price:\t₹{}".format(total_price)

thank_you = "\n\tThank you for shopping with us!"

receipt = receipt_header + "\n" + book1 + "\n" + book2 + "\n" + total_line + thank_you

print(receipt.upper())