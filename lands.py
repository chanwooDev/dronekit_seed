
class CoordinateSystem:
    """
    lat 위도
    lon 경도
    """
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return "latitude: {}, longitude: {}".format(self.lat, self.lon)
              
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
    
    def __str__(self):
        return "land: left up - {},\n right up - {},\n left down -  {},\n right down - {},\n sub_motor_angle = {}\n".format(self.left_up, self.right_up, self.left_down, self.right_down, self.sub_motor_angle)

class Lands:
 
    def __init_lands(self) -> list[Land]:
            """
                현재는 파일에서 정보를 가져오도록 함 
                todo:추후 데이터 저장, 로딩이 더 편한 방식으로 변경할 필요가 있음
            """
            lu = CoordinateSystem(0, 2)
            ru = CoordinateSystem(2, 2)
            ld = CoordinateSystem(0, 0)
            rd = CoordinateSystem(2, 0)
            return [Land(lu, ru, ld, rd, 45)]
