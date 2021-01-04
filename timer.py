import os
import time
from tkinter import *
from tkinter import messagebox
from winsound import *

from playsound import playsound

#setting the window
root = Tk()
root.geometry("300x100")
root.title("Countdown Timer")

#setting 2 frames for easy positioning
topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack()

#create 3 spin boxes for hours minutes and seconds
hourSpin = Spinbox(topframe, from_=00, to=24, width=2,wrap=TRUE)
minSpin = Spinbox(topframe, from_=00, to=59, width=2,wrap=TRUE)
secSpin = Spinbox(topframe, from_=00, to=59, width=2,wrap=TRUE)

#it shows how much time is left
timeRemaining=Text(bottomframe,height=1,width=13)
#label for alerting when time is up
alertaa=Label(bottomframe,anchor=CENTER,)

def submit():
    timp=int(hourSpin.get())*3600+int(minSpin.get())*60+int(secSpin.get())
    while timp >-1:
        #to divide 'timp' in hours , minutes and seconds
        mins,secs = divmod(timp, 60)
        hours,mins=divmod(mins,60)

        #updating the timeRemaining textbox with the lattest time
        timeRemaining.delete('0.0','end')
        timeRemaining.insert('0.0',("{:0>2d}".format(hours))+':'+("{:0>2d}".format(mins))+':'+("{:0>2d}".format(secs)))
        #timeRemaining.insert("0.0",str(hours)+"hr"+str(mins)+"min"+str(secs)+"sec")
        root.update()
        time.sleep(1)
        #when time is 0 we alert the user
        if(timp==0):
            alertaa.config(text="Time is up!!!!",fg="red")
            root.update()
            messagebox.showinfo("time up", "time has run out")
            PlaySound("darude-sandstorm_alarm.wav",SND_FILENAME)
            #alertaa.config(text="", fg="red")

        timp = timp - 1



#create start button
btn=Button(topframe, text="Start",command= submit)
#putting the elements in the window
hourSpin.pack(side = LEFT)
minSpin.pack(side = LEFT)
secSpin.pack(side = LEFT)
btn.pack(side=RIGHT)
timeRemaining.pack()
alertaa.pack()
timeRemaining.insert('0.0',"00:00:00")
mainloop()