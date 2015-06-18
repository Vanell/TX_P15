import os

directory = 'c:\Python33\Lib\Fanuc_xml\\'
file_name_py = 'tri_macro.py' 
file_name_macro = 'macro_catia.vba' 
destination = directory+file_name

if not os.path.exists(directory):
    os.makedirs(directory)

#Mouve python script
os.rename(file_name, destination)
#Mouve catia macro
os.rename(file_name, destination)
print('Install Done !')