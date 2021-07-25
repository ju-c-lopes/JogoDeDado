import tkinter as tk
from random import randint

window = tk.Tk()
b = '\u26AB'

lados = [
	[(' ', ' ', ' '),(' ', b, ' '),(' ', ' ', ' ')],
	[(b, ' ', ' '),(' ', ' ', ' '),(' ', ' ', b)],
	[(b, ' ', ' '),(' ', b, ' '),(' ', ' ', b)],
	[(b, ' ', b),(' ', ' ', ' '),(b, ' ', b)],
	[(b, ' ', b),(' ', b, ' '),(b, ' ', b)],
	[(b, ' ', b),(b, ' ', b),(b, ' ', b)],
	]


canvas = tk.Canvas(window, width=120, height=160)
canvas.grid(rowspan=4, columnspan=3)


def formar():
	jogada = randint(0, 5)

	for linha in range(3):
		for quadro in range(3):
			label = tk.Label(window, text=' ')
			label.grid(row=linha, column=quadro)

	for linha in range(3):
		for quadro in range(3):
			label = tk.Label(window, text=lados[jogada][linha][quadro])
			label.grid(row=linha, column=quadro)


texto = tk.StringVar()
botao = tk.Button(window, textvariable=texto, command=lambda: formar(), font="Arial", bg="#ddd", fg="#444")
texto.set("Jogar")
botao.grid(row=3, column=1)
		

window.mainloop()
