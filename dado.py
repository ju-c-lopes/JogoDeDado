import tkinter as tk
from random import randint
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Jogue O Dado...')
img = Image.open('dice.png')
img = ImageTk.PhotoImage(img)
window.iconphoto(True, img)

b = Image.open('ball.png')
b = ImageTk.PhotoImage(b)
nb = Image.open('noball.png')
nb = ImageTk.PhotoImage(nb)

lados = [
	[(nb, nb, nb), (nb, b, nb), (nb, nb, nb)],
	[(b, nb, nb), (nb, nb, nb), (nb, nb, b)],
	[(b, nb, nb), (nb, b, nb), (nb, nb, b)],
	[(b, nb, b), (nb, nb, nb), (b, nb, b)],
	[(b, nb, b), (nb, b, nb), (b, nb, b)],
	[(b, nb, b), (b, nb, b), (b, nb, b)],
	]

canvas = tk.Canvas(window, width=350, height=470)
canvas.grid(rowspan=4, columnspan=3)


def formar():
	jogada = randint(0, 5)

	for linha in range(3):
		for quadro in range(3):
			label = tk.Label(window, text=' ')
			label.grid(row=linha, column=quadro)

	for linha in range(3):
		for quadro in range(3):
			label = tk.Label(window, image=lados[jogada][linha][quadro])
			label.grid(row=linha, column=quadro)


texto = tk.StringVar()
botao = tk.Button(
			window,
			textvariable=texto,
			command=lambda: formar(),
			font="Arial",
			bg="#ddd",
			fg="#444")
texto.set("Jogar")
botao.grid(row=3, column=1)

window.mainloop()
