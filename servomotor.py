import RPi.GPIO as GPIO
import time
angle_map = {
    #각도 10도 단위로 할 것 0~90도 0 10 20 30 40 50 60 70 80 90
    0:3.0, 45:5.5, 90:7.5
}


class Servomotor:

    def __init__(self):
        servo_pin = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin, GPIO.OUT)
        self.pwm =  GPIO.PWM(servo_pin, 50)  # 50Hz (서보모터 PWM 동작을 위한 주파수) - 50hz은 공식적으로 약속된 값임
        self.pwm.start(3.0) #서보의 0도 위치(0.6ms)이동:값 3.0은 pwm주기인 20ms의 3%를 의미하므로,0.6ms됨.

    def change_duty_cycle(number, self):
        if angle_map.get(number) == None:
            print("없는 값을 입력했습니다. in  change_duty_cycle ")
            return
        
        self.pwm.ChangeDutyCycle(angle_map[number])
    
    def __del__(self):
        self.pwm.stop()
        GPIO.cleanup()
        print("연결된 pwm이 clean 됩니다")


servomoter = Servomotor()
servomoter.change_duty_cycle(90)
time.sleep(3)


