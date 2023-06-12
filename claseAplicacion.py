from tkinter import *
from tkinter import ttk,messagebox
from tkinter import ttk,font
class Aplicacion():
    __ventana=None
    __cantidad=None
    __precioAñoBase=None
    __precionActual=None
    
    
    
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title("Indices de precios al consuidor (IPC)")
        self.__ventana.resizable(0,0)
        self.marco=ttk.Frame(self.__ventana,padding=(10,10))
        self.__ipc=StringVar()
        ttk.Label(self.__ventana,textvariable=self.__ipc).grid(column=1,row=5,sticky=(W,E))
        ttk.Label(self.__ventana,text="IPC %").grid(column=0,row=5,sticky=W)
        self.__ItemLbl=ttk.Label(self.__ventana,text="Item" ,padding=(10,10))
        self.__vestimentaLbl=ttk.Label(self.__ventana,text="Vestimenta",padding=(10,10))
        self.__AlimentosLbl=ttk.Label(self.__ventana,text="Alimento",padding=(10,10))
        self.__EducacionLbl=ttk.Label(self.__ventana,text="Educacion",padding=(10,10))
        self.__cantidadLbl=ttk.Label(self.__ventana,text="Cantidad",padding=(10,10))
        self.__PrecioBaceLbl=ttk.Label(self.__ventana,text="Precio Año Bace",padding=(10,10))
        self.__PrecioActualLbl=ttk.Label(self.__ventana,text="Precion Año Actual",padding=(10,10))
        self.ctext1=ttk.Entry(self.__ventana,textvariable=self.__cantidad,width=20)
        self.ctext2=ttk.Entry(self.__ventana,textvariable=self.__cantidad,width=20)
        self.ctext3=ttk.Entry(self.__ventana,textvariable=self.__cantidad,width=20)
        self.ctext4=ttk.Entry(self.__ventana,textvariable=self.__precioAñoBase,width=20)
        self.ctext5=ttk.Entry(self.__ventana,textvariable=self.__precioAñoBase,width=20)
        self.ctext6=ttk.Entry(self.__ventana,textvariable=self.__precioAñoBase,width=20)
        self.ctext7=ttk.Entry(self.__ventana,textvariable=self.__precionActual,width=20)
        self.ctext8=ttk.Entry(self.__ventana,textvariable=self.__precionActual,width=20)
        self.ctext9=ttk.Entry(self.__ventana,textvariable=self.__precionActual,width=20)
        self.boton1=ttk.Button(self.__ventana,text="Calcular IPC",command=self.calcular)
        self.boton2=ttk.Button(self.__ventana,text="Salir",command=quit)
        self.__ItemLbl.grid(column=0,row=0)
        self.__cantidadLbl.grid(column=1,row=0)
        self.__PrecioBaceLbl.grid(column=2,row=0)
        self.__PrecioActualLbl.grid(column=3,row=0)
        self.__vestimentaLbl.grid(column=0,row=1)
        self.ctext1.grid(row=1,column=1)
        self.ctext2.grid(row=1,column=2)
        self.ctext3.grid(row=1,column=3)
        self.__AlimentosLbl.grid(row=2,column=0)
        self.ctext4.grid(row=2,column=1)
        self.ctext5.grid(row=2,column=2)
        self.ctext6.grid(row=2,column=3)
        self.__EducacionLbl.grid(row=3,column=0)
        self.ctext7.grid(row=3,column=1)
        self.ctext8.grid(row=3,column=2)
        self.ctext9.grid(row=3,column=3)
        
        self.boton1.grid(row=4,column=3)
        self.boton2.grid(row=4,column=2)
        
        self.__ventana.mainloop()
    def calcular(self):
        costoBase=(int(self.ctext1.get())*int(self.ctext4.get()))+(int(self.ctext2.get())*int(self.ctext5.get()))+(int(self.ctext3.get())*int(self.ctext6.get()))
        costoAcual=(int(self.ctext1.get())*int(self.ctext7.get()))+(int(self.ctext2.get())*int(self.ctext8.get()))+(int(self.ctext3.get())*int(self.ctext9.get()))
        costootal=int(costoAcual)/int(costoBase)
        total=costootal*100
        self.__ipc.set(total)