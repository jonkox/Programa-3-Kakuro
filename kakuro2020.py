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
boton_actual = []
borrar = False
reloj = 0
nivel = 1
partida_guardada = []
botones_por_columna = []
botones_por_fila = []



"""Funcion cambio boton: esta funcion tiene como tarea hacer que el boton seleccionado para asiganarle un valor para hacer una jugada se cambie, si se le asigna un valor vacio se retorna un error."""
def cambio_boton(Boton, jugada):
    global texto, lista_jugadas, boton_actual, borrar
    jugada = []
    jugada.append(Boton)
    jugada.append(Boton["text"])
    jugada.append(texto)
    if jugada not in lista_jugadas:
        lista_jugadas.append(jugada)


    #Con esta condicional se valida si lo que se quiere hacer es borrar una casilla o no
    if borrar == True:
        print(Boton["text"])
        if validar_texto(Boton) == False:
            messagebox.showinfo(title="ERROR", message="LA CASILLA NO SE PUEDE ELIMINAR")
            borrar = False

        else:
            Boton.configure(text="")
            borrar = False
            print(borrar)
        return

    #Valida que se haya seleccionado un boton del panel antes de configurar el boton
    if texto == '':
        ''' MessageBox
        -showinfo(), showerror(), showwarning(), askquestion(), askcancel(), askyesno(), askretrycancel()'''
        messagebox.showerror(message='Debe seleccionar un boton del panel de seleccion')
    else:
        Boton.configure(text=texto)
        boton_actual.insert(0,Boton)
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

def validar_texto(boton):
    if boton["text"] == "":
        return False
    return True

def deshacer_jugada(lista_jugadas, lista_eliminados):
    global texto
    lista_jugadas[-1][0].configure(text=lista_jugadas[-1][1])
    lista_eliminados.append(lista_jugadas[-1])
    lista_jugadas.pop()

"""Funcion ayuda manual: esta funcion muestra el manual de usuario donde se explica como funciona el juego."""
def ayuda_manual():

    wb.open_new(r"C:\Users\Jhonny Diaz\PycharmProjects\Programa 3 Kakuro\manual_de_usuario_kakuro2020.pdf")

def rehacer_jugada(lista_jugadas, lista_eliminados):
    lista_eliminados[-1][0].configure(text=lista_eliminados[-1][2])

    lista_jugadas.append(lista_eliminados[-1])
    lista_eliminados.pop()

