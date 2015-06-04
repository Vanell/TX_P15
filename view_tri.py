##Library

import xml.etree.ElementTree as etree

import json
from math import sqrt

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from tri import xml_sorted

filename = "ellipse_CAO.xml"
layers = xml_sorted(filename)

  
##View data
fig = plt.figure()
fig.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=1, hspace=1)
ax = fig.gca(projection='3d')
ax.set_xlim3d(-150, 150)
ax.set_ylim3d(-150, 150)


nb_layer = int(raw_input("View layer ? \n"))
# nb_layer = 2
for layer in layers :

  if layer == (nb_layer-1) :
    for part in layers[layer]:
      x = part[0][1]
      y = part[1][1]
      z = part[2][1]
      label = "(%s)"%((layers[layer].index(part))+1)
      ax.text(x, y, z, label, color='red')

label = "(0)"
ax.text(0, 0, z, label, color='red')
ax.set_zlim3d(z-0.5, z+0.5)
plt.axis('off')
plt.show()