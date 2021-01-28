"""Programa 3
Kakuro 2021
Jhonny Andres Diaz Coto
Carnet: 2020042119"""
#IMPORTACIONES----------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import pickle # modulo para cargar datos
import random
import copy
import webbrowser as wb
from tkinter import Tk, Label, Button, Frame
from random import randint
import winsound
import os
import time
#-----------------------------------------------------------------------------------------------------------------------
'''Variables globales '''
color = ""
texto = ""
lista_jugadas = []
lista_eliminados = []



"""Funcion cambio boton: esta funcion tiene como tarea hacer que el boton seleccionado para asiganarle un valor para hacer una jugada se cambie, si se le asigna un valor vacio se retorna un error."""
def cambio_boton(Boton, jugada):
    global texto, lista_jugadas
    if texto == '':
        ''' MessageBox
        -showinfo(), showerror(), showwarning(), askquestion(), askcancel(), askyesno(), askretrycancel()'''
        messagebox.showerror(message='Debe seleccionar un boton del panel de seleccion')
    else:
        Boton.configure(text=texto)
        lista_jugadas.append([Boton, texto])
        print(lista_jugadas)

"""Funcion panel de seleccion: esta funcion se encarga de darle a la variable global el color o el texto seleccionado, cada boton cada vez que se presione le asigna el color o valor que tenga en ese momento"""
def PanelSeleccion(color_seleccionado, texto_seleccionado, boton_seguro, lista_botones):
    global color, texto
    color = color_seleccionado
    texto = texto_seleccionado

    lista_botones[0].configure(bg="snow")
    lista_botones[1].configure(bg="snow")
    lista_botones[2].configure(bg="snow")
    lista_botones[3].configure(bg="snow")
    lista_botones[4].configure(bg="snow")
    lista_botones[5].configure(bg="snow")
    lista_botones[6].configure(bg="snow")
    lista_botones[7].configure(bg="snow")
    lista_botones[8].configure(bg="snow")

    def cambio_boton(Boton):
        Boton.configure(bg="gray")

    cambio_boton(boton_seguro)


