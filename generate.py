import pyrosim.pyrosim as pyrosim
import constants as c
import numpy

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="World", pos=[3,3,.5], size=[1,1,1])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5], size=[1,1,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[0.5,0,-0.5], size=[1,1,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5,0,-0.5], size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = ".5 0 1")
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "-.5 0 1")
    pyrosim.End()

def Generate_Angles(filename, length, frequency, amplitude, phaseOffset):
    x = numpy.linspace(-numpy.pi, numpy.pi, length)
    numpy.save(filename, amplitude * numpy.sin(frequency*x+phaseOffset))

Create_World()
Create_Robot()
Generate_Angles("data/front.npy", c.TIME, 7, 1, numpy.pi/2)
Generate_Angles("data/back.npy", c.TIME, 7, 1, 0)
