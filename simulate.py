import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import random
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# import leg angles
targetAnglesFront = numpy.load("data/front.npy")
targetAnglesBack = numpy.load("data/back.npy")

p.setGravity(0,0,c.GRAVITY)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = numpy.zeros(c.TIME)
frontLegSensorValues = numpy.zeros(c.TIME)

for i in range(0,c.TIME):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

	pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName="Torso_BackLeg", controlMode=p.POSITION_CONTROL , targetPosition=targetAnglesBack[i], maxForce=50)
	pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName="Torso_FrontLeg", controlMode=p.POSITION_CONTROL , targetPosition=targetAnglesFront[i], maxForce=50)
	time.sleep(c.SLEEP)

print(backLegSensorValues)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()
