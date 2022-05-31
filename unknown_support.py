

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import unknown

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = unknown.Toplevel1(_top1)
    # Creates a toplevel widget.
    root.mainloop()

if __name__ == '__main__':
    unknown.start_up()




