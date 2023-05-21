from tkinter import Tk,Label,Button,Frame,Checkbutton,Radiobutton,Entry,IntVar,ttk,StringVar

root=Tk()
root.title("Formulario")
root.geometry("800x600")
root.resizable(0,0)

tried=Label(root,text=" ")
tried.place(x=570,y=50)

def savew():

    if(data1.get()!=" " and data2.get()!=" " and data3.get()!=" " and data4.get()!=" " and data5.get()!=" " and rVar.get()!=0):

        if(rVar.get()==1):
            o4="Estudiante"
        if(rVar.get()==2):
            o4="Empleado"
        if(rVar.get()==3):
            o4="Desempleado"

        if(opt1.get()==1):
            o1="True"
        else:
            o1="False"
    
        if(opt2.get()==1):
            o2="True"
        else:
            o2="False"
    
        if(opt3.get()==1):
            o3="True"
        else:
            o3="False"

        d1=data1.get()
        d2=data2.get()
        d3=data3.get()
        d4=data4.get()
        d5=data5.get()

        o5=estn.get()

        w=["\nNombre: {}".format(d1),"\nApellido Paterno: {}".format(d2),"\nApellido Materno: {}".format(d3),"\nCorreo: {}".format(d4),
            "\nTelefono: {}".format(d5),"\nEstado: {}".format(o5),"\nLabor: {}".format(o4),"\nLeer: {}".format(o1),"\nMusica: {}".format(o2),"\nVideojuegos: {}".format(o3),"\n"]

        file=open("formulario.txt","a+")
        file.writelines(w)
        file.close()

        tried.config(text="Guardado!")
    else:
        tried.config(text="Error, faltan llenar campos!")

def cancelw():

    input1_data.delete(0,"end")
    input2_data.delete(0,"end")
    input3_data.delete(0,"end")
    input4_data.delete(0,"end")
    input5_data.delete(0,"end")
    input1_data.config(text=" ")
    input2_data.config(text=" ")
    input3_data.config(text=" ")
    input4_data.config(text=" ")
    input5_data.config(text=" ")

    r1.deselect()
    r2.deselect()
    r3.deselect()
    rVar.set(0)

    option1.deselect()
    option2.deselect()
    option3.deselect()
    opt1.set(0)
    opt2.set(0)
    opt3.set(0)

    tried.config(text=" ")


fr1=Frame(root)
fr1.place(x=20,y=10,width=450,height=380)
fr1.config(bg="white",bd=5,relief="raised")

#Row & Column configuration, frame 1.
fr1.columnconfigure(0,weight=1)
fr1.columnconfigure(1,weight=5)

fr1.rowconfigure(0,weight=1)
fr1.rowconfigure(1,weight=1)
fr1.rowconfigure(2,weight=1)
fr1.rowconfigure(3,weight=1)
fr1.rowconfigure(4,weight=1)

#Labels and Entry configuration, frame 1.

data1=StringVar()
data2=StringVar()
data3=StringVar()
data4=StringVar()
data5=StringVar()
#1
lbl1_data=Label(fr1,text="Nombre: ")
lbl1_data.grid(column=0,row=0)
lbl1_data.config(bg="white",font=40)

input1_data=Entry(fr1,text=" ")
input1_data.config(bd=3,relief="sunken",width=35,font=20,textvariable=data1)
input1_data.grid(column=1,row=0,stick="w")

#2
lbl2_data=Label(fr1,text="A. Paterno: ")
lbl2_data.grid(column=0,row=1)
lbl2_data.config(bg="white",font=40)

input2_data=Entry(fr1,text=" ")
input2_data.config(bd=3,relief="sunken",width=35,font=20,textvariable=data2)
input2_data.grid(column=1,row=1,stick="w")

#3
lbl3_data=Label(fr1,text="A. Materno: ")
lbl3_data.grid(column=0,row=2)
lbl3_data.config(bg="white",font=40)

