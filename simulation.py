import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import time

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
    def __del__(self):
        p.disconnect()
    def Run(self):
        for i in range(0,c.TIME):
            p.stepSimulation()
            self.robot.Sense(i)
            pyrosim.Set_Motor_For_Joint(bodyIndex=self.robot.robot, jointName="Torso_BackLeg", controlMode=p.POSITION_CONTROL , targetPosition=self.robot.targetAnglesBack[i], maxForce=50)
            pyrosim.Set_Motor_For_Joint(bodyIndex=self.robot.robot, jointName="Torso_FrontLeg", controlMode=p.POSITION_CONTROL , targetPosition=self.robot.targetAnglesFront[i], maxForce=50)
            time.sleep(c.SLEEP)
