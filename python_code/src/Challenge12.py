class Computer:

    def __init__(self):
        self.cpu = None
        self.monitor = None

    def __init__(self,monitor,cpu):
        self.cpu = cpu
        self.monitor = monitor

    def get_specs(self):
        self.monitor = input('Enter monitor model - ')
        self.cpu = input("Enter processor model - ")

    def display_specs(self):
        print("{0} ## {1}".format(self.monitor, self.cpu))


class Desktop(Computer):

    def __init__(self, weight):
        super(Desktop, self).__init__(None,None)
        self.weight = weight

    def get_weight(self):
        self.weight = input("Enter weight")

    def display_weight(self):
        print("Weight is ", self.weight)


class Laptop(Computer):
    def __init__(self, gpu):
        super(Laptop, self).__init__(None, None)
        self.gpu = gpu

    def get_gpu(self):
        self.gpu = input("Enter gpu")

    def display_gpu(self):
        print("GPU is ", self.gpu)


computer = Computer(None,None)
computer.display_specs()
computer.get_specs()
computer.display_specs()

desk = Desktop(None)
desk.get_weight()
desk.display_weight()
desk.display_specs()

lap = Laptop(None)
lap.get_gpu()
lap.display_gpu()
lap.display_specs()

