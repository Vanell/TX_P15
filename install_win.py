
#Import lib
import os
import urllib.request, urllib.parse, urllib.error
 
#Declare variable
directory = 'c:\Gen_XML\\'
directory_xml ='c:\Gen_X ML\\xml\\'
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
urllib.request.urlretrieve(url_vba, file_name_vba)

print("Create folder for marco")
if not os.path.exists(directory):
    os.makedirs(directory)
if not os.path.exists(directory_xml):
    os.makedirs(directory_xml)
    
print("Mouve python marco")
#Mouve python script
os.rename(file_name_py, destination_py)
print("Mouve vba marco")
#Mouve catia macro
os.rename(file_name_vba, destination_vba)
print('Install Done !')
print('Ready to config ?')
input()
print('Open Catia')
input()
print('Got to : Outils/Marco/Macros...')
input()
print('Bibliothèque de macros...')
print('Type de bibiothèque : Projets VBA')
print('Ajouter bibliothèque existante...')
input()
print('Go to : C:\Gen_XML')
print('Open : IHM.catvba')
input()
print('Close window')
print('Now it\'s ready and you can execute Gen_XML')
input()