"""This Vehicle class is to look at Interface Segregation Principle.

The interface segregation principle says that if a client implements an interface,
they should only have to implement the functionality they are interested in. Here's
an example with shapes to drive the point home.
"""


class Vehicle:
    def __init__(self):
        pass

    def get_wheels(self):
        pass

    def drop_anchor(self):
        pass

    def start_engine(self):
        print("Starting engine...")

class Boat(Vehicle):
    def __init__(self):
        super(Boat, self).__init__()

    def get_wheels(self):
        return 0

    def drop_anchor(self):
        print("Dropping anchor...")

    def start_engine(self):
        super(Boat, self).start_engine()

# Okay, this isn't exactly an interface. But, the idea is that this Vehicle class
# has a function that we're interested in for the Boat start_engine. However,
# We're also forced to inherit the get_wheels function, which is not useful for boats. 

# Instead, let's change Vehicle so it only has things that we're interested for 
# in all vehicles.

class Vehicle:
    def __init__(self):
        pass

    def start_engine(self):
        print("Starting engine...")


class Boat(Vehicle):
    def __init__(self):
        super(Circle, self).__init__()

    def drop_anchor(self):
        print("Dropping anchor...")

    def start_engine(self):
        super(Boat, self).start_engine()


class Car(Vehicle):
    def __init__(self):
        super(Car, self).__init__()

    def get_wheels(self):
        return 4

    def start_engine(self):
        super(Car, self).start_engine()

# We've cleaned up our interface, and now boats don't have wheels and cars don't have anchors.
