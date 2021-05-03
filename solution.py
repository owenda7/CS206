import numpy
import time
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random

class SOLUTION:
  def __init__(self, nextAvailableID):
    self.myID=nextAvailableID
    self.weights=numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)*2-1
    self.Create_World()
    self.Generate_Body()
    self.Generate_Brain()
    self.fitness=0

  def Evaluate(self, mode):
    os.system("python3 simulate.py "+mode+" "+str(self.myID)+" 2&>1 &")
    fitnessFileName = f"fitness{self.myID}.txt"
    while not os.path.exists(fitnessFileName):
      time.sleep(0.01)
    f = open(fitnessFileName, "r")
    self.fitness = f.read()
    print(self.fitness)
    f.close()

  def Start_Simulation(self, mode):
    os.system("python3 simulate.py "+mode+" "+str(self.myID)+" 2&>1 &")

  def Wait_For_Simulation_To_End(self):
    fitnessFileName = f"fitness{self.myID}.txt"
    while not os.path.exists(fitnessFileName):
      time.sleep(0.01)
    f = open(fitnessFileName, "r")
    self.fitness = f.read()
    print(self.fitness)
    f.close()
    #os.system(f"rm {fitnessFileName}")
    #os.system(f"rm brain{self.myID}.nndf")

  def Mutate(self):
    row = random.randint(0,c.numSensorNeurons-1)
    col = random.randint(0,c.numMotorNeurons-1)
    self.weights[row, col] = random.random()*2-1
    print(self.weights)
    self.Create_World()
    self.Generate_Body()
    self.Generate_Brain()

  def Create_World(self):
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="World", pos=[-3,-4,1], size=[2,2,2])
    pyrosim.Send_Cube(name="World",  pos=[-3,4,1], size=[2,2,2])
    pyrosim.Send_Cube(name="World", pos=[-5,-2,1], size=[2,2,2])
    pyrosim.Send_Cube(name="World", pos=[-10,3,1], size=[2,2,2])
    pyrosim.Send_Cube(name="World",  pos=[-7,5,1], size=[2,2,2])
    pyrosim.Send_Cube(name="World", pos=[-9,-4,1], size=[2,2,2])
    pyrosim.End()

  def Generate_Body(self):
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[1,1,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0], size=[.2,1,.2])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0], size=[.2,1,.2])
    pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0], size=[1,.2,.2])
    pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0], size=[1,.2,.2])
    pyrosim.Send_Cube(name="BackFoot", pos=[0,0,-0.5], size=[.2,.2,1])
    pyrosim.Send_Cube(name="FrontFoot", pos=[0,0,-0.5], size=[.2,.2,1])
    pyrosim.Send_Cube(name="LeftFoot", pos=[0,0,-0.5], size=[.2,.2,1])
    pyrosim.Send_Cube(name="RightFoot", pos=[0,0,-0.5], size=[.2,.2,1])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = "0 -.5 1" , jointAxis = "1 0 0")
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "0 .5 1" , jointAxis = "1 0 0")
    pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = "-.5 0 1" , jointAxis = "0 1 0")
    pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = ".5 0 1" , jointAxis = "0 1 0")
    pyrosim.Send_Joint( name = "BackKnee" , parent= "BackLeg" , child = "BackFoot" , type = "revolute", position = "0 -1 0" , jointAxis = "1 1 0")
    pyrosim.Send_Joint( name = "FrontKnee" , parent= "FrontLeg" , child = "FrontFoot" , type = "revolute", position = "0 1 0" , jointAxis = "1 1 0")
    pyrosim.Send_Joint( name = "LeftKnee" , parent= "LeftLeg" , child = "LeftFoot" , type = "revolute", position = "-1 0 0" , jointAxis = "1 1 0")
    pyrosim.Send_Joint( name = "RightKnee" , parent= "RightLeg" , child = "RightFoot" , type = "revolute", position = "1 0 0" , jointAxis = "1 1 0")
    pyrosim.End()

  def Generate_Brain(self):
    filename = "brain" + str(self.myID) + ".nndf"
    pyrosim.Start_NeuralNetwork(filename)
    pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
    pyrosim.Send_Sensor_Neuron(name = 3, linkName = "LeftLeg")
    pyrosim.Send_Sensor_Neuron(name = 4, linkName = "RightLeg")
    pyrosim.Send_Sensor_Neuron(name = 5, linkName = "BackFoot")
    pyrosim.Send_Sensor_Neuron(name = 6, linkName = "FrontFoot")
    pyrosim.Send_Sensor_Neuron(name = 7, linkName = "LeftFoot")
    pyrosim.Send_Sensor_Neuron(name = 8, linkName = "RightFoot")
    pyrosim.Send_Motor_Neuron(name = 9, jointName= "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name = 10, jointName= "Torso_FrontLeg")
    pyrosim.Send_Motor_Neuron(name = 11, jointName= "Torso_LeftLeg")
    pyrosim.Send_Motor_Neuron(name = 12, jointName= "Torso_RightLeg")
    pyrosim.Send_Motor_Neuron(name = 13, jointName= "BackKnee")
    pyrosim.Send_Motor_Neuron(name = 14, jointName= "FrontKnee")
    pyrosim.Send_Motor_Neuron(name = 15, jointName= "LeftKnee")
    pyrosim.Send_Motor_Neuron(name = 16, jointName= "RightKnee")
    for currentRow in range(0,c.numSensorNeurons):
        for currentColumn in range(0,c.numMotorNeurons):
            pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow][currentColumn] )
    pyrosim.End()

  def Set_ID(self, ID):
    self.myID = ID
