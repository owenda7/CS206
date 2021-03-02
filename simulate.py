import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import random

T = 2000

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

frequency = 7
phaseOffset = numpy.pi/2
amplitude = 1
x = numpy.linspace(-numpy.pi, numpy.pi, T)
numpy.save("data/front.npy", amplitude * numpy.sin(frequency*x+phaseOffset))
targetAnglesFront = numpy.load("data/front.npy")

frequency = 7
phaseOffset = 0
amplitude = 1
x = numpy.linspace(-numpy.pi, numpy.pi, T)
numpy.save("data/back.npy", amplitude * numpy.sin(frequency*x+phaseOffset))
targetAnglesBack = numpy.load("data/back.npy")

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = numpy.zeros(T)
frontLegSensorValues = numpy.zeros(T)

for i in range(0,T):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

	pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName="Torso_BackLeg", controlMode=p.POSITION_CONTROL , targetPosition=targetAnglesBack[i], maxForce=50)
	pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName="Torso_FrontLeg", controlMode=p.POSITION_CONTROL , targetPosition=targetAnglesFront[i], maxForce=50)
	time.sleep(1/60)

print(backLegSensorValues)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()
