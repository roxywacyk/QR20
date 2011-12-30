#Roxy Wacyk HW 10, created on a mac computer
#Click "Instructions" button for instructions on using the program

from Tkinter import *#Import Tkinter module
root=Tk()#create GUI window, root
c1=Canvas(root,width=610,height=320)#Create canvas in root, titled c1
c1.grid(row=1,column=1,rowspan=4)#grid the canvas
f="Times 18"#Standard font for widgets
import random#Import random module
from time import *#Import time module

#Set default colors for figure's skin, hair, eyes, lips
#Set lists of possible colors for each of these body parts (colors that could reasonably fit)
skin="bisque"
skincolors=["bisque","bisque2","blanched almond","brown","burlywood","burlywood2","burlywood4","khaki","chocolate4","pale goldenrod","peru","tan1","tan2","tan3","tan4"]
hair="tan4"
haircolors=["tan4","black","sienna","grey20","grey50","grey90","yellow","red2","red3","red4","firebrick3","firebrick4"]
eyes="dark blue"
eyecolors=["dark blue","grey50","cyan4","pale turquoise","peru","lavender","black","dark magenta","blue2","forest green","firebrick4","tan4"]
lips="brown1"
lipcolors=["brown1","brown2","brown3","brown4","deep pink","dark red","firebrick2","firebrick3","firebrick4","red1","red2","red3","red4"]
#let x1 and y1 be the top-center of the head of the body (to be used as reference points)
x1=120
y1=20
#Create polygons on the canvas for each body part. For body parts with variable colors, specify the fill/outline to be
#equal to the variables skin, hair, eyes, and lips created above. 
hair=c1.create_arc(x1-50,y1-5,x1+50,y1+160,start=0,extent=180,style="pieslice",fill=hair,outline=hair)
head=c1.create_oval(x1-30,y1,x1+30,y1+80,fill=skin,outline=skin)
Leye=c1.create_oval(x1-25,y1+20,x1-5,y1+35,fill="white")
Lpupil=c1.create_oval(x1-20,y1+20,x1-10,y1+35,fill=eyes)
Lblack=c1.create_oval(x1-17,y1+25,x1-13,y1+30,fill="black")
Reye=c1.create_oval(x1+25,y1+20,x1+5,y1+35,fill="white")
Rpupil=c1.create_oval(x1+20,y1+20,x1+10,y1+35,fill=eyes)
Rblack=c1.create_oval(x1+17,y1+25,x1+13,y1+30,fill="black")
nose=c1.create_arc(x1-5,y1+40,x1+5,y1+50,start=90,extent=180,style="arc")
Lmouthtop=c1.create_arc(x1-10,y1+55,x1,y1+65,start=0,extent=180,style="pieslice",fill=lips)
Rmouthtop=c1.create_arc(x1+10,y1+55,x1,y1+65,start=0,extent=180,style="pieslice",fill=lips)
mouthbottom=c1.create_arc(x1-10,y1+53,x1+10,y1+67,start=180,extent=180,style="pieslice",fill=lips)
Lbody=c1.create_polygon(x1,y1+80,x1-10,y1+80,x1-10,y1+90,x1-70,y1+140,x1-80,y1+140,x1-60,y1+160,x1-60,y1+150,x1-20,y1+115,x1-20,y1+180,x1-50,y1+290,x1-60,y1+290,x1-60,y1+300,x1-30,y1+300,x1-30,y1+290,x1,y1+180,fill=skin)
Rbody=c1.create_polygon(x1,y1+80,x1+10,y1+80,x1+10,y1+90,x1+70,y1+140,x1+80,y1+140,x1+60,y1+160,x1+60,y1+150,x1+20,y1+115,x1+20,y1+180,x1+50,y1+290,x1+60,y1+290,x1+60,y1+300,x1+30,y1+300,x1+30,y1+290,x1,y1+180,fill=skin)

#Find function to be used for finding the location of color name within a specified color list, so that colors are not
#repeated when circling through the list
def find(color,colorlist):
    for i in range(len(colorlist)):
        if color==colorlist[i]:
            return i#return index of the color

