# System Project  Q2

import simpy

# Define the simulation environment
env = simpy.Environment()

# Define the processing times for each operation
PROCESS_TIMES = {
    'filling': 6.5,
    'capping': 5,
    'labeling': 8,
    'sealing': 5,
    'carton packing': 6
}

# Define the buffer size between workstations
BUFFER_SIZE = 5


# Define the packaging line processes
class PackagingLine:
    def __init__(self, env):
        self.env = env
        self.filling_station = simpy.Store(env, capacity=BUFFER_SIZE)
        self.capping_station = simpy.Store(env, capacity=BUFFER_SIZE)
        self.labeling_station = simpy.Store(env, capacity=BUFFER_SIZE)
        self.sealing_station = simpy.Store(env, capacity=BUFFER_SIZE)
        self.carton_packing_station = simpy.Store(env, capacity=BUFFER_SIZE)
        self.total_units = 0
        self.blocking_count = {
            'filling': 0,
            'capping': 0,
            'labeling': 0,
            'sealing': 0,
            'carton packing': 0
        }
        self.start_time = None
        self.end_time = None

    def filling_process(self):
        while True:
            # Wait for a unit to arrive at the filling station
            unit = self.filling_station.get()
            # Process the unit
            yield self.env.timeout(PROCESS_TIMES['filling'])
            if len(self.filling_station.items) > 5:
                self.blocking_count['filling'] += 1
                print(f"{env.now}:is Filling Blocking Filing")

            # Send the unit to the next station
            yield self.capping_station.put(unit)

    def capping_process(self):
        while True:
            # Wait for a unit to arrive at the capping station
            unit = yield self.capping_station.get()

            # Process the unit
            yield self.env.timeout(PROCESS_TIMES['capping'])
            if len(self.capping_station.items) > 5:
                self.blocking_count['capping'] += 1
                print(f"{env.now}:is Filling Blocking Capping")

            # Send the unit to the next station
            yield self.labeling_station.put(unit)

    def labeling_process(self):
        while True:
            # Wait for a unit to arrive at the labeling station
            unit = yield self.labeling_station.get()

            # Process the unit
            yield self.env.timeout(PROCESS_TIMES['labeling'])
            if len(self.labeling_station.items) > 5:
                self.blocking_count['labeling'] += 1
                print(f"{env.now}:is Filling Blocking Labeling")

            # Send the unit to the next station
            yield self.sealing_station.put(unit)

    def sealing_process(self):
        while True:
            # Wait for a unit to arrive at the sealing station
            unit = yield self.sealing_station.get()

            # Process the unit
            yield self.env.timeout(PROCESS_TIMES['sealing'])
            if len(self.sealing_station.items) > 5:
                self.blocking_count['sealing'] += 1

            # Send the unit to the next station
            yield self.carton_packing_station.put(unit)

    def carton_packing_process(self):
        while True:
            # Wait for a unit to arrive at the carton packing station
            unit = yield self.carton_packing_station.get()

            # Process the unit
            yield self.env.timeout(PROCESS_TIMES['carton packing'])
            if len(self.carton_packing_station.items) > 5:
                self.blocking_count['carton packing'] += 1
            # Increment the total units count
            self.total_units += 1

            if (env.now > 10000):
                break
            # Send the unit to the beginning of the line (filling station)
            yield self.filling_station.put(unit)

    def run(self):
        # Start the filling process
        self.env.process(self.filling_process())
        self.env.process(self.capping_process())
        self.env.process(self.labeling_process())
        self.env.process(self.sealing_process())
        self.env.process(self.carton_packing_process())
        # Start the simulation
        self.start_time = self.env.now
        yield self.env.timeout(100000)
        self.end_time = self.env.now

        # Print the results
        print(f'Throughput: {self.total_units / (self.end_time - self.start_time)} units per second')
        print(f'Average inventory in filling station buffer: {len(self.filling_station.items)/total_units}')
        print(f'Average inventory in capping station buffer:{len(self.capping_station.items)/total_units}')
        print(f'Average inventory in labeling station buffer:{len(self.labeling_station.items)/total_units}')
        print(f'Averageinventory in sealing station buffer: {len(self.sealing_station.items)/total_units}')
        print(f'Average inventory in carton packing station buffer: {len(self.carton_packing_station.items)/total_units}')


# Create a new packaging line simulation
packaging_line = PackagingLine(env)

# Run the simulation
env.process(packaging_line.run())
env.run()
# Calculate downtime probabilities

filling_downtime = packaging_line.blocking_count['filling'] / packaging_line.total_units
capping_downtime = packaging_line.blocking_count['capping'] / packaging_line.total_units
labeling_downtime = packaging_line.blocking_count['labeling'] / packaging_line.total_units
sealing_downtime = packaging_line.blocking_count['sealing'] / packaging_line.total_units
carton_packing_downtime = packaging_line.blocking_count['carton packing'] / packaging_line.total_units
print(f'Downtime probability at filling station: {filling_downtime:.2%}')
print(f'Downtime probability at capping station: {capping_downtime:.2%}')
print(f'Downtime probability at labeling station: {labeling_downtime:.2%}')
print(f'Downtime probability at sealing station: {sealing_downtime:.2%}')
print(f'Downtime probability at carton packing station: {carton_packing_downtime:.2%}')

avg_flow_time = (packaging_line.end_time - packaging_line.start_time) / packaging_line.total_units
print(f'Average system flow time: {avg_flow_time:.2f} seconds')
