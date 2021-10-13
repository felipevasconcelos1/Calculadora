# Importando tkinter
from tkinter import *
from tkinter import ttk


# Cores - Color pick (Google)
black = '#1e1f1e'
white = '#feffff'
blue = '#38576b'
gray = '#ECEFF1'
orange = '#FFAB40'

# Criando a janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=black)

# Primeiro frame
frame_tela = Frame(janela, width=235, height=50, bg=blue)
frame_tela.grid(row=0, column=0)

# Segundo frame
frame_corpo = Frame(janela, width=235, height=268, bg=gray)
frame_corpo.grid(row=1, column=0)


# Variavel todos_valores
todos_valores = ''
valor_texto = StringVar()

# Criando função
def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)
    # Passando o valor para a tela
    valor_texto.set(todos_valores)


# Função de cálculo
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))


# Função C
def apagar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')


# Criando label
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=blue, fg=white)
app_label.place(x=0, y=0)

# Criando botões
botao_C = Button(frame_corpo, command=apagar_tela, text='C', width=11, height=2, bg=gray, relief=RAISED, overrelief=RIDGE, font=('Ivy 13 bold'))
botao_C.place(x=0, y=0)
botao_modulo = Button(frame_corpo, command=lambda: entrar_valores('%'), text='%', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_modulo.place(x=118, y=0)
botao_divisao = Button(frame_corpo, command=lambda: entrar_valores('/'), text='/', width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_divisao.place(x=177, y=0)

botao_7 = Button(frame_corpo, command=lambda: entrar_valores('7'), text='7', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_7.place(x=0, y=52)
botao_8 = Button(frame_corpo, command=lambda: entrar_valores('8'), text='8', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_8.place(x=59, y=52)
botao_9 = Button(frame_corpo, command=lambda: entrar_valores('9'), text='9', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_9.place(x=118, y=52)
botao_multi = Button(frame_corpo, command=lambda: entrar_valores('*'), text='*', width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_multi.place(x=177, y=52)

botao_4 = Button(frame_corpo, command=lambda: entrar_valores('4'), text='4', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_4.place(x=0, y=104)
botao_5 = Button(frame_corpo, command=lambda: entrar_valores('5'), text='5', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_5.place(x=59, y=104)
botao_6 = Button(frame_corpo, command=lambda: entrar_valores('6'), text='6', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_6.place(x=118, y=104)
botao_sub = Button(frame_corpo, command=lambda: entrar_valores('-'), text='-', width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_sub.place(x=177, y=104)

botao_1 = Button(frame_corpo, command=lambda: entrar_valores('1'), text='1', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_1.place(x=0, y=156)
botao_2 = Button(frame_corpo, command=lambda: entrar_valores('2'), text='2', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_2.place(x=59, y=156)
botao_3 = Button(frame_corpo, command=lambda: entrar_valores('3'), text='3', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_3.place(x=118, y=156)
botao_soma = Button(frame_corpo, command=lambda: entrar_valores('+'), text='+', width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_soma.place(x=177, y=156)

botao_0 = Button(frame_corpo, command=lambda: entrar_valores('0'), text='0', width=11, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_0.place(x=0, y=208)
botao_ponto = Button(frame_corpo, command=lambda: entrar_valores('.'), text='.', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_ponto.place(x=118, y=208)
botao_igual = Button(frame_corpo, command=calcular, text='=', width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_igual.place(x=177, y=208)




janela.mainloop()
