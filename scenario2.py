
speeds = [4, 6, 5, 7, 5, 6, 4, 8]

highest_speed = max(speeds)
lowest_speed = min(speeds)

unique_speeds = set(speeds)

speed_count = {}
for s in speeds:
    speed_count[s] = speed_count.get(s, 0) + 1


print("Speeds Data:", speeds)
print("Highest Speed:", highest_speed)
print("Lowest Speed:", lowest_speed)
print("Unique Speeds:", unique_speeds)
print("Count of Each Speed:", speed_count)
