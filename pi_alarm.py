import RPi.GPIO as GPIO
import time
import sys
import datetime
import subprocess

def rotateServo(servo_gpio, angle):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_gpio, GPIO.OUT)
    servo = GPIO.PWM(servo_gpio, 50)
    servo.start(0)
 
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo.stop()
    
    
    
def main():
    
    gp_out        = 4
    on_angle      = 45
    off_angle     = -90
    morning_start = datetime.time(1, 55, 0)
    morning_end   = datetime.time(1, 55, 20)
    evening_start = datetime.time(1, 55, 30)
    evening_end   = datetime.time(1, 55, 40)
    radio         = False

    radin_on_cmd  = "/usr/local/lib/pialerm/radio_on.sh"
    radio_off_cmd = "/usr/local/lib/pialerm/radio_off.sh"
    process = None
    
    while True:
        
        current_time = datetime.datetime.now().time()
        
        if ( morning_start < current_time < morning_end ):
            
            if not radio:
                rotateServo(gp_out, on_angle)
                process = subprocess.Popen(radin_on_cmd, shell=False)
                radio = True
        
        elif ( evening_start < current_time < evening_end ):
        
            if not radio:
                rotateServo(gp_out, on_angle)
                process = subprocess.Popen(radin_on_cmd, shell=False)
                radio = True
                
        else:
            if radio:
                rotateServo(gp_out, off_angle)
                process = subprocess.Popen(radio_off_cmd, shell=False)
                radio = False
      
        # print(radio)
        time.sleep(300)

    GPIO.cleanup()

    
if __name__ == "__main__":
    main()
