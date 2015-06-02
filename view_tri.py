##Library

import xml.etree.ElementTree as etree
import xml.etree.cElementTree as ET

import json
from math import sqrt

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

##Function

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def comp_z(v1,v2):
  if v1[1][2] < v2[1][2]:
        return -1
  elif v1[1][2] > v2[1][2]:
      return 1
  else:
      return 0
      
def comp_xy(v1,v2):
  if sqrt(v1[0][1]**2+v1[1][1]**2) < sqrt(v2[0][1]**2+v2[1][1]**2):
        return -1
  elif sqrt(v1[0][1]**2+v1[1][1]**2) > sqrt(v2[0][1]**2+v2[1][1]**2):
      return 1
  else:
      return 0
      

##Sorting

filename = "ellipse_CAO.xml"
file=open(filename, 'r')

esm = list()
dic_esm = dict()

id_part = 0

tree = etree.parse(file)

for h in tree.iter():
    if h.tag== 'POSI':
        part = list()
        part.append(("x",round(float(h.get('x')),2)))
        part.append(("y",round(float(h.get('y')),2)))
        part.append(("z",round(float(h.get('z')),2)))
        part.append(("w",round(float(h.get('w')),2)))
        part.append(("p",round(float(h.get('p')),2)))
        part.append(("r",round(float(h.get('r')),2)))
        part.append(("config_data",str(h.get('config_data'))))
        
        esm.append((id_part,part))
        dic_esm[id_part] = part
        
        id_part=id_part+1

##Trie en z
esm = sorted(esm,key=cmp_to_key(comp_z))

##Decoupage par couche
layers = dict()
tmp_layer = list()
list_layer = list()
c =0
zc = 0

for elmt in esm:
  if zc != elmt[1][2][1] or esm.index(elmt) == (len(esm)-1):

    layers[c] = tmp_layer

    tmp_layer = list()
    c += 1
    list_layer.append(zc)
    zc = elmt[1][2][1]

  elif zc == elmt[1][2][1]:
    tmp_layer.append(dic_esm[elmt[0]])

##Trie en X et Y

for layer in layers:
  layers[layer] = (sorted(layers[layer],key=cmp_to_key(comp_xy)))
  
##View data
fig = plt.figure()
fig.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=1, hspace=1)
ax = fig.gca(projection='3d')
ax.set_xlim3d(-150, 150)
ax.set_ylim3d(-150, 150)

nb_layer = int(raw_input("View layer ? \n"))
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