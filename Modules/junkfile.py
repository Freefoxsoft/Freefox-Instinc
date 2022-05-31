import shutil
import os
from tkinter.messagebox import *



def junkfile():
    locale = os.getenv('LOCALAPPDATA')
    try:
        print("supprimer")
        shutil.rmtree(locale + "\\Battle.net\\BrowserCache")
        shutil.rmtree(locale + "\\Battle.net\\Cache")
        os.remove(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Visited Links")
        os.remove(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\Web Data")
        os.remove(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History")
        shutil.rmtree(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache\\Cache_Data")
        shutil.rmtree(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Code Cache")
        shutil.rmtree(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\IndexedDB")
    except FileNotFoundError:
        pass
    except PermissionError:
        showwarning("navigateur", "fermer votre navigateur")
    try:
        shutil.rmtree(locale + "\\BraveSoftware\\Brave-Browser\\User Data\\GrShaderCache\\GPUCache")
    except FileNotFoundError:
        pass
    except PermissionError:
        showwarning("navigateur", "fermer votre navigateur")