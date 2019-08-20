# -*- coding: utf-8 -*-
"""

- Cria aleatoriamente um numero de 4 digitos

- Pede ao usuario 4 digitos (de forma separada)

- Retorna ao usuario bolinhas brancas (caso tenha algum numero certo, mas na posicao errada, e preta caso tenha um numero certo
na posicao certa)

- Da 10 tentativas ao usuario


"""

import random
from tkinter import *

root = Tk()
#--------DEFINICAO PAGINA INICIAL----------
root.geometry("1000x500+300+300")
root["bg"] = "cyan"
root.title("SENHA")

#---------FUNCOES PAGINA INICIAL---------
def regras():
    regras_lb.place(x=40, y=280)
    regras_bt["command"] = regras2
def regras2():
    regras_lb.place(x=-400, y=-400)
    regras_bt["command"] = regras
def jogar():
    root.destroy()
def corno():
    corno_lb.place(x=300, y=200)
    corno_bt["command"] = corno2
def corno2():
    corno_lb.place(x=-300, y=-200)
    corno_bt["command"] = corno
    






#--------WIDGETS PAGINA INICIAL---------
titulo_lb = Label(root, text = "SENHA", font = "Arial 44", bg = "cyan")
titulo_lb.place(x=390, y = 30)
regras_bt = Button(root, width=20, text="Regras", bg = "green", command = regras)
regras_bt.place(x=320, y=420)
jogar_bt = Button(root, width=20, text="Jogar", bg = "green", command = jogar)
jogar_bt.place(x=490, y=420)
regras_lb = Label(root, text = "Uma senha aleatoria de 4 digitos sera gerada, voce tem 10 chances para acerta-la!\n Para isso o jogo ira te dar dicas, ao colocar uma senha voce ira receber um feedback em numeros,\n caso voce tenha acertado um numero, mas o mesmo esta no lugar errado um numero 1 ira aparecer,\n caso voce acerte o numero no lugar certo, um O ira aparecer,\n caso voce acerte a senha voce ganha o jogo!", font = "Arial 15", bg = "cyan")
#regras_lb.place(x=40, y=280)
regras_lb.place(x=-400, y=-400)
#oqquiser_et = Entry(root, width = 10)
#oqquiser_et.place(x=470, y=100)
corno_bt = Button(root, width=20, text='Aperte aqui', command = corno, bg = "green")
corno_bt.place(x=390, y=150)
corno_lb = Label(root, text="Tenorio é corno", font = "Arial 44", bg = "cyan")


root.mainloop()


#---------PAGINA DO JOGO-----------

pagina = Tk()
pagina.geometry("1000x500+300+300")
pagina["bg"] = "cyan"
pagina.title("SENHA")

s1 = [random.randint(0, 9), 1]
s2 = [s1[0], 2]
s3 = [s1[0], 3]
s4 = [s1[0], 4]
while s2[0] == s1[0]:
    s2[0] = random.randint(0, 9)
while s3[0] == s2[0] or s3[0] == s1[0]:
    s3[0] = random.randint(0, 9)
while s4[0] == s3[0] or s4[0] == s2[0] or s4[0] == s1[0]:
    s4[0] = random.randint(0, 9)


print(s1[0], s2[0], s3[0], s4[0])
i = 1

#--------FUNCOES-----------------  