#Functions for changing body colors
def changeSkin():
    currentC=c1.itemcget(head,"fill")#Get the current color of the skin, currentC
    index=find(currentC,skincolors)#find the index of that color
#if the color is not the last color in the list, change the color to the next one in the relevant list for each skin colored body part
    if index<len(skincolors)-1:
        c1.itemconfig(head,fill=skincolors[index+1],outline=skincolors[index+1])
        c1.itemconfig(Lbody,fill=skincolors[index+1],outline=skincolors[index+1])
        c1.itemconfig(Rbody,fill=skincolors[index+1],outline=skincolors[index+1])
    else:#if last color in the list, move back to the first color in the relevant list
        c1.itemconfig(head,fill=skincolors[0],outline=skincolors[0])
        c1.itemconfig(Lbody,fill=skincolors[0],outline=skincolors[0])
        c1.itemconfig(Rbody,fill=skincolors[0],outline=skincolors[0])
    return

def changeEyes():#same as skin, except for eyes
    currentC=c1.itemcget(Lpupil,"fill")
    index=find(currentC,eyecolors)
    if index<len(eyecolors)-1:
        c1.itemconfig(Lpupil,fill=eyecolors[index+1])
        c1.itemconfig(Rpupil,fill=eyecolors[index+1])
    else:
        c1.itemconfig(Lpupil,fill=eyecolors[0])
        c1.itemconfig(Rpupil,fill=eyecolors[0])
    return

def changeHair():#same as skin, except for hair
    currentC=c1.itemcget(hair,"fill")
    index=find(currentC,haircolors)
    if index<len(haircolors)-1:
        c1.itemconfig(hair,fill=haircolors[index+1],outline=haircolors[index+1])
    else:
        c1.itemconfig(hair,fill=haircolors[0],outline=haircolors[0])
    return

def changeLips():#same as skin, except for lips
    currentC=c1.itemcget(Lmouthtop,"fill")
    index=find(currentC,lipcolors)
    if index<len(lipcolors)-1:
        c1.itemconfig(Lmouthtop,fill=lipcolors[index+1])
        c1.itemconfig(Rmouthtop,fill=lipcolors[index+1])
        c1.itemconfig(mouthbottom,fill=lipcolors[index+1])
    else:
        c1.itemconfig(Lmouthtop,fill=lipcolors[0])
        c1.itemconfig(Rmouthtop,fill=lipcolors[0])
        c1.itemconfig(mouthbottom,fill=lipcolors[0])
    return

#Create buttons allowing for changing body colors, and bind these buttons to the above functions. 
bSkin=Button(root,text="Skin",font=f,command=changeSkin)
bSkin.grid(column=0,row=1)#Grid them alongside the figure, on the left
bEyes=Button(root,text="Eyes",font=f,command=changeEyes)
bEyes.grid(column=0,row=2)
bHair=Button(root,text="Hair",font=f,command=changeHair)
bHair.grid(column=0,row=3)
bLips=Button(root,text="Lips",font=f,command=changeLips)
bLips.grid(column=0,row=4)

