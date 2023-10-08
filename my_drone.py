from dronekit import connect, VehicleMode, Vehicle
from lands import Land, CoordinateSystem

NOT_CONATAIN_ANGLE = 0

def get_global_location(connection_string): #"tcp:127.0.0.1:5760"

    # Connect to the Vehicle.
    print("Connecting to vehicle on: %s" % (connection_string,))
    vehicle = connect(connection_string, wait_ready=False)

    global_frame = vehicle.location.global_frame

    # Close vehicle object before exiting script
    vehicle.close()
    print("Completed")

    return global_frame

#todo:고도에 따라 닫아줘야함
def find_subomotor_angle(lat, lon):
    coordinateSystem = CoordinateSystem(lat, lon)

    lands = init_lands()
    for land in lands:
        if (land.contain(coordinateSystem)):
            return land.sub_motor_angle

    return NOT_CONATAIN_ANGLE

print(find_subomotor_angle(1,1))

def init_lands():
    lu = CoordinateSystem(0, 2)
    ru = CoordinateSystem(2, 2)
    ld = CoordinateSystem(0, 0)
    rd = CoordinateSystem(2, 0)
    return [Land(lu, ru, ld, rd, 50)]
    