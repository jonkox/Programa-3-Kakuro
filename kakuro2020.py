"""Programa 3
Kakuro 2021
Jhonny Andres Diaz Coto
Carnet: 2020042119
Link para el repositorio del proyecto: https://github.com/jonkox/Programa-3-Kakuro.git"""

#IMPORTACIONES----------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import pickle # modulo para cargar datos
import random
import copy
import webbrowser as wb
from tkinter import Tk, Label, Button
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
nivel = 0
partida_guardada = []
botones_por_columna = []
botones_por_fila = []
juego_iniciado = False
nombre_jugador = ""
horas = ""
minutos = ""
segundos = ""
lista_columnas = []
lista_filas = []
jugadas_de_partida = []
juego_terminado = False
tiempo_jugado = ""
top10 = [["Jonko", "0:30:50"], ["Daniel", "0:34:40"], ["Bryan", "0:39:02"], ["Gabriel", "0:42:37"], ["Maria", "0:45:15"],
         ["Dolly", "0:55:21"], ["Erick", "0:59:17"], ["Ana", "1:2:27"], ["Kenneth", "1:12:45"], ["Jessica", "1:20:36"]]



"""Funcion acomoda top: esta funcion recibe una lista que contiene el nombre del jugador y el tiempo del juego y ordena de buena manera el top 10 como se debe presentar"""
def acomoda_top(valores):
    global top10
    indice = -1
    if valores[1][0].isdigit() == True:
        horas = int(valores[1][0])

    if valores[1][2].isdigit() == True and valores[1][3].isdigit() == True:
        minutos = int(valores[1][2:4])
        segundos = int(valores[1][5:])
    else:
        minutos = int(valores[1][2])
        segundos = int(valores[1][4:])

    tiempo_en_segundos_nuevo = horas * 3600 + minutos * 60 + segundos

    for i in top10:
        indice += 1

        if i[1][0].isdigit() == True:
            horastop = int(i[1][0])

        if i[1][2].isdigit() == True and i[1][3].isdigit() == True:
            minutostop = int(i[1][2:4])
        else:
            minutostop = int(i[1][2])

        segundostop = int(i[1][5:])

        tiempo_en_segundos_top = (horastop * 3600) + (minutostop * 60) + segundostop

        if tiempo_en_segundos_top > tiempo_en_segundos_nuevo:
            top10.insert(indice, valores)
            top10.pop()
            return

"""Funcion iniciar juego: esta funcion es una de las mas importantes puesto que es la funcion que habilita y deshabilita distintas funciones, esta funcion habilita los botones de juego
y en caso de ser escogido es la funcion que muestra el timer o el cronometro segun se haya escogido"""
def iniciar_juego(ventana, deshacer_jugada, rehacer_jugada, borrar_casilla, borrar_juego, terminar_juego, top10, guardar_juego, validar_nombre, entrada, botones_de_juego):
    global reloj, juego_iniciado, tiempo_jugado, juego_terminado

    #En esta seccion se habilitan los botones necesarios una vez que se inicie el juego
    juego_iniciado = True
    deshacer_jugada.configure(state="normal")
    rehacer_jugada.configure(state="normal")
    borrar_casilla.configure(state="normal")
    borrar_juego.configure(state="normal")
    terminar_juego.configure(state="normal")
    top10.configure(state="normal")
    guardar_juego.configure(state="normal")
    validar_nombre.configure(state="disabled")
    entrada.configure(state="disabled")

    for i in botones_de_juego:
        i.configure(state="normal")

    #Se crea la funcion del cronometro en caso de que el usuario lo escoja
    def crono():
        def iniciar(h=00,m=00,s=00):
            global proceso

            #Validacion para el tiempo
            if s > 59:
                s = 00
                m += 1
                if m > 59:
                    m = 00
                    h += 1
                    if h == 1:
                        messagebox.showinfo(message="SE HA ACABADO SU TIEMPO")
                        ventana_menu.state(newstate="normal")
                        ventana.destroy()
                        juego_iniciado = False
                        contador_jugada = 1


            #Se muestra el tiempo
            time['text'] = str(h) + ":" + str(m) + ":" + str (s)
            tiempo_jugado = time["text"]



            proceso = time.after(1000, iniciar, h, m , (s + 1))

            #Validacion para ver si el usuario ingreso algun tiempo, si no lo hizo se usan los tiempos predeterminados
            if str(horas.get()) == "" and str(minutos.get()) == "" and str(segundos.get()) == "":

                if nivel.get() == 1:

                    tiempo = str(1) + ":" + str(0) + ":" + str(0)

                    if time["text"] == tiempo:
                        parar()
                        messagebox.showinfo(message="LO SENTIMOS, SE ACABO EL TIEMPO")

                if nivel.get() == 2:

                    tiempo = str(0) + ":" + str(45) + ":" + str(0)

                    if time["text"] == tiempo:
                        parar()
                        messagebox.showinfo(message="LO SENTIMOS, SE ACABO EL TIEMPO")

                if nivel.get() == 3:

                    tiempo = str(0) + ":" + str(30) + ":" + str(0)

                    if time["text"] == tiempo:
                        parar()
                        messagebox.showinfo(message="LO SENTIMOS, SE ACABO EL TIEMPO")

            #Si el usuario ingreso un tiempo se le ingresa al cronometro como limite de tiempo
            else:
                tiempo = str(horas.get()) + ":" + str(minutos.get()) + ":" + str(segundos.get())

                if time["text"] == tiempo:
                    parar()
                    messagebox.showinfo(message="LO SENTIMOS, SE ACABO EL TIEMPO")


        def parar():
            global proceso
            time.after_cancel(proceso)

        time = Label(ventana, fg='red', width=10, font=("", "18"))
        time.place(x=20, y=750)

        iniciar()
        if juego_terminado == True:
            parar()


    #Creacion del timer si el usuario lo desea
    def timer():
        #Validacion para ver si el usuario ingreso un tiempo, si no lo hizo se usan los tiempos predeterminados
        if str(horas.get()) == "" and str(minutos.get()) == "" and str(segundos.get()) == "":
            if nivel.get() == 1:
                h=1
                m=0
                s=0


            if nivel.get() == 2:
                h = 0
                m = 45
                s = 0


            if nivel.get() == 3:
                h = 0
                m = 30
                s = 0

        #Si lo hizo se le dan al timer para que use el tiempo ingresado
        else:
            h = int(horas.get())
            m = int(minutos.get())
            s = int(segundos.get())

        def iniciar(h,m,s):
            global proceso
            if h == 0 and m == 0 and s == 0:

                messagebox.showinfo(message="SE HA ACABADO SU TIEMPO")
                ventana_menu.state(newstate="normal")
                ventana.destroy()
                juego_iniciado = False
                contador_jugada = 1


            #Validacion para el tiempo
            if s == 0:
                s = 59
                if m != 0:
                    m -= 1
                if m == 0 and h == 0:
                    pass
                if m== 0 and h != 0:
                    m = 59
                    h -= 1



            #Se muestra el tiempo
            time['text'] = str(h) + ":" + str(m) + ":" + str (s)
            tiempo_jugado = time["text"]


            proceso = time.after(1000, iniciar, h, m , (s - 1))




        def parar():
            global proceso
            time.after_cancel(proceso)

        time = Label(ventana, fg='red', width=10, font=("", "18"))
        time.place(x=20, y=750)

        iniciar(h,m,s)
        if juego_terminado == True:
            parar()

    #Validacion para mostrar lo que el usuario eligio
    if reloj.get() == 1:
        crono()

    if reloj.get() == 3:
        timer()
    if juego_terminado == True:
        lista_jugadas = []
        lista_eliminados = []
        ventana_menu.state(newstate="normal")
        ventana.destroy()
        juego_terminado = False

