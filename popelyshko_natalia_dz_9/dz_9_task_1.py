from enum import Enum
from time import sleep


class Color(Enum):
    RED = "Красный"
    YELLOW = "Желтый"
    GREEN = "Зеленый"


class TrafficLight:
    _color: str = Color.RED
    _rules_colors: dict = {
        Color.RED: 7,
        Color.GREEN: 2,
        Color.YELLOW: 10
    }

    def running(self):
        for color, timer in self._rules_colors.items():
            print(f"Включился {color.value}")
            sleep(timer)


trafficLight = TrafficLight()
trafficLight.running()


