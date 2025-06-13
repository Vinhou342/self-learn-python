import time

duration = input("Enter timer duration: \n")
duration = int(duration)

for x in range(duration, 0, -1):
    time.sleep(1)

    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    print(f"Timer {hours:02}:{minutes:02}:{seconds:02}")
print("TIME'S UP!")