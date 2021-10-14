# Calculadora Python - um clássica calculadora.

from tkinter import *

# Instanciando a classe
master = Tk()

# Nomeando o title do programa
master.title("Calculadora em Python")

# Colocando o ícone ao lado do título (não renderizou corretamente)
master.iconbitmap(default="calculator.icon.png")

# Redimensionamento e Posicionamento de tela - Largura x Altura + dist esquerda + dist topo
master.geometry("557x721+505+0")

# Travando o redimensionamento
#master.wm_resizable(width=False, height=False)


#Importando Imagens
calculadoraImg = PhotoImage(file="calculadora.png")

# # Criação de Labels
fundoCalculadora = Label(master, image=calculadoraImg)
resposta = Label(master, font="Arial 40", text="0")
titulo = Label(master, font="Arial 20", text="Calculadora Python")
# labelCalculadora = Label(master, image=calculadoraImg)
# labelCalculadora.place(x=0, y=0)

# Posicionando Labels
fundoCalculadora.place(x=0, y=0)
resposta.place(width = 440, height = 94, x=57, y=188)
titulo.place(width = 445, height = 32, x=55, y=35)

# Criação dos botões
bt1 = Button(master, text="+", font="Arial 20", command=lambda: calcular(1))
bt2 = Button(master, text="-", anchor=S, font="Arial 20",  command=lambda: calcular(2))
bt3 = Button(master, text="/", font="Arial 20", command=lambda: calcular(3))
bt4 = Button(master, text="x", anchor=N, font="Arial 20", command=lambda: calcular(4))

# Posicionamento de botões
bt1.place(width = 90, height = 44, x=56, y=601)
bt2.place(width = 90, height = 44, x=180, y=601)
bt3.place(width = 90, height = 44, x=303, y=601)
bt4.place(width = 90, height = 44, x=421, y=601)

# Caixas de Entrada
num1 = Entry(master, font="Arial 20", justify=CENTER)
num2 = Entry(master, font="Arial 20", justify=CENTER)

# Posicionamento das caixas de entrada
num1.place(width = 191, height = 45, x=59, y=393)
num2.place(width = 189, height = 41, x=302, y=395)

# Valores iniciais das caixas de entrada
num1.insert(END, 0)
num2.insert(END, 0)


# Variáveis Globais - Utilizada para a função balizadora clique_esq_mouse
flag = x1 = y1 = x = 0


# Funções
def calcular(op):
    global resposta, num1, num2, x

    try:
        float(num1.get())
        float(num2.get())

        if op == 1:
            x = float(num1.get()) + float(num2.get())

        elif op == 2:
            x = float(num1.get()) - float(num2.get())

        elif op == 3:
            try:
                x = float(num1.get()) / float(num2.get())
            except ZeroDivisionError:
                x = 999999999999

        elif op == 4:
            x = float(num1.get()) * float(num2.get())

        return resposta.config(text=round(x, 4)) # Redefine o texto inicial para a resposta final com 4 casas

    except ValueError:
        resposta.config(text="Só números!!!")


# Mostrar as coordenadas corretas para inserção de botões e labels
def clique_esq_mouse(arg):
    global flag, x1, y1
    flag = not flag

    if flag:
        x1 = arg.x
        y1 = arg.y

    else:
        print(f'width = {arg.x - x1}, height = {arg.y - y1}, x={x1}, y={y1}')

# Mostra as coordenadas da tela ao clicar com o botão esquerdo sobre ela - ótima função para verificar o redimensionamento de tela
# def clique_esq_mouse(retorno):
#     print(f'X:{retorno.x} | Y:{retorno.y} Geo:{master.geometry()}') # Sem formatação fica - print(retorno)



# Eventos
master.bind("<Button-1>", clique_esq_mouse)




# Mantém em loop a visualização da janela do programa
master.mainloop()