"""Funcion cambio boton: esta funcion tiene como tarea hacer que el boton seleccionado para asiganarle un valor para hacer una jugada se cambie, si se le asigna un valor vacio se retorna un error."""
def cambio_boton(Boton, jugada):
    global texto, lista_jugadas, boton_actual, borrar, jugadas_de_partida

    # Con esta condicional se valida si lo que se quiere hacer es borrar una casilla o no
    if borrar == True:
        if validar_texto(Boton) == False:
            messagebox.showerror(title="ERROR", message="LA CASILLA NO SE PUEDE ELIMINAR")
            borrar = False

        else:
            Boton.configure(text="")
            borrar = False
        return



    indice_columnas = encuentra_indice(lista_columnas, Boton)
    indice_filas = encuentra_indice(lista_filas, Boton)

    if validar_columnas(texto, indice_columnas) == True:
        messagebox.showerror(title="ERROR", message="NO SE PUEDE AGREGAR EL VALOR PORQUE YA ESTA EN LA COLUMNA")
        return
    if validar_filas(texto, indice_filas) == True:
        messagebox.showerror(title="ERROR", message="NO SE PUEDE AGREGAR EL VALOR PORQUE YA ESTA EN LA FILA")
        return



    jugada = []
    jugada.append(Boton)
    jugada.append(Boton["text"])
    jugada.append(texto)
    if jugada not in lista_jugadas:
        lista_jugadas.append(jugada)




    #Valida que se haya seleccionado un boton del panel antes de configurar el boton
    if texto == '':
        ''' MessageBox
        -showinfo(), showerror(), showwarning(), askquestion(), askcancel(), askyesno(), askretrycancel()'''
        messagebox.showerror(message='Debe seleccionar un boton del panel de seleccion')
    else:
        Boton.configure(text=texto)
        boton_actual.insert(0,Boton)

    #validar_sumas(jugadas_de_partida)

    validacion_resultados()

