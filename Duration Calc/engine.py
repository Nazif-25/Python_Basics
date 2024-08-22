import math


def calc_time_in_min(d, s):
    new_duration = d / s
    rounded_val = round(new_duration, 2)
    return f"New video duration in minutes: {rounded_val} minutes"


def calc_time_min_and_sec(d, s):
    new_duration = d / s
    rounded_val = round(new_duration, 2)
    x = str(rounded_val).split('.')
    minutes = int(x[0])
    seconds = math.ceil((int(x[-1]) / 100) * 60)
    return f"New video duration in minutes and seconds: {minutes} min {seconds} sec"


duration = float(input("Enter the time in minutes: "))
speed = float(input("Enter the speed: "))

print(calc_time_in_min(d=duration, s=speed))
print(calc_time_min_and_sec(d=duration, s=speed))



def calc_min_and_sec_to_min(m, s):
    min = m+round(s/60, 2)
    return f"Duration: {min} min"


time = input("Enter time in m:s format: ").split(':')
minutes = int(time[0])
seconds = int(time[-1])
print(calc_min_and_sec_to_min(m=minutes, s=seconds))
