class YeastNode:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.ethanol_concentration = 0.0
        self.substrate = 0.0

    def feed_substrate(self, amount):
        self.substrate += amount
        # Ferment substrate into work done
        work = min(self.substrate, self.capacity * (1.0 - self.ethanol_concentration))
        self.substrate -= work
        self.ethanol_concentration = min(1.0, self.ethanol_concentration + work * 0.05)
        return work
