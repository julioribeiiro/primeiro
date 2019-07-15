# -*- coding: utf-8 -*-
from tkinter import *
from functools import partial
import time


#--------INSERINDO NOMES DOS JOGADORES PAGINA 1---------
def pegar_nomes():     # FUNÇAO PEGAR NOMES DOS JOGADORES
    global jogador1
    global jogador2
    jogador1 = et_nome1.get()
    jogador2 = et_nome2.get()
    root.destroy()


root = Tk()    #CONFIGURAÇAO PAGINA INICIAL
root.geometry("800x300+250+250")
root["bg"] = "white"
root.title("Jogo dos palitos, agora vai")


#LABELS, ENTRYS E BUTTONS PAGINA INICIAL


lbnomes = Label(root, text = "Digite o nome dos jogadores:", bg = "white")
lbnomes.place(x=190, y=100)
lb_nome1 = Label(root, text = "Jogador 1: ", bg = "white", relief=RAISED)
lb_nome1.place(x=137, y=130)
lb_nome2 = Label(root, text = "Jogador 2: ", bg = "white", relief=RAISED)
lb_nome2.place(x=137, y=160)

et_nome1 = Entry(root)
et_nome1.place(x=200, y=130)
et_nome2 = Entry(root)
et_nome2.place(x=200, y=160)

bt_nomes = Button(root, width=20, text="Confirmar", command = pegar_nomes)
bt_nomes.place(x=190, y=190)



root.mainloop()



#--------REMOVENDO PALITOS PAGINA 2-----------------
janela = Tk()
janela.geometry("800x300+250+250")
janela["bg"] = "white"
janela.title("Jogo dos Palitos, agora vai")

#FUNÇAO TIRA PALITO
def click():
    global vitoria
    a = int(espaco.get())
    global palitos_l
    global palitos_n
    palitos_n -= a
    palitos_l = "I "*palitos_n
    lb["text"] = "{} digite quantos palitos deseja retirar:".format(jogador2)
    bt["command"] = click2
    palitos["text"] = str(palitos_l)
    if a == 11031997:
        vitoria = jogador1
        janela.destroy()
    elif a <= 0 or a > 3 and a < 11031996:
        lb["text"] = "{} digitou um numero invalido, digite um numero de 1 a 3:".format(jogador1)
        bt["command"] = click
        palitos_n += a
        palitos_l = "I "*palitos_n
        palitos["text"] = str(palitos_l)
    elif palitos_n <= 0:
        vitoria = jogador2
        janela.destroy()
    
def click2():
    a = int(espaco.get())
    global vitoria
    global palitos_l
    global palitos_n
    palitos_n -= a
    palitos_l = "I "*palitos_n
    palitos["text"] = str(palitos_l)
    lb["text"] = "{} digite quantos palitos deseja retirar:".format(jogador1)
    bt["command"] = click
    if a == 11031997:
        vitoria = jogador2
        janela.destroy()
    elif a <= 0 or a > 3 and a < 110396:
        lb["text"] = "{} digitou um numero invalido, digite um numero de 1 a 3:".format(jogador2)
        bt["command"] = click2
        palitos_n += a
        palitos_l = "I "*palitos_n
        palitos["text"] = str(palitos_l)
    if palitos_n <= 0:
        vitoria = jogador1
        janela.destroy()
        
def corno():
    lb_corno["text"] = "Parabens, voce é corno! Você perdeu!!!"
    lb_corno["font"] = "Arial 12"
    
    



#LABELS, BUTTONS E ENTRYS
lb = Label(janela, text = "{} digite quantos palitos deseja retirar:".format(jogador1))
lb.place(x=200, y=100)
lb_corno = Label(janela, text = "")
lb_corno.place(x=200, y=250)

bt_corno = Button(janela, width=20, text="Aperte aqui se voce é corno.", command = corno)
bt_corno.place(x=100, y=50)
palitos_n = 21
palitos_l = "I I I I I I I I I I I I I I I I I I I I I"


ainda = Label(janela, text="Ainda restam:")
ainda.place(x=200, y=190)
palitos = Label(janela, text = str(palitos_l), font = "Arial 20")
palitos.place(x=285, y=190)

espaco = Entry(janela)
espaco.place(x=200, y=130)

bt = Button(janela, width=20, text="Tirar", command=click)
bt.place(x=200, y=160)

janela.mainloop()

#--------------PAGINA DE VITORIA-----------------
vit = Tk()
vit.geometry("800x300+250+250")
vit["bg"] = "white"
vit.title("Jogo dos Palitos, agora vai")

vitorioso = Label(vit, text = "VITORIA DO JOGADOR -> {}".format(vitoria), font = "Arial 30")
vitorioso.place(x=10, y=130)

vit.mainloop()