"""Funcion Top10: esta funcion es la que se encarga de mostrar una ventana con los valores del top 10"""
def Top10():
    global top10

    #region Creacion y configuracion de ventana
    ventana = Tk()
    # titulo
    ventana.title("KAKURO")

    # se le da tamaño a la ventana principal
    ventana.geometry("800x800")
    # color a la ventana principal
    ventana.configure(bg="gray70")

    etiqueta = Label(ventana, text="TOP 10", bg="gray29", fg="white", padx=100, pady=5, font="Helvetica 25",
                     relief="solid").place(x=250, y=5)
    #endregion

    #region Labels para cada tiempo
    lblnombre = Label(ventana, text="NOMBRE",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=60, y=90)
    lbltiempo = Label(ventana, text="TIEMPO",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=600, y=90)

    lbltop1 = Label(ventana, text="1",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=150)
    lbltop2 = Label(ventana, text="2",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=200)
    lbltop3 = Label(ventana, text="3",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=250)
    lbltop4 = Label(ventana, text="4",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=300)
    lbltop5 = Label(ventana, text="5",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=350)
    lbltop6 = Label(ventana, text="6",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=400)
    lbltop7 = Label(ventana, text="7",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=450)
    lbltop8 = Label(ventana, text="8",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=500)
    lbltop9 = Label(ventana, text="9",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=550)
    lbltop10 = Label(ventana, text="10",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=600)

    #endregion

    #region Labels que contienen los valores
    lblnombre1 = Label(ventana, text=top10[0][0], bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=60, y=150)
    lbltiempo1 = Label(ventana, text=top10[0][1], bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=600, y=150)

    lblnombre2 = Label(ventana, text=top10[1][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=200)
    lbltiempo2 = Label(ventana, text=top10[1][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=200)

    lblnombre3 = Label(ventana, text=top10[2][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=250)
    lbltiempo3 = Label(ventana, text=top10[2][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=250)

    lblnombre4 = Label(ventana, text=top10[3][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=300)
    lbltiempo4 = Label(ventana, text=top10[3][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=300)

    lblnombre5 = Label(ventana, text=top10[4][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=350)
    lbltiempo5 = Label(ventana, text=top10[4][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=350)

    lblnombre6 = Label(ventana, text=top10[5][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=400)
    lbltiempo6 = Label(ventana, text=top10[5][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=400)

    lblnombre7 = Label(ventana, text=top10[6][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=450)
    lbltiempo7 = Label(ventana, text=top10[6][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=450)

    lblnombre8 = Label(ventana, text=top10[7][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=500)
    lbltiempo8 = Label(ventana, text=top10[7][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=500)

    lblnombre9 = Label(ventana, text=top10[8][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=550)
    lbltiempo9 = Label(ventana, text=top10[8][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=550)

    lblnombre10 = Label(ventana, text=top10[9][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=600)
    lbltiempo10 = Label(ventana, text=top10[9][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=600)
    #endregion

    ventana.mainloop()

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

"""Funcion validar texto: esta funcion valida el un boton contiene texto o no y retorna un valor booleano para entender"""
def validar_texto(boton):
    if boton["text"] == "":
        return False
    return True

"""Funcion deshacer jugada: esta funcion recibe una lista de jugadas y una de eliminados, lo que hace esta funcion es deshacer la ultima jugada, y esa jugada deshecha la 
ingresa a la lista de eliminados."""
def deshacer_jugada(lista_jugadas, lista_eliminados):
    global texto
    if lista_jugadas == []:
        messagebox.showinfo(title="DESHACER JUGADA", message="NO HAY JUGADAS PARA DESHACER")
        return
    lista_jugadas[-1][0].configure(text=lista_jugadas[-1][1])
    lista_eliminados.append(lista_jugadas[-1])
    lista_jugadas.pop()

"""Funcion ayuda manual: esta funcion muestra el manual de usuario donde se explica como funciona el juego."""
def ayuda_manual():

    wb.open_new(r"C:\Users\Jhonny Diaz\PycharmProjects\Programa 3 Kakuro\manual_de_usuario_kakuro2020.pdf")

"""Funcion rehacer jugada: esta funcion recibe una lista de jugadas y una de eliminados, esta funcion rehace la jugada, eliminandola de la lista de eliminados e ingresandola en la lista de jugadas"""
def rehacer_jugada(lista_jugadas, lista_eliminados):
    if lista_eliminados == []:
        messagebox.showinfo(title="REHACER JUGADA", message="NO HAY JUGADAS PARA REHACER")
        return

    lista_eliminados[-1][0].configure(text=lista_eliminados[-1][2])
    lista_jugadas.append(lista_eliminados[-1])
    lista_eliminados.pop()

"""Funcion ventana de juego: esta funcion es la funcion mas importante del programa puesto que es la funcion que crea el tablero y demas cosas importantes que se deben mostrar
para poder jugar al juego"""
def ventana_de_juego(ventana_menu):
    ventana_menu.withdraw()

    global texto, nombre_jugador, lista_filas, lista_columnas, jugadas_de_partida



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

    if nivel.get() == 1:
        lbl_nivel = Label(ventana, text="Nivel: Fácil", bg="gray29",fg= "white", padx=10, pady=5, font="Helvetica 25",relief="solid").place(x=100, y=650)

    if nivel.get() == 2:
        lbl_nivel = Label(ventana, text="Nivel: Medio", bg="gray29",fg= "white", padx=10, pady=5, font="Helvetica 25",relief="solid").place(x=100, y=650)

    if nivel.get() == 3:
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
    global lista_botones_de_juego, lista_botones_juego_facil_1, jugad1
    lista_botones_de_juego = []
    lista_botones_juego_facil_1 = []
    jugada = []


    #region FILAS
    fila1_jugada1 = []
    fila1_jugada2 = []

    fila2_jugada1 = []
    fila2_jugada2 = []

    fila3_jugada1 = []
    fila3_jugada2 = []

    fila4_jugada1 = []
    fila4_jugada2 = []

    fila5_jugada1 = []
    fila5_jugada2 = []

    fila6_jugada1 = []
    fila6_jugada2 = []

    fila7_jugada1 = []
    fila7_jugada2 = []

    fila8_jugada1 = []
    fila8_jugada2 = []

    #endregion


    #region COLUMNA 1

    boton_juego1x1 = Button(ventana, width=4,bg="black",state="disabled", height=2,text="", command=lambda :cambio_boton(boton_juego1x1, texto))
    boton_juego1x1.place(x=100, y=100)
    #lista_botones_de_juego.append(boton_juego1x1)

    boton_juego1x2 = Button(ventana, width=4, height=2,bg="black",state="disabled", command=lambda: cambio_boton(boton_juego1x2, texto))
    boton_juego1x2.place(x=100, y=142)
    #lista_botones_de_juego.append(boton_juego1x2)

    boton_juego1x3 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego1x3, texto))
    boton_juego1x3.place(x=100, y=184)
    #lista_botones_de_juego.append(boton_juego1x3)

    boton_juego1x4 = Button(ventana, width=4, height=2, bg="black",state="disabled", text="12",fg="white", command=lambda: cambio_boton(boton_juego1x4, texto))
    boton_juego1x4.place(x=100, y=226)
    #lista_botones_de_juego.append(boton_juego1x4)

    boton_juego1x5 = Button(ventana, width=4, height=2, bg="black",state="disabled", text="3",fg="white",command=lambda: cambio_boton(boton_juego1x5, texto))
    boton_juego1x5.place(x=100, y=268)
    #lista_botones_de_juego.append(boton_juego1x5)

    boton_juego1x6 = Button(ventana, width=4, height=2, bg="black",state="disabled", text="17",fg="white", command=lambda: cambio_boton(boton_juego1x6, texto))
    boton_juego1x6.place(x=100, y=310)
    #lista_botones_de_juego.append(boton_juego1x6)

    boton_juego1x7 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego1x7, texto))
    boton_juego1x7.place(x=100, y=352)
    #lista_botones_de_juego.append(boton_juego1x7)

    boton_juego1x8 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="28",fg="white", command=lambda: cambio_boton(boton_juego1x8, texto))
    boton_juego1x8.place(x=100, y=394)
    #lista_botones_de_juego.append(boton_juego1x8)

    boton_juego1x9 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="6",fg="white", command=lambda: cambio_boton(boton_juego1x9, texto))
    boton_juego1x9.place(x=100, y=436)
    #lista_botones_de_juego.append(boton_juego1x9)
    #endregion

    # region COLUMNA 2
    columna2_jugada1 = []
    columna2_jugada2 = []

    boton_juego2x1 = Button(ventana, width=4, height=2,bg="black",state="disabled", command=lambda: cambio_boton(boton_juego2x1, texto))
    boton_juego2x1.place(x=140, y=100)

    boton_juego2x2 = Button(ventana, width=4, height=2,bg="black",state="disabled", text="    14\n     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego2x2, texto))
    boton_juego2x2.place(x=140, y=142)
    jugada.append(boton_juego2x2)


    boton_juego2x3 = Button(ventana, width=4, height=2,bg="black",state="disabled", text="    36\n7     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego2x3, texto))
    boton_juego2x3.place(x=140, y=184)


    boton_juego2x4 = Button(ventana, width=4, height=2,state="disabled", command=lambda: cambio_boton(boton_juego2x4, texto))
    boton_juego2x4.place(x=140, y=226)
    lista_botones_de_juego.append(boton_juego2x4)
    columna2_jugada1.append(boton_juego2x4)
    fila3_jugada1.append(boton_juego2x4)

    boton_juego2x5 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego2x5, texto))
    boton_juego2x5.place(x=140, y=268)
    lista_botones_de_juego.append(boton_juego2x5)
    columna2_jugada1.append(boton_juego2x5)
    fila4_jugada1.append(boton_juego2x5)

    boton_juego2x6 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego2x6, texto))
    boton_juego2x6.place(x=140, y=310)
    lista_botones_de_juego.append(boton_juego2x6)
    columna2_jugada1.append(boton_juego2x6)
    fila5_jugada1.append(boton_juego2x6)

    boton_juego2x7 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="   \n11     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego2x7, texto))
    boton_juego2x7.place(x=140, y=352)


    boton_juego2x8 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego2x8, texto))
    boton_juego2x8.place(x=140, y=394)
    lista_botones_de_juego.append(boton_juego2x8)
    columna2_jugada2.append(boton_juego2x8)
    fila7_jugada1.append(boton_juego2x8)

    boton_juego2x9 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego2x9, texto))
    boton_juego2x9.place(x=140, y=436)
    lista_botones_de_juego.append(boton_juego2x9)
    columna2_jugada2.append(boton_juego2x9)
    fila8_jugada1.append(boton_juego2x9)

    lista_columnas.append(columna2_jugada1)
    lista_columnas.append(columna2_jugada2)
    # endregion

    # region COLUMNA 3
    columna3_jugada1 = []
    columna3_jugada2 = []

    boton_juego3x1 = Button(ventana, width=4, height=2,bg="black",state="disabled", text="   \n19     ",fg="white",justify="right",  command=lambda: cambio_boton(boton_juego3x1, texto))
    boton_juego3x1.place(x=180, y=100)


    boton_juego3x2 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego3x2, texto))
    boton_juego3x2.place(x=180, y=142)
    lista_botones_de_juego.append(boton_juego3x2)
    columna3_jugada1.append(boton_juego3x2)
    fila1_jugada1.append(boton_juego3x2)
    jugada.append(boton_juego3x2)

    boton_juego3x3 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego3x3, texto))
    boton_juego3x3.place(x=180, y=184)
    lista_botones_de_juego.append(boton_juego3x3)
    columna3_jugada1.append(boton_juego3x3)
    fila2_jugada1.append(boton_juego3x3)

    boton_juego3x4 = Button(ventana, width=4, height=2,state="disabled",  command=lambda: cambio_boton(boton_juego3x4, texto))
    boton_juego3x4.place(x=180, y=226)
    lista_botones_de_juego.append(boton_juego3x4)
    columna3_jugada1.append(boton_juego3x4)
    fila3_jugada1.append(boton_juego3x4)

    boton_juego3x5 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego3x5, texto))
    boton_juego3x5.place(x=180, y=268)
    lista_botones_de_juego.append(boton_juego3x5)
    columna3_jugada1.append(boton_juego3x5)
    fila4_jugada1.append(boton_juego3x5)

    boton_juego3x6 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego3x6, texto))
    boton_juego3x6.place(x=180, y=310)
    lista_botones_de_juego.append(boton_juego3x6)
    columna3_jugada1.append(boton_juego3x6)
    fila5_jugada1.append(boton_juego3x6)

    boton_juego3x7 = Button(ventana, width=4, height=2,bg="black",state="disabled",text="13\n7     ",fg="white",justify="right",  command=lambda: cambio_boton(boton_juego3x7, texto))
    boton_juego3x7.place(x=180, y=352)


    boton_juego3x8 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego3x8, texto))
    boton_juego3x8.place(x=180, y=394)
    lista_botones_de_juego.append(boton_juego3x8)
    columna3_jugada2.append(boton_juego3x8)
    fila7_jugada1.append(boton_juego3x8)


    boton_juego3x9 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego3x9, texto))
    boton_juego3x9.place(x=180, y=436)
    lista_botones_de_juego.append(boton_juego3x9)
    columna3_jugada2.append(boton_juego3x9)
    fila8_jugada1.append(boton_juego3x9)

    lista_columnas.append(columna3_jugada1)
    lista_columnas.append(columna3_jugada2)
    # endregion

    # region COLUMNA 4
    columna4_jugada1 = []
    columna4_jugada2 = []

    boton_juego4x1 = Button(ventana, width=4, height=2,bg="black",state="disabled",text="   \n12     ",fg="white",justify="right",  command=lambda: cambio_boton(boton_juego4x1, texto))
    boton_juego4x1.place(x=220, y=100)


    boton_juego4x2 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego4x2, texto))
    boton_juego4x2.place(x=220, y=142)
    lista_botones_de_juego.append(boton_juego4x2)
    columna4_jugada1.append(boton_juego4x2)
    fila1_jugada1.append(boton_juego4x2)
    jugada.append(boton_juego4x2)

    boton_juego4x3 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego4x3, texto))
    boton_juego4x3.place(x=220, y=184)
    lista_botones_de_juego.append(boton_juego4x3)
    columna4_jugada1.append(boton_juego4x3)
    fila2_jugada1.append(boton_juego4x3)

    boton_juego4x4 = Button(ventana, width=4, height=2,bg="black",state="disabled",text="10\n       ",fg="white",justify="right",  command=lambda: cambio_boton(boton_juego4x4, texto))
    boton_juego4x4.place(x=220, y=226)


    boton_juego4x5 = Button(ventana, width=4, height=2,bg="black",state="disabled",text="    \n20     ",fg="white",justify="right",  command=lambda: cambio_boton(boton_juego4x5, texto))
    boton_juego4x5.place(x=220, y=268)


    boton_juego4x6 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego4x6, texto))
    boton_juego4x6.place(x=220, y=310)
    lista_botones_de_juego.append(boton_juego4x6)
    columna4_jugada2.append(boton_juego4x6)
    fila5_jugada1.append(boton_juego4x6)

    boton_juego4x7 = Button(ventana, width=4, height=2,state="disabled",  command=lambda: cambio_boton(boton_juego4x7, texto))
    boton_juego4x7.place(x=220, y=352)
    lista_botones_de_juego.append(boton_juego4x7)
    columna4_jugada2.append(boton_juego4x7)
    fila6_jugada1.append(boton_juego4x7)

    boton_juego4x8 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego4x8, texto))
    boton_juego4x8.place(x=220, y=394)
    lista_botones_de_juego.append(boton_juego4x8)
    columna4_jugada2.append(boton_juego4x8)
    fila7_jugada1.append(boton_juego4x8)

    boton_juego4x9 = Button(ventana, width=4, height=2, bg="black",state="disabled",command=lambda: cambio_boton(boton_juego4x9, texto))
    boton_juego4x9.place(x=220, y=436)

    lista_columnas.append(columna4_jugada1)
    lista_columnas.append(columna4_jugada2)
    # endregion

    # region COLUMNA 5
    columna5_jugada1 = []
    columna5_jugada2 = []

    boton_juego5x1 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego5x1, texto))
    boton_juego5x1.place(x=260, y=100)


    boton_juego5x2 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="    \n4     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego5x2, texto))
    boton_juego5x2.place(x=260, y=142)


    boton_juego5x3 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego5x3, texto))
    boton_juego5x3.place(x=260, y=184)
    lista_botones_de_juego.append(boton_juego5x3)
    columna5_jugada1.append(boton_juego5x3)
    fila2_jugada1.append(boton_juego5x3)

    boton_juego5x4 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego5x4, texto))
    boton_juego5x4.place(x=260, y=226)
    lista_botones_de_juego.append(boton_juego5x4)
    columna5_jugada1.append(boton_juego5x4)
    fila3_jugada2.append(boton_juego5x4)

    boton_juego5x5 = Button(ventana, width=4, height=2,bg="black",state="disabled",text="    20\n11     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego5x5, texto))
    boton_juego5x5.place(x=260, y=268)


    boton_juego5x6 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego5x6, texto))
    boton_juego5x6.place(x=260, y=310)
    lista_botones_de_juego.append(boton_juego5x6)
    columna5_jugada2.append(boton_juego5x6)
    fila5_jugada1.append(boton_juego5x6)

    boton_juego5x7 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego5x7, texto))
    boton_juego5x7.place(x=260, y=352)
    lista_botones_de_juego.append(boton_juego5x7)
    columna5_jugada2.append(boton_juego5x7)
    fila6_jugada1.append(boton_juego5x7)

    boton_juego5x8 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego5x8, texto))
    boton_juego5x8.place(x=260, y=394)
    lista_botones_de_juego.append(boton_juego5x8)
    columna5_jugada2.append(boton_juego5x8)
    fila7_jugada1.append(boton_juego5x8)

    boton_juego5x9 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego5x9, texto))
    boton_juego5x9.place(x=260, y=436)

    lista_columnas.append(columna5_jugada1)
    lista_columnas.append(columna5_jugada2)
    # endregion

    # region COLUMNA 6
    columna6_jugada1 = []
    columna6_jugada2 = []

    boton_juego6x1 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego6x1, texto))
    boton_juego6x1.place(x=300, y=100)


    boton_juego6x2 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="    \n11     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego6x2, texto))
    boton_juego6x2.place(x=300, y=142)


    boton_juego6x3 = Button(ventana, width=4, height=2,state="disabled",  command=lambda: cambio_boton(boton_juego6x3, texto))
    boton_juego6x3.place(x=300, y=184)
    lista_botones_de_juego.append(boton_juego6x3)
    columna6_jugada1.append(boton_juego6x3)
    fila2_jugada1.append(boton_juego6x3)

    boton_juego6x4 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego6x4, texto))
    boton_juego6x4.place(x=300, y=226)
    lista_botones_de_juego.append(boton_juego6x4)
    columna6_jugada1.append(boton_juego6x4)
    fila3_jugada2.append(boton_juego6x4)

    boton_juego6x5 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego6x5, texto))
    boton_juego6x5.place(x=300, y=268)
    lista_botones_de_juego.append(boton_juego6x5)
    columna6_jugada1.append(boton_juego6x5)
    fila4_jugada2.append(boton_juego6x5)

    boton_juego6x6 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="    \n8     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego6x6, texto))
    boton_juego6x6.place(x=300, y=310)


    boton_juego6x7 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego6x7, texto))
    boton_juego6x7.place(x=300, y=352)
    lista_botones_de_juego.append(boton_juego6x7)
    columna6_jugada2.append(boton_juego6x7)
    fila6_jugada1.append(boton_juego6x7)

    boton_juego6x8 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego6x8, texto))
    boton_juego6x8.place(x=300, y=394)
    lista_botones_de_juego.append(boton_juego6x8)
    columna6_jugada2.append(boton_juego6x8)
    fila7_jugada1.append(boton_juego6x8)

    boton_juego6x9 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="   8\n       ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego6x9, texto))
    boton_juego6x9.place(x=300, y=436)

    lista_columnas.append(columna6_jugada1)
    lista_columnas.append(columna6_jugada2)
    # endregion

    # region COLUMNA 7
    columna7_jugada1 = []
    columna7_jugada2 = []

    boton_juego7x1 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego7x1, texto))
    boton_juego7x1.place(x=340, y=100)


    boton_juego7x2 = Button(ventana, width=4, height=2,bg="black",state="disabled",text="   4\n17     ",fg="white",justify="right",  command=lambda: cambio_boton(boton_juego7x2, texto))
    boton_juego7x2.place(x=340, y=142)


    boton_juego7x3 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego7x3, texto))
    boton_juego7x3.place(x=340, y=184)
    lista_botones_de_juego.append(boton_juego7x3)
    columna7_jugada1.append(boton_juego7x3)
    fila2_jugada1.append(boton_juego7x3)

    boton_juego7x4 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego7x4, texto))
    boton_juego7x4.place(x=340, y=226)
    lista_botones_de_juego.append(boton_juego7x4)
    columna7_jugada1.append(boton_juego7x4)
    fila3_jugada2.append(boton_juego7x4)

    boton_juego7x5 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego7x5, texto))
    boton_juego7x5.place(x=340, y=268)
    lista_botones_de_juego.append(boton_juego7x5)
    columna7_jugada1.append(boton_juego7x5)
    fila4_jugada2.append(boton_juego7x5)

    boton_juego7x6 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="    6\n     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego7x6, texto))
    boton_juego7x6.place(x=340, y=310)


    boton_juego7x7 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="   10\n4     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego7x7, texto))
    boton_juego7x7.place(x=340, y=352)


    boton_juego7x8 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego7x8, texto))
    boton_juego7x8.place(x=340, y=394)
    lista_botones_de_juego.append(boton_juego7x8)
    columna7_jugada2.append(boton_juego7x8)
    fila7_jugada1.append(boton_juego7x8)

    boton_juego7x9 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego7x9, texto))
    boton_juego7x9.place(x=340, y=436)
    lista_botones_de_juego.append(boton_juego7x9)
    columna7_jugada2.append(boton_juego7x9)
    fila8_jugada2.append(boton_juego7x9)

    lista_columnas.append(columna7_jugada2)
    lista_columnas.append(columna7_jugada1)
    # endregion

    # region COLUMNA 8
    columna8_jugada1 = []
    columna8_jugada2 = []

    boton_juego8x1 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="    \n7     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego8x1, texto))
    boton_juego8x1.place(x=380, y=100)


    boton_juego8x2 = Button(ventana, width=4, height=2,state="disabled",  command=lambda: cambio_boton(boton_juego8x2, texto))
    boton_juego8x2.place(x=380, y=142)
    lista_botones_de_juego.append(boton_juego8x2)
    columna8_jugada1.append(boton_juego8x2)
    fila1_jugada2.append(boton_juego8x2)

    boton_juego8x3 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego8x3, texto))
    boton_juego8x3.place(x=380, y=184)
    lista_botones_de_juego.append(boton_juego8x3)
    columna8_jugada1.append(boton_juego8x3)
    fila2_jugada1.append(boton_juego8x3)

    boton_juego8x4 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="   \n25     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego8x4, texto))
    boton_juego8x4.place(x=380, y=226)


    boton_juego8x5 = Button(ventana, width=4, height=2,state="disabled",  command=lambda: cambio_boton(boton_juego8x5, texto))
    boton_juego8x5.place(x=380, y=268)
    lista_botones_de_juego.append(boton_juego8x5)
    columna8_jugada2.append(boton_juego8x5)
    fila4_jugada2.append(boton_juego8x5)

    boton_juego8x6 = Button(ventana, width=4, height=2,state="disabled",  command=lambda: cambio_boton(boton_juego8x6, texto))
    boton_juego8x6.place(x=380, y=310)
    lista_botones_de_juego.append(boton_juego8x6)
    columna8_jugada2.append(boton_juego8x6)
    fila5_jugada2.append(boton_juego8x6)

    boton_juego8x7 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego8x7, texto))
    boton_juego8x7.place(x=380, y=352)
    lista_botones_de_juego.append(boton_juego8x7)
    columna8_jugada2.append(boton_juego8x7)
    fila6_jugada2.append(boton_juego8x7)

    boton_juego8x8 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego8x8, texto))
    boton_juego8x8.place(x=380, y=394)
    lista_botones_de_juego.append(boton_juego8x8)
    columna8_jugada2.append(boton_juego8x8)
    fila7_jugada1.append(boton_juego8x8)

    boton_juego8x9 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego8x9, texto))
    boton_juego8x9.place(x=380, y=436)
    lista_botones_de_juego.append(boton_juego8x9)
    columna8_jugada2.append(boton_juego8x9)
    fila8_jugada2.append(boton_juego8x9)

    lista_columnas.append(columna8_jugada1)
    lista_columnas.append(columna8_jugada2)
    # endregion

    # region COLUMNA 9
    columna9_jugada1 = []
    columna9_jugada2 = []

    boton_juego9x1 = Button(ventana, width=4, height=2, bg="black",state="disabled",text="   \n10     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego9x1, texto))
    boton_juego9x1.place(x=420, y=100)


    boton_juego9x2 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego9x2, texto))
    boton_juego9x2.place(x=420, y=142)
    lista_botones_de_juego.append(boton_juego9x2)
    columna9_jugada1.append(boton_juego9x2)
    fila1_jugada2.append(boton_juego9x2)

    boton_juego9x3 = Button(ventana, width=4, height=2, state="disabled",  command=lambda: cambio_boton(boton_juego9x3, texto))
    boton_juego9x3.place(x=420, y=184)
    lista_botones_de_juego.append(boton_juego9x3)
    columna9_jugada1.append(boton_juego9x3)
    fila2_jugada1.append(boton_juego9x3)

    boton_juego9x4 = Button(ventana, width=4, height=2, bg="black",state="disabled", text="   \n14     ",fg="white",justify="right", command=lambda: cambio_boton(boton_juego9x4, texto))
    boton_juego9x4.place(x=420, y=226)


    boton_juego9x5 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego9x5, texto))
    boton_juego9x5.place(x=420, y=268)
    lista_botones_de_juego.append(boton_juego9x5)
    columna9_jugada2.append(boton_juego9x5)
    fila4_jugada2.append(boton_juego9x5)

    boton_juego9x6 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego9x6, texto))
    boton_juego9x6.place(x=420, y=310)
    lista_botones_de_juego.append(boton_juego9x6)
    columna9_jugada2.append(boton_juego9x6)
    fila5_jugada2.append(boton_juego9x6)

    boton_juego9x7 = Button(ventana, width=4, height=2, state="disabled", command=lambda: cambio_boton(boton_juego9x7, texto))
    boton_juego9x7.place(x=420, y=352)
    lista_botones_de_juego.append(boton_juego9x7)
    columna9_jugada2.append(boton_juego9x7)
    fila6_jugada2.append(boton_juego9x7)

    boton_juego9x8 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego9x8, texto))
    boton_juego9x8.place(x=420, y=394)


    boton_juego9x9 = Button(ventana, width=4, height=2, bg="black",state="disabled", command=lambda: cambio_boton(boton_juego9x9, texto))
    boton_juego9x9.place(x=420, y=436)

    lista_columnas.append(columna9_jugada1)
    lista_columnas.append(columna9_jugada2)
    # endregion

    #region adjuntar filas
    lista_filas.append(fila1_jugada1)
    lista_filas.append(fila1_jugada2)

    lista_filas.append(fila2_jugada1)
    lista_filas.append(fila2_jugada2)

    lista_filas.append(fila3_jugada1)
    lista_filas.append(fila3_jugada2)

    lista_filas.append(fila4_jugada1)
    lista_filas.append(fila4_jugada2)

    lista_filas.append(fila5_jugada1)
    lista_filas.append(fila5_jugada2)

    lista_filas.append(fila6_jugada1)
    lista_filas.append(fila6_jugada2)

    lista_filas.append(fila7_jugada1)
    lista_filas.append(fila7_jugada2)

    lista_filas.append(fila8_jugada1)
    lista_filas.append(fila8_jugada2)


    #endregion

    #region JUGADAS DE PARTIDA

    #region Jugadas por fila
    jugadas_de_partida.append(["14", fila1_jugada1])
    jugadas_de_partida.append(["4",  fila1_jugada2])
    jugadas_de_partida.append(["36", fila2_jugada1])
    jugadas_de_partida.append(["12", fila3_jugada1])
    jugadas_de_partida.append(["10", fila3_jugada2])
    jugadas_de_partida.append(["3",  fila4_jugada1])
    jugadas_de_partida.append(["20", fila4_jugada2])
    jugadas_de_partida.append(["17", fila5_jugada1])
    jugadas_de_partida.append(["6",  fila5_jugada2])
    jugadas_de_partida.append(["13", fila6_jugada1])
    jugadas_de_partida.append(["10", fila6_jugada2])
    jugadas_de_partida.append(["28", fila7_jugada1])
    jugadas_de_partida.append(["6",  fila8_jugada1])
    jugadas_de_partida.append(["8",  fila8_jugada2])
    #endregion

    #region jugadas por columna
    jugadas_de_partida.append(["7", columna2_jugada1])
    jugadas_de_partida.append(["11", columna2_jugada2])

    jugadas_de_partida.append(["19", columna2_jugada1])
    jugadas_de_partida.append(["7", columna2_jugada2])

    jugadas_de_partida.append(["12", columna2_jugada1])
    jugadas_de_partida.append(["20", columna2_jugada2])

    jugadas_de_partida.append(["4", columna2_jugada1])
    jugadas_de_partida.append(["11", columna2_jugada2])

    jugadas_de_partida.append(["11", columna2_jugada1])
    jugadas_de_partida.append(["8", columna2_jugada2])

    jugadas_de_partida.append(["17", columna2_jugada1])
    jugadas_de_partida.append(["4", columna2_jugada2])

    jugadas_de_partida.append(["7", columna2_jugada1])
    jugadas_de_partida.append(["25", columna2_jugada2])

    jugadas_de_partida.append(["10", columna2_jugada1])
    jugadas_de_partida.append(["14", columna2_jugada2])

    #endregion

    #endregion

    #endregion

    #region Botones principales
    boton_iniciar_juego = Button(ventana, width=15, height=2, text="INICIAR JUEGO", state="disabled",command= lambda : iniciar_juego(ventana, boton_deshacer_jugada, boton_rehacer_jugada, boton_borrar_casilla, boton_borrar_juego, boton_terminar_partida, boton_top10, boton_guardar_juego, evaluar_nombre, entrada_nombre, lista_botones_de_juego))
    boton_iniciar_juego.place(x=100, y=500)

    boton_deshacer_jugada = Button(ventana, width=15, height=2, text="DESHACER JUGADA", state="disabled", command=lambda : deshacer_jugada(lista_jugadas, lista_eliminados))
    boton_deshacer_jugada.place(x=100, y=550)

    boton_rehacer_jugada = Button(ventana, width=15, height=2, text="REHACER JUGADA", state="disabled", command= lambda : rehacer_jugada(lista_jugadas, lista_eliminados))
    boton_rehacer_jugada.place(x=100, y=600)

    boton_borrar_casilla = Button(ventana, width=15, height=2, text="BORRAR CASILLA", state="disabled", command=lambda: borrar_casilla())
    boton_borrar_casilla.place(x=250, y=500)

    boton_borrar_juego = Button(ventana, width=15, height=2,text="BORRAR JUEGO", state="disabled", command= lambda : borrar_juego(lista_botones_de_juego))
    boton_borrar_juego.place(x=250,y=550)

    boton_terminar_partida = Button(ventana, width=15, height=2,text="TERMINAR JUEGO", state="disabled", command= lambda : terminar_juego(ventana))
    boton_terminar_partida.place(x=250,y=600)

    boton_top10 = Button(ventana, width=15, height=2, text="TOP 10",state="disabled",  command= lambda : Top10())
    boton_top10.place(x=400, y=500)

    boton_guardar_juego = Button(ventana, width=15, height=2, text="GUARDAR JUEGO",state="disabled", command=lambda : guardar_juego(ventana_menu, ventana))
    boton_guardar_juego.place(x=400, y=550)

    boton_cargar_juego = Button(ventana, width=15, height=2, text="CARGAR JUEGO", command= lambda : cargar_juego(lista_botones_de_juego))
    boton_cargar_juego.place(x=400, y=600)
    #endregion

    #region Entry nombre de jugador
    nombre_jugador = StringVar(ventana)
    entrada_nombre = Entry(ventana, textvariable=nombre_jugador)
    entrada_nombre.place(x=300, y=660)
    evaluar_nombre = Button(ventana, bg='SkyBlue1', text='OK', activebackground='SkyBlue1',bd=5, command=lambda: validar_nombre(boton_iniciar_juego, entrada_nombre))
    evaluar_nombre.place(x=430,y=655)
    #endregion


    ventana.mainloop()

