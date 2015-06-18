import os
import urllib.request, urllib.parse, urllib.error
 
directory_py = 'c:\Python33\Lib\Fanuc_xml\\'
file_name_py = 'tri_macro.py'
file_name_vba = 'macro_catia.vba'
destination_py = directory_py+file_name_py
destination_vba = directory_vba+file_name_vba
 
url_python = "https://raw.githubusercontent.com/Vanell/TX_P15/master/tri_macro.py"
url_vba = "https://raw.githubusercontent.com/Vanell/TX_P15/master/macro_xml_catia.vba"
 
print("Downloading tri macro python")
urllib.request.urlretrieve(url_python, file_name_py)
print("Downloading tri macro vba")
urllib.request.urlretrieve(url_python, file_name_vba)

print("Create folder for python marco")
if not os.path.exists(directory_py):
    os.makedirs(directory_py)

print("Mouve python marco")
#Mouve python script
os.rename(file_name_py, destination_py)
print("Mouve vba marco")
#Mouve catia macro
os.rename(file_name_vba, destination_vba)
print('Install Done !')