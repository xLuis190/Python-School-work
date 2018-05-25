"""
Suppose there is a class AirConditioner.
The class supports the following behaviors: turning the air conditioner on, off, and setting the desired temperature.
The following methods are provided for these behaviors: turn_on and turn_off, which accept no arguments and return
no value, and set_temp, which accepts an int argument and returns no value.

There is a reference variable office_a_c of type AirConditioner.
Create a new object of type AirConditioner using the office_a_c reference variable.
After that, turn the air conditioner on using the reference to the new object, and set the desired temperature to 69 degrees.

class WeatherForecast:
    def set_skies(self,skies):
        self.skies = skies
    def set_high(self,integer):
        self.high  = integer;
    def set_low(self,low):
        self.low = low;
    def get_skies(self):
        return self.skies;
    def get_high(self):
        return self.high
    def get_low(self):
        return self.low
"""
class Player(object):
    name = ""
    score = 0
    def set_name(self,name):
        self.name = name
    def set_score(self,score):
        self.score = score
    def get_name(self):
        return self.name
    def get_score(self):
        return self.score
        
