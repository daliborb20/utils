import os

print(os.getcwd()) #get curent working directory
print(os.path.getsize) #get file size
ciljaniDirektorijum = ("c:\\users\\boogyman\\Documents\\")
spisakFajlovaFoldera = os.listdir(ciljaniDirektorijum)
listaSpisak = []
recnikVelicinaFajla = {}

for i in spisakFajlovaFoldera:
    listaSpisak.append(ciljaniDirektorijum + i)
for i in listaSpisak:
    if os.path.isfile(i):
        recnikVelicinaFajla[i] = os.path.getsize(i)
n=0
for i in recnikVelicinaFajla:
    print("Velicina fajla " + i + " " + "je " +  str(recnikVelicinaFajla[i]) + " bajta ili " + str(round(recnikVelicinaFajla[i]/1048576, 3)) + " Megabajta" )
    n=n+1
