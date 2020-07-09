day_temperatures = {"morning": 50.0, "noon": 55.0, "evening": 60.0}

# tuples are lists with parenthesis
# tuples are immutable
# lists are mutable

color_codes = ((2,4,5),(0,1,3),(7,6,8))

day_temperatures = {"morning": (50.0,51.0,52.0), "noon": (55.0,56.0,57.0), "evening": (60.0,61.0,62.0)}

monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures.append(8.1)

seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)
print(seconds)

seconds.remove(1.4534345567)
print(seconds)

print(seconds.__getitem__(1))
print(seconds[1])

workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print(workdays)
print(len(workdays))
