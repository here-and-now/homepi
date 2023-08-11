from gpiozero import MotionSensor, Device
from signal import pause
import time

pir = MotionSensor(23)

# pir.when_motion = lambda: print("Motion detected!")
# pir.when_no_motion = lambda: print("All is quiet...")

while True:
    if pir.motion_detected:
        print("Motion detected!")
    else:
        print("All is quiet...")
        time.sleep(1)

pause()