def pegarSenha():
    global s1, s2, s3, s4, i, vencer, su1, su2, su3, su4
    su1 = [int(e1_et.get()), 1]
    su2 = [int(e2_et.get()), 2]
    su3 = [int(e3_et.get()), 3]
    su4 = [int(e4_et.get()), 4]

    if i == 1:
        cc["text"] += str(su1[0])+str(su2[0])+str(su3[0])+str(su4[0])+"  "
    if i == 2:
        cc2["text"] += str(su1[0])+str(su2[0])+str(su3[0])+str(su4[0])+"  "
    if i == 3:
        cc3["text"] += str(su1[0])+str(su2[0])+str(su3[0])+str(su4[0])+"  "
    if i == 4:
        cc4["text"] += str(su1[0])+str(su2[0])+str(su3[0])+str(su4[0])+"  "    
    if i == 5:
        cc5["text"] += str(su1[0])+str(su2[0])+str(su3[0])+str(su4[0])+"  "
    if i == 6:
        cc6["text"] += str(su1[0])+str(su2[0])+str(su3[0])+str(su4[0])+"  "       
    if i == 7:
        cc7["text"] += str(su1[0])+str(su2[0])+str(su3[0])+str(su4[0])+"  "
    if i == 8:
        cc8["text"] += str(su1[0])+str(su2[0])+str(su3[0])+str(su4[0])+"  "
    if i == 9:
        cc9["text"] += str(su1[0])+str(su2[0])+str(su3[0])+str(su4[0])+"  "
    if i == 10:
        cc10["text"] += str(su1[0])+str(su2[0])+str(su3[0])+str(su4[0])+"  "




    if su1 == s1:
        if i == 1:
            cc["text"] += " O"
        if i == 2:
            cc2["text"] += " O"
        if i == 3:
            cc3["text"] += " O"
        if i == 4:
            cc4["text"] += " O"
        if i == 5:
            cc5["text"] += " O"
        if i == 6:
            cc6["text"] += " O"
        if i == 7:
            cc7["text"] += " O"
        if i == 8:
            cc8["text"] += " O"
        if i == 9:
            cc9["text"] += " O"
        if i == 10:
            cc10["text"] += " O"   
    if su2 == s2:
        if i == 1:
            cc["text"] += " O"
        if i == 2:
            cc2["text"] += " O"
        if i == 3:
            cc3["text"] += " O"
        if i == 4:
            cc4["text"] += " O"
        if i == 5:
            cc5["text"] += " O"
        if i == 6:
            cc6["text"] += " O"
        if i == 7:
            cc7["text"] += " O"
        if i == 8:
            cc8["text"] += " O"
        if i == 9:
            cc9["text"] += " O"
        if i == 10:
            cc10["text"] += " O"   
    if su3 == s3:
        if i == 1:
            cc["text"] += " O"
        if i == 2:
            cc2["text"] += " O"
        if i == 3:
            cc3["text"] += " O"
        if i == 4:
            cc4["text"] += " O"
        if i == 5:
            cc5["text"] += " O"
        if i == 6:
            cc6["text"] += " O"
        if i == 7:
            cc7["text"] += " O"
        if i == 8:
            cc8["text"] += " O"
        if i == 9:
            cc9["text"] += " O"
        if i == 10:
            cc10["text"] += " O"    
    if su4 == s4:
        if i == 1:
            cc["text"] += " O"
        if i == 2:
            cc2["text"] += " O"
        if i == 3:
            cc3["text"] += " O"
        if i == 4:
            cc4["text"] += " O"
        if i == 5:
            cc5["text"] += " O"
        if i == 6:
            cc6["text"] += " O"
        if i == 7:
            cc7["text"] += " O"
        if i == 8:
            cc8["text"] += " O"
        if i == 9:
            cc9["text"] += " O"
        if i == 10:
            cc10["text"] += " O" 
        
    if su1[0] == s2[0] and su1[0] != s1[0]:
        if i == 1:
            cc["text"] += " 1"
        if i == 2:
            cc2["text"] += " 1"
        if i == 3:
            cc3["text"] += " 1"
        if i == 4:
            cc4["text"] += " 1"
        if i == 5:
            cc5["text"] += " 1"
        if i == 6:
            cc6["text"] += " 1"
        if i == 7:
            cc7["text"] += " 1"
        if i == 8:
            cc8["text"] += " 1"
        if i == 9:
            cc9["text"] += " 1"
        if i == 10:
            cc10["text"] += " 1"
    elif su1[0] == s3[0] and su1[0] != s1[0]:
        if i == 1:
            cc["text"] += " 1"
        if i == 2:
            cc2["text"] += " 1"
        if i == 3:
            cc3["text"] += " 1"
        if i == 4:
            cc4["text"] += " 1"
        if i == 5:
                cc5["text"] += " 1"
        if i == 6:
            cc6["text"] += " 1"
        if i == 7:
            cc7["text"] += " 1"
        if i == 8:
            cc8["text"] += " 1"
        if i == 9:
            cc9["text"] += " 1"
        if i == 10:
            cc10["text"] += " 1"
    elif su1[0] == s4[0] and su1[0] != s1[0]: 
        if i == 1:
            cc["text"] += " 1"
        if i == 2:
            cc2["text"] += " 1"
        if i == 3:
            cc3["text"] += " 1"
        if i == 4:
            cc4["text"] += " 1"
        if i == 5:
            cc5["text"] += " 1"
        if i == 6:
            cc6["text"] += " 1"
        if i == 7:
            cc7["text"] += " 1"
        if i == 8:
            cc8["text"] += " 1"
        if i == 9:
            cc9["text"] += " 1"
        if i == 10:
            cc10["text"] += " 1"
    if su2[0] == s1[0] and su2[0] != s2[0]:
        if i == 1:
            cc["text"] += " 1"
        if i == 2:
            cc2["text"] += " 1"
        if i == 3:
            cc3["text"] += " 1"
        if i == 4:
            cc4["text"] += " 1"
        if i == 5:
            cc5["text"] += " 1"
        if i == 6:
            cc6["text"] += " 1"
        if i == 7:
            cc7["text"] += " 1"
        if i == 8:
            cc8["text"] += " 1"
        if i == 9:
            cc9["text"] += " 1"
        if i == 10:
            cc10["text"] += " 1"
    elif su2[0] == s3[0] and su2[0] != s2[0]:
        if i == 1:
            cc["text"] += " 1"
        if i == 2:
            cc2["text"] += " 1"
        if i == 3:
            cc3["text"] += " 1"
        if i == 4:
            cc4["text"] += " 1"
        if i == 5:
            cc5["text"] += " 1"
        if i == 6:
            cc6["text"] += " 1"
        if i == 7:
            cc7["text"] += " 1"
        if i == 8:
            cc8["text"] += " 1"
        if i == 9:
            cc9["text"] += " 1"
        if i == 10:
            cc10["text"] += " 1"
    elif su2[0] == s4[0] and su2[0] != s2[0]:
        if i == 1:
            cc["text"] += " 1"
        if i == 2:
            cc2["text"] += " 1"
        if i == 3:
            cc3["text"] += " 1"
        if i == 4:
            cc4["text"] += " 1"
        if i == 5:
            cc5["text"] += " 1"
        if i == 6:
            cc6["text"] += " 1"
        if i == 7:
            cc7["text"] += " 1"
        if i == 8:
            cc8["text"] += " 1"
        if i == 9:
            cc9["text"] += " 1"
        if i == 10:
            cc10["text"] += " 1"
    if su3[0] == s1[0] and su3[0] != s3[0]:
        if i == 1:
            cc["text"] += " 1"
        if i == 2:
            cc2["text"] += " 1"
        if i == 3:
            cc3["text"] += " 1"
        if i == 4:
            cc4["text"] += " 1"
        if i == 5:
            cc5["text"] += " 1"
        if i == 6:
            cc6["text"] += " 1"
        if i == 7:
            cc7["text"] += " 1"
        if i == 8:
            cc8["text"] += " 1"
        if i == 9:
            cc9["text"] += " 1"
        if i == 10:
            cc10["text"] += " 1"
    elif su3[0] == s2[0] and su3[0] != s3[0]:
        if i == 1:
            cc["text"] += " 1"
        if i == 2:
            cc2["text"] += " 1"
        if i == 3:
            cc3["text"] += " 1"
        if i == 4:
            cc4["text"] += " 1"
        if i == 5:
            cc5["text"] += " 1"
        if i == 6:
            cc6["text"] += " 1"
        if i == 7:
            cc7["text"] += " 1"
        if i == 8:
            cc8["text"] += " 1"
        if i == 9:
            cc9["text"] += " 1"
        if i == 10:
            cc10["text"] += " 1"
    elif su3[0] == s4[0] and su3[0] != s3[0]:
        if i == 1:
            cc["text"] += " 1"
        if i == 2:
            cc2["text"] += " 1"
        if i == 3:
            cc3["text"] += " 1"
        if i == 4:
            cc4["text"] += " 1"
        if i == 5:
            cc5["text"] += " 1"
        if i == 6:
            cc6["text"] += " 1"
        if i == 7:
            cc7["text"] += " 1"
        if i == 8:
            cc8["text"] += " 1"
        if i == 9:
            cc9["text"] += " 1"
        if i == 10:
            cc10["text"] += " 1"
    if su4[0] == s1[0] and su4[0] != s4[0]:
        if i == 1:
            cc["text"] += " 1"
        if i == 2:
            cc2["text"] += " 1"
        if i == 3:
            cc3["text"] += " 1"
        if i == 4:
            cc4["text"] += " 1"
        if i == 5:
            cc5["text"] += " 1"
        if i == 6:
            cc6["text"] += " 1"
        if i == 7:
            cc7["text"] += " 1"
        if i == 8:
            cc8["text"] += " 1"
        if i == 9:
            cc9["text"] += " 1"
        if i == 10:
            cc10["text"] += " 1"
    elif su4[0] == s2[0] and su4[0] != s4[0]:
        if i == 1:
            cc["text"] += " 1"
        if i == 2:
            cc2["text"] += " 1"
        if i == 3:
            cc3["text"] += " 1"
        if i == 4:
            cc4["text"] += " 1"
        if i == 5:
            cc5["text"] += " 1"
        if i == 6:
            cc6["text"] += " 1"
        if i == 7:
            cc7["text"] += " 1"
        if i == 8:
            cc8["text"] += " 1"
        if i == 9:
            cc9["text"] += " 1"
        if i == 10:
            cc10["text"] += " 1"
    elif su4[0] == s3[0] and su4[0] != s4[0]:
        if i == 1:
            cc["text"] += " 1"
        if i == 2:
            cc2["text"] += " 1"
        if i == 3:
            cc3["text"] += " 1"
        if i == 4:
            cc4["text"] += " 1"
        if i == 5:
            cc5["text"] += " 1"
        if i == 6:
            cc6["text"] += " 1"
        if i == 7:
            cc7["text"] += " 1"
        if i == 8:
            cc8["text"] += " 1"
        if i == 9:
            cc9["text"] += " 1"
        if i == 10:
            cc10["text"] += " 1"
    i+= 1
    print (i)
    if su1 == s1 and su2 == s2 and su3 == s3 and su4 == s4:
        pagina.destroy()
        vencer = 1
    if i == 11:
        pagina.destroy()
        vencer = 0
        
        