"Funcion validar columnas: esta funcion recibe el texto o el valor que se quiere poner al boton y un indice que indica en donde se encuentra el boton, con una variable global de los botones" \
"la funcion busca en ese grupo de botones si el valor que se quiere ingresar ya esta, si lo esta indice el error, si no esta posigue con el cambio del boton"
def validar_columnas(texto, indice):
    global lista_columnas
    for i in lista_columnas[indice]:
        if i["text"] == texto:
            return True

    return False

"""Funcion validar filas: esta funcion recibe el valor que se le quiere poner al boton y un indice que indica en que posicion se encuentra dentrto de una variable global q ue contiene
todas las listas de las jugadas por filas y valida si el valor ya se encuentra dentro de la fila o no."""
def validar_filas(texto, indice):
    global lista_filas
    for i in lista_filas[indice]:
        if i["text"] == texto:
            return True

    return False

"""Funcion pantalla menu: esta funcion es la pantalla principal que muestra el menu y sus funciones, muestra funciones como inciar juego o el manual de usuario"""
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

"""Funcion acerca de: esat funcion muestra un pequeña venta donce se muestra la informacion mas basica del programa como la fecha de cracion o el autor"""
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

"""Funcion guardar juego: esta funcion guarda el juego actual dentro de una variable que se guarda dentro de un archivo .dat"""
def guardar_juego(venatana_menu, ventana_juego):
    global partida_guardada, lista_eliminados, lista_jugadas
    partida_guardada = lista_jugadas[:]
    seleccion = messagebox.askyesno(title="SEGUIR JUGANDO", message="¿DESEA SEGUIR JUGANDO?")
    if seleccion == False:
        lista_jugadas = []
        lista_eliminados = []
        venatana_menu.state(newstate="normal")
        ventana_juego.destroy()

