import psutil
from plyer import notification
from time import sleep

MIN_BATTERY_THRESHOLD = 20
FULL_CHARGE = 100

while True:
    battery = psutil.sensors_battery()
    percentage = battery.percent

    if percentage == FULL_CHARGE:
        notification.notify(title="Battery Notification", message="Charging full, Time to remove the plug.", timeout=None)

    elif percentage < MIN_BATTERY_THRESHOLD:
        notification.notify(title="Battery Notification", message="Low battery, consider charging.", timeout=None)

    # Sleep for 6 minute before checking again
    sleep(6*60)
