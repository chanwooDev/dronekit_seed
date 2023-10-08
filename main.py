from drone_sitl import DroneSitl 
from my_drone import MyDrone

drone_sitl = DroneSitl()
my_drone = MyDrone(drone_sitl.sitl.connection_string())
my_drone.seed_start()