def ventana_de_juego(ventana_menu):
    ventana_menu.withdraw()

    global texto



    #region creacion y configuracion de la ventana
    ventana = Tk()

    # titulo
    ventana.title("KAKURO")

    # se le da tamaño a la ventana principal
    ventana.geometry("700x800")
    # color a la ventana principal
    ventana.configure(bg="gray70")

    etiqueta = Label(ventana, text="KAKURO", bg="gray29",fg= "white", padx=100, pady=5, font="Helvetica 25",relief="solid").place(x=200, y=5)
    # se agrega un icono personalizado
    #ventana.iconbitmap(r'C:\Users\Jhonny Diaz\PycharmProjects\Programa 2\icono.ico')

    ventana.resizable(False, False)

    if nivel == 1:
        lbl_nivel = Label(ventana, text="Nivel: Fácil", bg="gray29",fg= "white", padx=10, pady=5, font="Helvetica 25",relief="solid").place(x=100, y=650)

    if nivel == 2:
        lbl_nivel = Label(ventana, text="Nivel: Medio", bg="gray29",fg= "white", padx=10, pady=5, font="Helvetica 25",relief="solid").place(x=100, y=650)

    if nivel == 3:
        lbl_nivel = Label(ventana, text="Nivel: Difícil", bg="gray29",fg= "white", padx=10, pady=5, font="Helvetica 25",relief="solid").place(x=100, y=650)
    #endregion

    #region Panel de botones
    boton0 = Button(ventana, width=5, height=2, bg='snow', text='1', activebackground='snow',command=lambda: PanelSeleccion('snow', '1', boton0, lista_panel_de_seleccion))
    boton0.place(x=600, y=70)

    boton1 = Button(ventana, width=5, height=2, bg='snow', text='2', activebackground='snow',command=lambda: PanelSeleccion('snow', '2', boton1, lista_panel_de_seleccion))
    boton1.place(x=600, y=120)

    boton2 = Button(ventana, width=5, height=2, bg='snow', text='3', activebackground='snow',command=lambda: PanelSeleccion('snow', '3', boton2, lista_panel_de_seleccion))
    boton2.place(x=600, y=170)

    boton3 = Button(ventana, width=5, height=2, bg='snow', text='4', activebackground='snow',command=lambda: PanelSeleccion('snow', '4',boton3, lista_panel_de_seleccion))
    boton3.place(x=600, y=220)

    boton4 = Button(ventana, width=5, height=2, bg='snow', text='5', activebackground='snow',command=lambda: PanelSeleccion('snow', '5',boton4, lista_panel_de_seleccion))
    boton4.place(x=600, y=270)

    boton5 = Button(ventana, width=5, height=2, bg='snow', text='6', activebackground='snow',command=lambda: PanelSeleccion('snow', '6',boton5, lista_panel_de_seleccion))
    boton5.place(x=600, y=320)

    boton6 = Button(ventana, width=5, height=2, bg='snow', text='7', activebackground='snow',command=lambda: PanelSeleccion('snow', '7',boton6, lista_panel_de_seleccion))
    boton6.place(x=600, y=370)

    boton7 = Button(ventana, width=5, height=2, bg='snow', text='8', activebackground='snow', command=lambda: PanelSeleccion('snow', '8',boton7, lista_panel_de_seleccion))
    boton7.place(x=600, y=420)

    boton8 = Button(ventana, width=5, height=2, bg='snow', text='9', activebackground='snow',command=lambda: PanelSeleccion('snow', '9',boton8, lista_panel_de_seleccion ))
    boton8.place(x=600, y=470)

    #Creacion de una lista global con los botones para que se mantenga un color sobre el boton que se tiene seleccionado
    global lista_panel_de_seleccion
    lista_panel_de_seleccion = [boton0, boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8]
    #endregion

    #region botones de juego
    global lista_botones_de_juego
    lista_botones_de_juego = []



    #region COLUMNA 1
    boton_juego1x1 = Button(ventana, width=4,bg="black",state="disabled", height=2,text="", command=lambda :cambio_boton(boton_juego1x1, texto))
    boton_juego1x1.place(x=100, y=100)
    lista_botones_de_juego.append(boton_juego1x1)

    boton_juego1x2 = Button(ventana, width=4, height=2,bg="black",state="disabled", command=lambda: cambio_boton(boton_juego1x2, texto))
    boton_juego1x2.place(x=100, y=142)
    lista_botones_de_juego.append(boton_juego1x2)

    boton_juego1x3 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego1x3, texto))
    boton_juego1x3.place(x=100, y=184)
    lista_botones_de_juego.append(boton_juego1x3)

    boton_juego1x4 = Button(ventana, width=4, height=2, bg="black",state="disabled", text="12",fg="white", command=lambda: cambio_boton(boton_juego1x4, texto))
    boton_juego1x4.place(x=100, y=226)
    lista_botones_de_juego.append(boton_juego1x4)

    boton_juego1x5 = Button(ventana, width=4, height=2, bg="black",state="disabled", text="3",fg="white",command=lambda: cambio_boton(boton_juego1x5, texto))
    boton_juego1x5.place(x=100, y=268)
    lista_botones_de_juego.append(boton_juego1x5)

    boton_juego1x6 = Button(ventana, width=4, height=2, bg="black",state="disabled", text="17",fg="white", command=lambda: cambio_boton(boton_juego1x6, texto))
    boton_juego1x6.place(x=100, y=310)
    lista_botones_de_juego.append(boton_juego1x6)

    boton_juego1x7 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego1x7, texto))
    boton_juego1x7.place(x=100, y=352)
    lista_botones_de_juego.append(boton_juego1x7)

    boton_juego1x8 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="28",fg="white", command=lambda: cambio_boton(boton_juego1x8, texto))
    boton_juego1x8.place(x=100, y=394)
    lista_botones_de_juego.append(boton_juego1x8)

    boton_juego1x9 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="6",fg="white", command=lambda: cambio_boton(boton_juego1x9, texto))
    boton_juego1x9.place(x=100, y=436)
    lista_botones_de_juego.append(boton_juego1x9)
    #endregion

    # region COLUMNA 2
    boton_juego2x1 = Button(ventana, width=4, height=2,bg="black",state="disabled", command=lambda: cambio_boton(boton_juego2x1, texto))
    boton_juego2x1.place(x=140, y=100)
    lista_botones_de_juego.append(boton_juego2x1)

    boton_juego2x2 = Button(ventana, width=4, height=2,bg="black",state="disabled", text="14\n     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego2x2, texto))
    boton_juego2x2.place(x=140, y=142)
    lista_botones_de_juego.append(boton_juego2x2)

    boton_juego2x3 = Button(ventana, width=4, height=2,bg="black",state="disabled", text="36\n7     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego2x3, texto))
    boton_juego2x3.place(x=140, y=184)
    lista_botones_de_juego.append(boton_juego2x3)

    boton_juego2x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x4, texto))
    boton_juego2x4.place(x=140, y=226)
    lista_botones_de_juego.append(boton_juego2x4)

    boton_juego2x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x5, texto))
    boton_juego2x5.place(x=140, y=268)
    lista_botones_de_juego.append(boton_juego2x5)

    boton_juego2x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x6, texto))
    boton_juego2x6.place(x=140, y=310)
    lista_botones_de_juego.append(boton_juego2x6)

    boton_juego2x7 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="   \n7     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego2x7, texto))
    boton_juego2x7.place(x=140, y=352)
    lista_botones_de_juego.append(boton_juego2x7)

    boton_juego2x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x8, texto))
    boton_juego2x8.place(x=140, y=394)
    lista_botones_de_juego.append(boton_juego2x8)

    boton_juego2x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego2x9, texto))
    boton_juego2x9.place(x=140, y=436)
    lista_botones_de_juego.append(boton_juego2x9)
    # endregion

    # region COLUMNA 3
    boton_juego3x1 = Button(ventana, width=4, height=2,bg="black",state="disabled", text="   \n19     ",fg="white",justify="right",  command=lambda: cambio_boton(boton_juego3x1, texto))
    boton_juego3x1.place(x=180, y=100)
    lista_botones_de_juego.append(boton_juego3x1)

    boton_juego3x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x2, texto))
    boton_juego3x2.place(x=180, y=142)
    lista_botones_de_juego.append(boton_juego3x2)

    boton_juego3x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x3, texto))
    boton_juego3x3.place(x=180, y=184)
    lista_botones_de_juego.append(boton_juego3x3)

    boton_juego3x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x4, texto))
    boton_juego3x4.place(x=180, y=226)
    lista_botones_de_juego.append(boton_juego3x4)

    boton_juego3x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x5, texto))
    boton_juego3x5.place(x=180, y=268)
    lista_botones_de_juego.append(boton_juego3x5)

    boton_juego3x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x6, texto))
    boton_juego3x6.place(x=180, y=310)
    lista_botones_de_juego.append(boton_juego3x6)

    boton_juego3x7 = Button(ventana, width=4, height=2,bg="black",state="disabled",text="13\n7     ",fg="white",justify="right",  command=lambda: cambio_boton(boton_juego3x7, texto))
    boton_juego3x7.place(x=180, y=352)
    lista_botones_de_juego.append(boton_juego3x7)

    boton_juego3x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x8, texto))
    boton_juego3x8.place(x=180, y=394)
    lista_botones_de_juego.append(boton_juego3x8)

    boton_juego3x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego3x9, texto))
    boton_juego3x9.place(x=180, y=436)
    lista_botones_de_juego.append(boton_juego3x9)
    # endregion

    # region COLUMNA 4
    boton_juego4x1 = Button(ventana, width=4, height=2,bg="black",state="disabled",text="   \n12     ",fg="white",justify="right",  command=lambda: cambio_boton(boton_juego4x1, texto))
    boton_juego4x1.place(x=220, y=100)
    lista_botones_de_juego.append(boton_juego4x1)

    boton_juego4x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x2, texto))
    boton_juego4x2.place(x=220, y=142)
    lista_botones_de_juego.append(boton_juego4x2)

    boton_juego4x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x3, texto))
    boton_juego4x3.place(x=220, y=184)
    lista_botones_de_juego.append(boton_juego4x3)

    boton_juego4x4 = Button(ventana, width=4, height=2,bg="black",state="disabled",text="10\n       ",fg="white",justify="right",  command=lambda: cambio_boton(boton_juego4x4, texto))
    boton_juego4x4.place(x=220, y=226)
    lista_botones_de_juego.append(boton_juego4x4)

    boton_juego4x5 = Button(ventana, width=4, height=2,bg="black",state="disabled",text="    \n20     ",fg="white",justify="right",  command=lambda: cambio_boton(boton_juego4x5, texto))
    boton_juego4x5.place(x=220, y=268)
    lista_botones_de_juego.append(boton_juego4x5)

    boton_juego4x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x6, texto))
    boton_juego4x6.place(x=220, y=310)
    lista_botones_de_juego.append(boton_juego4x6)

    boton_juego4x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x7, texto))
    boton_juego4x7.place(x=220, y=352)
    lista_botones_de_juego.append(boton_juego4x7)

    boton_juego4x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego4x8, texto))
    boton_juego4x8.place(x=220, y=394)
    lista_botones_de_juego.append(boton_juego4x8)

    boton_juego4x9 = Button(ventana, width=4, height=2, bg="black",state="disabled",command=lambda: cambio_boton(boton_juego4x9, texto))
    boton_juego4x9.place(x=220, y=436)
    lista_botones_de_juego.append(boton_juego4x9)
    # endregion

    # region COLUMNA 5
    boton_juego5x1 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego5x1, texto))
    boton_juego5x1.place(x=260, y=100)
    lista_botones_de_juego.append(boton_juego5x1)

    boton_juego5x2 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="    \n4     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego5x2, texto))
    boton_juego5x2.place(x=260, y=142)
    lista_botones_de_juego.append(boton_juego5x2)

    boton_juego5x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x3, texto))
    boton_juego5x3.place(x=260, y=184)
    lista_botones_de_juego.append(boton_juego5x3)

    boton_juego5x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x4, texto))
    boton_juego5x4.place(x=260, y=226)
    lista_botones_de_juego.append(boton_juego5x4)

    boton_juego5x5 = Button(ventana, width=4, height=2,bg="black",state="disabled",text="20\n11     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego5x5, texto))
    boton_juego5x5.place(x=260, y=268)
    lista_botones_de_juego.append(boton_juego5x5)

    boton_juego5x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x6, texto))
    boton_juego5x6.place(x=260, y=310)
    lista_botones_de_juego.append(boton_juego5x6)

    boton_juego5x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x7, texto))
    boton_juego5x7.place(x=260, y=352)
    lista_botones_de_juego.append(boton_juego5x7)

    boton_juego5x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego5x8, texto))
    boton_juego5x8.place(x=260, y=394)
    lista_botones_de_juego.append(boton_juego5x8)

    boton_juego5x9 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego5x9, texto))
    boton_juego5x9.place(x=260, y=436)
    lista_botones_de_juego.append(boton_juego5x9)
    # endregion

    # region COLUMNA 6
    boton_juego6x1 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego6x1, texto))
    boton_juego6x1.place(x=300, y=100)
    lista_botones_de_juego.append(boton_juego6x1)

    boton_juego6x2 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="    \n11     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego6x2, texto))
    boton_juego6x2.place(x=300, y=142)
    lista_botones_de_juego.append(boton_juego6x2)

    boton_juego6x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x3, texto))
    boton_juego6x3.place(x=300, y=184)
    lista_botones_de_juego.append(boton_juego6x3)

    boton_juego6x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x4, texto))
    boton_juego6x4.place(x=300, y=226)
    lista_botones_de_juego.append(boton_juego6x4)

    boton_juego6x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x5, texto))
    boton_juego6x5.place(x=300, y=268)
    lista_botones_de_juego.append(boton_juego6x5)

    boton_juego6x6 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="    \n8     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego6x6, texto))
    boton_juego6x6.place(x=300, y=310)
    lista_botones_de_juego.append(boton_juego6x6)

    boton_juego6x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x7, texto))
    boton_juego6x7.place(x=300, y=352)
    lista_botones_de_juego.append(boton_juego6x7)

    boton_juego6x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego6x8, texto))
    boton_juego6x8.place(x=300, y=394)
    lista_botones_de_juego.append(boton_juego6x8)

    boton_juego6x9 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="   8\n       ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego6x9, texto))
    boton_juego6x9.place(x=300, y=436)
    lista_botones_de_juego.append(boton_juego6x9)
    # endregion

    # region COLUMNA 7
    boton_juego7x1 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego7x1, texto))
    boton_juego7x1.place(x=340, y=100)
    lista_botones_de_juego.append(boton_juego7x1)

    boton_juego7x2 = Button(ventana, width=4, height=2,bg="black",state="disabled",text="   4\n17     ",fg="white",justify="right",  command=lambda: cambio_boton(boton_juego7x2, texto))
    boton_juego7x2.place(x=340, y=142)
    lista_botones_de_juego.append(boton_juego7x2)

    boton_juego7x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x3, texto))
    boton_juego7x3.place(x=340, y=184)
    lista_botones_de_juego.append(boton_juego7x3)

    boton_juego7x4 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x4, texto))
    boton_juego7x4.place(x=340, y=226)
    lista_botones_de_juego.append(boton_juego7x4)

    boton_juego7x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x5, texto))
    boton_juego7x5.place(x=340, y=268)
    lista_botones_de_juego.append(boton_juego7x5)

    boton_juego7x6 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="    6\n     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego7x6, texto))
    boton_juego7x6.place(x=340, y=310)
    lista_botones_de_juego.append(boton_juego7x6)

    boton_juego7x7 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="   10\n4     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego7x7, texto))
    boton_juego7x7.place(x=340, y=352)
    lista_botones_de_juego.append(boton_juego7x7)

    boton_juego7x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x8, texto))
    boton_juego7x8.place(x=340, y=394)
    lista_botones_de_juego.append(boton_juego7x8)

    boton_juego7x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego7x9, texto))
    boton_juego7x9.place(x=340, y=436)
    lista_botones_de_juego.append(boton_juego7x9)
    # endregion

    # region COLUMNA 8
    boton_juego8x1 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="    \n7     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego8x1, texto))
    boton_juego8x1.place(x=380, y=100)
    lista_botones_de_juego.append(boton_juego8x1)

    boton_juego8x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x2, texto))
    boton_juego8x2.place(x=380, y=142)
    lista_botones_de_juego.append(boton_juego8x2)

    boton_juego8x3 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x3, texto))
    boton_juego8x3.place(x=380, y=184)
    lista_botones_de_juego.append(boton_juego8x3)

    boton_juego8x4 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="   \n25     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego8x4, texto))
    boton_juego8x4.place(x=380, y=226)
    lista_botones_de_juego.append(boton_juego8x4)

    boton_juego8x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x5, texto))
    boton_juego8x5.place(x=380, y=268)
    lista_botones_de_juego.append(boton_juego8x5)

    boton_juego8x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x6, texto))
    boton_juego8x6.place(x=380, y=310)
    lista_botones_de_juego.append(boton_juego8x6)

    boton_juego8x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x7, texto))
    boton_juego8x7.place(x=380, y=352)
    lista_botones_de_juego.append(boton_juego8x7)

    boton_juego8x8 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x8, texto))
    boton_juego8x8.place(x=380, y=394)
    lista_botones_de_juego.append(boton_juego8x8)

    boton_juego8x9 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego8x9, texto))
    boton_juego8x9.place(x=380, y=436)
    lista_botones_de_juego.append(boton_juego8x9)
    # endregion

    # region COLUMNA 9
    boton_juego9x1 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="   \n10     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego9x1, texto))
    boton_juego9x1.place(x=420, y=100)
    lista_botones_de_juego.append(boton_juego9x1)

    boton_juego9x2 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x2, texto))
    boton_juego9x2.place(x=420, y=142)
    lista_botones_de_juego.append(boton_juego9x2)

    boton_juego9x3 = Button(ventana, width=4, height=2,  command=lambda: cambio_boton(boton_juego9x3, texto))
    boton_juego9x3.place(x=420, y=184)
    lista_botones_de_juego.append(boton_juego9x3)

    boton_juego9x4 = Button(ventana, width=4, height=2, bg="black",state="disabled", text="   \n14     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego9x4, texto))
    boton_juego9x4.place(x=420, y=226)
    lista_botones_de_juego.append(boton_juego9x4)

    boton_juego9x5 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x5, texto))
    boton_juego9x5.place(x=420, y=268)
    lista_botones_de_juego.append(boton_juego9x5)

    boton_juego9x6 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x6, texto))
    boton_juego9x6.place(x=420, y=310)
    lista_botones_de_juego.append(boton_juego9x6)

    boton_juego9x7 = Button(ventana, width=4, height=2, command=lambda: cambio_boton(boton_juego9x7, texto))
    boton_juego9x7.place(x=420, y=352)
    lista_botones_de_juego.append(boton_juego9x7)

    boton_juego9x8 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego9x8, texto))
    boton_juego9x8.place(x=420, y=394)
    lista_botones_de_juego.append(boton_juego9x8)

    boton_juego9x9 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego9x9, texto))
    boton_juego9x9.place(x=420, y=436)
    lista_botones_de_juego.append(boton_juego9x9)
    # endregion


    #endregion

    #region Botones principales
    boton_iniciar_juego = Button(ventana, width=15, height=2, text="INICIAR JUEGO", command=1)
    boton_iniciar_juego.place(x=100, y=500)

    boton_deshacer_jugada = Button(ventana, width=15, height=2, text="DESHACER JUGADA", command=lambda : deshacer_jugada(lista_jugadas, lista_eliminados))
    boton_deshacer_jugada.place(x=100, y=550)

    boton_rehacer_jugada = Button(ventana, width=15, height=2, text="REHACER JUGADA", command= lambda : rehacer_jugada(lista_jugadas, lista_eliminados))
    boton_rehacer_jugada.place(x=100, y=600)

    boton_borrar_casilla = Button(ventana, width=15, height=2, text="BORRAR CASILLA", command=lambda: borrar_casilla())
    boton_borrar_casilla.place(x=250, y=500)

    boton_borrar_juego = Button(ventana, width=15, height=2,text="BORRAR JUEGO", command= lambda : borrar_juego(lista_botones_de_juego))
    boton_borrar_juego.place(x=250,y=550)

    boton_terminar_partida = Button(ventana, width=15, height=2,text="TERMINAR JUEGO", command= lambda : terminar_juego(ventana))
    boton_terminar_partida.place(x=250,y=600)

    boton_top10 = Button(ventana, width=15, height=2, text="TOP 10", command=1)
    boton_top10.place(x=400, y=500)

    boton_guardar_juego = Button(ventana, width=15, height=2, text="GUARDAR JUEGO", command=lambda : guardar_juego(lista_jugadas, ventana_menu, ventana))
    boton_guardar_juego.place(x=400, y=550)

    boton_cargar_juego = Button(ventana, width=15, height=2, text="CARGAR JUEGO", command= lambda : cargar_juego(partida_guardada))
    boton_cargar_juego.place(x=400, y=600)
    #endregion



    ventana.mainloop()