input3_data=Entry(fr1,text=" ")
input3_data.config(bd=3,relief="sunken",width=35,font=20,textvariable=data3)
input3_data.grid(column=1,row=2,stick="w")

#4
lbl4_data=Label(fr1,text="Correo: ")
lbl4_data.grid(column=0,row=3)
lbl4_data.config(bg="white",font=40)

input4_data=Entry(fr1,text=" ")
input4_data.config(bd=3,relief="sunken",width=35,font=20,textvariable=data4)
input4_data.grid(column=1,row=3,stick="w")

#5
lbl5_data=Label(fr1,text="Telefono: ")
lbl5_data.grid(column=0,row=4)
lbl5_data.config(bg="white",font=40)

input5_data=Entry(fr1,text=" ")
input5_data.config(bd=3,relief="sunken",width=35,font=20,textvariable=data5)
input5_data.grid(column=1,row=4,stick="w")

fr2=Frame(root)
fr2.place(x=20,y=440,width=450,height=60)
fr2.config(bg="white",bd=5,relief="raised")

#Row & Column configuration, frame 2.
fr2.columnconfigure(0,weight=1)
fr2.columnconfigure(1,weight=1)
fr2.columnconfigure(2,weight=1)
fr2.rowconfigure(0,weight=1)
fr2.rowconfigure(1,weight=3)

lbl1_options=Label(fr2,text="Aficiones")
lbl1_options.config(bg="white")
lbl1_options.grid(column=1,row=0)

#Options

opt1=IntVar()
opt2=IntVar()
opt3=IntVar()
opt1.set(0)
opt2.set(0)
opt3.set(0)

#1
option1=Checkbutton(fr2,text="Leer")
option1.config(bg="white",onvalue=1,offvalue=0,variable=opt1)
option1.grid(column=0,row=1,sticky="e")


#2
option2=Checkbutton(fr2,text="Musica")
option2.config(bg="white",onvalue=1,offvalue=0,variable=opt2)
option2.grid(column=1,row=1)

#3
option3=Checkbutton(fr2,text="Videojuegos")
option3.config(bg="white",onvalue=1,offvalue=0,variable=opt3)
option3.grid(column=2,row=1,sticky="w")

#Radio options.

rVar=IntVar()
rVar.set(0)
#1
r1=Radiobutton(root,text="Estudiante",value=1,variable=rVar)
r1.config(font=40,state="normal")
r1.place(x=570,y=150)
r1.deselect()

#2
r2=Radiobutton(root,text="Empleado",value=2,variable=rVar)
r2.config(font=40,state="normal")
r2.place(x=570,y=180)
r2.deselect()

#3
r3=Radiobutton(root,text="Desempleado",value=3,variable=rVar)
r3.config(font=40,state="normal")
r3.place(x=570,y=210)
r3.deselect()

#Combobox

estn=StringVar()

estados=ttk.Combobox(state="readonly",textvariable=estn)
estados.config(values=["Aguascalientes","Baja California","Baja California Sur","Campeche","Chiapas","Chihuahua","Ciudad de Mexico","Coahuila","Colima","Durango","Guanajuato","Guerrero","Hidalgo","Jalisco",
"Estado de Mexico","Michoacan","Morelos","Nayarit","Nuevo Leon","Oaxaca","Puebla","Queretaro","Quintana Roo","San Luis Potosi","Sinaloa","Sonora","Tabasco","Tamaulipas","Tlaxcala","Veracruz","Yucatan","Zacatecas"],
font=40)
estados.current(0)
estados.place(x=540,y=460)
estados.bind("<<ComboboxSelected>>")

#Buttons

#Guardar
save=Button(root,text="Guardar")
save.config(bg="white",command=savew)
save.place(x=50,y=535,width=120,height=30)

#Cancelar
cancel=Button(root,text="Cancelar")
cancel.config(bg="white",command=cancelw)
cancel.place(x=320,y=535,width=120,height=30)

root.mainloop()