import numpy as np
import matrix
import tkinter as tk
from PIL import Image, ImageTk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400+10+10")
        self.bind('<Button-1>', self.callback)

        game = matrix.create_field(12,8)
        matrix.rand_array(game,15)
        self.game = matrix.modify(game)
 
    def callback(self, event):
        print ("Pointer now at x = %d  and y = %d" %(event.x, event.y))
        x = event.x//50
        y = event.y//50
        print ("game = ",x , y)
        print (self.game[y,x])
        cnv = tk.Canvas(bg= "white", height= 50, width = 50)
        
        img = ImageTk.PhotoImage(file = '/home/rv/code/tmp/pointer/1.gif')
        cnv.create_image(50, 50, image = img)

        cnv.place(x = x*50, y = y*50)
        
        
def main():
    
    myField = MyApp()
    myField.mainloop()

if __name__ == '__main__':
    main()
