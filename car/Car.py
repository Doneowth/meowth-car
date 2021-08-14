from Vehicle import Vehicle, print_line
class Car(Vehicle):
    
    def __init__(self, power = False, name = 'duo'):
         #Vehicle.__init__(self, 'ss')
         super(Car, self).__init__()
         self.__power = power
         self.__name = name
    
    def get_name(self):
        return self.__name
    
    def get_power(self):
        return self.__power
    
    def move_forward(self):
        print('forward -----')
    
    def move_backward(self):
        print('backward -----')
    
    def move_left(self):
        print('left -----')
        
    def move_right(self):
        print('right -----')


car = Car(True, 'a')
print(car.get_name()
,car.get_power()
,car.get_year()
,car.get_make()
)

car.move_left()
car.horn()
print_line()