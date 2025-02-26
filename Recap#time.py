import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))

if 5 <= hour < 12:
    print("Good morning")
elif 12 <= hour < 18:
    print("Good Afternoon")
else:
    print("Good Evening")