from tkinter import *
class connect4:
    ACTIVE_COLOR = '#2E2A29'
    PASSIVE_COLOR = '#2BAE66'
    PASSIVE_COLOR_2 ='#2BAE66'
    def __init__(self, c, size, height=6, width=6):
        self.height = height
        self.width = width
        self.c = c
        self.size = size
        self.board_row = self.size // self.width
        self.board_columns = self.size // self.height
        self.board = [['' for x in range(width)] for i in range(height)]
        self.draw()
 
    def return_board(self):
        return self.board

    def get_column(self, index):
        return [i[index] for i in self.board]

    def get_row(self, index):
        return self.board[index]

    def get_diagonals(self):
        diagonals = []
        for p in range(self.height + self.width - 1):
            diagonals.append([])
            for q in range(max(p - self.height + 1, 0),
                           min(p + 1, self.height)):
                diagonals[p].append(self.board[self.height - p + q - 1][q])

        for p in range(self.height + self.width - 1):
            diagonals.append([])
            for q in range(max(p - self.height + 1, 0),
                           min(p + 1, self.height)):
                diagonals[p].append(self.board[p - q][q])
        self.draw()
        return diagonals


    def moveto(self, team, columnn):
        if '' not in self.get_column(columnn):
            return self.board

        i = self.height - 1
        while self.board[i][columnn] != '':
            i -= 1
        self.board[i][columnn] = team
        self.draw()
        return self.board
    
    

    def draw(self):
        for i in range(self.height):
            for j in range(self.width):
                self.c.create_rectangle(   
                    j * self.board_row,
                    i * self.board_columns,
                    (j + 1) * self.board_row,
                    (i + 1) * self.board_columns,
                    fill=connect4.ACTIVE_COLOR
                )
                self.c.create_text(
                    j * self.board_columns + self.board_row / 2,
                    i * self.board_columns + self.board_row / 2,
                    text=self.board[i][j],
                    font=f'Helvetica {220//self.height} bold',
                    fill=connect4.PASSIVE_COLOR
                )
                
 
    def check_win(self):
        for i in range(self.height):  # check rows
            for x in range(self.width - 3):
                if self.get_row(i)[x:x + 4] in [['x', 'x','x', 'x'], 
                                                ['o', 'o', 'o', 'o']]:
                    return self.board[i][x]

        for i in range(self.width):  # check columns
            for x in range(self.height - 3):
                if self.get_column(i)[x:x + 4] in [['x', 'x', 'x', 'x'], 
                                                   ['o', 'o', 'o', 'o']]:
                    return self.board[x][i]

        for i in self.get_diagonals(): #check dioganals
            for x in range(len(i)):
                if i[x:x + 4] in [['x', 'x', 'x', 'x'],
                                  ['o', 'o', 'o', 'o']]:
                    return i[x]
        self.draw()
        return 

root = Tk()
root.geometry("640x640")

c = Canvas(root, width=640, height=640)
c.pack()
b = connect4(c, 640)
while True:
    for i in b.return_board():
        print(i)
    if b.check_win() != None:
        break
    columnn = int(input('Team 0 choose column: '))-1
    b.moveto('x' , columnn)
    for i in b.return_board():
        print(i)
    if b.check_win() != None:
        break
    columnn = int(input('Team 1 choose column: '))-1
    b.moveto('o' , columnn)


print('Thank you for playing')

root.mainloop()