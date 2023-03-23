from tkinter import *
import pygame, sys
from pygame.locals import *
from tkinter import filedialog 
from PIL import ImageTk, Image
import os




pygame.init() #iniciamos modulo de pygame

#Funcion abrir archivo
def openFileSong():
    cancion = filedialog.askopenfilename()    #guardar el nombre o cancion que queramos reproducir
    print(cancion)
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play()

def playSong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def pauseSong():
    pygame.mixer.music.pause()

def resumeSong():
    pygame.mixer.music.unpause()

def bajarVolumen():
    volumenlevel = pygame.mixer.music.get_volume()-0.1
    print(volumenlevel)
    pygame.mixer.music.set_volume(volumenlevel)

def subirVolumen():
    volumenlevelup = pygame.mixer.music.get_volume()+0.1
    print(volumenlevelup)
    pygame.mixer.music.set_volume(volumenlevelup)





raiz= Tk()
raiz.title("Reproductor MP3- GUI")
raiz.iconbitmap("led.ico")
raiz.geometry("700x700")
raiz.resizable(0,0)

#crear frame

framePrincipal = Frame(raiz, bg="black")

framePrincipal.pack(fill="both", expand=1)

tituloReproductorMP3 = Label(framePrincipal, text="Reproductor valdo - GUI", font = ("Roboto",15,"bold"), bg = "blue", fg = "#fbfbfb")
tituloReproductorMP3.pack()

#boton open song
botonOpenSong = Button(framePrincipal, text="Open Song", bg="blue", fg = "#fbfbfb", font=("Roboto",10, "bold"), width = 18, height= 2, command = openFileSong)
botonOpenSong.place(relx=0.01, rely=0.5)

#boton Play song
botonPlaySong = Button(framePrincipal, text="Play Song", bg="#42ab49", fg = "#fbfbfb", font=("Roboto",10, "bold"), width = 18, height= 2, command=playSong)
botonPlaySong.place(relx=0.2, rely=0.5)

#boton Stop 
botonStopSong = Button(framePrincipal, text="Stop Song", bg="red", fg = "#fbfbfb", font=("Roboto",10, "bold"), width = 18, height= 2, command = stopSong)
botonStopSong.place(relx=0.4, rely=0.5)

#boton Resume
botonResumeSong = Button(framePrincipal, text="Resume", bg="#ffc400", fg = "#fbfbfb", font=("Roboto",10, "bold"), width = 18, height= 2, command = resumeSong)
botonResumeSong.place(relx=0.6, rely=0.5)

#boton Pause 
botonPauseSong = Button(framePrincipal, text="Pause ", bg="#550099", fg = "#fbfbfb", font=("Roboto",10, "bold"), width = 18, height= 2, command = pauseSong)
botonPauseSong.place(relx=0.8, rely=0.5)

#boton bajar volumen
botonbajarVolumen = Button(framePrincipal, text="Bajar Volumen", bg="brown", fg = "#fbfbfb", font=("Roboto",10, "bold"), width = 18, height= 2, command = bajarVolumen)
botonbajarVolumen.place(relx=0.2, rely=0.6)

#boton subir volumen
botonsubirVolumen = Button(framePrincipal, text="Subir Volumen", bg="brown", fg = "#fbfbfb", font=("Roboto",10, "bold"), width = 18, height= 2, command = subirVolumen)
botonsubirVolumen.place(relx=0.6, rely=0.6)

imagen=Image.open("redbull.ico")
imagenReproductor=imagen.resize((200,120))
img= ImageTk.PhotoImage(imagenReproductor)

TituloImagen=Label(framePrincipal, image=img)
TituloImagen.place(relx=0.35, rely=0.1)

#42ab49 verde
#550099 morado
#ffc400 amarillo
#e25045c rojo



raiz.mainloop()