def ventana_de_juego():
    global texto

    #region creacion y configuracion de la ventana
    ventana = Tk()

    # titulo
    ventana.title("KAKURO")

    # se le da tamaño a la ventana principal
    ventana.geometry("900x900")
    # color a la ventana principal
    ventana.configure(bg="gray70")

    #imagen = PhotoImage(file="fondo_jugar.png")
    #fondo = Label(ventana, image=imagen).place(x=0, y=0)
    etiqueta = Label(ventana, text="KAKURO", bg="gray29",fg= "white", padx=100, pady=5, font="Helvetica 25",relief="solid").place(x=275, y=5)
    # se agrega un icono personalizado
    #ventana.iconbitmap(r'C:\Users\Jhonny Diaz\PycharmProjects\Programa 2\icono.ico')

    ventana.resizable(False, False)
    #endregion

    #region Panel de botones
    boton0 = Button(ventana, width=5, height=2, bg='snow', text='1', activebackground='snow',command=lambda: PanelSeleccion('snow', '1', boton0, lista_panel_de_seleccion))
    boton0.place(x=850, y=70)

    boton1 = Button(ventana, width=5, height=2, bg='snow', text='2', activebackground='snow',command=lambda: PanelSeleccion('snow', '2', boton1, lista_panel_de_seleccion))
    boton1.place(x=850, y=120)

    boton2 = Button(ventana, width=5, height=2, bg='snow', text='3', activebackground='snow',command=lambda: PanelSeleccion('snow', '3', boton2, lista_panel_de_seleccion))
    boton2.place(x=850, y=170)

    boton3 = Button(ventana, width=5, height=2, bg='snow', text='4', activebackground='snow',command=lambda: PanelSeleccion('snow', '4',boton3, lista_panel_de_seleccion))
    boton3.place(x=850, y=220)

    boton4 = Button(ventana, width=5, height=2, bg='snow', text='5', activebackground='snow',command=lambda: PanelSeleccion('snow', '5',boton4, lista_panel_de_seleccion))
    boton4.place(x=850, y=270)

    boton5 = Button(ventana, width=5, height=2, bg='snow', text='6', activebackground='snow',command=lambda: PanelSeleccion('snow', '6',boton5, lista_panel_de_seleccion))
    boton5.place(x=850, y=320)

    boton6 = Button(ventana, width=5, height=2, bg='snow', text='7', activebackground='snow',command=lambda: PanelSeleccion('snow', '7',boton6, lista_panel_de_seleccion))
    boton6.place(x=850, y=370)

    boton7 = Button(ventana, width=5, height=2, bg='snow', text='8', activebackground='snow', command=lambda: PanelSeleccion('snow', '8',boton7, lista_panel_de_seleccion))
    boton7.place(x=850, y=420)

    boton8 = Button(ventana, width=5, height=2, bg='snow', text='9', activebackground='snow',command=lambda: PanelSeleccion('snow', '9',boton8, lista_panel_de_seleccion ))
    boton8.place(x=850, y=470)

    #Creacion de una lista global con los botones para que se mantenga un color sobre el boton que se tiene seleccionado
    global lista_panel_de_seleccion
    lista_panel_de_seleccion = [boton0, boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8]
    #endregion

    #region botones de juego
    #region COLUMNA 1
    boton_juego1x1 = Button(ventana, width=4, height=2, command=lambda :cambio_boton(boton_juego1x1, texto))
    boton_juego1x1.place(x=100, y=100)

    boton_juego1x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego1x2, texto))
    boton_juego1x2.place(x=100, y=142)

    boton_juego1x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego1x3, texto))
    boton_juego1x3.place(x=100, y=184)

    boton_juego1x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego1x4, texto))
    boton_juego1x4.place(x=100, y=226)

    boton_juego1x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego1x5, texto))
    boton_juego1x5.place(x=100, y=268)

    boton_juego1x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego1x6, texto))
    boton_juego1x6.place(x=100, y=310)

    boton_juego1x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego1x7, texto))
    boton_juego1x7.place(x=100, y=352)

    boton_juego1x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego1x8, texto))
    boton_juego1x8.place(x=100, y=394)

    boton_juego1x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego1x9, texto))
    boton_juego1x9.place(x=100, y=436)
    #endregion

    # region COLUMNA 2
    boton_juego2x1 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x1, texto))
    boton_juego2x1.place(x=140, y=100)

    boton_juego2x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x2, texto))
    boton_juego2x2.place(x=140, y=142)

    boton_juego2x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x3, texto))
    boton_juego2x3.place(x=140, y=184)

    boton_juego2x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x4, texto))
    boton_juego2x4.place(x=140, y=226)

    boton_juego2x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x5, texto))
    boton_juego2x5.place(x=140, y=268)

    boton_juego2x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x6, texto))
    boton_juego2x6.place(x=140, y=310)

    boton_juego2x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x7, texto))
    boton_juego2x7.place(x=140, y=352)

    boton_juego2x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x8, texto))
    boton_juego2x8.place(x=140, y=394)

    boton_juego2x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x9, texto))
    boton_juego2x9.place(x=140, y=436)
    # endregion

    # region COLUMNA 3
    boton_juego3x1 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x1, texto))
    boton_juego3x1.place(x=180, y=100)

    boton_juego3x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x2, texto))
    boton_juego3x2.place(x=180, y=142)

    boton_juego3x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x3, texto))
    boton_juego3x3.place(x=180, y=184)

    boton_juego3x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x4, texto))
    boton_juego3x4.place(x=180, y=226)

    boton_juego3x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x5, texto))
    boton_juego3x5.place(x=180, y=268)

    boton_juego3x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x6, texto))
    boton_juego3x6.place(x=180, y=310)

    boton_juego3x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x7, texto))
    boton_juego3x7.place(x=180, y=352)

    boton_juego3x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x8, texto))
    boton_juego3x8.place(x=180, y=394)

    boton_juego3x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x9, texto))
    boton_juego3x9.place(x=180, y=436)
    # endregion

    # region COLUMNA 4
    boton_juego4x1 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x1, texto))
    boton_juego4x1.place(x=220, y=100)

    boton_juego4x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x2, texto))
    boton_juego4x2.place(x=220, y=142)

    boton_juego4x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x3, texto))
    boton_juego4x3.place(x=220, y=184)

    boton_juego4x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x4, texto))
    boton_juego4x4.place(x=220, y=226)

    boton_juego4x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x5, texto))
    boton_juego4x5.place(x=220, y=268)

    boton_juego4x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x6, texto))
    boton_juego4x6.place(x=220, y=310)

    boton_juego4x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x7, texto))
    boton_juego4x7.place(x=220, y=352)

    boton_juego4x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x8, texto))
    boton_juego4x8.place(x=220, y=394)

    boton_juego4x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x9, texto))
    boton_juego4x9.place(x=220, y=436)
    # endregion

    # region COLUMNA 5
    boton_juego5x1 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x1, texto))
    boton_juego5x1.place(x=260, y=100)

    boton_juego5x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x2, texto))
    boton_juego5x2.place(x=260, y=142)

    boton_juego5x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x3, texto))
    boton_juego5x3.place(x=260, y=184)

    boton_juego5x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x4, texto))
    boton_juego5x4.place(x=260, y=226)

    boton_juego5x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x5, texto))
    boton_juego5x5.place(x=260, y=268)

    boton_juego5x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x6, texto))
    boton_juego5x6.place(x=260, y=310)

    boton_juego5x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x7, texto))
    boton_juego5x7.place(x=260, y=352)

    boton_juego5x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x8, texto))
    boton_juego5x8.place(x=260, y=394)

    boton_juego5x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x9, texto))
    boton_juego5x9.place(x=260, y=436)
    # endregion

    # region COLUMNA 6
    boton_juego6x1 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x1, texto))
    boton_juego6x1.place(x=300, y=100)

    boton_juego6x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x2, texto))
    boton_juego6x2.place(x=300, y=142)

    boton_juego6x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x3, texto))
    boton_juego6x3.place(x=300, y=184)

    boton_juego6x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x4, texto))
    boton_juego6x4.place(x=300, y=226)

    boton_juego6x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x5, texto))
    boton_juego6x5.place(x=300, y=268)

    boton_juego6x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x6, texto))
    boton_juego6x6.place(x=300, y=310)

    boton_juego6x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x7, texto))
    boton_juego6x7.place(x=300, y=352)

    boton_juego6x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x8, texto))
    boton_juego6x8.place(x=300, y=394)

    boton_juego6x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x9, texto))
    boton_juego6x9.place(x=300, y=436)
    # endregion

    # region COLUMNA 7
    boton_juego7x1 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x1, texto))
    boton_juego7x1.place(x=340, y=100)

    boton_juego7x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x2, texto))
    boton_juego7x2.place(x=340, y=142)

    boton_juego7x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x3, texto))
    boton_juego7x3.place(x=340, y=184)

    boton_juego7x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x4, texto))
    boton_juego7x4.place(x=340, y=226)

    boton_juego7x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x5, texto))
    boton_juego7x5.place(x=340, y=268)

    boton_juego7x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x6, texto))
    boton_juego7x6.place(x=340, y=310)

    boton_juego7x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x7, texto))
    boton_juego7x7.place(x=340, y=352)

    boton_juego7x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x8, texto))
    boton_juego7x8.place(x=340, y=394)

    boton_juego7x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x9, texto))
    boton_juego7x9.place(x=340, y=436)
    # endregion

    # region COLUMNA 8
    boton_juego8x1 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x1, texto))
    boton_juego8x1.place(x=380, y=100)

    boton_juego8x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x2, texto))
    boton_juego8x2.place(x=380, y=142)

    boton_juego8x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x3, texto))
    boton_juego8x3.place(x=380, y=184)

    boton_juego8x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x4, texto))
    boton_juego8x4.place(x=380, y=226)

    boton_juego8x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x5, texto))
    boton_juego8x5.place(x=380, y=268)

    boton_juego8x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x6, texto))
    boton_juego8x6.place(x=380, y=310)

    boton_juego8x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x7, texto))
    boton_juego8x7.place(x=380, y=352)

    boton_juego8x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x8, texto))
    boton_juego8x8.place(x=380, y=394)

    boton_juego8x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x9, texto))
    boton_juego8x9.place(x=380, y=436)
    # endregio
    #endregion

    # region COLUMNA 9
    boton_juego9x1 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x1, texto))
    boton_juego9x1.place(x=420, y=100)

    boton_juego9x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x2, texto))
    boton_juego9x2.place(x=420, y=142)

    boton_juego9x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x3, texto))
    boton_juego9x3.place(x=420, y=184)

    boton_juego9x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x4, texto))
    boton_juego9x4.place(x=420, y=226)

    boton_juego9x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x5, texto))
    boton_juego9x5.place(x=420, y=268)

    boton_juego9x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x6, texto))
    boton_juego9x6.place(x=420, y=310)

    boton_juego9x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x7, texto))
    boton_juego9x7.place(x=420, y=352)

    boton_juego9x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x8, texto))
    boton_juego9x8.place(x=420, y=394)

    boton_juego9x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x9, texto))
    boton_juego9x9.place(x=420, y=436)
    # endregion
    #endregion


    ventana.mainloop()

ventana_de_juego()