from gpiozero import MotionSensor, Device
from signal import pause
import time

pir_1 = MotionSensor(23, sample_rate=10, queue_len=40,threshold=0.2)
pir_2 = MotionSensor(24, sample_rate=10, queue_len=40,threshold=0.2)

# pir.when_motion = lambda: print("Motion detected!")
# pir.when_no_motion = lambda: print("All is quiet...")

while True:
    if pir_1.motion_detected:
        print("pir_1 detected!")

    elif pir_2.motion_detected:
        print("pir_2 detected!")
    else:
        print("_________________")
        # time.sleep(1)

pause()


