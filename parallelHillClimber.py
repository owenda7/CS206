import solution
import constants as c
import copy

class PARALLEL_HILLCLIMBER:
  def __init__(self):
    self.nextAvailableID = 0
    self.parents = {}
    for i in range (0,c.populationSize):
      self.parents[i] = solution.SOLUTION(i)
      self.nextAvailableID += 1

  def Evolve(self):
    self.Evaluate(self.parents)


  def Evolve_For_One_Generation(self):
    self.Spawn()
    self.Mutate()
    self.Evaluate(self.children)
    self.Print()
    self.Select()
    self.Show_Best()


  def Spawn(self):
    self.children={}
    for key in self.parents.keys():
      self.children[key] = copy.deepcopy(self.parents[key])
      self.children[key].Set_ID(self.nextAvailableID)
      self.nextAvailableID += 1


  def Mutate(self):
    for key in self.children.keys():
        self.children[key].Mutate()

  def Evaluate(self, solutions):
     for key in solutions.keys():
       solutions[key].Start_Simulation("DIRECT")
     for key in solutions.keys():
       solutions[key].Wait_For_Simulation_To_End()



  def Print(self):
     print("\n")
     for key in self.parents.keys():
         print("PARENT-"+str(key)+"-FITNESS="+str(self.parents[key].fitness)+" CHILD-"+str(key)+"-FITNESS="+str(self.children[key].fitness))
     print("\n")

  def Select(self):
    for key in self.parents.keys():
      if(float(self.parents[key].fitness)<float(self.children[key].fitness)):
        self.parents[key] = copy.deepcopy(self.children[key])

  def Show_Best(self):
    best = 0
    current = 1000
    for key in self.parents.keys():
      if float(self.parents[key].fitness) < float(current):
        best = key
    self.parents[best].Start_Simulation("GUI")
