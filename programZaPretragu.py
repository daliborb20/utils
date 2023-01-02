#!python
import re
import pyperclip

#todo: create a regex for phone numbers
telefonRegex = re.compile(r'''
(
((d\d\)*| (\(d\d\d\))* | (\d\d\d)*)         #area code optional  PIPE - ILI, ima ESCAPE karatker ispred zagrada, da bi i zagrade ukljucio u pretragu
(\s|-)       #first separator --> SEPARATOR MOZE BITI --SPACE-- ILI --MINUS--
\d\d\d       #first 3 digits
-            #separator
\d\d\d\d  #last 4 digits
(((ext(\.)?\s)|x) #extension (optional)
 (\d{2,5}))?))
''', re.VERBOSE)

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+        #name part []uglaste zagrade za kreiranje klase - u kojoj ne moraju da se eskejpuju karakteri
@    #@symbol
[a-zA-Z0-9_.+]+   #domain name part
 ''', re.VERBOSE)
#todo: create a regex for email addresses 

tekstIzKlipborda = pyperclip.paste()
#Get the text off the clipboard
ekstrahovaniTelefoni = telefonRegex.findall(tekstIzKlipborda)
ekstrahovaniEmailovi = emailRegex.findall(tekstIzKlipborda)
#Extract the email and phone from this text #Copy the extracted email and phone to the clipboard


telefoni = []#kreiramo tip podatka LISTA
emailovi = []#kreiramo tip podatka LISTA
for i in ekstrahovaniTelefoni: #dodajemo vrednosti u varijablu telefoni
    telefoni.append(i[0])
for i in ekstrahovaniEmailovi: # dodajemo vrednosti  u varijablu emailovi
    emailovi.append(i)

for i in telefoni:
    print(i)
for i in emailovi:
    print(i)
rezultati  = '\n'.join(telefoni) + '\n ' + '\n'.join(emailovi)
pyperclip.copy(rezultati)