"""Funcion cargar juego: esta funcion lo que hace es cargar el juego que este guardado dentro de la variable del juego que se guardo anteriormente"""
def cargar_juego(botones_juego):
    global partida_guardada, lista_jugadas

    lista_jugadas = partida_guardada[:]

    for i in botones_juego:
        i.configure(state="normal")

    for i in partida_guardada:
        for j in i:
            try:
                j.configure(text=i[2])

            except AttributeError:
                print("")

"""Funcion atras: esta funcion basica lo que hace es que recibe dos ventanas y muestra una mintras la otra fue destruida"""
def atras(ventana_destruir, ventanar_recuperar):
    ventanar_recuperar.state(newstate="normal")
    ventana_destruir.destroy()

"""Funcion configuracion: esat funcion muestra un pantalla donde se muestran las ocnfiguraciones que se pueden hacer para que el juego ffuncione de la mejor manera, muestra
opciones como el nivel de dificultad, si se quiere el cronometro o un timer y el tiempo que se desea para jugar"""
def configuracion(ventana_menu):
    ventana_menu.withdraw()
    global nivel, reloj, horas, minutos, segundos

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

    #region Entrada de tiempos
    horas = StringVar(ventana)
    label_horas = Label(ventana, text="Horas:", bg="gray29", fg="white", relief="solid").place(x=20, y=220)
    entrada_horas = Entry(ventana, textvariable=horas)
    entrada_horas.place(x=20, y=250)

    minutos = StringVar(ventana)
    label_minutos = Label(ventana, text="Minutos:", bg="gray29", fg="white", relief="solid").place(x=20, y=280)
    entrada_minutos = Entry(ventana, textvariable=minutos)
    entrada_minutos.place(x=20, y=310)

    segundos = StringVar(ventana)
    label_segundos = Label(ventana, text="Segundos:", bg="gray29", fg="white", relief="solid").place(x=20, y=340)
    entrada_segundos = Entry(ventana, textvariable=segundos)
    entrada_segundos.place(x=20, y=370)



    #endregion
    agregar_configuraciones = Button(ventana, text="ACEPTAR", bg="gray29", relief="solid", fg="white", command=lambda: agrega_configuracion(ventana_menu, ventana, nivel.get()))
    agregar_configuraciones.place(x=245, y=400)

    ventana.mainloop()

