speed_of_light = 300000. # km per second

def speed_fraction(time, distance):
    time = (0.0 + time) / 2
    distance = (0.0 + distance)
    return (distance / time) / (speed_of_light / 1000)
