import numpy
import time
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random

class SOLUTION:
  def __init__(self, nextAvailableID):
    self.myID=nextAvailableID
    self.weights=numpy.random.rand(3,2)*2-1
    self.Create_World()
    self.Generate_Body()
    self.Generate_Brain()
    self.fitness=0

  def Evaluate(self, mode):
    os.system("python3 simulate.py "+mode+" "+str(self.myID)+" &")
    fitnessFileName = f"fitness{self.myID}.txt"
    while not os.path.exists(fitnessFileName):
      time.sleep(0.01)
    f = open(fitnessFileName, "r")
    self.fitness = f.read()
    print(self.fitness)
    f.close()

  def Start_Simulation(self, mode):
    os.system("python3 simulate.py "+mode+" "+str(self.myID)+" &")

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
    row = random.randint(0,2)
    col = random.randint(0,1)
    self.weights[row, col] = random.random()*2-1
    self.Create_World()
    self.Generate_Body()
    self.Generate_Brain()

  def Create_World(self):
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="World", pos=[3,3,.5], size=[1,1,1])
    pyrosim.End()

  def Generate_Body(self):
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5], size=[1,1,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[0.5,0,-0.5], size=[1,1,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5,0,-0.5], size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = ".5 0 1")
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "-.5 0 1")
    pyrosim.End()

  def Generate_Brain(self):
    filename = "brain" + str(self.myID) + ".nndf"
    pyrosim.Start_NeuralNetwork(filename)
    pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
    pyrosim.Send_Motor_Neuron(name = 3, jointName= "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name = 4, jointName= "Torso_FrontLeg")
    for currentRow in range(0,3):
        for currentColumn in range(0,2):
            pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight = self.weights[currentRow][currentColumn] )
    pyrosim.End()

  def Set_ID(self, ID):
    self.myID = ID
