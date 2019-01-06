from tkinter import *
from tkinter.colorchooser import *
import random
import time


def initfenetre():
    fenetre = Tk()
    fenetre.title('Pong')
    fenetre.resizable(0,0)
    fenetre.wm_attributes('-topmost',1)
    fenetre.update()
    return fenetre

def initcanvas(fenetre):
    canvas = Canvas(fenetre, width = 800, height = 600, bd = 0, highlightthickness = 0)
    canvas.config(bg = 'black')
    canvas.pack()
    fenetre.update()
    canvas.create_line(400,0,400,600, fill = 'white')
    return canvas


class balle:
    def __init__(self,canvas,colorballe,bare,bare2):
        self.canvas = canvas
        self.bare = bare
        self.bare2 = bare2
        self.compteur1 = 0
        self.compteur2 = 0
        self.id = canvas.create_oval(10,10,25,25, fill = colorballe)
        self.canvas.move(self.id,385,300)
        start = [-3,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.colorballe = colorballe

        

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
            self.score(True)
        if pos[2] >= self.canvas_width:
            self.x = -3
            self.score(False)
        if self.choc_bar1(pos) == True:
            self.x = 3
        if self.choc_bar2(pos) == True:
            self.x = -3

    def choc_bar1(self,pos):
        barepos = self.canvas.coords(self.bare.id)
        if pos[1] >= barepos[1] and pos [1] <= barepos[3]:
            if pos[0] >= barepos[0] and pos[0] <= barepos[2]:
                return True
            return False
    
    def choc_bar2(self,pos):
        barepos = self.canvas.coords(self.bare2.id)
        if pos[1] >= barepos[1] and pos [1] <= barepos[3]:
            if pos[2] >= barepos[0] and pos[2] <= barepos[2]:
                return True
            return False

    def score(self,val):
        global compteur1
        global compteur2

        if val == True:
            a = self.canvas.create_text(200,40,text = self.compteur1, font =('Arial',60),fill = 'white')
            self.canvas.itemconfig(a,fill = 'black')
            self.compteur1 += 1
            a = self.canvas.create_text(200,40,text = self.compteur1, font =('Arial',60),fill = 'white')
           
        if val == False:
            a = self.canvas.create_text(600,40,text = self.compteur2, font =('Arial',60),fill = 'white')
            self.canvas.itemconfig(a,fill = 'black')
            self.compteur2 += 1
            a = self.canvas.create_text(600,40,text = self.compteur2, font =('Arial',60),fill = 'white')
        

class Bare:

    def __init__(self,canvas,colorbare):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,30,100, fill =colorbare)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_widht = self.canvas.winfo_width()
        self.canvas.bind_all('a',self.haut)
        self.canvas.bind_all('e',self.bas)
        self.colorbare = colorbare

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        #Pour le champs de la bare ! [x1,y1,x2,y2]
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1 

    def haut(self,evt):
        self.y = -3

    def bas(self,evt):
        self.y = 3
    
    

class Bare2:
    def __init__(self,canvas,colorbare2):
        self.canvas = canvas
        self.id = canvas.create_rectangle(800,100,770,0, fill = colorbare2)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_widht = self.canvas.winfo_width()
        self.canvas.bind_all('1',self.haut)
        self.canvas.bind_all('3',self.bas)
        self.colorbare2 = colorbare2

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        #Pour le champs de la bare ! [x1,y1,x2,y2]
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1
        
    def haut(self,evt):
        self.y = -3

    def bas(self,evt):
        self.y = 3

def stop():
    Balle.x = 0
    Balle.y = 0
    bare.x = 0
    bare.y = 0
    bare2.x = 0
    bare2.y = 0
    canvas.create_text(400,300,text = " Bien joué à vous ! " ,font = ("Purisa", 32), fill = 'red')
    stoper_chrono()
    message.configure(text="Chrono prêt")
    #mbutton = Button(fenetre,font=('sans', 20, 'bold'),text = "Rejouer", command = lambda: game(Balle,bare,bare2,fenetre,canvas)).pack()



#Deux fonction qui servent de Check, et casser une boucle
checkx = 0
check = 0
def play():
    global check
    check = 1

clique = 0
def cliquecheck():
    global clique
    clique += 1


#Pour la couleur de base!
color =''
colorbare = 'orange'
colorbare2 = 'orange'
colorballe = 'orange'





