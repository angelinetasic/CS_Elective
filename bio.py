
blood_pressure = [120, 135, 118, 140, 128, 135, 122, 130]

average_bp = sum(blood_pressure) / len(blood_pressure)

unique_bp = set(blood_pressure)

bp_count = {}
for bp in blood_pressure:
    bp_count[bp] = bp_count.get(bp, 0) + 1


print("Blood Pressure Data:", blood_pressure)
print("Average Blood Pressure:", average_bp)
print("Unique Blood Pressure Values:", unique_bp)
print("Count of Each Value:", bp_count)