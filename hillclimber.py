import solution
import constants as c
import copy

class HILLCLIMBER:
  def __init__(self):
    self.parent = solution.SOLUTION()
  
  def Evolve(self):
    self.parent.Evaluate("GUI")
    for currentGeneration in range(0,c.numberOfGenerations):
      self.Evolve_For_One_Generation()
    self.ShowBest()

  def Evolve_For_One_Generation(self):
    self.Spawn()
    self.Mutate()
    self.child.Evaluate("DIRECT")
    self.Print()
    self.Select()

  def Spawn(self):
    self.child = copy.deepcopy(self.parent)

  def Mutate(self):
    self.child.Mutate()
    print(self.parent.weights)
    print(self.child.weights)

  def Select(self):
    if(float(self.parent.fitness)>float(self.child.fitness)):
      self.parent = self.child

  def Print(self):
    print("PARENT-FITNESS="+str(self.parent.fitness)+" CHILD-FITNESS="+str(self.child.fitness))

  def ShowBest(self):
    self.parent.Evaluate("GUI")
