import os
fajl = open(".\\Lista_fajlova.txt", "w", encoding="utf-8")
print(os.getcwd()) #get curent working directory
print(os.path.getsize) #get file size
ciljaniDirektorijum = ("c:\\users\\pc\\Documents\\")
spisakFajlovaFoldera = os.listdir(ciljaniDirektorijum)
listaSpisak = []
recnikVelicinaFajla = {}

for i in spisakFajlovaFoldera:
    listaSpisak.append(ciljaniDirektorijum + i)
for i in listaSpisak:
    if os.path.isfile(i):
        recnikVelicinaFajla[i] = os.path.getsize(i)
for i in recnikVelicinaFajla:
    fajl.write("Velicina fajla " + i + " " + "je " +  str(recnikVelicinaFajla[i]) + " bajta ili " + str(round(recnikVelicinaFajla[i]/1048576, 3)) + " Megabajta\n" )


fajl.close()
