import nxt.locator
import nxt.motor

import time

ROTATIONS_PER_TURN = 1880
ROTATIONS_PER_DEGREE = ROTATIONS_PER_TURN/360

brick = nxt.locator.find()
right = brick.get_motor(nxt.motor.Port.B)
left = brick.get_motor(nxt.motor.Port.A)

jingle = [
    (523, 200),   # C5
    (659, 200),   # E5
    (784, 200),   # G5
    (1047, 400),  # C6
    (784, 200),   # G5
    (1047, 200),  # C6
    (1319, 600),  # E6
]

def play_jingle():
    for note in jingle:
        brick.play_tone_and_wait(*note)

def forward(degrees, speed=100):
    move(degrees, speed)

def backward(degrees, speed=100):
    move(degrees, -speed)

def left_turn(degrees, speed=80):

    deg = int(degrees * ROTATIONS_PER_DEGREE)
    turn(right, deg, speed)

def right_turn(degrees, speed=80):

    deg = int(degrees * ROTATIONS_PER_DEGREE)
    turn(left, deg, speed)

def turn(motor, rots, speed):

    motor.reset_position(False)

    while abs(motor.get_tacho().rotation_count) < rots:
        motor.run(speed)

    left.idle()
    right.idle()


def move(rots, speed):

    left.reset_position(False)
    right.reset_position(False)

    while abs(left.get_tacho().rotation_count) < rots:
        left.run(speed)
        right.run(speed)

    right.idle()
    left.idle()

    #print(type(left.get_tacho().rotation_count), left.get_tacho().rotation_count)



if __name__ == "__main__":

    forward(100, 80)
    backward(100, 80)
    left_turn(100, 70)
    right_turn(100, 70)
    play_jingle()
