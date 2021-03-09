import constants as c
import numpy

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.values = numpy.zeros(c.TIME)