#Set variables and default colors for the 4 clothing peices to be manipulated
shirtcolor="cyan"
tankcolor="dark magenta"
pantscolor="blue4"
skirtcolor="forest green"
#List of possible clothing colors 
clothingcolors=["cyan","dark blue","dark gray","dark green","dark magenta","dark orange","dark red","dark violet","deep pink","chartreuse","chocolate1","coral1","cornflower blue","cornsilk","blue","violet","blue4","brown1","brown4","firebrick2","firebrick4","forest green","gray50","hot pink","magenta","lime green","maroon","pale turquoise","purple1","red1","sea green","tomato1","steel blue","yellow","black","grey90","tan4"]
#let x2,y2 be top-center of t-shirt
#let x4,y4 be top-center of skirt
#let x5,y5 be top-center of tank-top
#let x3,y3 be top-center of pants
x2=x4=350
y2=y5=40
x3=x5=500
y3=y4=200
#Create polygons for each clothing peice, and set color equal to the associated variables above
shirt=c1.create_polygon(x2-20,y2,x2-70,y2+40,x2-50,y2+60,x2-30,y2+40,x2-30,y2+90,x2+30,y2+90,x2+30,y2+40,x2+50,y2+60,x2+70,y2+40,x2+20,y2,fill=shirtcolor,outline="black")
pants=c1.create_polygon(x3-30,y3,x3-60,y3+100,x3-20,y3+100,x3,y3+40,x3+20,y3+100,x3+60,y3+100,x3+30,y3,fill=pantscolor,outline="black")
tanktop=c1.create_polygon(x5,y5+20,x5-20,y5,x5-30,y5,x5-30,y5+80,x5+30,y5+80,x5+30,y5,x5+20,y5,x5,y5+20,fill=tankcolor,outline="black")
skirt=c1.create_polygon(x4-30,y4,x4-50,y4+50,x4+50,y4+50,x4+30,y4,fill=skirtcolor,outline="black")
#Create functions that find the current color of the clothing peice, and change it to the next color in the clothingcolors list.
#Same structure as "changeSkin" function above. Create separate function for each clothing peice.
def changeShirt():
    currentC=c1.itemcget(shirt,"fill")
    index=find(currentC,clothingcolors)
    if index<len(clothingcolors)-1:
        c1.itemconfig(shirt,fill=clothingcolors[index+1])
    else:
        c1.itemconfig(shirt,fill=clothingcolors[0])
    return
def changePants():
    currentC=c1.itemcget(pants,"fill")
    index=find(currentC,clothingcolors)
    if index<len(clothingcolors)-1:
        c1.itemconfig(pants,fill=clothingcolors[index+1])
    else:
        c1.itemconfig(pants,fill=clothingcolors[0])
    return
def changeTank():
    currentC=c1.itemcget(tanktop,"fill")
    index=find(currentC,clothingcolors)
    if index<len(clothingcolors)-1:
        c1.itemconfig(tanktop,fill=clothingcolors[index+1])
    else:
        c1.itemconfig(tanktop,fill=clothingcolors[0])
    return
def changeSkirt():
    currentC=c1.itemcget(skirt,"fill")
    index=find(currentC,clothingcolors)
    if index<len(clothingcolors)-1:
        c1.itemconfig(skirt,fill=clothingcolors[index+1])
    else:
        c1.itemconfig(skirt,fill=clothingcolors[0])
    return
#Create buttons to be bound to the above functions for changing the colors of the clothing.
#Grid these along the right side of the screen, next to the clothing peices.
bPants=Button(root,text="Pants",font=f,command=changePants)
bPants.grid(column=2,row=4)
bTank=Button(root,text="Tank-Top",font=f,command=changeTank)
bTank.grid(column=2,row=2)
bSkirt=Button(root,text="Skirt",font=f,command=changeSkirt)
bSkirt.grid(column=2,row=3)
bShirt=Button(root,text="Shirt",font=f,command=changeShirt)
bShirt.grid(column=2,row=1)
#Function that animates the clothing by having each peice randomly change colors 21 times
def animateClothes():
    i=0#Set a counter = 0
    for i in range(20):#Change color 21 times
        while i<=20:#keep changing the color until the max 21 is reached
            i+=1#update the counter
#change the color of each clothing peice by reconfiguring the fill to a color randomly chosen from the "clothingcolors" list
            c1.itemconfig(shirt,fill=random.choice(clothingcolors))
            c1.itemconfig(tanktop,fill=random.choice(clothingcolors))
            c1.itemconfig(skirt,fill=random.choice(clothingcolors))
            c1.itemconfig(pants,fill=random.choice(clothingcolors))
            sleep(.25)#have the color remain for .25s
            c1.update()#update the cavas to reflect the new colors
        return
#Create and grid button bound to the above function that will initiate the changing colors of the clothing
bAnimate=Button(root,text="PARTY TIME!",font=f,command=animateClothes)
bAnimate.grid(column=1,row=5,pady=20)

#Allow for movement of the clothing articles
item=0#set default handle of the closest item
oldx=oldy=0#set default starting locations to 0