def pantalla_menu():
    # region creacion y configuracion de la ventana
    global ventana_menu
    ventana_menu = Tk()

    # titulo
    ventana_menu.title("KAKURO")

    # se le da tamaño a la ventana principal
    ventana_menu.geometry("500x600")
    # color a la ventana principal
    ventana_menu.configure(bg="gray70")

    etiqueta = Label(ventana_menu, text="KAKURO", bg="gray29", fg="white", padx=100, pady=5, font="Helvetica 25", relief="solid").place(x=85, y=5)

    #endregion

    #region Botones de opcion
    boton_iniciar_juego = Button(ventana_menu, width=15, height=2,text="INICIAR JUEGO",bd=15, command= lambda : ventana_de_juego(ventana_menu))
    boton_iniciar_juego.place(x=200,y=100)


    boton_configuracion = Button(ventana_menu, width=15, height=2,text="CONFIGURACION",bd=15, command= lambda : configuracion(ventana_menu))
    boton_configuracion.place(x=200,y=200)

    boton_ayuda = Button(ventana_menu, width=15, height=2,text="AYUDA",bd=15, command= lambda : ayuda_manual())
    boton_ayuda.place(x=200,y=300)

    boton_acerca_de = Button(ventana_menu, width=15, height=2,text="ACERCA DE:",bd=15, command= lambda :acerca_de(ventana_menu))
    boton_acerca_de.place(x=200,y=400)

    boton_salir = Button(ventana_menu, width=15, height=2,text="SALIR",bd=15, command= lambda : salir(ventana_menu))
    boton_salir.place(x=200,y=500)
    #endregion

    ventana_menu.mainloop()

