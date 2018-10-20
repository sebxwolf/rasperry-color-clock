from sense_hat import SenseHat
import time
import calendar
import datetime
offset = datetime.timedelta(hours=2)
no_offset = datetime.timedelta(hours=0)
utc = datetime.timezone(no_offset)
spanish_timezone = datetime.timezone(offset)

sense = SenseHat()
sense.set_rotation(270)

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
y = (255, 255, 0)
p = (255, 0, 255)
c = (0, 255, 255)
w = (255, 255, 255)
e = (0, 0, 0)

icon = [
    w, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
]

color = [w,y,g,b,p,r,c,e]
while True:
    for x in range(len(color)):
        for i in range(len(icon)):
            icon[i] = color[x]
            sense.set_pixels(icon)
            time.sleep(58/64)
            sense.clear()
        now = datetime.datetime.now(tz=utc)
        now.astimezone(spanish_timezone)
        sense.show_message(now.astimezone(spanish_timezone).strftime('%H:%M'))


'''
while True:
    #sense.load_image("img/jordan.png")
    sense.set_pixels(icon)
    time.sleep(10)
    sense.show_message("!")
    time.sleep(1)
    sense.clear()
'''
