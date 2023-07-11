import psutil

battery = psutil.sensors_battery()
percentage = battery.percent

print(f"Battery percentage: {percentage}%")