def acerca_de(ventana_menu):
    ventana_menu.withdraw()

    acerca = Tk()
    # titulo
    ventana_menu.title("KAKURO")

    # se le da tamaño a la ventana principal
    ventana_menu.geometry("700x800")
    # color a la ventana principal
    ventana_menu.configure(bg="gray70")
    # Titulo


    lbl = Label(acerca, text="Acerca De", bg="green", fg="white", font=("Aharoni", 30), \
                bd=1, relief="solid").pack()

    lbl2 = Label(acerca,
                 text="Nombre del Programa: KAKURO\n Version: 1.0\n Fecha de creacion: 27/01/2021 \n Autor del Programa: Jhonny Andrés Díaz Coto",
                 bg="white", fg="Black", font=("Aharoni", 30)).pack()

    # Boton para salir
    btn5 = Button(acerca, bitmap="error", command= lambda : atras(acerca, ventana_menu))
    btn5.place(x=800, y=10)

    acerca.mainloop()

def guardar_juego(lista_jugadas, venatana_menu, ventana_juego):
    global partida_guardada, lista_eliminados
    partida_guardada = lista_jugadas[:]
    seleccion = messagebox.askyesno(title="SEGUIR JUGANDO", message="¿DESEA SEGUIR JUGANDO?")
    if seleccion == False:
        lista_jugadas = []
        lista_eliminados = []
        venatana_menu.state(newstate="normal")
        ventana_juego.destroy()

