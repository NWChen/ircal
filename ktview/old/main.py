import gui
import ktview
import time

data = ktview.get_data("../2014_KT15_82_calib_217_155922.txt")
data = zip(*data)
x = []
print data[0]
for t in data[0]:
    x.append(time.mktime(t.timetuple()))
gui.plot([x, data[1]])
