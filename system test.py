import os
import shutil
from tkinter import *
from tkinter.messagebox import *
import winreg
import ctypes
import webbrowser
from update_check import *
import platform



root = Tk()
root.geometry("720x720")

locale = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')





def blocker():
    if platform.system() == "Windows":
        pathToHosts = r"C:\Windows\System32\drivers\etc\hosts"
    elif platform.system() == "Linux":
        pathToHosts = r"/etc/hosts"

    redirect = "127.0.0.1"
    websites = ["www.adfpoint.com","www.passeura.com","www.dirtyleague.com","www.ultimateaderaser.com","www.d1gpk60s9m56kt.cloudfront.net","www.youporn.com","www.iyfbodn.com"]
    with open(pathToHosts, 'r+') as file:
        content = file.read()
        for site in websites:
            if site in content:
                pass
            else:
                file.write(redirect + " " + site + "\n")

# nettoyage navigateur google===========================================================================================
def navigateur():
    try:
        os.remove(locale + "\\Google\\Chrome\\User Data\\Default\\Login Data")
        os.remove(locale + "\\Google\\Chrome\\User Data\\Default\\History")
        os.remove(locale + "\\Google\\Chrome\\User Data\\Default\\Visited Links")
        os.remove(locale + "\\Google\\Chrome\\User Data\\Default\\Web Data")
        os.remove(locale + "\\Google\\Chrome\\User Data\\Default\\Login Data For Account")
        shutil.rmtree(locale + "\\Google\\Chrome\\User Data\\Default\\GPUCACHE")
        shutil.rmtree(locale + "\\Google\\Chrome\\User Data\\Default\\Session Storage")
        shutil.rmtree(locale + "\\Google\\Chrome\\User Data\\Default\\Cache\\Cache_Data")
    except FileNotFoundError:
        try:
            os.remove(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Login Data")
            os.remove(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Visited Links")
            os.remove(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\Web Data")
            os.remove(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History")
            shutil.rmtree(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\GrShaderCache\\GPUCache")
            shutil.rmtree(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache\\Cache_Data")
            showinfo("réussite", "opération reussite")
        except PermissionError:
            showwarning("navigateur", "fermer votre navigateur")


# fixbug====================================================================================================
def reparations():
    try:
        shutil.rmtree(locale + "\\EpicGamesLauncher\\Saved\\webcache_4430")
        shutil.rmtree(locale + "\\EpicGamesLauncher\\Saved\\webcache")
    except FileNotFoundError:
        pass
    except PermissionError:
        os.system("taskkill /IM EpicGamesLauncher.exe")
    os.system("ipconfig /flushdns")
    os.system("netsh int ip reset")
    os.system("netsh winsock reset")
    os.system("DISM /Online /Cleanup-Image /ScanHealth")  # commande batch
    os.system("sfc /scannow")
    # os.system("wsreset")
    showinfo("Redémmarage", "redémarrer votre pc")



# nettoyage windows=====================================================================================================
def windows():
    try:
        shutil.rmtree(locale + "\\cache")
        shutil.rmtree(locale + "\\Package Cache")
        shutil.rmtree(locale + "\\D3DSCache")
        shutil.rmtree("C:\\Windows\\SystemTemp")
        shutil.rmtree("C:\\Windows\\Prefetch")
        shutil.rmtree(locale + "\\Microsoft\\Windows\\History")
        shutil.rmtree(locale + "\\Microsoft\\Windows\\INetCache")
        shutil.rmtree("C:\\Windows\\SoftwareDistribution\\Download")
        shutil.rmtree("C:\\Windows\\Temp")
        shutil.rmtree(roaming + "\\discord\\Cache")
        shutil.rmtree(roaming + "\\discord\\Cookies")
        shutil.rmtree(locale + "\\NVIDIA\\GLCache")
        showinfo("reussite", "opération réussite")
    except FileNotFoundError:
        pass
    try:
        shutil.rmtree(locale + "\\Temp")
    except PermissionError:
        showwarning("application", "fermer les applications en cours")
    except FileNotFoundError:
        pass

    try:
        shutil.rmtree(locale + "\\NVIDIA\\DXCache")
    except PermissionError:
        pass


def registre():
    winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Local Settings\\Software\\Microsoft\\Windows\\Shell\\BagMRU')


# ccleaner=============================================================================================================
def updater():
    update("requirement.txt", "https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/mail_domain.txt")
    showinfo("update", "application mise à jour avec succès")


button = Button(root, text="nettoyage navigateur", command=navigateur)
button.pack()
updates = Button(root, text="updatechecker", command=updater)
updates.pack()
windos = Button(root, text="windowsnettoyage", command=windows)
windos.pack()
reparation = Button(root, text="all fixbug", command=reparations)
reparation.pack()
blocker = Button(root, text="blocker", command=blocker)
blocker.pack()
root.mainloop()