def cargar_juego(partida_guardada):
    global lista_botones_de_juego
    for i in partida_guardada:
        valor = i[2]
        i[0].configure(text=valor)

def atras(ventana_destruir, ventanar_recuperar):
    ventanar_recuperar.state(newstate="normal")
    ventana_destruir.destroy()

def configuracion(ventana_menu):
    ventana_menu.withdraw()

    # region creacion y configuracion de la ventana
    ventana = Tk()

    # titulo
    ventana.title("CONFIGURACION")

    # se le da tamaño a la ventana principal
    ventana.geometry("565x450")
    # color a la ventana principal
    ventana.configure(bg="gray70")

    etiqueta = Label(ventana, text="KAKURO", bg="gray29",fg= "white", padx=100, pady=5, font="Helvetica 25",relief="solid").place(x=120, y=5)

    ventana.resizable(False, False)

    #endregion


    # region dificultad
    label_dificultad = Label(ventana, text="Nivel de dificultad:", bg="gray29", fg="white", relief="solid").place(x=20, y=100)

    nivel = IntVar(ventana)

    facil = Radiobutton(ventana, text="Fácil (1 hora)", bg="gray70", variable=nivel, value=1)
    facil.place(x=20, y=140)
    facil.select()

    medio = Radiobutton(ventana, text="Medio (45 minutos)", bg="gray70", variable=nivel, value=2)
    medio.place(x=20, y=160)

    dificil = Radiobutton(ventana, text="Difícil (30 minutos)", bg="gray70", variable=nivel, value=3)
    dificil.place(x=20, y=180)
    # endregion

    # region reloj
    label_reloj = Label(ventana, text="Reloj:", relief="solid", bg="gray29",fg="white").place(x=450, y=100)

    reloj = IntVar(ventana)

    si = Radiobutton(ventana, text="Si", bg="gray70", variable=reloj, value=1)
    si.place(x=400, y=120)

    no = Radiobutton(ventana, text="No", bg="gray70", variable=reloj, value=2)
    no.place(x=400, y=140)
    no.select()

    timer = Radiobutton(ventana, text="Timer", bg="gray70", variable=reloj, value=3)
    timer.place(x=400, y=160)

    #endregion

    agregar_configuraciones = Button(ventana, text="ACEPTAR", bg="gray29", relief="solid", fg="white", command=lambda: agrega_configuracion(ventana_menu, ventana, nivel.get()))
    agregar_configuraciones.place(x=245, y=250)
    ventana.mainloop()

