import lands, mydrone

global_location =mydrone.get_global_location
angle = lands.find_subomotor_angle(global_location.lat ,global_location.lon)

#아두이노로 전송
