#Optional: Autocomplete
#Arbeitstage pro Jahr werden noch nicht berücksichtigt?

#Eingebenen Werte werden korrekt in die Funktion "rechneBetrag" übertragen

import requests
import json
import urllib.parse
from tkinter import *
import tkinter as tk
import tkinter

#def berechneFahrtkosten():

#Console Input (Dev)
#startAdresse = input("Bitte Adresse und Hausnummer eingeben:")
#zielAdresse = input("Bitte Ziel Adresse und Hausnummer eingeben:")

def findeRoute():
    #Liefert uns die Lat und Long zurück (Start Adresse)
    startAdresse = sa.get()
    zielAdresse = za.get()
    print(startAdresse)
    print(zielAdresse)
    startlatlng = requests.get("https://api.opencagedata.com/geocode/v1/json?q={0}&key=6bd072af2b394258b70cb1923811cf25".format(startAdresse))
    #print(startlatlng)
    xy = startlatlng.json()
    latstart = xy['results'][0]['bounds']['northeast']['lat']
    print(latstart)
    lngstart = xy['results'][0]['bounds']['northeast']['lng']
    print(lngstart)
    ziellatlng = requests.get("https://api.opencagedata.com/geocode/v1/json?q={0}&key=6bd072af2b394258b70cb1923811cf25".format(zielAdresse))
    #JSON File auf lat und lng parsen
    xx = ziellatlng.json()
    latziel = xx['results'][0]['bounds']['northeast']['lat']
    print(latziel)
    lngziel = xx['results'][0]['bounds']['northeast']['lng']
    print(lngziel)
    #Route mit OpenRouteService bestimmen und kürzeste "Driving Car" Route finden
    route = requests.get("https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248cf56f374d7f14bdba928b87f5caece16&start={0},{1}&end={2},{3}".format(lngstart,latstart,lngziel,latziel))
    #Check HTTP Header for Faults: Maybe implement Error Warning
    print(route)
    rt = route.json()
    distan = rt['features'][0]['properties']['segments'][0]['distance']
    sdistan = distan / 1000
    print(sdistan)
    #epkm aus Entry beziehen:
    eprokm = epkm.get()
    #Validierung Variable epkm
    print(eprokm)
    erg = float(sdistan)*float(eprokm)
    print(erg)
    gesK.insert(END, round(erg,2))
    gesK.insert(END," €")
master = Tk()
#set App Name:
master.title("Fahrtkostenrechner")
#App Icon:
img = PhotoImage(file='icon.ico')
master.tk.call('wm', 'iconphoto', master._w, img)
#Set Width and Hight (Application Window)
master.geometry("722x496")
# Add image file 
bg = PhotoImage(file = "backround.png") 
# Show image using label 
label1 = Label( master, image = bg) 
label1.place(x = 0, y = 0) 
#Label Startadresse:
Label(master, text="Startadresse:").place(x = 115, y = 80, width = 85, height = 25)
#Label Zieladresse:
Label(master, text="Zieladresse:").place(x = 115, y = 180, width = 80, height = 25)
#Label Betrag pro KM (0.30€ 2021)
Label(master, text="Kosten pro KM:").place(x = 115, y = 285, width = 100, height = 25)
#Label Ausgabe Ergebnis:
Label(master, text="Gesamtkosten:").place(x = 380, y = 285, width = 100, height = 25)
#Registriere Benutzereingaben:
sa = Entry(master)
za= Entry(master)
epkm = Entry(master)
epkm.insert(0,"0.30")
#Return Ergebnis
gesK = Entry(master)

#Anordung auf der Oberfläche
za.place(x = 235, y = 180, width=350, height=25)
sa.place(x = 235, y = 80, width=350, height=25)
epkm.place(x = 220, y = 285, width=100, height=25)
gesK.place(x = 485, y = 285, width=100, height=25)

#Buttons:
Button(master, text='Quit', command=master.quit).place(x = 220, y = 380)
Button(master, text='Berechnen', command=findeRoute).place(x = 485,y = 380)

master.mainloop( )
