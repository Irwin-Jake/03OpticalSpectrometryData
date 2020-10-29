#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import os
#from uncertainties import ufloat
#from uncertainties.umath import *  # sin(), etc.
#x = ufloat(1, 0.1)  # x = 1+/-0.1
def get_data(file_name):
    '''
    Get the file data and send it back

    file_name: name of the file to be used
    returns:x,y x and y columns for the data
    '''
    with open(file_name,'r') as f:
        return np.loadtxt(f,unpack=True)


def clean_fig_name(file_name):
    fig_name = './figures/'+file_name[7:-3]
    fig_name = fig_name.replace(' ','_')
    return fig_name
def plot_data(file_name, title, x_label, y_label):
    x_data, y_data = get_data(file_name)
    plt.plot(x_data, y_data, label = 'data')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    fig_name = clean_fig_name(file_name)
    plt.savefig(fig_name)
    #plt.show()
    plt.clf()


def plot_white_light():
    plot_data('./data/white_light_data.txt','White light data', 'Wave length/nm', 'Amplitude/A')

def default_labels(file_name):
    xaxis = '(Wave length)/nm'
    yaxis = '(Amplitude)/A'
    title = file_name[:-4].replace('_',' ')
    title = title.replace('sdl','sodium discharge lamp')
    title = 'A plot of ' + xaxis + ' against '+ yaxis + ' \n for a '+ title
    #Remove all numbers from the title
    translation = title.maketrans('','','1234567890')
    title = title.translate(translation)
    return file_name, title, xaxis, yaxis

def plot_all_in_data_folder(data_dir):
    for file_name in os.listdir(data_dir):
        file_name, title, x_label, y_label = default_labels(file_name)
        plot_data('./data/'+file_name, title, x_label, y_label)

#plot_white_light()
plot_all_in_data_folder('./data')
