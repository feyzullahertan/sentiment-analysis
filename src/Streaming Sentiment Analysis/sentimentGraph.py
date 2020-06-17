import re
import nltk
import pyodbc
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ggplot kullanıp grafiği olusturuyoruz

style.use("ggplot")
fig = plt.figure()
ax1  = fig.add_subplot(1,1,1)

def animate(i):
    #twitter-out.txt'i okuyup alt alta satır satır okuyoruz.
    pullData= open("twitter-out.txt","r").read()
    lines = pullData.split("\n")
    
    xar = []
    yar = []
    
    x = 0
    y = 0
    #txt içersinde pozitif görürse +1, negatif görürse -1 verip grafiğin gidişatını hazırlamaktadır.
    for l in lines:
        x+=1
        if "positive" in l:
            y += 1
        elif "negative" in l:
            y-=1
        xar.append(x)
        yar.append(y)
    
    ax1.clear()
    ax1.plot(xar,yar)
#Animation fonksiyonu kullanıp dinamikleştirme işlemi.
ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()
