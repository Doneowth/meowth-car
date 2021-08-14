class Vehicle:
    def __init__(self, make = 'mb'):
        self.__make = make
        self.__year = 1995
    
    def get_make(self):
        return self.__make
    
    def get_year(self):
        return self.__year
    
    def horn(self):
        print('b---------')
        
def print_line():
    print('====LINE====')