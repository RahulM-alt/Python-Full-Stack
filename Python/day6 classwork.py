attendance = [18, 20, 19, 15, 21]

full_day = 0
total_attendance = 0

for day in attendance:
    if day >= 20:
        print(day, "- full")
        full_day += 1
    else:
        print(day, "- not full")
        total_attendance += day

print("Number of full days:", full_day)
print("Total attendance on non-full days:", total_attendance)