#Menu
def jsp():

    global message

    mainmenue = Menu(fenetre)
    menu1 = Menu(mainmenue, tearoff=0)
    menu1.add_command(label = "Couleur J1", command = lambda: getColorbare(color))
    menu1.add_command(label = "Couleur J2", command = lambda: getColorbare2(color))
    menu1.add_command(label = "Couleur Balle",command = lambda: getColorballe(color))

    menu2 = Menu(mainmenue, tearoff=0)
    menu2.add_command(label = "Pas de temps", command = lambda: pasdetemps())
    menu2.add_command(label = "30Sec", command = lambda: lancer_chrono2())
    menu2.add_command(label = "45Sec", command = lambda: lancer_chrono3())
    menu2.add_command(label = "60Sec", command = lambda: lancer_chrono4())
    menu2.add_command(label = "90Sec", command = lambda: lancer_chrono5())
    menu2.add_command(label = "120Sec", command = lambda: lancer_chrono6())

    menu3 = Menu(mainmenue, tearoff=0)
    menu3.add_command(label = "Pas de points", command = lambda: nopoint())
    menu3.add_command(label = "3 Points", command = lambda: troispoint())
    menu3.add_command(label = "5 Points", command = lambda: cinqpoint())
    menu3.add_command(label = "10 Points", command = lambda: dixpoint())
    menu3.add_command(label = "20 Points", command = lambda: twentypoint())

    mainmenue.add_cascade(label = 'Couleur', menu=menu1)
    mainmenue.add_cascade(label = 'Temps', menu=menu2)
    mainmenue.add_cascade(label = 'Points', menu=menu3)

    mainmenue.add_command(label = "Go", command=lancer_chrono)
    mainmenue.add_command(label = "Stop", command=stoper_chrono)
    mainmenue.add_command(label = "Quitter", command=fenetre.destroy)

    message = Label(fenetre,font=('sans', 20, 'bold'),text="Chrono prêt")
    message.pack(side = BOTTOM)

    fenetre.config(menu = mainmenue)


#Pour les points !!!

global scorex
scorex = 10000

def nopoint():
    global scorex
    scorex = 1000

def troispoint():
    global scorex
    scorex = 3

def cinqpoint():
    global scorex
    scorex = 5

def dixpoint():
    global scorex
    scorex = 10

def twentypoint():
    global scorex
    scorex = 20


#Couleur

def getColorbare(color):
    colorpick = askcolor()
    colorbare = colorpick[1]
    canvas.delete(bare.id)
    bare.id = canvas.create_rectangle(0,0,30,100, fill =colorbare)
    canvas.coords(bare.id)
    bare.colorbare = colorbare

    return color

def getColorbare2(color):
    colorpick = askcolor()
    colorbare2 = colorpick[1]
    canvas.delete(bare2.id)
    bare2.id = canvas.create_rectangle(800,100,770,0, fill =colorbare2)
    canvas.coords(bare2.id)
    bare2.colorbare2 = colorbare2
   
    return color

def getColorballe(color):
    colorpick = askcolor()
    colorballe = colorpick[1]
    canvas.delete(Balle.id)
    Balle.id = canvas.create_oval(10,10,25,25, fill = colorballe)
    canvas.coords(Balle.id)
    Balle.colorballe = colorballe
   

    return color


#Pour le temps !

def trentesec():
    lancer_chrono()
    print(secondes)
    if flag:
        print('Good')
    fenetre.after(1000,top_horloge)
    
def lancer_chrono():
    global depart,flag
    flag=1
    depart = time.time()
    top_horloge()
    
def stoper_chrono():
    global flag
    flag=0

def top_horloge():
    global depart,flag
    global minutes
    global secondes
    y=time.time()-depart    
    minutes = time.localtime(y)[4]
    secondes = time.localtime(y)[5]
    if flag :
        message.configure(text = "%i min %i sec " %(minutes,secondes))
    fenetre.after(1000,top_horloge)

def pasdetemps():
    message.configure(text = "Pas de Temps !")

def lancer_chrono2():
    global depart,flag
    flag=1
    depart = time.time()
    top_horloge30()

def lancer_chrono3():
    global depart,flag
    flag=1
    depart = time.time()
    top_horloge45()

def lancer_chrono4():
    global depart,flag
    flag=1
    depart = time.time()
    top_horloge60()

def lancer_chrono5():
    global depart,flag
    flag=1
    depart = time.time()
    top_horloge90()

def lancer_chrono6():
    global depart,flag
    flag=1
    depart = time.time()
    top_horloge120()

