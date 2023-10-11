
import json
from modules.lands import Land, CoordinateSystem

LANDS_FILE = "land_data/data.json"

def load_lands():
    try:
        with open(LANDS_FILE, "r") as json_file:
            if is_empty_file(json_file):
                return []
            
            data = json.load(json_file)
            lands = []
            coordinate_systems = []
            for land_data in data:
                coordinate_systems.append(CoordinateSystem(land_data["left_up"]["lat"], land_data["left_up"]["lon"]))
                coordinate_systems.append(CoordinateSystem(land_data["left_down"]["lat"], land_data["left_down"]["lon"]))
                coordinate_systems.append(CoordinateSystem(land_data["right_up"]["lat"], land_data["right_up"]["lon"]))
                coordinate_systems.append(CoordinateSystem(land_data["right_down"]["lat"], land_data["right_down"]["lon"]))
                servo_motor_angle = land_data["servo_motor_angle"]
                land = Land(coordinate_systems, servo_motor_angle)
                lands.append(land)
            return lands
    except FileNotFoundError:
        return []

def is_empty_file(json_file):
    try:
        data = json.load(json_file)
        return False
    
    except json.decoder.JSONDecodeError as e:
        return True

def save_lands(lands):
    with open(LANDS_FILE, "w") as json_file:
        json.dump(lands_to_dict_list(lands), json_file)

def lands_to_dict_list(lands):
    lands_dict_list = []
    for land in lands:
        lands_dict_list.append(land_to_dict(land))

    return lands_dict_list

def land_to_dict(land):
    land_dict = {
        "left_up": coordinate_system_to_dict(land.left_up),
        "right_up": coordinate_system_to_dict(land.right_up),
        "left_down": coordinate_system_to_dict(land.left_down),
        "right_down": coordinate_system_to_dict(land.right_down),
        "servo_motor_angle": land.servo_motor_angle
    }
    
    return land_dict

def coordinate_system_to_dict(object):
    if isinstance(object, CoordinateSystem):
        return {"lat": object.lat, "lon": object.lon}
    raise TypeError("Object of type 'CoordinateSystem' is not JSON serializable")
