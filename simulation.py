import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import time

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        if(directOrGUI == "DIRECT"):
          self.physicsClient = p.connect(p.DIRECT)
        else:
          self.physicsClient = p.connect(p.GUI)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        self.directOrGUI = directOrGUI
    def __del__(self):
        p.disconnect()
    def Run(self):
        for i in range(0,c.TIME):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI == "GUI":
                time.sleep(c.SLEEP)
    def Get_Fitness(self):
        self.robot.Get_Fitness()
