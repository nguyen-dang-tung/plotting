#use this plotting file to plot all data file in a single plot, use for comparision
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axis as ax
import os as os
import math as math
import itertools
import tkinter as tk
from tkinter import filedialog
import matplotlib.ticker as ticker
marker = itertools.cycle(('s','o','v','^','>', '<', '*', '.',',')) #, '.',','
markersize = itertools.cycle(('0','0'))
color = itertools.cycle(('k','r','b','g','c','m','y','k'))
linestyle = itertools.cycle(('-','-'))
linewidth = itertools.cycle(('2','2'))
label_size ='24'
tick_size = '20'
#color = itertools.cycle(('b','g','r','c','m','y'))
#to plot the file, data file should be organized into 2 column-data file,
# first line the name of the data
# second line is the unit of each column, for example [s]

def transform_text(text):
    text = text.replace("\n", "")
    text = text.replace("\ufeff", "")
    text = text.replace("Vg", "$\mathrm{V_g}$")
    text = text.replace("Vd", "$\mathrm{V_d}$")
    text = text.replace("Ig", "$\mathrm{I_g}$")
    text = text.replace("Id", "$\mathrm{I_d}$")
    return text

#change plot default parameters to the customized format    
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right']= True
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['font.family'] = "Helvetica"
plt.rcParams['font.size'] = tick_size
plt.rcParams['figure.figsize'] = 5, 5

#import data file here
#data wil be imported into 2 arrays, X and Y
#plot consists of using these arrays in scatter mode#
#current_path= os.getcwd()
#parent_path = os.path.dirname(current_path)
#print(current_path)
#print(parent_path)
#data_path = parent_path +"/data"
#tk.Tk().withdraw()
#tempdir = filedialog.askdirectory(title='choose data files')
#if len(tempdir) > 0:
#    data_path = tempdir
#plot_path = data_path +"/plot"
#print(data_path)
#print(plot_path)
#if os.path.isdir(data_path) == False:
#    os.mkdir(data_path)
#if os.path.isdir(plot_path) == False:
#    os.mkdir(plot_path)
#os.chdir(data_path)
#fileList = os.listdir()
tk.Tk().withdraw()
fileList = filedialog.askopenfilenames(title='choose data files')
print(fileList)

#for i in fileList:
#    fileName = i
#    print("Processing " + fileName)
#    tempdir = os.path.dirname(os.path.realpath(fileName))
#    if len(tempdir) > 0:
#        data_path = tempdir
#    plot_path = data_path +"/plot"
#    #print(data_path)
#    #print(plot_path)
#    #if os.path.isdir(data_path) == False:
#    #    os.mkdir(data_path)
#    if os.path.isdir(plot_path) == False:
#        os.mkdir(plot_path)
#    os.chdir(data_path)
#   fileList = os.listdir()

def XY_plot(fileName):
    print("Processing " + fileName)
    fileRaw = open(fileName, "r")
    fileContent = fileRaw.readlines()
    x_col = 3
    y_col = 0

#    print(fileContent)
    xy_Name = fileContent[0].split(',')
    x_name = xy_Name[x_col]
    y_name = xy_Name[y_col]

    xy_Unit = fileContent[1].split(',')
    x_unit = xy_Unit[x_col]
    y_unit = xy_Unit[y_col]
    
    xy_Legend = fileContent[2].split(',')
    x_legend = transform_text(xy_Legend[x_col])
    y_legend = transform_text(xy_Legend[y_col])
    
    x_data = [];
    y_data = [];
    x_abs =[]
    y_abs =[]
    #x_err = [];
    #y_err = [];
    for i in range(3, len(fileContent)):
        lineContent = fileContent[i].split(",")
        x_content = float(lineContent[x_col])
        y_content = float(lineContent[y_col])
        x_data.append(x_content)
        y_data.append(y_content)
        x_abs.append(np.abs(x_content))
        y_abs.append(np.abs(y_content))

        #x_err.append(float(lineContent[0])*0.1)
        #y_err.append(float(lineContent[1])*0.1)
    
    fileRaw.close()
    #plot the data with label
    #fig, ax1 = plt.subplots()
    #plt.plot(x_data, y_data, color = next(color), marker = next(marker), markersize = next(markersize), linestyle = next(linestyle),  label = fileName, linewidth = next(linewidth) )
    plt.plot(x_data, y_abs, color = next(color), marker = next(marker), markersize = next(markersize), linestyle = next(linestyle),  label = y_legend, linewidth = next(linewidth) )
    #plt.errorbar(x_data, y_data,yerr = y_err, xerr = None, color = 'b', linestyle = '--', capsize = 5)#,  fmt = 'kl', capsize = None
    #ax1.legend(loc = 'best') #attribute are center, upper, lower, right, left, best
    #ax1.ticklabel_format(style = 'sci', axis ='y')
    
    #setting label for y-axis
    y_label = y_name + " (" + y_unit + ")"
    y_label = transform_text(y_label)
    plt.ylabel(y_label, fontsize = label_size)
    
    #setting the label for x-axis
    x_label = x_name + " (" + x_unit + ")"
    x_label = transform_text(x_label)
    plt.xlabel(x_label, fontsize = label_size)
    #create minor tick
    #ax.xaxis.set_minor_locator(MultipleLocator(4))
    #ax.xaxis.set_minor_locator(AutoMinorLocator())
    #ax1.yaxis.set_minor_locator(AutoMinorLocator())
    #ax1.invert_yaxis()
    #plt.yscale('log')
    #plt.xscale('log')
    #xlim_bottom = 106
    #xlim_top = 107
    #plt.xlim(left = xlim_bottom, right = xlim_top)
    #plt.show()
    return


### parameter of the axes
#ylim_bottom = 0
#ylim_top = 6e15
#plt.ylim(bottom =  ylim_bottom, top  = ylim_top) # set limit in the y

#xlim_bottom = 400
#xlim_top = 750
#plt.xlim(left = xlim_bottom, right = xlim_top)

#plt.vlines(0,ylim_bottom,ylim_top, linestyles = '--',linewidth = 0.5) #draw a dash line in the center y =0
#plt.hlines(0,xlim_bottom, xlim_top, linestyles = '--', linewidth =0.5) #draw a dash line at x=0
#plt.yscale('log') #choose style for yscale 'log' or 'linear'
#plt.xscale('log') #choose style for xscale 'log' or 'linear'

#plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0)) #change the tick to 'sci' or 'plain'
#title = "testTitle"
#plt.title(title, loc = "center", pad = 30.0)


###plot folder
exportName = ''
for i in fileList:
    if(".csv" in i):
        try:
            XY_plot(i)
            #plt.tight_layout()
            plt.legend(loc =(1.04,0.5), frameon= False)
            #plt.savefig(plot_path + '/' + name + ".tiff", bbox_inches =''  )
            if len(exportName)< 10:
                exportName = i
        except:
            print("Failed at " + i)
### files to plot

### plot
#locator = ticker.AutoLocator()
#ax.Axis.set_minor_locator(locator, locator)
#plt.savefig(plot_path + '/' + exportName + ".tiff")
#plt.savefig(exportName + ".tiff")

plt.show()
