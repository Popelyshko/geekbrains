class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_calculation(self):
        thickness = 0.125
        intake = self.__length * self.__width * thickness
        print(f'Надо {intake} асфальта')

road = Road(20, 5000)
road.mass_calculation()
