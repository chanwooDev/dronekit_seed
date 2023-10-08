
class CoordinateSystem:
    """
    lat 위도
    lon 경도
    """
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def info(self):
        print("latitude: {}, longitude: {}".format(self.lat, self.lon))
              
class Land:
    def __init__(self, left_up, right_up, left_down, right_down, sub_motor_angle):
        self.left_up = left_up
        self.right_up = right_up
        self.left_down = left_down
        self.right_down = right_down
        self.sub_motor_angle = sub_motor_angle      

        # todo: 어떤 좌표가 순서대로 들어올지 몰라서 sort 해야함 
    
    def contain(self, coordinate):  
        """
            직사각형이라고 가정함
        """
        if self.left_up.lat > coordinate.lat or coordinate.lat > self.right_up.lat:
            return False
        
        if self.left_up.lon < coordinate.lon or coordinate.lon < self.left_down.lon:
            return False
        
        return True
    
    def info(self):
        print("land: left up - {}, right up - {}, left down -  {}, right down - {}, sub_motor_angle = {}"
              .format(self.left_up, self.right_up, self.left_down, self.right_down, self.sub_motor_angle))
    