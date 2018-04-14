import random


class Plane:
    def __init__(self, limit_rate_abs):
        start_value_limiter = 0.1
        self.angle = random.gauss(0, 1) * limit_rate_abs * start_value_limiter
        self.limit_rate_abs = limit_rate_abs

    def set_angle(self, new_angle):
        if abs(new_angle) <= self.limit_rate_abs:
            self.angle = new_angle;

    def __str__(self):
        return "Plane's angle:{}, out of max abs angle: {}".format(self.angle, self.limit_rate_abs)


class Env:
    def __init__(self, limit_rate_abs=15):
        self.plane = Plane(limit_rate_abs)

    def get_flight_info(self):
        return self.__get_info().__next__()

    def __get_info(self):
        while True:
            yield str(self.plane)
