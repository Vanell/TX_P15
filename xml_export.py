import xml.etree.cElementTree as ET


def xml_export(layers,name):
  i = 0
  PRODUCT = ET.Element("PRODUCT")
  for layer in layers:
    
    for part in layers[layer]:
      i +=1
      POSI = ET.SubElement(PRODUCT, "POSI",x=str(part[0][1]),y=str(part[1][1]),z=str(part[2][1]),w=str(part[3][1]),p=str(part[4][1]), r=str(part[5][1]), config_data=str(part[6][1]))
    
  print(i)
  tree = ET.ElementTree(PRODUCT)
  tree.write(str(name))