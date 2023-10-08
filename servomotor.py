import RPi.GPIO as GPIO
import time

duty_cycle_by_angle = {
    #듀티비는 서보모터에 따라 다를 수 있음
    0:3.0, 15:4, 30:5, 45:6, 60:7, 75:8, 90:9
}

class Servomotor:

    def __init__(self):
        servo_pin = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin, GPIO.OUT)
        self.pwm =  GPIO.PWM(servo_pin, 50)  # 50Hz (서보모터 PWM 동작을 위한 주파수) - 50hz은 공식적으로 약속된 값임
        self.change_angle(0)
        
    def change_angle(self, angle):
        if duty_cycle_by_angle.get(angle) == None:
            raise Exception("없는 값을 입력했습니다. number: "+ angle)
        
        self.pwm.ChangeDutyCycle(duty_cycle_by_angle[angle])
    
    def __del__(self):
        self.pwm.stop()
        GPIO.cleanup()
        print("연결된 pwm이 clean 됩니다")


servomoter = Servomotor()
servomoter.change_angle(0)
time.sleep(1)
servomoter.change_angle(90)
time.sleep(3)


