##Library

import xml.etree.ElementTree as etree
import json
from math import sqrt
import xml.etree.cElementTree as ET
import sys

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
  dx = -150
  dy = -150
  if sqrt((v1[0][1]+dx)**2+(v1[1][1]+dy)**2) < sqrt((v2[0][1]+dx)**2+(v2[1][1]+dy)**2):
        return -1
  elif sqrt((v1[0][1]+dx)**2+(v1[1][1]+dy)**2) > sqrt((v2[0][1]+dx)**2+(v2[1][1]+dy)**2):
      return 1
  else:
      return 0
      
def xml_export(layers,name):

  PRODUCT = ET.Element("PRODUCT")
  for layer in layers:
    
    for part in layers[layer]:
      POSI = ET.SubElement(PRODUCT, "POSI",x=str(part[0][1]),y=str(part[1][1]),z=str(part[2][1]),w=str(part[3][1]),p=str(part[4][1]), r=str(part[5][1]), config_data=str(part[6][1]))
    
  tree = ET.ElementTree(PRODUCT)
  tree.write(str(name))


def xml_sorted(file):
  
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
  
  ##Tri en z
  esm = sorted(esm,key=cmp_to_key(comp_z))
  
  ##Decoupage par couche
  layers = dict()
  tmp_layer = list()
  list_layer = list()
  c =0
  zc = esm[0][1][2][1]
  
  for elmt in esm:

    if zc != elmt[1][2][1]:
  
      layers[c] = tmp_layer
      tmp_layer = list()
      c += 1
      list_layer.append(zc)
    zc = elmt[1][2][1]
    
    if esm.index(elmt) != (len(esm)-1):
      tmp_layer.append(dic_esm[elmt[0]])
      
    if esm.index(elmt) == (len(esm)-1):
      tmp_layer.append(dic_esm[elmt[0]])
      layers[c] = tmp_layer
      
  ##Tri en X et Y
  
  for layer in layers:
    layers[layer] = (sorted(layers[layer],key=cmp_to_key(comp_xy)))
  
  return layers

##Sorting

filename = sys.argv[1]
file=open(filename, 'r')
layers = xml_sorted(filename)

##Generate XML

xml_export(layers,"%s_sorted.xml"%(filename.split(".")[0]))