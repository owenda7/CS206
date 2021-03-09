import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy

class MOTOR:
    def __init__(self, robot, jointName, amplitude, frequency, offset):
        self.jointName = jointName
        self.robot = robot
        x = numpy.linspace(-numpy.pi, numpy.pi, c.TIME)
        self.values = amplitude * numpy.sin(frequency*x+offset)
        print(frequency)

    def Set_Value(self, i):
        pyrosim.Set_Motor_For_Joint(bodyIndex=self.robot, jointName=self.jointName, controlMode=p.POSITION_CONTROL , targetPosition=self.values[i], maxForce=c.MAX_FORCE)
