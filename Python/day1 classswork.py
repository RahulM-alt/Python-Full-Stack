import random

apple = 15.5
orange = 20
grape = 10.25

total = apple + orange + grape
print("Total volume:", total)

total_int = int(total)
print("Integer total:", total_int)

total_str = str(total)
print("Total volume as string: " + total_str + " liters")

bonus = random.randint(5, 10)
final_total = total + bonus

print("Bonus liters:", bonus)
print("Final total:", final_total)