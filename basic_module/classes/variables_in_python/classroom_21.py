"""
Part 1: Variables, constants and code complexity

CONSTANT = "Variables" that will not change
Too many conditions in the same if (bad)
    <- Complexity count (bad)
"""
speed = 61 # current speed of the car
car_location = 100 # location where the car is on the road

RADAR_1 = 60 # maximum speed of radar 1
LOCAL_1 = 100 # location where radar 1 is
RADAR_RANGE = 1 # The distance where the radar picks up

speed_car_pass_radar_1 = speed > RADAR_1
car_passed_radar_1 = car_location >= (LOCAL_1 - RADAR_RANGE) and \
    car_location <= (LOCAL_1 + RADAR_RANGE)
car_fined_radar_1 = car_passed_radar_1 and speed_car_pass_radar_1

if speed_car_pass_radar_1:
    print('Car speed passed radar 1')

if car_passed_radar_1:
    print('Car passed radar 1')

if car_fined_radar_1:
    print('car fined on radar 1')