#----------WIDGETS------------
titulo_lb = Label(pagina, text = "SENHA", font = "Arial 44", bg = "cyan")
titulo_lb.place(x=390, y = 30)
inserir_bt = Button(pagina, width = 20, text = "Inserir", command = pegarSenha)
inserir_bt.place(x=390, y = 150)


#-----ENTRYS------

e1_et = Entry(pagina, width = 5)
e1_et.place(x=390, y=100)
e2_et = Entry(pagina, width = 5)
e2_et.place(x=420, y=100)
e3_et = Entry(pagina, width = 5)
e3_et.place(x=450, y=100)
e4_et = Entry(pagina, width = 5)
e4_et.place(x=480, y=100)

#------LABELS------
cc = Label(pagina, text = "Tentativa 1:  ", font = "Arial 20", bg = "cyan")
cc.place(x = 390, y = 200)

cc2 = Label(pagina, text = "Tentativa 2:  ", font = "Arial 20", bg = "cyan")
cc2.place(x = 390, y = 230)

cc3 = Label(pagina, text = "Tentativa 3:  ", font = "Arial 20", bg = "cyan")
cc3.place(x = 390, y = 260)

cc4 = Label(pagina, text = "Tentativa 4:  ", font = "Arial 20", bg = "cyan")
cc4.place(x = 390, y = 290)

