import pyrosim.pyrosim as pyrosim
import constants as c
import numpy

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="World", pos=[3,3,.5], size=[1,1,1])
    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5], size=[1,1,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[0.5,0,-0.5], size=[1,1,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5,0,-0.5], size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = ".5 0 1")
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "-.5 0 1")
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
    pyrosim.Send_Motor_Neuron(name = 3, jointName= "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name = 4, jointName= "Torso_FrontLeg")
    pyrosim.Send_Synapse( sourceNeuronName = 0, targetNeuronName = 3, weight = 1.0 ) 
    pyrosim.End()

def Generate_Angles(filename, length, frequency, amplitude, phaseOffset):
    x = numpy.linspace(-numpy.pi, numpy.pi, length)
    numpy.save(filename, amplitude * numpy.sin(frequency*x+phaseOffset))

Create_World()
Generate_Body()
Generate_Brain()
Generate_Angles("data/front.npy", c.TIME, 7, 1, numpy.pi/2)
Generate_Angles("data/back.npy", c.TIME, 7, 1, 0)


