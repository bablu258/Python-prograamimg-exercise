class Vehicle:
    def __init__(self, **kwargs):
        self.var = kwargs

    def mile (self):
        print ("The car model")

    def year (self):
        print(" The year of the model")

    def get_param (self):
        return self.var

    def get_param (self, key):
        return self.var.get(key)


def main ():
    truck = Vehicle(year='2004')
    print (truck.get_param('year'))

    bus = Vehicle(model='Honda', year='2013')
    print (bus.get_param('model'))
    print (bus.get_param('year'))


if __name__ == "__main__": main()