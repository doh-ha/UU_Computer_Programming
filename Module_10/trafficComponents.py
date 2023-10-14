import destinations

# Traffic system components


class Vehicle:
    """Represents vehicles in traffic simulations"""

    def __init__(self, destination, borntime):
        """Creates the vehicle with specified properties."""
        self.destination = destination
        self.borntime = borntime

    def __str__(self):
        return f"Vehicle({self.destination}, {self.borntime})"


class Lane:
    """Represents a lane with (possibly) vehicles"""

    def __init__(self, length):
        """Creates a lane of specified length."""
        self.length = length
        self.vehicles = [None] * length

    def __str__(self):
        lane_str = ''.join(
            ['.' if vehicle is None else vehicle.destination for vehicle in self.vehicles])
        return f"[{lane_str}]"

    def get_first(self):
        """Return the vehicle in the first position without removing it."""
        return self.vehicles[0]

    def remove_first(self):
        """Remove the vehicle in the first position and return it."""
        vehicle = self.vehicles[0]
        self.vehicles[0] = None
        return vehicle

    def step(self):
        """Move all vehicles except the first one one step forward."""
        for i in range(1, self.length):
            if self.vehicles[i] is not None and self.vehicles[i - 1] is None:
                self.vehicles[i - 1] = self.vehicles[i]
                self.vehicles[i] = None

    def last_free(self):
        """Return True if the last space is free, otherwise False."""
        return self.vehicles[-1] is None

    def enter(self, vehicle):
        """Store the vehicle last in the file."""
        if self.last_free():
            for i in range(self.length - 1, -1, -1):
                if self.vehicles[i] is None:
                    self.vehicles[i] = vehicle
                    break

    def number_in_lane(self):
        """Return the number of vehicles in the file."""
        return sum(1 for vehicle in self.vehicles if vehicle is not None)


def demo_lane():
    """Demonstration of the class Lane"""
    a_lane = Lane(10)
    print(a_lane)
    v = Vehicle('N', 34)
    a_lane.enter(v)
    print(a_lane)

    a_lane.step()
    print(a_lane)
    for i in range(20):
        if i % 2 == 0:
            u = Vehicle('S', i)
            a_lane.enter(u)
        a_lane.step()
        print(a_lane)
        if i % 3 == 0:
            print('  out: ',
                  a_lane.remove_first())
    print('Number in lane:',
          a_lane.number_in_lane())


class Light:
    """Represents a traffic light"""

    def __init__(self, period, green_period):
        """Create a light with the specified timers."""
        # Implement this method.
        self.period = period
        self.green_period = green_period
        self.timer = 0

    def __str__(self):
        """Report current state of the light."""
        if self.is_green():
            return "(G)"
        else:
            return "(R)"

    def step(self):
        """Take one light time step."""
        # Implement this method.
        self.timer = (self.timer + 1) % self.period

    def is_green(self):
        """Return whether the light is currently green."""
        # Implement this method.
        return self.timer < self.green_period


def demo_light():
    """Demonstrats the Light class"""
    a_light = Light(7, 3)
    for i in range(15):
        print(i, a_light,
              a_light.is_green())
        a_light.step()


def main():
    """Demonstrates the classes"""
    # print('\nLight demonstration\n')
    # demo_light()
    print('\nLane demonstration')
    demo_lane()


if __name__ == '__main__':
    main()
