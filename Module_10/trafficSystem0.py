
from statistics import mean, median
from time import sleep
import destinations
import trafficComponents as tc


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        """Initialize all components of the traffic
        system."""
        self.time = 0

    def snapshot(self):
        """Print a snap shot of the current state of the system."""
        print(f'Time step {self.time}')

    def step(self):
        """Take one time step for all components."""
        self.time += 1


def main():
    ts = TrafficSystem()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1)  # Pause for 0.1 s.
    print('\nFinal state:')
    ts.snapshot()
    print()


if __name__ == '__main__':
    main()
