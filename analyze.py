import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
backLegLine, = matplotlib.pyplot.plot(backLegSensorValues, linewidth=3)
frontLegLine, = matplotlib.pyplot.plot(frontLegSensorValues)
backLegLine.set_label('Back Leg')
frontLegLine.set_label('Front Leg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
