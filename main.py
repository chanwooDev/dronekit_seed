import lands, my_drone
from drone_sitl import DroneSitl 

def seed_start(connection_string):
    global_location = my_drone.get_global_location(connection_string)
    angle = lands.find_subomotor_angle(global_location.lat ,global_location.lon)

drone_sitl = DroneSitl()
seed_start(drone_sitl.sitl.connection_string())