"""Funcion agrega configuracion: esta funcion lo que hace es que guarda los cambios efectuados por el usuario dentro de la pantalla de configuracion"""
def agrega_configuracion(ventana_menu, ventana, nivel):
    global horas,minutos,segundos
    if nivel == 2 or nivel == 3:
        messagebox.showerror(title="ERROR", message="LO SENTIMOS MUCHO, PERO NO TENEMOS PARTIDAS PARA ESE NIVEL.")
        return

    if horas.get() == "" and minutos.get() == "" and segundos.get() == "":
        ventana_menu.state(newstate="normal")
        messagebox.showinfo(title="CONFIGURACION", message="LA CONFIGURACION HA SIDO REGISTRADA")
        ventana.destroy()
        return

    if int(horas.get()) <= 2 and int(horas.get()) >= 0 and int(minutos.get()) <= 59 and int(minutos.get()) >= 0 and int(segundos.get()) <= 59 and int(segundos.get()) >= 0:
        ventana_menu.state(newstate="normal")
        messagebox.showinfo(title="CONFIGURACION", message="LA CONFIGURACION HA SIDO REGISTRADA")
        ventana.destroy()
        return
    messagebox.showinfo(title="CONFIGURACION",
                        message="LOS DATOS INGRESADOS NO SON VALIDOS\nPOR FAVOR INGRSELOS NUEVAMENTE")

