from abc import ABC, abstractmethod

class motor_mechanism(ABC):
    connection_made=False
    def motor_color(self):  # virtual function
        return "Black"
    @abstractmethod
    def make_electric_connection(self): # abstract function
        self.connection_made=True
    def rotate(self):       # virtual function
        if self.connection_made==True: 
            print("Start rotating")
        else:
            print("Please check connection => connection_made: ",self.connection_made)
class fan(motor_mechanism):
    def wind_range(self,ground_height,fan_radius):
        self.ground_length_half=fan_radius
        for i in range(1,ground_height+1):
            self.ground_length_half+=1
        self.edge_length_from_fan_center=self.ground_length_half
        self.area_covered=3.14*self.ground_length_half**2
        return {"edge length from center(m)":self.edge_length_from_fan_center, "area covered(m^2)":self.area_covered}
    def make_electric_connection(self,connection):
        self.connection_made=connection
fan1=fan()
fan_wind_coverage=fan1.wind_range(3,1)
print("fan wind coverage:",fan_wind_coverage)
fan1.make_electric_connection(True)
fan1.rotate()
print("fan's motor color:",fan1.motor_color())