cc5 = Label(pagina, text = "Tentativa 5:  ", font = "Arial 20", bg = "cyan")
cc5.place(x = 390, y = 320)

cc6 = Label(pagina, text = "Tentativa 6:  ", font = "Arial 20", bg = "cyan")
cc6.place(x = 390, y = 350)

cc7 = Label(pagina, text = "Tentativa 7:  ", font = "Arial 20", bg = "cyan")
cc7.place(x = 390, y = 380)

cc8 = Label(pagina, text = "Tentativa 8:  ", font = "Arial 20", bg = "cyan")
cc8.place(x = 390, y = 410)

cc9 = Label(pagina, text = "Tentativa 9:  ", font = "Arial 20", bg = "cyan")
cc9.place(x = 390, y = 440)

cc10 = Label(pagina, text = "Tentativa 10:  ", font = "Arial 20", bg = "cyan")
cc10.place(x = 390, y = 470)

pagina.mainloop()


vencedor = Tk()
vencedor.geometry("1000x500+300+300")
vencedor["bg"] = "cyan"
vencedor.title("SENHA")

vencedor_lb = Label(vencedor, text = "Voce venceu! A senha era {}".format(str(s1[0])+str(s2[0])+str(s3[0])+str(s4[0])), bg = "cyan", font = "Arial 40")
perdedor_lb = Label(vencedor, text = "Voce perdeu! A senha era: {}\n e sua resposta final foi: {}".format(str(s1[0])+str(s2[0])+str(s3[0])+str(s4[0]), str(su1[0])+str(su2[0])+str(su3[0])+str(su4[0])), bg = "cyan", font = "Arial 40")

if vencer == 0:
    perdedor_lb.place(x = 10, y = 200)
if vencer == 1:
    vencedor_lb.place(x = 10, y = 200)

vencedor.mainloop()






















