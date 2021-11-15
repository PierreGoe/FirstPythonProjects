import tkinter
import Kelio
#-------------------------------------------------------------------------
mainapp = tkinter.Tk()
mainapp.title("Kelio") # Changer titre fenetre 
# mainapp.geometry("800x600+100+100") #Prend comme argument X*Y)
# mainapp.minsize("640x480") #Taille minimal
# mainapp.maxsize("1200x800") #Taille maximal
# mainapp.resizable(width=False, height=True) # Choisir si la fenetre est redimentionnable 
# mainapp.positionfrom("user") # Possition par defaut 


def fonction1():
    Kelio.UserID =entry_name.get()
    Kelio.Password = entry_password.get()
    Kelio.fonction_main()


#Centrage fenetre sur l'ecrant -------------------------------------------
screen_x = int(mainapp.winfo_screenwidth())
screen_y = int(mainapp.winfo_screenheight())
window_x = 800 
window_y = 600
pos_x = (screen_x//2) - (window_x//2)
pos_y = (screen_y//2) - (window_y//2)


geo = "{}x{}+{}+{}".format(window_x,window_y,pos_x,pos_y)
mainapp.geometry(geo)

# ------------------------------------------------------------------------

# Premier Widget --------------------------------------------------------
label_name = tkinter.Label(mainapp, text="User :")
entry_name = tkinter.Entry(mainapp, width=45)
label_password = tkinter.Label(mainapp, text="Password :")
entry_password = tkinter.Entry(mainapp, width=45, show='*')

Button = tkinter.Button(mainapp, text="submit", width=40, command=fonction1)

label_name.pack()
entry_name.pack()
label_password.pack()
entry_password.pack()

Button.pack()











mainapp.mainloop()
#mainapp.quit() #Quiter la fenetre grace au code 

