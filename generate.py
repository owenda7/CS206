import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = .5

pyrosim.Start_SDF("box.sdf")
for x in range(0,6):
    for y in range(0,6):
        length = 1
        width = 1
        height = 1
        z = .5
        for k in range(0,10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
            z = z+height
            length = length * .9
            width = width * .9
            height = height * .9

pyrosim.End()
