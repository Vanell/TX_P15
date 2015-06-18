
#Import lib
import os
import urllib.request, urllib.parse, urllib.error
 
#Declare variable
directory = 'c:\Gen_Xml\\'
file_name_py = 'tri_macro.py'
file_name_vba = 'IHM.catvba'
destination_py = directory+file_name_py
destination_vba = directory+file_name_vba
 
url_python = "https://github.com/Vanell/TX_P15/raw/master/tri_macro.py"
url_vba = "https://github.com/Vanell/TX_P15/raw/master/IHM.catvba"
 
#Begin install
print("Downloading tri macro python")
urllib.request.urlretrieve(url_python, file_name_py)
print("Downloading tri macro vba")
urllib.request.urlretrieve(url_python, file_name_vba)

print("Create folder for marco")
if not os.path.exists(directory):
    os.makedirs(directory)

print("Mouve python marco")
#Mouve python script
os.rename(file_name_py, destination_py)
print("Mouve vba marco")
#Mouve catia macro
os.rename(file_name_vba, destination_py)
print('Install Done !')
raw_input()