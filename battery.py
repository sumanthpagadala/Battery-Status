import psutil

battery = psutil.sensors_battery()
percentage = battery.percent

if percentage > 95:
    print("The charging is about to be full")
elif percentage == 100:
    print("Charging full, time to unplug")
else:
    print(f"Battery percentage: {percentage}%")
