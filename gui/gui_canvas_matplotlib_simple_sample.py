#!/usr/bin/env python
import sys

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import tkinter as Tk


"""
Demonstrates one way of embedding Matplotlib figures into a PySimpleGUI window.
Paste your Pyplot code into the section marked below.
Do all of your plotting as you normally would, but do NOT call plt.show(). 
Stop just short of calling plt.show() and let the GUI do the rest.
The remainder of the program will convert your plot and display it in the GUI.
If you want to change the GUI, make changes to the GUI portion marked below.
"""

# ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE -------------------------------

import numpy as np
import matplotlib.pyplot as plt

# data setting - tuple
values_to_plot = (20, 35, 30, 35, 27)
width = 0.4

# pandas.dataframe -> {convert} -> numpy
# data..
p1 = plt.bar(np.arange(len(values_to_plot)), values_to_plot, width)

# visual?,...
plt.ylabel('Y-Axis Values')
plt.title('Plot Title')
plt.xticks(np.arange(len(values_to_plot)), ('Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'))
plt.yticks(np.arange(0, 60, 10))
plt.legend((p1[0],), ('Data Group 1',))


# ------------------------------- END OF YOUR MATPLOTLIB CODE -------------------------------

# ------------------------------- Beginning of Matplotlib helper code -----------------------


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas
    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = Tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
    canvas.create_image(loc[0] + figure_w / 2, loc[1] + figure_h / 2, image=photo)
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    return photo


# ------------------------------- Beginning of GUI CODE -------------------------------

fig = plt.gcf()  # if using Pyplot then get the figure from the plot

# 1. modify size
fig.set_size_inches(6, 4)

figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
# figure_w : 600, h : 400..


# define the window layout


layout = [[sg.Text('Plot test', font='Any 18')],
          [sg.Text('Please Enter FC Search Conditions')],
          [sg.Text('Base File', size=(20, 1)), sg.Input(key='_file_path_', do_not_clear=True), sg.FileBrowse()],
          [sg.Text('FC', size=(20, 1)), sg.InputText('Default FC', key='_fc_', do_not_clear=True)],
          [sg.Text('DATE_START', size=(20, 1)),
           sg.InputText('Default DATE_START', key='_date_start_', do_not_clear=True)],
          [sg.Text('DATE_END', size=(20, 1)), sg.InputText('Default DATE_END', key='_date_end_', do_not_clear=True)],
          [sg.Text('APPOINTMENT_STATUS1', size=(20, 1)),
           sg.InputText('Default APPOINTMENT_STATUS1', key='_appointment_status1_', do_not_clear=True)],
          [sg.Text('APPOINTMENT_STATUS2', size=(20, 1)),
           sg.InputText('Default APPOINTMENT_STATUS2', key='_appointment_status2_', do_not_clear=True)],
          [sg.Text('RESULT (Double Click -> move data to SELECTED table)', size=(50, 1))],
            [sg.OK(pad=((figure_w / 2, 0), 3), size=(4, 2))],
          [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
          ]

# create the form and show it without the plot
window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI', force_toplevel=True).Layout(
    layout).Finalize()

# add the plot to the window
fig_photo = draw_figure(window.FindElement('canvas').TKCanvas, fig)

# show it all again and get buttons
# event, values = window.Read()

i = 10

while True:
    # window라는 객체는 Layout을 품고 있는데, Layout의 Read() 이벤트를 Blocking해서 기다리고 있다.
    event, values = window.Layout(layout).Read()

    if event == 'OK':
        i += 5

        values_to_plot = (20 + i, 35 + i, 30 + i, 35 + i, 27 + i)

        # draw bar
        p1 = plt.bar(np.arange(len(values_to_plot)), values_to_plot, width)

        # visual?,...
        plt.ylabel('Y-Axis Values')
        plt.title('Plot Title')
        plt.xticks(np.arange(len(values_to_plot)), ('Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'))
        plt.yticks(np.arange(0, 60, 10))
        plt.legend((p1[0],), ('Data Group 1',))

        fig_photo = draw_figure(window.FindElement('canvas').TKCanvas, fig)