def startmove(event):#function that starts the move by grabbing the coordinates of the closest clothing peice
    global item,oldx,oldy#set global vars for the item handle number, and original coords
    item=c1.find_closest(event.x,event.y)#find closest item on canvas to the event (mouse click)
    oldx=event.x#record the "old" original positions of the item
    oldy=event.y
    return
    
def move(event):#function that moves the selected clothing item to a new location, specified by the event (moving mouse)
    global oldx,oldy,x2,y2,x3,y3,x4,y4,x5,y5#set global values to the reference points of the shapes and the old coords
    if item[0]==shirt:#if closest item is the shirt (first in the list of items found in the previous function startmove)
    #change x2 and y2,the shirt reference points, by the amount the mouse moves
        x2=x2+(event.x-oldx)
        y2=y2+(event.y-oldy)
        #save the new positions of the mouse
        oldx=event.x
        oldy=event.y
        #update the coordinates of the shirt using new x2 and y2 values
        c1.coords(item,x2-20,y2,x2-70,y2+40,x2-50,y2+60,x2-30,y2+40,x2-30,y2+90,x2+30,y2+90,x2+30,y2+40,x2+50,y2+60,x2+70,y2+40,x2+20,y2)
    if item[0]==skirt:#ditto for skirt
    #change x4 and y4,the skirt reference points, by the amount the mouse moves
        x4=x4+(event.x-oldx)
        y4=y4+(event.y-oldy)
        #save the new positions of the mouse
        oldx=event.x
        oldy=event.y
        #update the coordinates of the skirt using new x2, y3 values
        c1.coords(item,x4-30,y4,x4-50,y4+50,x4+50,y4+50,x4+30,y4)
    if item[0]==tanktop:#ditto for tanktop
    #change x5 and y5,the tanktop reference points, by the amount the mouse moves
        x5=x5+(event.x-oldx)
        y5=y5+(event.y-oldy)
        #save the new positions of the mouse
        oldx=event.x
        oldy=event.y
        #update the coordinates of the tanktop using new x3, y2 values
        c1.coords(item,x5,y5+20,x5-20,y5,x5-30,y5,x5-30,y5+80,x5+30,y5+80,x5+30,y5,x5+20,y5,x5,y5+20)
    if item[0]==pants:#ditto for pants
    #change x3 and y3,the pants reference points, by the amount the mouse moves
        x3=x3+(event.x-oldx)
        y3=y3+(event.y-oldy)
        #save the new positions of the mouse
        oldx=event.x
        oldy=event.y
        #update the coordinates of the pants using new x3, y3 values
        c1.coords(item,x3-30,y3,x3-60,y3+100,x3-20,y3+100,x3,y3+40,x3+20,y3+100,x3+60,y3+100,x3+30,y3)
    return
#Create events for moving the peices using the previous 2 functions
c1.bind("<Button-1>",startmove)#grab the item by mouse click, and record its location
c1.bind("<B1-Motion>",move)#while holding down the mouse, move the item

#Create a label with the title of the GUI to go on the top of the page, and grid it
title=Label(root,width=20,height=2,bd=1,pady=5,text="My Dress-Up Doll",font="Times 24",bg="blue",fg="pink",relief=RAISED)
title.grid(row=0,column=1)

#Create a separate frame for the instructions
f1=Frame(root)

def showinstructions():#function that shows the instructions by displaying the frame
    f1.grid(row=7,column=1)
    return

def hideinstructions():#function that hides the instructions by "forgetting" the frame
    f1.grid_forget()
    return

#Create button that is bound to showing the instructions at the bottom of the page
BshowInst=Button(root,text="Instructions",font=f,command=showinstructions)
BshowInst.grid(row=5,column=0)
#Create label containing the instruction text that will be displayed.
instText=Label(f1,wraplength=600,text="Click the buttons on either side of the screen to change the colors of the indicated body parts or clothing articles. Feel free to try various outfits on the figure by clicking the desired clothing article, and then dragging it onto the figure. Click the "'PARTY TIME'" button for a psychedelic effect!",font=f)
instText.pack()
#In the instruction frame, create and pack a button that can be used to hid the instruction frame
BhideInst=Button(f1,text="Hide Instructions",font=f,command=hideinstructions)
BhideInst.pack()

root.mainloop()