"""Funcion salir: esta funcion destruye la ventana para cuando el usuario quiera terminar el juego"""
def salir(ventana):
    seleccion = messagebox.askyesno(title="SALIR", message="¿DESEA SALIR DEL JUEGO?")
    if seleccion == True:
        ventana.destroy()

"""Funcion borrar juego: esta funcion pregunta al usuario si quiere borrar su juego actual, si el usuario accede muestra todas las casillas de juego en blanco nuevamente para dar un nuevo inicio al juego"""
def borrar_juego(lista_botones):
    global lista_jugadas, lista_eliminados
    seleccion = messagebox.askyesno(title="BORRAR PARTIDA", message="¿DESEA BORRAR LA PARTIDA?")
    if seleccion == True:
        lista_jugadas = []
        lista_eliminados = []
        for i in lista_botones:
            i.configure(text="")

"""Funcion borrar casilla: esat funcion elimina el valor que tenga una casilla, solo se puede hacer si la casilla ya tiene un valor determinado, si no lo posee indica al usuario del error"""
def borrar_casilla():
    global borrar
    borrar = True
    messagebox.showinfo(title="CONFIGURACION", message="SELECCIONE LA CASILLA QUE DESEA ELIMINAR")

"""Funcion terminar juego: esta funcion c=termina el juego actual del usuario, mostrandole nuevamente el tabledo en caso de que desee iniciar nuevamente"""
def terminar_juego(ventana):
    global ventana_menu, lista_jugadas
    seleccion = messagebox.askyesno(title="TERMINAR PARTIDA", message="¿DESEA TERMINAR EL JUEGO?")
    if seleccion == True:
        lista_jugadas = []
        ventana.destroy()
        ventana_de_juego(ventana_menu)

"""Funcion validar nombre: esta funcion revibe el boton de iniciar juego y el nombre que ingreso el usuario, esta funcion valida el largo de este nombre para poder continuar con el juego"""
def validar_nombre(iniciar_juego, nombre):
    if len(nombre.get()) >= 1 and len(nombre.get()) <= 30:
        messagebox.showinfo(title="Nombre", message="EL NOMBRE ES VALIDO:\nPUEDE INICIAR EL JUEGO")
        iniciar_juego.configure(state="normal")

    else:
        messagebox.showinfo(title="INCORRECTO", message="ERROR:\nEL NOMBRE DEBE ESTAR ENTRE 1 Y 30 CARACTERES\n POR FAVOR INGRESE DE NUEVO")

"""Funcion encuentra indice: esta funcion recibe una lista y el elemento que se desea buscar, de esta manera la funcion busca el elemento dentro de ;a l;ista y retorna el indice del lugar donde se encuentra el elemento"""
def encuentra_indice(lista, elemento):
    indice = 0

    for i in lista:
        if elemento in i:
            return indice
        else:
            indice += 1

"""Funcion validar sumas: esta funcion valida que los valores que se deben cumplir sean los resultados de las jugadas, esat funcion 
recibe la lista con las jugadas del tablero y revisa que cada jugada sea el valor correcto, el momento en que se haya completado se le indica al usaurio con un mensaje"""
def validar_sumas(jugadas):
    contador = 0
    for i in jugadas:
        if validar_textos(i) == False:
            if validar_sumas(i) == True:
                contador += 1

            else:
                messagebox.showerror(title="ERROR", message="LA SUMA DE SUS RESPUESTAS NO ES IGUAL A LA CLAVE")

