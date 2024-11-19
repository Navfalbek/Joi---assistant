import psutil


def battery_percent() -> bool:
    battery = psutil.sensors_battery()
    if battery.percent == 20:
        return True
    return False


def is_power_plugged() -> bool:
    return psutil.sensors_battery().power_plugged
