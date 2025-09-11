
aqi_values = [50, 65, 55, 80, 70, 65, 90, 100]


average_aqi = sum(aqi_values) / len(aqi_values)


unique_aqi = set(aqi_values)


aqi_count = {}
for aqi in aqi_values:
    aqi_count[aqi] = aqi_count.get(aqi, 0) + 1


print("AQI Data:", aqi_values)
print("Average AQI:", average_aqi)
print("Unique AQI Levels:", unique_aqi)
print("Count of Each AQI:", aqi_count)