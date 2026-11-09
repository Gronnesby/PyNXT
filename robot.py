import time
from lego import *


forward(1000)
right_turn(90)
forward(300)
left_turn(90)

forward(200)

time.sleep(1)

backward(200)
right_turn(90)
backward(300)
left_turn(90)
backward(1000)