"""Funcion resta de tiempos: esta funcion resta los tiempos del total de tiempo jugado y el tiempo restante para asi saber cuanto fue el tiempo que duro el usuario jugando"""
def resta_de_tiempos():
    global horas, minutos, segundos, tiempo_jugado
    # Validacion para ver si el usuario ingreso un tiempo, si no lo hizo se usan los tiempos predeterminados
    if str(horas.get()) == "" and str(minutos.get()) == "" and str(segundos.get()) == "":
        if nivel.get() == 1:
            tiempo = "1:0:0"

        if nivel.get() == 2:
            tiempo = "0:45:0"

        if nivel.get() == 3:
            tiempo = "0:30:0"

        tiempo_inicial_en_segundos = convertir_a_segundos(tiempo)
        tiempo_final_en_segundos = convertir_a_segundos(tiempo_jugado)

        tiempo_final = tiempo_inicial_en_segundos - tiempo_final_en_segundos

        tiempo_jugado = convertir_segundos_a_horas(tiempo_final)

        return str(tiempo_jugado)



    # Si lo hizo se le dan al timer para que use el tiempo ingresado
    else:
        h = int(horas.get())
        m = int(minutos.get())
        s = int(segundos.get())

        tiempo_inicial_segundos = (h * 3600) + (m * 60) + s
        tiempo_final_segundos = convertir_a_segundos(tiempo_jugado)

        tiempo_final = tiempo_inicial_segundos - tiempo_final_segundos

        tiempo_jugado = convertir_segundos_a_horas(tiempo_final)

        return tiempo_jugado

"""Funcion validar textos: esta funcion recibe una jugada y retorna un valor booleano para saber si tiene todos sus valores en blanco o no"""
def validar_textos(jugada):
    JUGADA = jugada[1:]
    largo = len(jugada)
    contador = 0



    for i in JUGADA:

        for j in i:
            if obtiene_texto(j) == "":
                contador += 1



    if contador == largo:
        return True
    else:
        return False

"""Funcion obtiene texto: esat funcion obtiene el valor de un boton"""
def obtiene_texto(boton):
    return boton["text"]

"""Funcion validacion de resultados: esta funcion recibe una lista con las jugadas de la partida y evaluda las jugadas con el valor del resultado que deben de dar las sumas y se maneja con un contado
este contador es el que define si las partida ha terminado o no"""
def validacion_resultados():
    global jugadas_de_partida, juego_terminado, nombre_jugador, horas, minutos, segundos, reloj, tiempo_jugado, top10, lista_jugadas, lista_eliminados
    contador = 0


    for i in jugadas_de_partida:
        resultado = int(i[0])
        suma = 0

        for j in i[1]:
            if j["text"] == "":
                pass
            else:
                suma = suma + int(j["text"])

        if suma == resultado:
            contador += 1

    print(contador)
    if contador == 18:
        if reloj.get() == 1:
            #valores = [str(nombre_jugador), str(tiempo_jugado)]
            #acomoda_top(valores)
            messagebox.showinfo(message="FELICIDADES\n HA GANADO EL KAKURO")
            juego_terminado = True
            pantalla_menu()



        if reloj.get() == 2:
            messagebox.showinfo(message="FELICIDADES\n HA GANADO EL KAKURO")
            juego_terminado = True
            pantalla_menu()




        if reloj.get() == 3:
            #tiempo_jugado = resta_de_tiempos()
            #acomoda_top([str(nombre_jugador), str(tiempo_jugado)])
            messagebox.showinfo(message="FELICIDADES\n HA GANADO EL KAKURO")
            juego_terminado = True
            pantalla_menu()

"""Funcion convertir a segundos: esta funcion recibe un tiempo que es un string con el formato hhmmss y retorna el valor del tiempo convertido en segundos"""
def convertir_a_segundos(tiempo):
    if tiempo[0].isdigit() == True:
        horas = int(tiempo[0])

    if tiempo[2].isdigit() == True and tiempo[3].isdigit() == True:
        minutos = int(tiempo[2:4])
        segundos = int(tiempo[5:])
    else:
        minutos = int(tiempo[2])
        segundos = int(tiempo[4:])


    tiempo_en_segundos_nuevo = (horas * 3600) + (minutos * 60) + segundos

    return tiempo_en_segundos_nuevo

"""Funcion convertir los segundos a horas en un formato hhmmss"""
def convertir_segundos_a_horas(segundos):
    horas = (segundos // 60) // 60
    minutos = (segundos // 60) - (horas * 60)
    segundos = (segundos % 60)

    return str(horas) + ":" + str(minutos) + ":" + str(segundos)


pantalla_menu()


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ESPACIO PARA FUNCIONES DE PRUEBA>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""Este espacio fue utilizado para hacer funciones de prueba y probar distintos metodos
La funcion que se encuentra a continuacion es un ejemplio del funcionamiento de la funcion que esncontrarmos anteriormente del top 10
La funcion muestra una ventana con el top 10, para probarla debemos descomentar las instrucciones de abajo."""
def Top10ejemplo(valores):
    global top10

    acomoda_top(valores)

    #region Creacion y configuracion de ventana
    ventana = Tk()
    # titulo
    ventana.title("KAKURO")

    # se le da tamaño a la ventana principal
    ventana.geometry("800x800")
    # color a la ventana principal
    ventana.configure(bg="gray70")

    etiqueta = Label(ventana, text="TOP 10", bg="gray29", fg="white", padx=100, pady=5, font="Helvetica 25",
                     relief="solid").place(x=250, y=5)
    #endregion

    #region Labels para cada tiempo
    lblnombre = Label(ventana, text="NOMBRE",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=60, y=90)
    lbltiempo = Label(ventana, text="TIEMPO",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=600, y=90)

    lbltop1 = Label(ventana, text="1",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=150)
    lbltop2 = Label(ventana, text="2",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=200)
    lbltop3 = Label(ventana, text="3",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=250)
    lbltop4 = Label(ventana, text="4",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=300)
    lbltop5 = Label(ventana, text="5",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=350)
    lbltop6 = Label(ventana, text="6",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=400)
    lbltop7 = Label(ventana, text="7",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=450)
    lbltop8 = Label(ventana, text="8",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=500)
    lbltop9 = Label(ventana, text="9",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=550)
    lbltop10 = Label(ventana, text="10",bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=10, y=600)

    #endregion

    #region Labels que contienen los valores
    lblnombre1 = Label(ventana, text=top10[0][0], bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=60, y=150)
    lbltiempo1 = Label(ventana, text=top10[0][1], bg="gray29", fg="white",font="Helvetica 25", relief="solid").place(x=600, y=150)

    lblnombre2 = Label(ventana, text=top10[1][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=200)
    lbltiempo2 = Label(ventana, text=top10[1][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=200)

    lblnombre3 = Label(ventana, text=top10[2][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=250)
    lbltiempo3 = Label(ventana, text=top10[2][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=250)

    lblnombre4 = Label(ventana, text=top10[3][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=300)
    lbltiempo4 = Label(ventana, text=top10[3][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=300)

    lblnombre5 = Label(ventana, text=top10[4][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=350)
    lbltiempo5 = Label(ventana, text=top10[4][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=350)

    lblnombre6 = Label(ventana, text=top10[5][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=400)
    lbltiempo6 = Label(ventana, text=top10[5][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=400)

    lblnombre7 = Label(ventana, text=top10[6][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=450)
    lbltiempo7 = Label(ventana, text=top10[6][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=450)

    lblnombre8 = Label(ventana, text=top10[7][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=500)
    lbltiempo8 = Label(ventana, text=top10[7][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=500)

    lblnombre9 = Label(ventana, text=top10[8][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=550)
    lbltiempo9 = Label(ventana, text=top10[8][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=550)

    lblnombre10 = Label(ventana, text=top10[9][0], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=60, y=600)
    lbltiempo10 = Label(ventana, text=top10[9][1], bg="gray29", fg="white", font="Helvetica 25", relief="solid").place(x=600, y=600)
    #endregion

    ventana.mainloop()

#Top10ejemplo(["Katthya", "1:45:41"])
#pruebas()