#import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Subplots
"""f, (ax1,ax2,ax3) = \
plt.subplots(3,1,figsize=[10,7]) 
plt.subplots_adjust(hspace=.9)"""
# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

f,ax1= plt.subplots(figsize=[10,7])
ax1.bar(range(len(games)),viewers,color='#8532a8')
ax1.set_xlabel("Game")
ax1.set_ylabel("Number of Viewers")
ax1.set_xticks(range(len(games)))
ax1.set_xticklabels(games,rotation=45)
ax1.set_title("Number of viewers per game")
ax1.legend(["Twich"])
plt.show()
# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1)

f,ax2= plt.subplots(figsize=[10,7])
ax2.pie(countries,autopct='%d%%',pctdistance=1.25, colors=colors,explode=explode,startangle=300,shadow=True)
ax2.legend(labels)
ax2.set_title("League of Legends Viewers' Locations")
plt.show()
# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

hour_label = ["0"+str(t) + ":00" if t <10 else str(t) + ":00" for t in hour]

viewers_hour_upper = \
[1.15*t for t in viewers_hour]
viewers_hour_lower = \
[0.85*t for t in viewers_hour]

f,ax3 = plt.subplots(figsize=[10,7])

ax3.fill_between(hour,\
                 viewers_hour_upper,\
                  viewers_hour_lower,alpha=.2)
ax3.plot(hour,viewers_hour,color='#1f22db')
ax3.set_title("Number of viewers by hour")
ax3.set_xlabel("Time")
ax3.set_ylabel("Number of Viewers")
ax3.set_xticks(hour)
ax3.set_xticklabels(hour_label,rotation=45)

plt.show()