def agrega_configuracion(ventana_menu, ventana, nivel):
    ventana_menu.state(newstate="normal")
    messagebox.showinfo(title="CONFIGURACION", message="LA CONFIGURACION HA SIDO REGISTRADA")
    ventana.destroy()

def salir(ventana):
    seleccion = messagebox.askyesno(title="SALIR", message="¿DESEA SALIR DEL JUEGO?")
    if seleccion == True:
        ventana.destroy()

def borrar_juego(lista_botones):
    global lista_jugadas, lista_eliminados
    seleccion = messagebox.askyesno(title="BORRAR PARTIDA", message="¿DESEA BORRAR LA PARTIDA?")
    if seleccion == True:
        lista_jugadas = []
        lista_eliminados = []
        for i in lista_botones:
            i.configure(text="")

def borrar_casilla():
    global borrar
    borrar = True
    messagebox.showinfo(title="CONFIGURACION", message="SELECCIONE LA CASILLA QUE DESEA ELIMINAR")
    print(borrar)

def terminar_juego(ventana):
    global ventana_menu
    seleccion = messagebox.askyesno(title="TERMINAR PARTIDA", message="¿DESEA TERMINAR EL JUEGO?")
    if seleccion == True:
        ventana.destroy()
        ventana_de_juego(ventana_menu)

pantalla_menu()


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ESPACIO PARA FUNCIONES DE PRUEBA>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
lista = []
def PanelSeleccionPrueba(color_seleccionado, texto_seleccionado):
    global color, texto
    color = color_seleccionado
    texto = texto_seleccionado

def impresion(boton, lista):
    if boton["text"] == "":
        print("PUTA MADRE")


def pruebas():
    ventana = Tk()
    lista_panel_seleccion = []
    boton0 = Button(ventana, width=5, height=2, bg='snow', text='1', activebackground='snow', command=lambda: PanelSeleccionPrueba('snow', '1'))
    boton0.pack()


    boton_juego = Button(ventana, width=4, height=2, command=lambda : print(validar_texto(boton_juego)))
    boton_juego.pack()

    ventana.mainloop()


pruebas()