from gpiozero import Motor, LineSensor
from time import sleep

motor_L = Motor(forward=17, backward=27)
motor_R = Motor(forward=23, backward=22)
left_sensor = LineSensor(18)
right_sensor= LineSensor(21)

def moveForward():
    print ("Moving Forward")
    motor_L.forward(speed=0.25)
    motor_R.forward(speed=0.25)
    
def moveLeft():
    print ("Moving Left")
    motor_L.forward(speed=0)
    motor_R.forward(speed=0.3)

def moveRight():
    print ("Moving Right")
    motor_L.forward(speed=0.3)
    motor_R.forward(speed=0)

def robotStop():
    print ("Robot Stop")
    motor_L.forward(speed=0)
    motor_R.forward(speed=0)
    
while True:
    left_detect  = int(left_sensor.value)
    right_detect = int(right_sensor.value)

    #Stage 1
    if left_detect == 0 and right_detect == 0:
        moveForward()
    #Stage 2
    if left_detect == 0 and right_detect == 1:
        moveRight()
    #Stage 3
    if left_detect == 1 and right_detect == 0:
        moveLeft()
    




    
