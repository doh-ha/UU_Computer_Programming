
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
        self.first_lane = tc.Lane(10)  # Create the first file
        self.second_lane = tc.Lane(10)  # Create the second file
        self.light = tc.Light(7, 3)  # Create the traffic light
        # Create the destination generator
        self.destination_generator = destinations.DestinationGenerator()
        self.queue = []  # Initialize an empty queue for vehicles

    def snapshot(self):
        """Print a snap shot of the current state of the system."""
        first_lane_str = self.first_lane.__str__()
        light_str = self.light.__str__()
        second_lane_str = self.second_lane.__str__()

        # Convert the queue into a list of destination characters
        queue_str = [str(vehicle.destination) for vehicle in self.queue]

        # Display the traffic system snapshot
        print(f'Time step {self.time}')
        print(f"{first_lane_str} {light_str} {second_lane_str}   {queue_str}")

    def step(self):
        """Take one time step for all components."""
        first_lane_vehicle = self.first_lane.remove_first()
        self.first_lane.step()

        if self.light.is_green() and self.second_lane.get_first():
            second_lane_vehicle = self.second_lane.remove_first()
            self.first_lane.enter(second_lane_vehicle)

        self.light.step()
        self.second_lane.step()

        destination = self.destination_generator.step()
        if destination and destination != 'None':
            new_vehicle = tc.Vehicle(destination, self.time)
            self.queue.append(new_vehicle)  # Add new vehicles to the queue

        if self.queue:  # If the queue is not empty
            if self.second_lane.last_free():
                # Get the first vehicle from the queue and put it in the second lane
                self.second_lane.enter(self.queue.pop(0))

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
