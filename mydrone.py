from dronekit import connect, VehicleMode, Vehicle

def get_global_location():
    # Import DroneKit-Python
    connection_string = "tcp:127.0.0.1:5760"

    # Connect to the Vehicle.
    print("Connecting to vehicle on: %s" % (connection_string,))
    vehicle = connect(connection_string, wait_ready=False)

    global_frame = vehicle.location.global_frame

    # Close vehicle object before exiting script
    vehicle.close()
    

    print("Completed")

    return global_frame