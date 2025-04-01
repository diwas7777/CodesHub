import psutil
from plyer import notification

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

notification.notify(title="Battery percentage",message=str(percent)+"% Battery remain!!")

if percent < 30 and plugged!=True:
    notification.notify(title="Battery Low",message=str(percent) + "% Battery remain!!")
