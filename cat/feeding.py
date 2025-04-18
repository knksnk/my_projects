import time

def countdown():
    num_of_hours = 8
    while num_of_hours > 0:
        time.sleep(3600)
        num_of_hours -= 1
    print('time to feed.')


countdown()