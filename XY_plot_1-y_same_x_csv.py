#use this plotting file to plot all data file in a single plot, use for comparision
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.axis as ax
import matplotlib.ticker
import os as os
import math as math
import itertools
import tkinter as tk
from tkinter import filedialog
import matplotlib.ticker as ticker
marker = itertools.cycle(('v','o','r','^','>', '<', '*', '.',',')) #, '.',','
markersize = itertools.cycle(('9'))
color = itertools.cycle(('r','b','g','c','m','y','k'))
linestyle = itertools.cycle(('-','-'))
linewidth = itertools.cycle(('1','1'))
label_size ='24'
tick_size = '20'
#color = itertools.cycle(('b','g','r','c','m','y'))
#to plot the file, data file should be organized into 2 column-data file,
# first line the name of the data
# second line is the unit of each column, for example [s]
#change plot default parameters to the customized format    
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right']= True
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['font.family'] = "Helvetica"
plt.rcParams['font.size'] = tick_size
plt.rcParams['figure.figsize'] = 5, 5
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#import data file here
#data wil be imported into 2 arrays, X and Y
#plot consists of using these arrays in scatter mode
current_path= os.getcwd()
parent_path = os.path.dirname(current_path)
#print(current_path)
#print(parent_path)
#data_path = parent_path +"/data"
tk.Tk().withdraw()
fileList = filedialog.askopenfilenames(title='choose data files')
print(fileList)
for i in fileList:
    print(i)
tempdir = os.path.dirname(os.path.realpath(fileName))
if len(tempdir) > 0:
    data_path = tempdir
plot_path = data_path +"/plot"
#print(data_path)
#print(plot_path)
#if os.path.isdir(data_path) == False:
#    os.mkdir(data_path)
if os.path.isdir(plot_path) == False:
    os.mkdir(plot_path)
os.chdir(data_path)
fileList = os.listdir()



x_col = 0
y1_col = 13
#y2_col = 10

y_data = []

print("Processing " + fileName)
fileRaw = open(fileName, "r")
fileContent = fileRaw.readlines()
#    print(fileContent)
xy_Name = fileContent[0].split(',')
x_name = xy_Name[x_col]
print(x_name)
y1_name = xy_Name[y1_col]
#y2_name = xy_Name[y2_col]

xy_Unit = fileContent[1].split(',')
x_unit = xy_Unit[x_col]
y1_unit = xy_Unit[y1_col]
#y2_unit = xy_Unit[y1_col]

xy_legend = fileContent[2].split(',')
print(xy_legend)
x_legend = xy_legend[x_col]
y1_legend = xy_legend[y1_col]
#y2_legend = xy_legend[y2_col]

x_data = [];
y1_data = [];
#y2_data = [];

x_abs =[]
y1_abs =[]
#y2_abs = []
#x_err = [];
#y_err = [];
line = 0
for i in range(3, len(fileContent)):
    lineContent = fileContent[i].split(",")
    #print(lineContent)
    line += 1
    try:
        x_content = float(lineContent[x_col].strip())
        y1_content = float(lineContent[y1_col].strip())
        #y2_content = float(lineContent[y2_col].strip())
        x_data.append(x_content)
        y1_data.append(y1_content)
        #y2_data.append(y2_content)
    
        x_abs.append(np.abs(x_content))
        y1_abs.append(np.abs(y1_content))
    except:
        print('error at line ' + str(line))

    #x_err.append(float(lineContent[0])*0.1)
    #y_err.append(float(lineContent[1])*0.1)
print(x_data)
print(y1_data)
#print(y2_data)
fileRaw.close()
#plot the data with label
fig, ax = plt.subplots()
#plt.plot(x_data, y_data, color = next(color), marker = next(marker), markersize = next(markersize), linestyle = next(linestyle),  label = fileName, linewidth = next(linewidth) )
#ylabels = itertools.cycle(('', ''))
#ax.plot(x_data, y1_data)
#ax.plot(x_data, y2_data)
ax.plot(x_data, y1_abs, color = next(color), marker = next(marker), markersize = next(markersize), linestyle = next(linestyle),  label = y1_legend, linewidth = next(linewidth) )
#ax.plot(x_data, y2_data, color = next(color), marker = next(marker), markersize = next(markersize), linestyle = next(linestyle),  label = y2_legend, linewidth = next(linewidth) )
#plt.errorbar(x_data, y_data,yerr = y_err, xerr = None, color = 'b', linestyle = '--', capsize = 5)#,  fmt = 'kl', capsize = None
#ax1.legend(loc = 'best') #attribute are center, upper, lower, right, left, best
#ax1.ticklabel_format(style = 'sci', axis ='y')
#setting label for y-axis
y_label = y1_name + " (" + y1_unit + ")"
y_label = y_label.replace("\n", "")
y_label = y_label.replace("Id", '$\mathrm{I_d}$')
ax.set_ylabel(y_label, fontsize = label_size)
#ax.set_ylabel(r"$\rm I_d$ (A)", fontsize = label_size)
#setting the label for x-axis
x_label = x_name + " (" + x_unit + ")"
#x_label = x_label.replace("\n", "")
#x_label = x_label.replace("Vg", "$\mathrm{V_g}$")
#x_label = x_label.replace("Vd", "$\mathrm{V_d}$")
print(x_label)
ax.set_xlabel(x_label, fontsize = label_size)

#plt.legend(loc =(1.04,0.5), frameon= False)
#plt.legend(frameon = False)

#create minor tick
#ax.xaxis.set_minor_locator(MultipleLocator(4))
#ax.xaxis.set_minor_locator(AutoMinorLocator())
#ax1.yaxis.set_minor_locator(AutoMinorLocator())
#ax1.invert_yaxis()
#plt.yscale('log')
plt.xscale('log')

#xlim_bottom = 0.3
#xlim_top = 100
#ax.set_xlim(left = xlim_bottom, right = xlim_top)


### parameter of the axes
#ylim_bottom = 0.009
#ylim_top = 101
#plt.ylim(bottom =  ylim_bottom, top  = ylim_top) # set limit in the y

#ticks = [0.2, 0.5, 1, 2, 5, 10, 20, 50, 100]
#print(ticks)
#ax.set_xticks = (ticks)
#ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
#xlim_bottom = -101
#xlim_top = 301
#plt.xlim(left = xlim_bottom, right = xlim_top)
#plt.vlines(0,ylim_bottom,ylim_top, linestyles = '--',linewidth = 0.5) #draw a dash line in the center y =0
#plt.hlines(0,xlim_bottom, xlim_top, linestyles = '--', linewidth =0.5) #draw a dash line at x=0
#plt.yscale('log') #choose style for yscale 'log' or 'linear'
#plt.xscale('log') #choose style for xscale 'log' or 'linear'

#plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0)) #change the tick to 'sci' or 'plain'
#title = "testTitle"
#plt.title(title, loc = "center", pad = 30.0)


###plot folder


### plot
#locator = ticker.AutoLocator()
#ax.Axis.set_minor_locator(locator, locator)
plt.savefig(fileName.replace(".csv",".tiff"), bbox_inches ='tight'  )
#plt.savefig(fileName.replace(".csv", ".tiff"))
plt.show()

