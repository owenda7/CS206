import pybullet as p
import numpy
import os
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import constants as c

class ROBOT:
    def __init__(self, solutionID):
        # load robot urdf
        self.robot = p.loadURDF("body.urdf")
        # import leg angles
        self.targetAnglesFront = numpy.load("data/front.npy")
        self.targetAnglesBack = numpy.load("data/back.npy")

        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.solutionID = solutionID
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        

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
        i = 0
        for jointName in pyrosim.jointNamesToIndices:
            if i == 1:
                self.frequency = self.frequency/2
            self.motors[jointName] = MOTOR(self.robot, jointName, self.amplitude, self.frequency, self.offset)
            i = 1

    def Act(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle*c.motorJointRange)



    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
       stateOfLinkZero=p.getLinkState(self.robot,0)
       xCoordinateOfLinkZero=stateOfLinkZero[0][0]
       file = open(f"tmp{self.solutionID}.txt", "w")
       file.write(str(xCoordinateOfLinkZero))
       file.close()
       os.system(f"mv tmp{self.solutionID}.txt fitness{self.solutionID}.txt")
