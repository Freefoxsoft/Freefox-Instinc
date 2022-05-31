import sys
import tkinter as tk
import tkinter.ttk as ttk
import os
import random
from tkinter import *
import getpass
from tkinter.messagebox import showinfo
from tkinter import messagebox
import hashlib
from update_check import *
import unknown_support
from Modules import blocker
from Modules import unblocker
import webbrowser
btnState = True


unblocker.unblocker()
blocker.blocker()
class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1095x618+330+101")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(0,  0)
        top.title("OXA-Instinc")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#ff0080")
        top.configure(highlightcolor="black")
        top.iconbitmap("./image/OXA1.ico")

        self.top = top
        try:
            update("./basededonné/viruse.txt",
                   'https://raw.githubusercontent.com/Freefoxsoft/antivirus/main/basededonn%C3%A9.txt')
            update("./basededonné/gpo.txt.txt",
                   'https://raw.githubusercontent.com/Freefoxsoft/antivirus/main/codegpo.txt')
        except OSError:
            pass

        #Les variables
        username = (getpass.getuser())
        Donne1 = ('./basededonné/viruse.txt')
        appdatalocale = "C:\\Users\\" + username + "\\AppData"
        desktop = "C:\\users\\" + username + "\\desktop"
        OneDrive = "C:\\users\\" + username + "\\OneDrive\\Bureau"
        top.attributes('-alpha', 0.970)
        def discorde():
            webbrowser.open_new("https://discord.gg/RE7nbv5QWy")

        def youtubee():
            webbrowser.open_new("https://www.youtube.com/channel/UCKDBiC4chKH8uzzzb365X5w")

        def slide(x):
            top.attributes('-alpha', self.Scale1.get())

        def setting():
            root2 = tk.Toplevel(top)

            root2.geometry("428x438+732+341")
            root2.minsize(120, 1)
            root2.maxsize(3844, 1061)
            root2.resizable(0, 0)
            root2.title("settings")
            root2.configure(background="#090513")
            root2.configure(highlightbackground="#8000ff")
            root2.configure(highlightcolor="black")

            self.che47 = tk.IntVar()

            self.Label1 = tk.Label(root2)
            self.Label1.place(relx=0.28, rely=0.046, height=21, width=124)
            self.Label1.configure(activebackground="#090513")
            self.Label1.configure(activeforeground="black")
            self.Label1.configure(anchor='w')
            self.Label1.configure(background="#090513")
            self.Label1.configure(compound='left')
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font="-family {Segoe UI} -size 12 -weight bold")
            self.Label1.configure(foreground="#ffffff")
            self.Label1.configure(highlightbackground="#d9d9d9")
            self.Label1.configure(highlightcolor="black")
            self.Label1.configure(text='''Transparence''')

            self.Scale1 = tk.Scale(root2, from_=0.1, to=1.0, command=slide)
            self.Scale1.place(relx=0.023, rely=0.046, relheight=0.096
                              , relwidth=0.248)
            self.Scale1.configure(activebackground="#090513")
            self.Scale1.configure(background="#090513")
            self.Scale1.configure(borderwidth="0")
            self.Scale1.configure(font="-family {Arial} -size 12")
            self.Scale1.configure(foreground="#ffffff")
            self.Scale1.configure(highlightbackground="#282828")
            self.Scale1.configure(highlightcolor="black")
            self.Scale1.configure(length="106")
            self.Scale1.configure(orient="horizontal")
            self.Scale1.configure(resolution="0.0")
            self.Scale1.configure(sliderrelief="flat")
            self.Scale1.configure(troughcolor="#d11444")

            self.Checkbutton1 = tk.Checkbutton(root2)
            self.Checkbutton1.place(relx=0.023, rely=0.16, relheight=0.08
                                    , relwidth=0.586)
            self.Checkbutton1.configure(activebackground="#090513")
            self.Checkbutton1.configure(activeforeground="white")
            self.Checkbutton1.configure(activeforeground="#000000")
            self.Checkbutton1.configure(anchor='w')
            self.Checkbutton1.configure(background="#090513")
            self.Checkbutton1.configure(borderwidth="0")
            self.Checkbutton1.configure(compound='left')
            self.Checkbutton1.configure(disabledforeground="#a3a3a3")
            self.Checkbutton1.configure(font="-family {Segoe UI} -size 14 -weight bold")
            self.Checkbutton1.configure(foreground="#ffffff")
            self.Checkbutton1.configure(highlightbackground="#d9d9d9")
            self.Checkbutton1.configure(highlightcolor="black")
            self.Checkbutton1.configure(justify='left')
            self.Checkbutton1.configure(offrelief="flat")
            photo_location = "image/mail.png"
            global _img18
            _img18 = tk.PhotoImage(file=photo_location)
            self.Checkbutton1.configure(selectimage=_img18)
            self.Checkbutton1.configure(text='''change the design''')
            self.Checkbutton1.configure(variable=self.che47)


        #roblox============================
        def gpo():
            if os.path.exists("basededonné/gpo.txt"):
                with open("basededonné/gpo.txt", "r+") as file:
                 world_list = file.readlines()
                world_random_list = random.choice(world_list)
                message = world_random_list
                file.close()
                self.EntryCODE.delete(0, END)
                self.EntryCODE.insert(0, message)

        def roblox():
            try:
                self.Frameroblox.destroy()
                self.Frameroblox = tk.Frame(self.top)
                self.Frameroblox.place(relx=0.119, rely=0.065, relheight=0.947
                                       , relwidth=0.89)
                self.Frameroblox.configure(relief="groove")
                self.Frameroblox.configure(background="#242436")

                self.Buttonserveur = tk.Button(self.Frameroblox)
                self.Buttonserveur.place(relx=0.021, rely=0.034, height=34, width=137)
                self.Buttonserveur.configure(activebackground="#090513")
                self.Buttonserveur.configure(activeforeground="white")
                self.Buttonserveur.configure(activeforeground="#000000")
                self.Buttonserveur.configure(background="#090513")
                self.Buttonserveur.configure(borderwidth="0")
                self.Buttonserveur.configure(compound='left')
                self.Buttonserveur.configure(disabledforeground="#a3a3a3")
                self.Buttonserveur.configure(foreground="#ffffff")
                self.Buttonserveur.configure(highlightbackground="#d9d9d9")
                self.Buttonserveur.configure(highlightcolor="black")
                self.Buttonserveur.configure(pady="0")
                self.Buttonserveur.configure(text='''serveur privé''', command=privé)

                self.Buttoninjecteur = tk.Button(self.Frameroblox)
                self.Buttoninjecteur.place(relx=0.021, rely=0.12, height=34, width=137)
                self.Buttoninjecteur.configure(activebackground="#090513")
                self.Buttoninjecteur.configure(activeforeground="white")
                self.Buttoninjecteur.configure(activeforeground="#000000")
                self.Buttoninjecteur.configure(background="#090513")
                self.Buttoninjecteur.configure(borderwidth="0")
                self.Buttoninjecteur.configure(compound='left')
                self.Buttoninjecteur.configure(disabledforeground="#a3a3a3")
                self.Buttoninjecteur.configure(foreground="#ffffff")
                self.Buttoninjecteur.configure(highlightbackground="#d9d9d9")
                self.Buttoninjecteur.configure(highlightcolor="black")
                self.Buttoninjecteur.configure(pady="0")
                self.Buttoninjecteur.configure(text='''Injecteur''')

                self.ButtonFPS = tk.Button(self.Frameroblox)
                self.ButtonFPS.place(relx=0.021, rely=0.205, height=34, width=137)
                self.ButtonFPS.configure(activebackground="#090513")
                self.ButtonFPS.configure(activeforeground="white")
                self.ButtonFPS.configure(activeforeground="#000000")
                self.ButtonFPS.configure(background="#090513")
                self.ButtonFPS.configure(borderwidth="0")
                self.ButtonFPS.configure(compound='left')
                self.ButtonFPS.configure(disabledforeground="#a3a3a3")
                self.ButtonFPS.configure(foreground="#ffffff")
                self.ButtonFPS.configure(highlightbackground="#d9d9d9")
                self.ButtonFPS.configure(highlightcolor="black")
                self.ButtonFPS.configure(pady="0")
                self.ButtonFPS.configure(text='''FPS Unlocker''',command=fpsdebloqueur)

                self.Frameprivé = tk.Frame(self.Frameroblox)
                self.Frameprivé.place(relx=0.287, rely=0.017, relheight=0.949
                                      , relwidth=0.692)
                self.Frameprivé.configure(relief="groove")
                self.Frameprivé.configure(background="#242436")

                self.Label7 = tk.Label(self.Frameroblox)
                self.Label7.place(relx=0.021, rely=0.291, height=31, width=144)
                self.Label7.configure(anchor='w')
                self.Label7.configure(background="#242436")
                self.Label7.configure(compound='left')
                self.Label7.configure(disabledforeground="#a3a3a3")
                self.Label7.configure(font="-family {Segoe UI Black} -size 14 -weight bold")
                self.Label7.configure(foreground="#ffffff")
                self.Label7.configure(text='''Coming soon...''')
            except AttributeError:
                self.Frameroblox = tk.Frame(self.top)
                self.Frameroblox.place(relx=0.119, rely=0.065, relheight=0.947
                                       , relwidth=0.89)
                self.Frameroblox.configure(relief="groove")
                self.Frameroblox.configure(background="#242436")

                self.Buttonserveur = tk.Button(self.Frameroblox)
                self.Buttonserveur.place(relx=0.021, rely=0.034, height=34, width=137)
                self.Buttonserveur.configure(activebackground="#090513")
                self.Buttonserveur.configure(activeforeground="white")
                self.Buttonserveur.configure(activeforeground="#000000")
                self.Buttonserveur.configure(background="#090513")
                self.Buttonserveur.configure(borderwidth="0")
                self.Buttonserveur.configure(compound='left')
                self.Buttonserveur.configure(disabledforeground="#a3a3a3")
                self.Buttonserveur.configure(foreground="#ffffff")
                self.Buttonserveur.configure(highlightbackground="#d9d9d9")
                self.Buttonserveur.configure(highlightcolor="black")
                self.Buttonserveur.configure(pady="0")
                self.Buttonserveur.configure(text='''serveur privé''', command=privé)

                self.Buttoninjecteur = tk.Button(self.Frameroblox)
                self.Buttoninjecteur.place(relx=0.021, rely=0.12, height=34, width=137)
                self.Buttoninjecteur.configure(activebackground="#090513")
                self.Buttoninjecteur.configure(activeforeground="white")
                self.Buttoninjecteur.configure(activeforeground="#000000")
                self.Buttoninjecteur.configure(background="#090513")
                self.Buttoninjecteur.configure(borderwidth="0")
                self.Buttoninjecteur.configure(compound='left')
                self.Buttoninjecteur.configure(disabledforeground="#a3a3a3")
                self.Buttoninjecteur.configure(foreground="#ffffff")
                self.Buttoninjecteur.configure(highlightbackground="#d9d9d9")
                self.Buttoninjecteur.configure(highlightcolor="black")
                self.Buttoninjecteur.configure(pady="0")
                self.Buttoninjecteur.configure(text='''Injecteur''')

                self.ButtonFPS = tk.Button(self.Frameroblox)
                self.ButtonFPS.place(relx=0.021, rely=0.205, height=34, width=137)
                self.ButtonFPS.configure(activebackground="#090513")
                self.ButtonFPS.configure(activeforeground="white")
                self.ButtonFPS.configure(activeforeground="#000000")
                self.ButtonFPS.configure(background="#090513")
                self.ButtonFPS.configure(borderwidth="0")
                self.ButtonFPS.configure(compound='left')
                self.ButtonFPS.configure(disabledforeground="#a3a3a3")
                self.ButtonFPS.configure(foreground="#ffffff")
                self.ButtonFPS.configure(highlightbackground="#d9d9d9")
                self.ButtonFPS.configure(highlightcolor="black")
                self.ButtonFPS.configure(pady="0")
                self.ButtonFPS.configure(text='''FPS Unlocker''',command=fpsdebloqueur)

                self.Frameprivé = tk.Frame(self.Frameroblox)
                self.Frameprivé.place(relx=0.287, rely=0.017, relheight=0.949
                                      , relwidth=0.692)
                self.Frameprivé.configure(relief="groove")
                self.Frameprivé.configure(background="#242436")

                self.Label7 = tk.Label(self.Frameroblox)
                self.Label7.place(relx=0.021, rely=0.291, height=31, width=144)
                self.Label7.configure(anchor='w')
                self.Label7.configure(background="#242436")
                self.Label7.configure(compound='left')
                self.Label7.configure(disabledforeground="#a3a3a3")
                self.Label7.configure(font="-family {Segoe UI Black} -size 14 -weight bold")
                self.Label7.configure(foreground="#ffffff")
                self.Label7.configure(text='''Coming soon...''')

        def privé():
            self.EntryCODE = tk.Entry(self.Frameprivé)
            self.EntryCODE.place(relx=0.459, rely=0.234, height=60, relwidth=0.524)
            self.EntryCODE.configure(background="#090513")
            self.EntryCODE.configure(borderwidth="0")
            self.EntryCODE.configure(disabledforeground="#a3a3a3")
            self.EntryCODE.configure(font="-family {Courier New} -size 48 -weight bold")
            self.EntryCODE.configure(foreground="#ffffff")
            self.EntryCODE.configure(insertbackground="black")

            self.ButtonGPO = tk.Button(self.Frameprivé)
            self.ButtonGPO.place(relx=0.044, rely=0.036, height=34, width=137)
            self.ButtonGPO.configure(activebackground="#090513")
            self.ButtonGPO.configure(activeforeground="white")
            self.ButtonGPO.configure(activeforeground="#ffffff")
            self.ButtonGPO.configure(background="#090513")
            self.ButtonGPO.configure(borderwidth="0")
            self.ButtonGPO.configure(compound='left')
            self.ButtonGPO.configure(disabledforeground="#a3a3a3")
            self.ButtonGPO.configure(foreground="#ffffff")
            self.ButtonGPO.configure(highlightbackground="#d9d9d9")
            self.ButtonGPO.configure(highlightcolor="black")
            self.ButtonGPO.configure(pady="0")
            self.ButtonGPO.configure(text='''GPO CODE''',command=gpo)

            self.Buttoncoming = tk.Button(self.Frameprivé)
            self.Buttoncoming.place(relx=0.044, rely=0.126, height=34, width=137)
            self.Buttoncoming.configure(activebackground="#090513")
            self.Buttoncoming.configure(activeforeground="white")
            self.Buttoncoming.configure(activeforeground="#ffffff")
            self.Buttoncoming.configure(background="#090513")
            self.Buttoncoming.configure(borderwidth="0")
            self.Buttoncoming.configure(compound='left')
            self.Buttoncoming.configure(disabledforeground="#a3a3a3")
            self.Buttoncoming.configure(foreground="#ffffff")
            self.Buttoncoming.configure(highlightbackground="#d9d9d9")
            self.Buttoncoming.configure(highlightcolor="black")
            self.Buttoncoming.configure(pady="0")
            self.Buttoncoming.configure(text='''Coming soon''')

        def fpsdebloqueur():
            self.Frame2 = tk.Frame(self.top)
            self.Frame2.place(relx=0.374, rely=0.081, relheight=0.898
                              , relwidth=0.616)
            self.Frame2.configure(background="#242436")

            self.Label8 = tk.Label(self.Frame2)
            self.Label8.place(relx=0.193, rely=0.252, height=151, width=504)
            self.Label8.configure(anchor='w')
            self.Label8.configure(background="#242436")
            self.Label8.configure(borderwidth="0")
            self.Label8.configure(compound='left')
            self.Label8.configure(disabledforeground="#a3a3a3")
            self.Label8.configure(font="-family {Segoe UI Black} -size 48 -weight bold")
            self.Label8.configure(foreground="#ffffff")
            self.Label8.configure(text='''Coming soon...''')

            self.Label8_1 = tk.Label(self.Frame2)
            self.Label8_1.place(relx=0.207, rely=0.252, height=51, width=244)
            self.Label8_1.configure(activebackground="#f9f9f9")
            self.Label8_1.configure(anchor='w')
            self.Label8_1.configure(background="#242436")
            self.Label8_1.configure(borderwidth="0")
            self.Label8_1.configure(compound='left')
            self.Label8_1.configure(disabledforeground="#a3a3a3")
            self.Label8_1.configure(font="-family {Segoe UI Black} -size 28 -weight bold")
            self.Label8_1.configure(foreground="#ffffff")
            self.Label8_1.configure(highlightbackground="#d9d9d9")
            self.Label8_1.configure(highlightcolor="black")
            self.Label8_1.configure(text='''Fps unlocker''')
        #finroblox======================================================================================================

        #débutantivirus=================================================================================================
        def smartscan():
            try:
                virus_found = False
                print("analyse en cours")
                dir_list = list()
                for (dirpath, dirnames, filename) in os.walk(OneDrive):
                    dir_list += [os.path.join(dirpath, file) for file in filename]
                for i in dir_list:
                    print(i)
                    with open(i, "rb") as f:
                        bytes = f.read()
                        readable_hash = hashlib.sha256(bytes).hexdigest();

                    with open(Donne1, 'r') as f:
                        lines = [line.rstrip() for line in f]
                        top.update()
                        self.Listbox1.delete(0, END)
                        self.Listbox1.insert(0, i)
                        for line in lines:
                            if str(readable_hash) == str(line.split(";")[0]):
                                chemin = (i)
                                print("liste des virus " + chemin)
                                self.Listbox2.delete(0, END)
                                self.Listbox2.insert(0, chemin)
                                if messagebox.askyesno("Virus Trouvé",
                                                       "virus trouvé voulez vous le supprimer ?") == True:
                                    os.remove(i)
                                else:
                                    pass
                                virus_found = True
                                f.close()
                print("analyse terminé")
                if virus_found == False:
                    messagebox.showinfo("analyse", "aucun virus trouvé")
            except PermissionError:
                pass
            try:
                virus_found = False
                print("analyse en cours")
                dir_list = list()
                for (dirpath, dirnames, filename) in os.walk(desktop):
                    dir_list += [os.path.join(dirpath, file) for file in filename]
                for i in dir_list:
                    print(i)
                    with open(i, "rb") as f:
                        bytes = f.read()
                        readable_hash = hashlib.sha256(bytes).hexdigest();

                    with open(Donne1, 'r') as f:
                        lines = [line.rstrip() for line in f]
                        top.update()
                        self.Listbox1.delete(0, END)
                        self.Listbox1.insert(0, i)
                        for line in lines:
                            if str(readable_hash) == str(line.split(";")[0]):
                                chemin = (i)
                                print("liste des virus " + chemin)
                                self.Listbox2.delete(0, END)
                                self.Listbox2.insert(0, chemin)
                                if messagebox.askyesno("Virus Trouvé",
                                                       "virus trouvé voulez vous le supprimer ?") == True:
                                    os.remove(i)
                                else:
                                    pass
                                virus_found = True
                                f.close()
                print("analyse terminé")
                if virus_found == False:
                    messagebox.showinfo("analyse", "aucun virus trouvé")
            except PermissionError:
                pass

        def switchon():
            blocker.blocker()
            print("webblocker active")
            self.Buttonwebblocker = tk.Button(self.Frameantivirus)
            self.Buttonwebblocker.place(relx=0.123, rely=0.205, height=44, width=57)
            self.Buttonwebblocker.configure(activebackground="#242436")
            self.Buttonwebblocker.configure(activeforeground="white")
            self.Buttonwebblocker.configure(activeforeground="#000000")
            self.Buttonwebblocker.configure(background="#242436")
            self.Buttonwebblocker.configure(borderwidth="0")
            self.Buttonwebblocker.configure(compound='left')
            self.Buttonwebblocker.configure(disabledforeground="#a3a3a3")
            self.Buttonwebblocker.configure(foreground="#000000")
            self.Buttonwebblocker.configure(highlightbackground="#d9d9d9")
            self.Buttonwebblocker.configure(highlightcolor="black",command=switch)
            photo_location = "./image/switch-on.png"
            global _img5000
            _img5000 = tk.PhotoImage(file=photo_location)
            self.Buttonwebblocker.configure(image=_img5000)
            self.Buttonwebblocker.configure(pady="0")
            btnState = True

        def switch():
            global btnState
            if btnState:
                unblocker.unblocker()
                print("webblocker desactivé")
                self.Buttonwebblocker = tk.Button(self.Frameantivirus)
                self.Buttonwebblocker.place(relx=0.123, rely=0.205, height=44, width=57)
                self.Buttonwebblocker.configure(activebackground="#242436")
                self.Buttonwebblocker.configure(activeforeground="white")
                self.Buttonwebblocker.configure(activeforeground="#000000")
                self.Buttonwebblocker.configure(background="#242436")
                self.Buttonwebblocker.configure(borderwidth="0")
                self.Buttonwebblocker.configure(compound='left')
                self.Buttonwebblocker.configure(disabledforeground="#a3a3a3")
                self.Buttonwebblocker.configure(foreground="#000000")
                self.Buttonwebblocker.configure(highlightbackground="#d9d9d9")
                self.Buttonwebblocker.configure(highlightcolor="black",command=switchon)
                photo_location = "./image/switch-off.png"
                global _img20
                _img20 = tk.PhotoImage(file=photo_location)
                self.Buttonwebblocker.configure(image=_img20)
                self.Buttonwebblocker.configure(pady="0")
            showinfo("Netfiltering", "webblocker desactivé")

        def antivirusee():
            self.Frameantivirus = tk.Frame(self.top)
            self.Frameantivirus.place(relx=0.119, rely=0.065, relheight=0.947
                                      , relwidth=0.89)
            self.Frameantivirus.configure(relief="groove")
            self.Frameantivirus.configure(background="#242436")

            self.Button4 = tk.Button(self.Frameantivirus)
            self.Button4.place(relx=0.113, rely=0.667, height=84, width=267)
            self.Button4.configure(activebackground="#090513")
            self.Button4.configure(activeforeground="white")
            self.Button4.configure(activeforeground="#ffffff")
            self.Button4.configure(background="#d11444")
            self.Button4.configure(borderwidth="0")
            self.Button4.configure(compound='left')
            self.Button4.configure(disabledforeground="#a3a3a3")
            self.Button4.configure(font="-family {Segoe UI} -size 18 -weight bold")
            self.Button4.configure(foreground="#ffffff")
            self.Button4.configure(highlightbackground="#d9d9d9")
            self.Button4.configure(highlightcolor="black")
            self.Button4.configure(pady="0")
            self.Button4.configure(relief="flat")
            self.Button4.configure(text='''Smart Scan ''', command=smartscan)

            self.Button4_1 = tk.Button(self.Frameantivirus)
            self.Button4_1.place(relx=0.523, rely=0.667, height=84, width=267)
            self.Button4_1.configure(activebackground="#090513")
            self.Button4_1.configure(activeforeground="white")
            self.Button4_1.configure(activeforeground="#ffffff")
            self.Button4_1.configure(background="#d11444")
            self.Button4_1.configure(borderwidth="0")
            self.Button4_1.configure(compound='left')
            self.Button4_1.configure(disabledforeground="#a3a3a3")
            self.Button4_1.configure(font="-family {Segoe UI} -size 18 -weight bold")
            self.Button4_1.configure(foreground="#ffffff")
            self.Button4_1.configure(highlightbackground="#d9d9d9")
            self.Button4_1.configure(highlightcolor="black")
            self.Button4_1.configure(pady="0")
            self.Button4_1.configure(relief="flat")
            self.Button4_1.configure(text='''System Scan''')

            self.Label9 = tk.Label(self.Frameantivirus)
            self.Label9.place(relx=0.021, rely=0.017, height=31, width=134)
            self.Label9.configure(anchor='w')
            self.Label9.configure(background="#242436")
            self.Label9.configure(compound='left')
            self.Label9.configure(disabledforeground="#a3a3a3")
            self.Label9.configure(font="-family {Segoe UI} -size 14 -weight bold")
            self.Label9.configure(foreground="#d11444")
            self.Label9.configure(text='''Scanning File :''')

            self.Label9_1 = tk.Label(self.Frameantivirus)
            self.Label9_1.place(relx=0.021, rely=0.085, height=31, width=134)
            self.Label9_1.configure(activebackground="#f9f9f9")
            self.Label9_1.configure(anchor='w')
            self.Label9_1.configure(background="#242436")
            self.Label9_1.configure(compound='left')
            self.Label9_1.configure(disabledforeground="#a3a3a3")
            self.Label9_1.configure(font="-family {Segoe UI} -size 14 -weight bold")
            self.Label9_1.configure(foreground="#d11444")
            self.Label9_1.configure(highlightbackground="#d9d9d9")
            self.Label9_1.configure(highlightcolor="black")
            self.Label9_1.configure(text='''Virus Found :''')

            self.Listbox1 = tk.Listbox(self.Frameantivirus)
            self.Listbox1.place(relx=0.164, rely=0.017, relheight=0.055
                                , relwidth=0.825)
            self.Listbox1.configure(background="#242436")
            self.Listbox1.configure(borderwidth="0")
            self.Listbox1.configure(disabledforeground="#a3a3a3")
            self.Listbox1.configure(font="-family {Courier New} -size 15 -weight bold")
            self.Listbox1.configure(foreground="#d11444")
            self.Listbox1.configure(highlightbackground="#242436")

            self.Listbox2 = tk.Listbox(self.Frameantivirus)
            self.Listbox2.place(relx=0.154, rely=0.085, relheight=0.055
                                , relwidth=0.835)
            self.Listbox2.configure(background="#242436")
            self.Listbox2.configure(borderwidth="0")
            self.Listbox2.configure(disabledforeground="#a3a3a3")
            self.Listbox2.configure(font="-family {Courier New} -size 15 -weight bold")
            self.Listbox2.configure(foreground="#d11444")
            self.Listbox2.configure(highlightbackground="#242436")

            self.Buttonwebblocker = tk.Button(self.Frameantivirus)
            self.Buttonwebblocker.place(relx=0.123, rely=0.205, height=44, width=57)
            self.Buttonwebblocker.configure(activebackground="#242436")
            self.Buttonwebblocker.configure(activeforeground="white")
            self.Buttonwebblocker.configure(activeforeground="#000000")
            self.Buttonwebblocker.configure(background="#242436")
            self.Buttonwebblocker.configure(borderwidth="0")
            self.Buttonwebblocker.configure(compound='left')
            self.Buttonwebblocker.configure(disabledforeground="#a3a3a3")
            self.Buttonwebblocker.configure(foreground="#000000")
            self.Buttonwebblocker.configure(highlightbackground="#d9d9d9")
            self.Buttonwebblocker.configure(highlightcolor="black", command=switch)
            photo_location = "./image/switch-on.png"
            global _img20
            _img20 = tk.PhotoImage(file=photo_location)
            self.Buttonwebblocker.configure(image=_img20)
            self.Buttonwebblocker.configure(pady="0")
            self.tooltip_font = "TkDefaultFont"
            self.Buttonwebblocker_tooltip = \
                ToolTip(self.Buttonwebblocker, self.tooltip_font, '''bloque les sites frauduleux''')

            self.Label10 = tk.Label(self.Frameantivirus)
            self.Label10.place(relx=0.185, rely=0.222, height=31, width=94)
            self.Label10.configure(anchor='w')
            self.Label10.configure(background="#242436")
            self.Label10.configure(compound='left')
            self.Label10.configure(disabledforeground="#a3a3a3")
            self.Label10.configure(font="-family {Segoe UI} -size 11 -weight bold")
            self.Label10.configure(foreground="#ffffff")
            self.Label10.configure(text='''WEB blocker''')

            self.Buttonantivirus = tk.Button(self.Frameantivirus)
            self.Buttonantivirus.place(relx=0.123, rely=0.291, height=44, width=57)
            self.Buttonantivirus.configure(activebackground="#242436")
            self.Buttonantivirus.configure(activeforeground="white")
            self.Buttonantivirus.configure(activeforeground="#000000")
            self.Buttonantivirus.configure(background="#242436")
            self.Buttonantivirus.configure(borderwidth="0")
            self.Buttonantivirus.configure(compound='left')
            self.Buttonantivirus.configure(disabledforeground="#a3a3a3")
            self.Buttonantivirus.configure(foreground="#000000")
            self.Buttonantivirus.configure(highlightbackground="#d9d9d9")
            self.Buttonantivirus.configure(highlightcolor="black")
            photo_location = "./image/switch-off.png"
            global _img21
            _img21 = tk.PhotoImage(file=photo_location)
            self.Buttonantivirus.configure(image=_img21)
            self.Buttonantivirus.configure(pady="0")
            self.tooltip_font = "TkDefaultFont"
            self.Buttonantivirus_tooltip = \
                ToolTip(self.Buttonantivirus, self.tooltip_font,
                        '''fonctionne mais en fasse test donc deconseillez''')

            self.Label11 = tk.Label(self.Frameantivirus)
            self.Label11.place(relx=0.185, rely=0.308, height=31, width=184)
            self.Label11.configure(activebackground="#f9f9f9")
            self.Label11.configure(anchor='w')
            self.Label11.configure(background="#242436")
            self.Label11.configure(compound='left')
            self.Label11.configure(disabledforeground="#a3a3a3")
            self.Label11.configure(font="-family {Segoe UI} -size 11 -weight bold")
            self.Label11.configure(foreground="#ffffff")
            self.Label11.configure(highlightbackground="#d9d9d9")
            self.Label11.configure(highlightcolor="black")
            self.Label11.configure(text='''ANTIVIRUS on real time''')
        #finantivirus===================================================================================================


        def systemee():
            try:
                self.Framesysteme.destroy()
                self.Framesysteme = tk.Frame(self.top)
                self.Framesysteme.place(relx=0.119, rely=0.065, relheight=0.947
                                        , relwidth=0.89)
                self.Framesysteme.configure(relief="groove")
                self.Framesysteme.configure(background="#242436")

                self.Label12 = tk.Label(self.Framesysteme)
                self.Label12.place(relx=0.072, rely=0.205, height=211, width=804)
                self.Label12.configure(anchor='w')
                self.Label12.configure(background="#242436")
                self.Label12.configure(compound='left')
                self.Label12.configure(disabledforeground="#a3a3a3")
                self.Label12.configure(font="-family {Segoe UI Black} -size 36 -weight bold -slant italic")
                self.Label12.configure(foreground="#d11444")
                self.Label12.configure(text='''Arrive à la prochaine mise à jour''')

                self.Label13 = tk.Label(self.Framesysteme)
                self.Label13.place(relx=0.072, rely=0.427, height=61, width=264)
                self.Label13.configure(anchor='w')
                self.Label13.configure(background="#242436")
                self.Label13.configure(compound='left')
                self.Label13.configure(disabledforeground="#a3a3a3")
                self.Label13.configure(font="-family {Segoe UI} -size 28 -weight bold")
                self.Label13.configure(foreground="#ffffff")
                self.Label13.configure(text='''Donc Samedi ou Dimanche ;)''')
            except AttributeError:
                self.Framesysteme = tk.Frame(self.top)
                self.Framesysteme.place(relx=0.119, rely=0.065, relheight=0.947
                                        , relwidth=0.89)
                self.Framesysteme.configure(relief="groove")
                self.Framesysteme.configure(background="#242436")

                self.Label12 = tk.Label(self.Framesysteme)
                self.Label12.place(relx=0.072, rely=0.205, height=211, width=804)
                self.Label12.configure(anchor='w')
                self.Label12.configure(background="#242436")
                self.Label12.configure(compound='left')
                self.Label12.configure(disabledforeground="#a3a3a3")
                self.Label12.configure(font="-family {Segoe UI Black} -size 36 -weight bold -slant italic")
                self.Label12.configure(foreground="#d11444")
                self.Label12.configure(text='''Arrive à la prochaine mise à jour''')

                self.Label13 = tk.Label(self.Framesysteme)
                self.Label13.place(relx=0.072, rely=0.427, height=61, width=510)
                self.Label13.configure(anchor='w')
                self.Label13.configure(background="#242436")
                self.Label13.configure(compound='left')
                self.Label13.configure(disabledforeground="#a3a3a3")
                self.Label13.configure(font="-family {Segoe UI} -size 28 -weight bold")
                self.Label13.configure(foreground="#ffffff")
                self.Label13.configure(text='''Donc Samedi ou Dimanche ;)''')

        def passwordee():
            try:
                self.Framepassword.destroy()
                self.Framepassword = tk.Frame(self.top)
                self.Framepassword.place(relx=0.119, rely=0.065, relheight=0.947
                                         , relwidth=0.89)
                self.Framepassword.configure(background="#242436")

                self.Label14 = tk.Label(self.Framepassword)
                self.Label14.place(relx=0.195, rely=0.274, height=161, width=524)
                self.Label14.configure(anchor='w')
                self.Label14.configure(background="#242436")
                self.Label14.configure(compound='left')
                self.Label14.configure(disabledforeground="#a3a3a3")
                self.Label14.configure(font="-family {Segoe UI} -size 30")
                self.Label14.configure(foreground="#d11444")
                self.Label14.configure(text='''En cours de devellopement''')
            except AttributeError:
                self.Framepassword = tk.Frame(self.top)
                self.Framepassword.place(relx=0.119, rely=0.065, relheight=0.947
                                         , relwidth=0.89)
                self.Framepassword.configure(background="#242436")

                self.Label14 = tk.Label(self.Framepassword)
                self.Label14.place(relx=0.195, rely=0.274, height=161, width=524)
                self.Label14.configure(anchor='w')
                self.Label14.configure(background="#242436")
                self.Label14.configure(compound='left')
                self.Label14.configure(disabledforeground="#a3a3a3")
                self.Label14.configure(font="-family {Segoe UI} -size 30")
                self.Label14.configure(foreground="#d11444")
                self.Label14.configure(text='''En cours de devellopement''')

        def Credit():
            self.FrameCrédit = tk.Frame(self.top)
            self.FrameCrédit.place(relx=0.119, rely=0.065, relheight=0.947
                                   , relwidth=0.9)
            self.FrameCrédit.configure(background="#242436")

            self.Label4 = tk.Label(self.FrameCrédit)
            self.Label4.place(relx=0.0, rely=0.923, height=31, width=114)
            self.Label4.configure(anchor='w')
            self.Label4.configure(background="#242436")
            self.Label4.configure(compound='left')
            self.Label4.configure(disabledforeground="#a3a3a3")
            self.Label4.configure(font="-family {Segoe UI} -size 28 -weight bold")
            self.Label4.configure(foreground="#d11444")
            self.Label4.configure(text='''Crédit''')

            self.Label5 = tk.Label(self.FrameCrédit)
            self.Label5.place(relx=0.02, rely=0.017, height=51, width=264)
            self.Label5.configure(anchor='w')
            self.Label5.configure(background="#242436")
            self.Label5.configure(compound='left')
            self.Label5.configure(disabledforeground="#a3a3a3")
            self.Label5.configure(font="-family {Segoe UI} -size 20 -weight bold")
            self.Label5.configure(foreground="#d11444")
            self.Label5.configure(text='''Interface graphique''')

            self.Label6 = tk.Label(self.FrameCrédit)
            self.Label6.place(relx=0.02, rely=0.103, height=21, width=154)
            self.Label6.configure(anchor='w')
            self.Label6.configure(background="#242436")
            self.Label6.configure(compound='left')
            self.Label6.configure(disabledforeground="#a3a3a3")
            self.Label6.configure(font="-family {Segoe UI Black} -size 15 -weight bold")
            self.Label6.configure(foreground="#ffffff")
            self.Label6.configure(text='''Alicee #0819''')

            self.Label5_1 = tk.Label(self.FrameCrédit)
            self.Label5_1.place(relx=0.02, rely=0.171, height=51, width=164)
            self.Label5_1.configure(activebackground="#f9f9f9")
            self.Label5_1.configure(anchor='w')
            self.Label5_1.configure(background="#242436")
            self.Label5_1.configure(compound='left')
            self.Label5_1.configure(disabledforeground="#a3a3a3")
            self.Label5_1.configure(font="-family {Segoe UI} -size 20 -weight bold")
            self.Label5_1.configure(foreground="#d11444")
            self.Label5_1.configure(highlightbackground="#d9d9d9")
            self.Label5_1.configure(highlightcolor="black")
            self.Label5_1.configure(text='''Devellopeur''')

            self.Label6_1 = tk.Label(self.FrameCrédit)
            self.Label6_1.place(relx=0.02, rely=0.256, height=21, width=194)
            self.Label6_1.configure(activebackground="#f9f9f9")
            self.Label6_1.configure(anchor='w')
            self.Label6_1.configure(background="#242436")
            self.Label6_1.configure(compound='left')
            self.Label6_1.configure(disabledforeground="#a3a3a3")
            self.Label6_1.configure(font="-family {Segoe UI Black} -size 15 -weight bold")
            self.Label6_1.configure(foreground="#ffffff")
            self.Label6_1.configure(highlightbackground="#d9d9d9")
            self.Label6_1.configure(highlightcolor="black")
            self.Label6_1.configure(text='''Sachune_off #8342''')

            self.Label5_1_1 = tk.Label(self.FrameCrédit)
            self.Label5_1_1.place(relx=0.02, rely=0.325, height=51, width=154)
            self.Label5_1_1.configure(activebackground="#f9f9f9")
            self.Label5_1_1.configure(anchor='w')
            self.Label5_1_1.configure(background="#242436")
            self.Label5_1_1.configure(compound='left')
            self.Label5_1_1.configure(disabledforeground="#a3a3a3")
            self.Label5_1_1.configure(font="-family {Segoe UI} -size 20 -weight bold")
            self.Label5_1_1.configure(foreground="#d11444")
            self.Label5_1_1.configure(highlightbackground="#d9d9d9")
            self.Label5_1_1.configure(highlightcolor="black")
            self.Label5_1_1.configure(text='''Beta tester''')

            self.Label6_1_1 = tk.Label(self.FrameCrédit)
            self.Label6_1_1.place(relx=0.02, rely=0.41, height=21, width=194)
            self.Label6_1_1.configure(activebackground="#f9f9f9")
            self.Label6_1_1.configure(anchor='w')
            self.Label6_1_1.configure(background="#242436")
            self.Label6_1_1.configure(compound='left')
            self.Label6_1_1.configure(disabledforeground="#a3a3a3")
            self.Label6_1_1.configure(font="-family {Segoe UI Black} -size 15 -weight bold")
            self.Label6_1_1.configure(foreground="#ffffff")
            self.Label6_1_1.configure(highlightbackground="#d9d9d9")
            self.Label6_1_1.configure(highlightcolor="black")
            self.Label6_1_1.configure(text='''Ratibe #4386''')

        def acceuilles():
            top.update()
            self.FRAMEacceuille = tk.Frame(self.top)
            self.FRAMEacceuille.place(relx=0.119, rely=0.065, relheight=0.939
                                      , relwidth=0.9)
            self.FRAMEacceuille.configure(relief='flat')
            self.FRAMEacceuille.configure(borderwidth="2")
            self.FRAMEacceuille.configure(background="#242436")
            self.FRAMEacceuille.configure(highlightbackground="#d11444")
            self.FRAMEacceuille.configure(highlightcolor="black")

            self.Label2 = tk.Label(self.FRAMEacceuille)
            self.Label2.place(relx=0.892, rely=0.948, height=30, width=85)
            self.Label2.configure(activebackground="#f9f9f9")
            self.Label2.configure(activeforeground="black")
            self.Label2.configure(anchor='w')
            self.Label2.configure(background="#242436")
            self.Label2.configure(compound='left')
            self.Label2.configure(disabledforeground="#a3a3a3")
            self.Label2.configure(font="-family {Segoe UI} -size 11 -weight bold")
            self.Label2.configure(foreground="#ffffff")
            self.Label2.configure(highlightbackground="#d9d9d9")
            self.Label2.configure(highlightcolor="black")
            self.Label2.configure(text='''Version 1.0''')

            self.Labelbienvenue = tk.Label(self.FRAMEacceuille)
            self.Labelbienvenue.place(relx=0.284, rely=0.241, height=99, width=368)
            self.Labelbienvenue.configure(activebackground="#f9f9f9")
            self.Labelbienvenue.configure(activeforeground="black")
            self.Labelbienvenue.configure(anchor='w')
            self.Labelbienvenue.configure(background="#242436")
            self.Labelbienvenue.configure(compound='left')
            self.Labelbienvenue.configure(disabledforeground="#a3a3a3")
            self.Labelbienvenue.configure(font="-family {Segoe UI} -size 48 -weight bold")
            self.Labelbienvenue.configure(foreground="#d11444")
            self.Labelbienvenue.configure(highlightbackground="#d9d9d9")
            self.Labelbienvenue.configure(highlightcolor="black")
            self.Labelbienvenue.configure(text='''Bienvenue !''')

            self.Buttonsitedestreaming = tk.Button(self.FRAMEacceuille)
            self.Buttonsitedestreaming.place(relx=0.771, rely=-0.017, height=44
                                             , width=217)
            self.Buttonsitedestreaming.configure(activebackground="#242436")
            self.Buttonsitedestreaming.configure(activeforeground="white")
            self.Buttonsitedestreaming.configure(activeforeground="#000000")
            self.Buttonsitedestreaming.configure(background="#242436")
            self.Buttonsitedestreaming.configure(borderwidth="0")
            self.Buttonsitedestreaming.configure(compound='left')
            self.Buttonsitedestreaming.configure(disabledforeground="#a3a3a3")
            self.Buttonsitedestreaming.configure(font="-family {Segoe UI Variable Text} -size 17 -weight bold")
            self.Buttonsitedestreaming.configure(foreground="#ff8000")
            self.Buttonsitedestreaming.configure(highlightbackground="#d9d9d9")
            self.Buttonsitedestreaming.configure(highlightcolor="black")
            self.Buttonsitedestreaming.configure(pady="0")
            self.Buttonsitedestreaming.configure(relief="flat")
            self.Buttonsitedestreaming.configure(text='''FreefoxStreaming''')
            self.tooltip_font = "TkDefaultFont"
            self.Buttonsitedestreaming_tooltip = \
                ToolTip(self.Buttonsitedestreaming, self.tooltip_font, '''coming soon''')

            self.Buttondiscord = tk.Button(self.FRAMEacceuille)
            self.Buttondiscord.place(relx=0.172, rely=0.534, height=54, width=77)
            self.Buttondiscord.configure(activebackground="#242436")
            self.Buttondiscord.configure(activeforeground="white")
            self.Buttondiscord.configure(activeforeground="#000000")
            self.Buttondiscord.configure(background="#242436")
            self.Buttondiscord.configure(borderwidth="0")
            self.Buttondiscord.configure(compound='left')
            self.Buttondiscord.configure(disabledforeground="#a3a3a3")
            self.Buttondiscord.configure(foreground="#000000")
            self.Buttondiscord.configure(highlightbackground="#d9d9d9")
            self.Buttondiscord.configure(highlightcolor="black",command=discorde)
            photo_location = "./image/discord.png"
            global _img19
            _img19 = tk.PhotoImage(file=photo_location)
            self.Buttondiscord.configure(image=_img19)
            self.Buttondiscord.configure(pady="0")
            self.Buttondiscord.configure(relief="flat")

            self.Button25 = tk.Button(self.FRAMEacceuille)
            self.Button25.place(relx=0.0, rely=0.931, height=34, width=87)
            self.Button25.configure(activebackground="#242436")
            self.Button25.configure(activeforeground="white")
            self.Button25.configure(activeforeground="#ffffff")
            self.Button25.configure(background="#242436")
            self.Button25.configure(borderwidth="0")
            self.Button25.configure(compound='left')
            self.Button25.configure(disabledforeground="#a3a3a3")
            self.Button25.configure(font="-family {Segoe UI Black} -size 16 -weight bold")
            self.Button25.configure(foreground="#ffffff")
            self.Button25.configure(highlightbackground="#d9d9d9")
            self.Button25.configure(highlightcolor="black")
            self.Button25.configure(pady="0")
            self.Button25.configure(relief="flat")
            self.Button25.configure(text='''CREDIT''',command=Credit)

        def checkingupdate():
            try:
                update("oxa-Instinc.exe", 'https://raw.githubusercontent.com/Freefoxsoft/antivirus/main/oxa-Instinc.exe')
            except OSError:
                showinfo("mise à jour", "aucune mise à jour disponible")
            top.destroy()









        self.Frame_menedroite = tk.Frame(self.top)
        self.Frame_menedroite.place(relx=-0.009, rely=0.065, relheight=0.939
                , relwidth=0.132)
        self.Frame_menedroite.configure(relief='flat')
        self.Frame_menedroite.configure(borderwidth="2")
        self.Frame_menedroite.configure(background="#090513")
        self.Frame_menedroite.configure(highlightbackground="#d9d9d9")
        self.Frame_menedroite.configure(highlightcolor="black")

        self.Buttonsettings = tk.Button(self.Frame_menedroite)
        self.Buttonsettings.place(relx=-0.069, rely=0.914, height=54, width=77)
        self.Buttonsettings.configure(activebackground="#090513")
        self.Buttonsettings.configure(activeforeground="white")
        self.Buttonsettings.configure(activeforeground="#000000")
        self.Buttonsettings.configure(background="#090513")
        self.Buttonsettings.configure(borderwidth="0")
        self.Buttonsettings.configure(compound='left')
        self.Buttonsettings.configure(disabledforeground="#a3a3a3")
        self.Buttonsettings.configure(foreground="#000000")
        self.Buttonsettings.configure(highlightbackground="#d9d9d9")
        self.Buttonsettings.configure(highlightcolor="black",command=setting)
        photo_location = "./image/settings.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Buttonsettings.configure(image=_img0)
        self.Buttonsettings.configure(pady="0")
        self.Buttonsettings.configure(relief="flat")

        self.Buttonsysteme = tk.Button(self.Frame_menedroite)
        self.Buttonsysteme.place(relx=0.0, rely=0.621, height=34, width=137)
        self.Buttonsysteme.configure(activebackground="#090513")
        self.Buttonsysteme.configure(activeforeground="white")
        self.Buttonsysteme.configure(activeforeground="#ffffff")
        self.Buttonsysteme.configure(background="#090513")
        self.Buttonsysteme.configure(borderwidth="0")
        self.Buttonsysteme.configure(compound='left')
        self.Buttonsysteme.configure(disabledforeground="#a3a3a3")
        self.Buttonsysteme.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.Buttonsysteme.configure(foreground="#ffffff")
        self.Buttonsysteme.configure(highlightbackground="#d9d9d9")
        self.Buttonsysteme.configure(highlightcolor="black")
        photo_location = "./image/cpu.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Buttonsysteme.configure(image=_img1)
        self.Buttonsysteme.configure(pady="0")
        self.Buttonsysteme.configure(relief="flat")
        self.Buttonsysteme.configure(text='''Système''',command=systemee)

        self.Buttonshopping = tk.Button(self.Frame_menedroite)
        self.Buttonshopping.place(relx=0.0, rely=0.534, height=34, width=137)
        self.Buttonshopping.configure(activebackground="#090513")
        self.Buttonshopping.configure(activeforeground="white")
        self.Buttonshopping.configure(activeforeground="#ffffff")
        self.Buttonshopping.configure(background="#090513")
        self.Buttonshopping.configure(borderwidth="0")
        self.Buttonshopping.configure(compound='left')
        self.Buttonshopping.configure(disabledforeground="#a3a3a3")
        self.Buttonshopping.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.Buttonshopping.configure(foreground="#ffffff")
        self.Buttonshopping.configure(highlightbackground="#d9d9d9")
        self.Buttonshopping.configure(highlightcolor="black")
        photo_location = "./image/shopping-bag.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Buttonshopping.configure(image=_img2)
        self.Buttonshopping.configure(pady="0")
        self.Buttonshopping.configure(relief="flat")
        self.Buttonshopping.configure(text='''Shopping''')
        self.tooltip_font = "TkDefaultFont"
        self.Buttonshopping_tooltip = \
        ToolTip(self.Buttonshopping, self.tooltip_font, '''coming soon...''')

        self.Button1 = tk.Button(self.Frame_menedroite)
        self.Button1.place(relx=0.138, rely=0.293, height=34, width=127)
        self.Button1.configure(activebackground="#090513")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="#ffffff")
        self.Button1.configure(background="#090513")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="flat")
        self.Button1.configure(text='''Roblox''',command=roblox)

        self.Buttonpassword = tk.Button(self.Frame_menedroite)
        self.Buttonpassword.place(relx=0.069, rely=0.448, height=34, width=127)
        self.Buttonpassword.configure(activebackground="#090513")
        self.Buttonpassword.configure(activeforeground="white")
        self.Buttonpassword.configure(activeforeground="#ffffff")
        self.Buttonpassword.configure(background="#090513")
        self.Buttonpassword.configure(borderwidth="0")
        self.Buttonpassword.configure(compound='left')
        self.Buttonpassword.configure(disabledforeground="#a3a3a3")
        self.Buttonpassword.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.Buttonpassword.configure(foreground="#ffffff")
        self.Buttonpassword.configure(highlightbackground="#d9d9d9")
        self.Buttonpassword.configure(highlightcolor="black")
        photo_location = "./image/key.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Buttonpassword.configure(image=_img3)
        self.Buttonpassword.configure(pady="0")
        self.Buttonpassword.configure(relief="flat")
        self.Buttonpassword.configure(text='''password''',command=passwordee)

        self.Buttonfoxprotect = tk.Button(self.Frame_menedroite)
        self.Buttonfoxprotect.place(relx=0.069, rely=0.362, height=34, width=127)

        self.Buttonfoxprotect.configure(activebackground="#090513")
        self.Buttonfoxprotect.configure(activeforeground="white")
        self.Buttonfoxprotect.configure(activeforeground="#ffffff")
        self.Buttonfoxprotect.configure(background="#090513")
        self.Buttonfoxprotect.configure(borderwidth="0")
        self.Buttonfoxprotect.configure(compound='left')
        self.Buttonfoxprotect.configure(disabledforeground="#a3a3a3")
        self.Buttonfoxprotect.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.Buttonfoxprotect.configure(foreground="#ffffff")
        self.Buttonfoxprotect.configure(highlightbackground="#d9d9d9")
        self.Buttonfoxprotect.configure(highlightcolor="black")
        photo_location = "./image/shield.png"
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Buttonfoxprotect.configure(image=_img4)
        self.Buttonfoxprotect.configure(pady="0")
        self.Buttonfoxprotect.configure(relief="flat")
        self.Buttonfoxprotect.configure(text='''oxa-protect''',command=antivirusee)

        self.Buttontravaille = tk.Button(self.Frame_menedroite)
        self.Buttontravaille.place(relx=0.0, rely=0.069, height=34, width=127)
        self.Buttontravaille.configure(activebackground="#090513")
        self.Buttontravaille.configure(activeforeground="white")
        self.Buttontravaille.configure(activeforeground="#ffffff")
        self.Buttontravaille.configure(background="#090513")
        self.Buttontravaille.configure(borderwidth="0")
        self.Buttontravaille.configure(compound='left')
        self.Buttontravaille.configure(disabledforeground="#a3a3a3")
        self.Buttontravaille.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
        self.Buttontravaille.configure(foreground="#ffffff")
        self.Buttontravaille.configure(highlightbackground="#d9d9d9")
        self.Buttontravaille.configure(highlightcolor="black")
        photo_location = "./image/coffee.png"
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.Buttontravaille.configure(image=_img5)
        self.Buttontravaille.configure(pady="0")
        self.Buttontravaille.configure(relief="flat")
        self.Buttontravaille.configure(text='''travaille''')
        self.tooltip_font = "TkDefaultFont"
        self.Buttontravaille_tooltip = \
        ToolTip(self.Buttontravaille, self.tooltip_font, '''COMING SOON....''')

        self.Label3 = tk.Label(self.Frame_menedroite)
        self.Label3.place(relx=0.069, rely=0.0, height=31, width=74)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#090513")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''MODE :''')

        self.TSeparator2 = ttk.Separator(self.Frame_menedroite)
        self.TSeparator2.place(relx=0.0, rely=0.276,  relwidth=1.172)

        self.Button2 = tk.Button(self.Frame_menedroite)
        self.Button2.place(relx=0.0, rely=0.138, height=34, width=147)
        self.Button2.configure(activebackground="#090513")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(activeforeground="#ffffff")
        self.Button2.configure(background="#090513")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        photo_location = "./image/shield.png"
        global _img6
        _img6 = tk.PhotoImage(file=photo_location)
        self.Button2.configure(image=_img6)
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="flat")
        self.Button2.configure(text='''Cybersecurité''')

        self.Button3 = tk.Button(self.Frame_menedroite)
        self.Button3.place(relx=-0.138, rely=0.207, height=34, width=147)
        self.Button3.configure(activebackground="#090513")
        self.Button3.configure(activeforeground="white")
        self.Button3.configure(activeforeground="#ffffff")
        self.Button3.configure(background="#090513")
        self.Button3.configure(borderwidth="0")
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.Button3.configure(foreground="#ffffff")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        photo_location = "./image/briefcase.png"
        global _img7
        _img7 = tk.PhotoImage(file=photo_location)
        self.Button3.configure(image=_img7)
        self.Button3.configure(pady="0")
        self.Button3.configure(relief="flat")
        self.Button3.configure(text='''Setup''')

        self.Frame_menu = tk.Frame(self.top)
        self.Frame_menu.place(relx=-0.009, rely=-0.016, relheight=0.095
                , relwidth=1.016)
        self.Frame_menu.configure(relief='flat')
        self.Frame_menu.configure(borderwidth="2")
        self.Frame_menu.configure(background="#090513")
        self.Frame_menu.configure(highlightbackground="#d9d9d9")
        self.Frame_menu.configure(highlightcolor="#d11444")

        self.Label1 = tk.Label(self.Frame_menu)
        self.Label1.place(relx=0.009, rely=0.153, height=46, width=225)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#090513")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial} -size 24 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''OXA-Instinc''')

        self.Buttonacceuille = tk.Button(self.Frame_menu)
        self.Buttonacceuille.place(relx=0.252, rely=0.169, height=44, width=47)
        self.Buttonacceuille.configure(activebackground="#090513")
        self.Buttonacceuille.configure(activeforeground="white")
        self.Buttonacceuille.configure(activeforeground="#000000")
        self.Buttonacceuille.configure(background="#090513")
        self.Buttonacceuille.configure(borderwidth="0")
        self.Buttonacceuille.configure(compound='left')
        self.Buttonacceuille.configure(disabledforeground="#a3a3a3")
        self.Buttonacceuille.configure(foreground="#000000")
        self.Buttonacceuille.configure(highlightbackground="#d9d9d9")
        self.Buttonacceuille.configure(highlightcolor="black",command=acceuilles)
        photo_location = "./image/home.png"
        global _img8
        _img8 = tk.PhotoImage(file=photo_location)
        self.Buttonacceuille.configure(image=_img8)
        self.Buttonacceuille.configure(pady="0")
        self.Buttonacceuille.configure(relief="flat")
        self.tooltip_font = "TkDefaultFont"
        self.Buttonacceuille_tooltip = \
        ToolTip(self.Buttonacceuille, self.tooltip_font, '''acceuille''')
        def github():
            webbrowser.open_new("https://github.com/Freefoxsoft")

        self.Buttongithub = tk.Button(self.Frame_menu)
        self.Buttongithub.place(relx=0.961, rely=0.0, height=64, width=37)
        self.Buttongithub.configure(activebackground="#090513")
        self.Buttongithub.configure(activeforeground="white")
        self.Buttongithub.configure(activeforeground="#000000")
        self.Buttongithub.configure(background="#090513")
        self.Buttongithub.configure(borderwidth="0")
        self.Buttongithub.configure(compound='left')
        self.Buttongithub.configure(disabledforeground="#a3a3a3")
        self.Buttongithub.configure(foreground="#000000")
        self.Buttongithub.configure(highlightbackground="#d9d9d9")
        self.Buttongithub.configure(highlightcolor="black",command=github)
        photo_location = "./image/github.png"
        global _img9
        _img9 = tk.PhotoImage(file=photo_location)
        self.Buttongithub.configure(image=_img9)
        self.Buttongithub.configure(pady="0")
        self.Buttongithub.configure(relief="flat")

        self.Buttonyoutube = tk.Button(self.Frame_menu)
        self.Buttonyoutube.place(relx=0.925, rely=0.339, height=24, width=37)
        self.Buttonyoutube.configure(activebackground="#090513")
        self.Buttonyoutube.configure(activeforeground="white")
        self.Buttonyoutube.configure(activeforeground="#000000")
        self.Buttonyoutube.configure(background="#090513")
        self.Buttonyoutube.configure(borderwidth="0")
        self.Buttonyoutube.configure(compound='left')
        self.Buttonyoutube.configure(disabledforeground="#a3a3a3")
        self.Buttonyoutube.configure(foreground="#000000")
        self.Buttonyoutube.configure(highlightbackground="#d9d9d9")
        self.Buttonyoutube.configure(highlightcolor="black",command=youtubee)
        photo_location = "./image/youtube.png"
        global _img10
        _img10 = tk.PhotoImage(file=photo_location)
        self.Buttonyoutube.configure(image=_img10)
        self.Buttonyoutube.configure(pady="0")
        self.Buttonyoutube.configure(relief="flat")

        self.Buttoninstagram = tk.Button(self.Frame_menu)
        self.Buttoninstagram.place(relx=0.889, rely=0.169, height=44, width=37)
        self.Buttoninstagram.configure(activebackground="#090513")
        self.Buttoninstagram.configure(activeforeground="white")
        self.Buttoninstagram.configure(activeforeground="#000000")
        self.Buttoninstagram.configure(background="#090513")
        self.Buttoninstagram.configure(borderwidth="0")
        self.Buttoninstagram.configure(compound='left')
        self.Buttoninstagram.configure(disabledforeground="#a3a3a3")
        self.Buttoninstagram.configure(foreground="#000000")
        self.Buttoninstagram.configure(highlightbackground="#d9d9d9")
        self.Buttoninstagram.configure(highlightcolor="black")
        photo_location = "./image/instagram.png"
        global _img11
        _img11 = tk.PhotoImage(file=photo_location)
        self.Buttoninstagram.configure(image=_img11)
        self.Buttoninstagram.configure(pady="0")
        self.Buttoninstagram.configure(relief="flat")

        self.Buttonupdater = tk.Button(self.Frame_menu)
        self.Buttonupdater.place(relx=0.18, rely=0.169, height=44, width=37)
        self.Buttonupdater.configure(activebackground="#090513")
        self.Buttonupdater.configure(activeforeground="white")
        self.Buttonupdater.configure(activeforeground="#000000")
        self.Buttonupdater.configure(background="#090513")
        self.Buttonupdater.configure(borderwidth="0")
        self.Buttonupdater.configure(compound='left')
        self.Buttonupdater.configure(disabledforeground="#a3a3a3")
        self.Buttonupdater.configure(foreground="#000000")
        self.Buttonupdater.configure(highlightbackground="#d9d9d9")
        self.Buttonupdater.configure(highlightcolor="black",command=checkingupdate)
        photo_location = "./image/download.png"
        global _img12
        _img12 = tk.PhotoImage(file=photo_location)
        self.Buttonupdater.configure(image=_img12)
        self.Buttonupdater.configure(pady="0")
        self.Buttonupdater.configure(relief="flat")
        self.tooltip_font = "TkDefaultFont"
        self.Buttonupdater_tooltip = \
        ToolTip(self.Buttonupdater, self.tooltip_font, '''Dowload the latest version''')

        self.Buttonbancaire = tk.Button(self.Frame_menu)
        self.Buttonbancaire.place(relx=0.701, rely=0.169, height=44, width=47)
        self.Buttonbancaire.configure(activebackground="#090513")
        self.Buttonbancaire.configure(activeforeground="white")
        self.Buttonbancaire.configure(activeforeground="#000000")
        self.Buttonbancaire.configure(background="#090513")
        self.Buttonbancaire.configure(borderwidth="0")
        self.Buttonbancaire.configure(compound='left')
        self.Buttonbancaire.configure(disabledforeground="#a3a3a3")
        self.Buttonbancaire.configure(foreground="#000000")
        self.Buttonbancaire.configure(highlightbackground="#d9d9d9")
        self.Buttonbancaire.configure(highlightcolor="black")
        photo_location = "./image/credit-card.png"
        global _img13
        _img13 = tk.PhotoImage(file=photo_location)
        self.Buttonbancaire.configure(image=_img13)
        self.Buttonbancaire.configure(pady="0")
        self.Buttonbancaire.configure(relief="flat")
        self.tooltip_font = "TkDefaultFont"
        self.Buttonbancaire_tooltip = \
        ToolTip(self.Buttonbancaire, self.tooltip_font, '''coming soon...''')

        self.Buttontwitter = tk.Button(self.Frame_menu)
        self.Buttontwitter.place(relx=0.854, rely=0.169, height=44, width=37)
        self.Buttontwitter.configure(activebackground="#090513")
        self.Buttontwitter.configure(activeforeground="white")
        self.Buttontwitter.configure(activeforeground="#000000")
        self.Buttontwitter.configure(background="#090513")
        self.Buttontwitter.configure(borderwidth="0")
        self.Buttontwitter.configure(compound='left')
        self.Buttontwitter.configure(disabledforeground="#a3a3a3")
        self.Buttontwitter.configure(foreground="#000000")
        self.Buttontwitter.configure(highlightbackground="#d9d9d9")
        self.Buttontwitter.configure(highlightcolor="black")
        photo_location = "./image/twitter.png"
        global _img14
        _img14 = tk.PhotoImage(file=photo_location)
        self.Buttontwitter.configure(image=_img14)
        self.Buttontwitter.configure(pady="0")
        self.Buttontwitter.configure(relief="flat")

        self.Buttontwitch = tk.Button(self.Frame_menu)
        self.Buttontwitch.place(relx=0.818, rely=0.169, height=44, width=37)
        self.Buttontwitch.configure(activebackground="#090513")
        self.Buttontwitch.configure(activeforeground="white")
        self.Buttontwitch.configure(activeforeground="#000000")
        self.Buttontwitch.configure(background="#090513")
        self.Buttontwitch.configure(borderwidth="0")
        self.Buttontwitch.configure(compound='left')
        self.Buttontwitch.configure(disabledforeground="#a3a3a3")
        self.Buttontwitch.configure(foreground="#000000")
        self.Buttontwitch.configure(highlightbackground="#d9d9d9")
        self.Buttontwitch.configure(highlightcolor="black")
        photo_location = "./image/twitch.png"
        global _img15
        _img15 = tk.PhotoImage(file=photo_location)
        self.Buttontwitch.configure(image=_img15)
        self.Buttontwitch.configure(pady="0")
        self.Buttontwitch.configure(relief="flat")

        self.Buttonlinkedin = tk.Button(self.Frame_menu)
        self.Buttonlinkedin.place(relx=0.782, rely=0.169, height=44, width=37)
        self.Buttonlinkedin.configure(activebackground="#090513")
        self.Buttonlinkedin.configure(activeforeground="white")
        self.Buttonlinkedin.configure(activeforeground="#000000")
        self.Buttonlinkedin.configure(background="#090513")
        self.Buttonlinkedin.configure(borderwidth="0")
        self.Buttonlinkedin.configure(compound='left')
        self.Buttonlinkedin.configure(disabledforeground="#a3a3a3")
        self.Buttonlinkedin.configure(foreground="#000000")
        self.Buttonlinkedin.configure(highlightbackground="#d9d9d9")
        self.Buttonlinkedin.configure(highlightcolor="black")
        photo_location = "./image/linkedin.png"
        global _img16
        _img16 = tk.PhotoImage(file=photo_location)
        self.Buttonlinkedin.configure(image=_img16)
        self.Buttonlinkedin.configure(pady="0")

        self.Buttonemail = tk.Button(self.Frame_menu)
        self.Buttonemail.place(relx=0.737, rely=0.169, height=44, width=37)
        self.Buttonemail.configure(activebackground="#090513")
        self.Buttonemail.configure(activeforeground="white")
        self.Buttonemail.configure(activeforeground="#000000")
        self.Buttonemail.configure(background="#090513")
        self.Buttonemail.configure(borderwidth="0")
        self.Buttonemail.configure(compound='left')
        self.Buttonemail.configure(disabledforeground="#a3a3a3")
        self.Buttonemail.configure(foreground="#000000")
        self.Buttonemail.configure(highlightbackground="#d9d9d9")
        self.Buttonemail.configure(highlightcolor="black")
        photo_location = "./image/mail.png"
        global _img17
        _img17 = tk.PhotoImage(file=photo_location)
        self.Buttonemail.configure(image=_img17)
        self.Buttonemail.configure(pady="0")
        self.Buttonemail.configure(relief="flat")
        self.tooltip_font = "TkDefaultFont"
        self.Buttonemail_tooltip = \
        ToolTip(self.Buttonemail, self.tooltip_font, '''coming soon''')

        self.Buttonsupport = tk.Button(self.Frame_menu)
        self.Buttonsupport.place(relx=0.216, rely=0.169, height=44, width=37)
        self.Buttonsupport.configure(activebackground="#090513")
        self.Buttonsupport.configure(activeforeground="white")
        self.Buttonsupport.configure(activeforeground="#000000")
        self.Buttonsupport.configure(background="#090513")
        self.Buttonsupport.configure(borderwidth="0")
        self.Buttonsupport.configure(compound='left')
        self.Buttonsupport.configure(disabledforeground="#a3a3a3")
        self.Buttonsupport.configure(foreground="#000000")
        self.Buttonsupport.configure(highlightbackground="#d9d9d9")
        self.Buttonsupport.configure(highlightcolor="black")
        photo_location = "./image/send.png"
        global _img18
        _img18 = tk.PhotoImage(file=photo_location)
        self.Buttonsupport.configure(image=_img18)
        self.Buttonsupport.configure(pady="0")
        self.Buttonsupport.configure(relief="flat")
        self.tooltip_font = "TkDefaultFont"
        self.Buttonsupport_tooltip = \
        ToolTip(self.Buttonsupport, self.tooltip_font, '''Mise à jour dimanche ;)''')

        self.TSeparator1 = ttk.Separator(self.Frame_menu)
        self.TSeparator1.place(relx=0.774, rely=0.203,  relheight=3.559)
        self.TSeparator1.configure(orient="vertical")

        self.FRAMEacceuille = tk.Frame(self.top)
        self.FRAMEacceuille.place(relx=0.119, rely=0.065, relheight=0.939
                , relwidth=0.9)
        self.FRAMEacceuille.configure(relief='flat')
        self.FRAMEacceuille.configure(borderwidth="2")
        self.FRAMEacceuille.configure(background="#242436")
        self.FRAMEacceuille.configure(highlightbackground="#d11444")
        self.FRAMEacceuille.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.FRAMEacceuille)
        self.Label2.place(relx=0.892, rely=0.948, height=30, width=85)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#242436")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Version 1.0''')

        self.Labelbienvenue = tk.Label(self.FRAMEacceuille)
        self.Labelbienvenue.place(relx=0.284, rely=0.241, height=99, width=368)
        self.Labelbienvenue.configure(activebackground="#f9f9f9")
        self.Labelbienvenue.configure(activeforeground="black")
        self.Labelbienvenue.configure(anchor='w')
        self.Labelbienvenue.configure(background="#242436")
        self.Labelbienvenue.configure(compound='left')
        self.Labelbienvenue.configure(disabledforeground="#a3a3a3")
        self.Labelbienvenue.configure(font="-family {Segoe UI} -size 48 -weight bold")
        self.Labelbienvenue.configure(foreground="#d11444")
        self.Labelbienvenue.configure(highlightbackground="#d9d9d9")
        self.Labelbienvenue.configure(highlightcolor="black")
        self.Labelbienvenue.configure(text='''Bienvenue !''')

        self.Buttonsitedestreaming = tk.Button(self.FRAMEacceuille)
        self.Buttonsitedestreaming.place(relx=0.771, rely=-0.017, height=44
                , width=217)
        self.Buttonsitedestreaming.configure(activebackground="#242436")
        self.Buttonsitedestreaming.configure(activeforeground="white")
        self.Buttonsitedestreaming.configure(activeforeground="#000000")
        self.Buttonsitedestreaming.configure(background="#242436")
        self.Buttonsitedestreaming.configure(borderwidth="0")
        self.Buttonsitedestreaming.configure(compound='left')
        self.Buttonsitedestreaming.configure(disabledforeground="#a3a3a3")
        self.Buttonsitedestreaming.configure(font="-family {Segoe UI Variable Text} -size 17 -weight bold")
        self.Buttonsitedestreaming.configure(foreground="#ff8000")
        self.Buttonsitedestreaming.configure(highlightbackground="#d9d9d9")
        self.Buttonsitedestreaming.configure(highlightcolor="black")
        self.Buttonsitedestreaming.configure(pady="0")
        self.Buttonsitedestreaming.configure(relief="flat")
        self.Buttonsitedestreaming.configure(text='''FreefoxStreaming''')
        self.tooltip_font = "TkDefaultFont"
        self.Buttonsitedestreaming_tooltip = \
        ToolTip(self.Buttonsitedestreaming, self.tooltip_font, '''coming soon''')

        self.Buttondiscord = tk.Button(self.FRAMEacceuille)
        self.Buttondiscord.place(relx=0.172, rely=0.534, height=54, width=77)
        self.Buttondiscord.configure(activebackground="#242436")
        self.Buttondiscord.configure(activeforeground="white")
        self.Buttondiscord.configure(activeforeground="#000000")
        self.Buttondiscord.configure(background="#242436")
        self.Buttondiscord.configure(borderwidth="0")
        self.Buttondiscord.configure(compound='left')
        self.Buttondiscord.configure(disabledforeground="#a3a3a3")
        self.Buttondiscord.configure(foreground="#000000")
        self.Buttondiscord.configure(highlightbackground="#d9d9d9")
        self.Buttondiscord.configure(highlightcolor="black",command=discorde)
        photo_location = "./image/discord.png"
        global _img19
        _img19 = tk.PhotoImage(file=photo_location)
        self.Buttondiscord.configure(image=_img19)
        self.Buttondiscord.configure(pady="0")
        self.Buttondiscord.configure(relief="flat")

        self.Button25 = tk.Button(self.FRAMEacceuille)
        self.Button25.place(relx=0.0, rely=0.931, height=34, width=87)
        self.Button25.configure(activebackground="#242436")
        self.Button25.configure(activeforeground="white")
        self.Button25.configure(activeforeground="#ffffff")
        self.Button25.configure(background="#242436")
        self.Button25.configure(borderwidth="0")
        self.Button25.configure(compound='left')
        self.Button25.configure(disabledforeground="#a3a3a3")
        self.Button25.configure(font="-family {Segoe UI Black} -size 16 -weight bold")
        self.Button25.configure(foreground="#ffffff")
        self.Button25.configure(highlightbackground="#d9d9d9")
        self.Button25.configure(highlightcolor="black")
        self.Button25.configure(pady="0")
        self.Button25.configure(relief="flat")
        self.Button25.configure(text='''CREDIT''',command=Credit)

# Support code for Balloon Help (also called tooltips).
# derived from http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
from time import time, localtime, strftime
class ToolTip(tk.Toplevel):
    """ Provides a ToolTip widget for Tkinter. """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=0.5, follow=True):
        self.wdgt = wdgt
        self.parent = self.wdgt.master
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        self.withdraw()
        self.overrideredirect(True)
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')
    def spawn(self, event=None):
        self.visible = 1
        self.after(int(self.delay * 1000), self.show)
    def show(self):
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()
    def move(self, event):
        self.lastMotion = time()
        if self.follow is False:
            self.withdraw()
            self.visible = 1
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)
    def hide(self, event=None):
        self.visible = 0
        self.withdraw()
    def update(self, msg):
        self.msgVar.set(msg)
#                   End of Class ToolTip

def start_up():
    unknown_support.main()
if __name__ == '__main__':
    unknown_support.main()
