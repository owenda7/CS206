import pybullet as p
import numpy
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:
    def __init__(self):
        # load robot urdf
        self.robot = p.loadURDF("body.urdf")
        # import leg angles
        self.targetAnglesFront = numpy.load("data/front.npy")
        self.targetAnglesBack = numpy.load("data/back.npy")

        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()

        self.sensors = {}
        self.motors = {}

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)

    def Prepare_To_Act(self):
        self.amplitude = c.AMPLITUDE
        self.frequency = c.FREQUENCY
        self.offset = c.OFFSET
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
