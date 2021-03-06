import tkinter as tk
import tkinter.scrolledtext as tkst
from LIBback import Database

database = Database('lib.db')

class TopFrame():

    def __init__(self, win):

        self.win = win
        self.frame = tk.Frame(win, relief = 'groove')
        self.frame.pack(fill = 'x', expand = False)
        #self.topwidgets()

    #def topwidgets(self):

        self.title_val = tk.StringVar()
        self.lbl1 = tk.Label(self.frame, text = 'Title:')
        self.e1 = tk.Entry(self.frame, width = 25, textvariable = self.title_val)
        self.lbl1.grid(row = 0, column = 0, ipadx = 10, ipady = 10)
        self.e1.grid(row = 0, column = 1, sticky = 'e')

        self.author_val = tk.StringVar()
        self.lbl2 = tk.Label(self.frame, text = 'Author:')
        self.e2 = tk.Entry(self.frame, width = 25, textvariable = self.author_val)
        self.lbl2.grid(row = 0, column = 2, ipadx = 10)
        self.e2.grid(row = 0, column = 3, sticky = 'e')

        self.year_val = tk.StringVar()
        self.lbl3 = tk.Label(self.frame, text = 'Year:')
        self.e3 = tk.Entry(self.frame, width = 25, textvariable = self.year_val)
        self.lbl3.grid(row = 1, column = 0, ipady = 5)
        self.e3.grid(row = 1, column = 1)

        self.isbn_val = tk.StringVar()
        self.lbl4 = tk.Label(self.frame, text = 'ISBN:')
        self.e4 = tk.Entry(self.frame, width = 25, textvariable = self.isbn_val)
        self.lbl4.grid(row = 1, column = 2)
        self.e4.grid(row = 1, column = 3)

class BottomFrame():

    def __init__(self, win, top):
        self.top = top
        self.win = win
        self.frame1 = tk.Frame(win)
        self.frame1.pack(fill = 'both', side = "left", expand = False)
        self.frame2 = tk.Frame(win)
        self.frame2.pack(fill = 'both', side = "left", expand = True)
        self.widgets()
        self.search_cmd()
        self.view_cmd()
        self.add_cmd()


    # Creating functions that connects to database
    def view_cmd(self):
        self.txtbox.delete('1.0', tk.END)
        for row in database.view_all():
            self.txtbox.insert(tk.END, row)

    def search_cmd(self):
        self.txtbox.delete('1.0',tk.END)
        for row in database.search_entry(self.top.title_val.get(), self.top.author_val.get(), self.top.year_val.get(), self.top.isbn_val.get()):
            self.txtbox.insert(tk.END, row)

    def add_cmd(self):
        self.txtbox.delete('1.0', tk.END)
        database.add_entry(self.top.title_val.get(), self.top.author_val.get(), self.top.year_val.get(), self.top.isbn_val.get())
        self.txtbox.insert(tk.END, (self.top.title_val.get(), self.top.author_val.get(), self.top.year_val.get(), self.top.isbn_val.get()))

    def update_cmd():
        self.txtbox.delete(0, tk.END)

    def delete_cmd():
        self.txtbox.delete(0, tk.END)


    # Frontend buttons of this frame
    def widgets(self):
        self.button1 = tk.Button(self.frame1, text = 'View All', height = 2 , width = 10, command = self.view_cmd)
        self.button1.pack(side = 'top', fill = 'y', pady = 5, padx = 10)

        self.button2 = tk.Button(self.frame1, text = 'Search Entry', height = 2 , width = 10, command = self.search_cmd)
        self.button2.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.button3 = tk.Button(self.frame1, text = 'Add Entry', height = 2 , width = 10)#, command = add_cmd)
        self.button3.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.button4 = tk.Button(self.frame1, text = 'Update Entry', height = 2 , width = 10)#, command = update_cmd)
        self.button4.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.button5 = tk.Button(self.frame1, text = 'Delete Entry', height = 2 , width = 10)#, command = delete_cmd)
        self.button5.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.button6 = tk.Button(self.frame1, text = 'Exit', height = 2 , width = 10)
        self.button6.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.txtbox = tkst.ScrolledText(self.frame2, width=40, height=10)
        self.txtbox.pack(fill = 'both', expand=True, padx = 7, pady = 7)
        self.txtbox.bind()



def main():

    win = tk.Tk()
    win.title('Book Shop')
    win.geometry("630x370")
    top = TopFrame(win)
    bottom = BottomFrame(win,top)
    win.mainloop()

if __name__ == '__main__':
    main()