def top_horloge30():
    global checkx
    global depart,flag
    global minutes
    global secondes
    y=time.time()-depart    
    minutes = time.localtime(y)[4]
    secondes = time.localtime(y)[5]
    if flag :
        message.configure(text = "%i min %i sec " %(minutes,secondes))
        if secondes == 10:
            checkx = 1
    fenetre.after(1000,top_horloge30)

def top_horloge45():
    global checkx
    global depart,flag
    global minutes
    global secondes
    y=time.time()-depart    
    minutes = time.localtime(y)[4]
    secondes = time.localtime(y)[5]
    if flag :
        message.configure(text = "%i min %i sec " %(minutes,secondes))
        if secondes == 45:
            checkx = 1
    fenetre.after(1000,top_horloge45)

def top_horloge60():
    global checkx
    global depart,flag
    global minutes
    global secondes
    y=time.time()-depart    
    minutes = time.localtime(y)[4]
    secondes = time.localtime(y)[5]
    if flag :
        message.configure(text = "%i min %i sec " %(minutes,secondes))
        if minutes == 1:
            checkx = 1
    fenetre.after(1000,top_horloge60)

def top_horloge90():
    global checkx
    global depart,flag
    global minutes
    global secondes
    y=time.time()-depart    
    minutes = time.localtime(y)[4]
    secondes = time.localtime(y)[5]
    if flag :
        message.configure(text = "%i min %i sec " %(minutes,secondes))
        if secondes == 30 and minutes == 1:
            checkx = 1
    fenetre.after(1000,top_horloge90)

def top_horloge120():
    global checkx
    global depart,flag
    global minutes
    global secondes
    y=time.time()-depart    
    minutes = time.localtime(y)[4]
    secondes = time.localtime(y)[5]
    if flag :
        message.configure(text = "%i min %i sec " %(minutes,secondes))
        if minutes == 2:
            checkx = 1
    fenetre.after(1000,top_horloge120)
    
flag=0
depart = 0



#Le score
def fin(balle):
    return balle.compteur1 >= scorex or balle.compteur2 >= scorex

#Pour refaire une partie(Marche pas)
def game(Balle,bare,bare2,fenetre,canvas):
    global checkx
    Balle.compteur1= 0
    Balle.compteur2 = 0

    while not fin(Balle):
        Balle.draw()
        bare.draw()
        bare2.draw()

        if fin(Balle) or checkx == 1:
            stop()
            fenetre.update()
            time.sleep(5)
            canvas.destroy()
            checkx = 0
            print(checkx)
        time.sleep(0.01)
        fenetre.update_idletasks()
        fenetre.update()
        
#Lancer le jeu
def startjeu(bare, bare2, Balle, fenetre):
    essai = 1 
    while 1:
        if fin(Balle):
            menu(Balle, bare, bare2, fenetre)
        else:
            if check == essai:
                button.destroy()
                ready(canvas, bare, bare2, Balle)
                essai += 1
        fenetre.update()
click = 1

#Acceuille + destruction + lance la fonction ready
def menu(Balle, bare, bare2, fenetre):
    global click
    canvas = initcanvas(fenetre)
    button = Button(canvas,width=800,height=600,image=img,bg='black',command=cliquecheck)
    button.pack()

    while fin(Balle):
        if clique == 1:
            button.destroy()
            ready(canvas, bare, bare2, Balle)
        fenetre.update()

#Sert initialiser tout ou lancer game
def ready(canvas,bare,bare2,Balle):
    if fin(Balle):
        canvas.destroy()
        canvas = initcanvas(fenetre)
        bare = Bare(canvas, colorbare)
        bare2 = Bare2(canvas, colorbare2)
        Balle = balle(canvas, colorballe, bare, bare2)
        Balle.compteur1 = 0
        Balle.compteur2 = 0

    while not fin(Balle):
        game(Balle,bare,bare2,fenetre,canvas)
        fenetre.update()
        

fenetre = initfenetre()
canvas = initcanvas(fenetre)
img = PhotoImage(file="acc.png")

button = Button(canvas,width=800,height=600,image=img,bg='black',command=play)
button.pack()


#Lance le munu
jsp()

bare = Bare(canvas, colorbare)
bare2 = Bare2(canvas, colorbare2)
Balle = balle(canvas, colorballe, bare, bare2)
startjeu(bare,bare2,Balle,fenetre)

colorbare = getColorbare(color)
colorbare2 = getColorbare2(color)
colorballe = getColorballe(color)
