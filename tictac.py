import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.turno = 'X'
        self.tabla = [['', '', ''], ['', '', ''], ['', '', '']]
        
        self.pantalla = tk.Tk()
        
        self.botones = []
        for fila in range(3):
            fila_botones = []
            for columna in range(3):
                boton = tk.Button(self.pantalla, text='', font=('Arial', 30), width=3, height=1, command= lambda f=fila, c=columna: self.click(fila=f, columna=c))
                boton.grid(row=fila, column=columna)
                fila_botones.append(boton)
            self.botones.append(fila_botones)
        
        self.mensaje_turno = tk.Label(self.pantalla, text=f'Jugador {self.turno}', font=('Arial', 20))
        self.mensaje_turno.grid(row=3, columnspan=3)
        
    def click(self, fila, columna):
        if self.tabla[fila][columna] == '':
            self.tabla[fila][columna] = self.turno
            self.botones[fila][columna].config(text=self.turno)
            if self.ganador():
                self.bloquear_botones()
            elif self.empate():
                self.bloquear_botones()
            else:
                if self.turno == 'X':
                    self.turno = 'O'
                else:
                    self.turno = 'X'
            self.botones[fila][columna].config(state='disabled')
            self.mensaje_turno.config(text=f'Jugador {self.turno}')
        
    def ganador(self):
        for i in range(3):
            if self.tabla[i][0] == self.tabla[i][1] == self.tabla[i][2] != '':
                self.botones[i][0].config(bg="green")
                self.botones[i][1].config(bg="green")
                self.botones[i][2].config(bg="green")
                return True
            if self.tabla[0][i] == self.tabla[1][i] == self.tabla[2][i] != '':
                self.botones[0][i].config(bg="green")
                self.botones[1][i].config(bg="green")
                self.botones[2][i].config(bg="green")
                return True
        if self.tabla[0][0] == self.tabla[1][1] == self.tabla[2][2] != '':
            self.botones[0][0].config(bg="green")
            self.botones[1][1].config(bg="green")
            self.botones[2][2].config(bg="green")
            return True
        if self.tabla[0][2] == self.tabla[1][1] == self.tabla[2][0] != '':
            self.botones[0][2].config(bg="green")
            self.botones[1][1].config(bg="green")
            self.botones[2][0].config(bg="green")
            return True
        return False
        
    def empate(self):
        for fila in self.tabla:
            for boton in fila:
                if boton == '':
                    return False
        for fila in self.botones:
            for boton in fila:
                boton.config(bg="red")
        return True
        
    def bloquear_botones(self):
        for fila in self.botones:
            for button in fila:
                button.config(state='disabled')
        
game = TicTacToe()
game.pantalla.mainloop()
