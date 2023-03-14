from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("Calculator")
root.geometry("340x440")
root["bg"] = "#EAFDFC"

myfont = font.Font(size=18)
fontbtn = font.Font(size=10)

e = Entry(root, width=22, borderwidth=0)
e["font"] = myfont
e["bg"] = "#BAD7E9"
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

def angka(nilai):
    sebelum = e.get()
    e.delete(0,END)
    e.insert(0,str(sebelum)+str(nilai))
def tambah():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "penjumlahan"
    n_awal = float(nomor_awal)
    e.delete(0, END)
def kurang():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pengurangan"
    n_awal = float(nomor_awal)
    e.delete(0, END)
def kali():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "perkalian"
    n_awal = float(nomor_awal)
    e.delete(0, END)
def bagi():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pembagian"
    n_awal = float(nomor_awal)
    e.delete(0, END)
def pangkat():
    nomor_awal = e.get()
    global n_awal
    n_awal = float(nomor_awal)
    e.delete(0, END)
    e.insert(0,n_awal **2)
def akar():
    nomor_awal = e.get()
    global n_awal
    n_awal = float(nomor_awal)
    e.delete(0, END)
    e.insert(0,math.sqrt(n_awal))
def sisabagi():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "sisabagi"
    n_awal = float(nomor_awal)
    e.delete(0, END)
def hapus():
    e.delete(0,END)
def samadengan():
    nomor_akhir = e.get()
    e.delete(0,END)
    if mtk == "penjumlahan":
        hitung= n_awal + float(nomor_akhir)
        hasil= round(hitung,5)
        e.insert(0,hasil)
    elif mtk == "pengurangan":
        hitung= n_awal - float(nomor_akhir)
        hasil= round(hitung,5)
        e.insert(0,hasil)
    elif mtk == "perkalian":
        hitung= n_awal * float(nomor_akhir)
        hasil= round(hitung,5)
        e.insert(0,hasil)
    elif mtk == "pembagian":
        try:
            hitung= n_awal / float(nomor_akhir)
            hasil= round(hitung,5)
            e.insert(0,hasil)
        except ZeroDivisionError:
            e.insert(0,'Cannot be divided by 0')
    elif mtk == "sisabagi":
        hitung= n_awal % float(nomor_akhir)
        hasil= round(hitung,5)
        e.insert(0,hasil)
def desimal():
    current = e.get()
    if '.' not in current:
        e.insert(END, '.')
def hapusSatu():
    current = e.get()
    e.delete(len(current)-1, END)



btn1  = Button(root,text="1",padx = 30,bg="#BFEAF5",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=lambda:angka(1))
btn2  = Button(root,text="2",padx = 30,bg="#BFEAF5",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=lambda:angka(2))
btn3  = Button(root,text="3",padx = 30,bg="#BFEAF5",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=lambda:angka(3))
btn4  = Button(root,text="4",padx = 30,bg="#BFEAF5",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=lambda:angka(4))
btn5  = Button(root,text="5",padx = 30,bg="#BFEAF5",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=lambda:angka(5))
btn6  = Button(root,text="6",padx = 30,bg="#BFEAF5",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=lambda:angka(6))
btn7  = Button(root,text="7",padx = 30,bg="#BFEAF5",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=lambda:angka(7))
btn8  = Button(root,text="8",padx = 30,bg="#BFEAF5",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=lambda:angka(8))
btn9  = Button(root,text="9",padx = 30,bg="#BFEAF5",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=lambda:angka(9))
btn0  = Button(root,text="0",padx = 30,bg="#BFEAF5",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=lambda:angka(0))
tam  = Button(root,text="+",padx = 30,bg="#91D8E4",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=tambah)
ak2  = Button(root,text="sq2",padx = 30,bg="#91D8E4",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=akar)
sisa  = Button(root,text="%",padx = 30,bg="#91D8E4",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=sisabagi)
pang  = Button(root,text="^2",padx = 30,bg="#91D8E4",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=pangkat)
kur  = Button(root,text="-",padx = 30,bg="#91D8E4",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=kurang)
kal  = Button(root,text="x",padx = 30,bg="#91D8E4",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=kali)
bag  = Button(root,text="/",padx = 30,bg="#91D8E4",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=bagi)
hap  = Button(root,text="C",padx = 30,bg="#91D8E4",fg="black",pady = 15,borderwidth= 0,font=fontbtn,command=hapus)
sama  = Button(root,text="=",padx = 130,bg="#0A2647",fg="white",pady = 15, borderwidth= 0,font=fontbtn, command=samadengan)
hap1 = Button(root,text="<-",padx = 30,bg="#91D8E4",fg="black", pady = 15, borderwidth= 0,font=fontbtn, command=hapusSatu)
dec = Button(root,text=".",padx = 30,bg="#91D8E4",fg="black", pady = 15, borderwidth= 0,font=fontbtn, command=desimal)


btn1.grid(row=4,column=0,pady=2,padx=2)
btn2.grid(row=4,column=1,pady=2,padx=2)
btn3.grid(row=4,column=2,pady=2,padx=2)
btn4.grid(row=3,column=0,pady=2,padx=2)
btn5.grid(row=3,column=1,pady=2,padx=2)
btn6.grid(row=3,column=2,pady=2,padx=2)
btn7.grid(row=2,column=0,pady=2,padx=2)
btn8.grid(row=2,column=1,pady=2,padx=2)
btn9.grid(row=2,column=2,pady=2,padx=2)
btn0.grid(row=5,column=1,pady=2,padx=2)

tam.grid(row=5,column=3,pady=2,padx=2)
kur.grid(row=4,column=3,pady=2,padx=2)
kal.grid(row=3,column=3,pady=2,padx=2)
bag.grid(row=2,column=3,pady=2,padx=2)
hap.grid(row=1,column=2,pady=2,padx=2)
sama.grid(row=6,column=0,pady=4,padx=2, columnspan=4)
ak2.grid(row=1,column=0,pady=2,padx=2)
sisa.grid(row=5,column=0,pady=2,padx=2)
pang.grid(row=1,column=1,pady=2,padx=2)
hap1.grid(row=1, column=3, pady=2,padx=2)
dec.grid(row=5, column=2, pady=2,padx=2)




root.mainloop()