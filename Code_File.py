from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from typing import Sized
from random import sample
# from Try import Graph, start
from tkinter import *
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd
import math


myMap={}
myfile="Ages"
x=[]
y=[]


with open(myfile+".csv") as my_file:
    data=csv.DictReader(my_file)
    xlabel="Ages"
    ylabel="Frequency"
    for i in data:
        val=int(i[data.fieldnames[1]])
        x.append(val)
        if val in myMap.keys():
            myMap[val]+=1
        else:
            myMap[val]=1
    xlabel=data.fieldnames[1]
    x=np.array(x)
    for j in x:
        y.append(myMap[j])
    y=np.array(y)

    
            

def Bar_Chart (x):
    plt.figure('Bar Chart')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if myfile!="Programming Languages":
        plt.bar(x[:1000], y[:1000])
    elif myfile=="Programming Languages":
        plt.barh(x, y)
    plt.title(myfile)
    plt.legend()
    plt.tight_layout()
    plt.show()
def Dot_Plot(x):
    plt.figure('Dot_Plot')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.scatter(x, y, linewidth=0,alpha=0.75)
    plt.title(myfile)
    plt.legend()
    plt.tight_layout()
    plt.show()
def box_Plot(x):
    plt.figure('box_Plot')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.boxplot(x)
    plt.title(myfile)
    plt.legend()
    plt.tight_layout()
    plt.show()
def Histogram(x):
    plt.figure('Histogram')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylabel("Frequency")
    plt.hist(x,bins=10,edgecolor='black')
    plt.axvline(np.median(x),color='orange',label='Median')
    #plt.axvline(np.mean(x),color='red',label='Mean')
    plt.title(myfile)
    plt.legend()
    plt.tight_layout()
    plt.show()







class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground




def Start(window):
    
    window.title("STATs")
    window.geometry('550x600')
    LBL_Greating=Label(window,text="Welcome to our Statistics App",bg='#2a5289',fg='#e2d3f4',font=("arial",18))
    ############################################Hypothesis######################################################
    
    LBL_Greating.place(x=100,y=0)
    LBL_indata=Label(window,text="Hypothesis Testing",font=("Georgia"),bg='#2a5289',fg='#e2d3f4').place(x=0,y=65)
    INPUT_BUTTON=HoverButton(window,text="Hypothesis",command=Hypothesis,borderwidth=2,font="Georgia", relief=RAISED, bg='#e2d3f4',fg='#2a5289'
    ,activebackground='#e2dfff')
    INPUT_BUTTON.place(x=315,y=60)
    
    ############################################Graphs######################################################
    #For Statistics Window
    
    # def ChooseGraph():
    #     my_file = chosenFile.get()
    #     if(my_file=="Ages"):
    #         pass
    #     elif(my_file=="Programming Languages"):
    #         pass
    LbL_GRAPHs=Label(window,text="Descriptive Statistics", font= "Georgia",bg='#2a5289',fg='#e2d3f4').place(x=0,y=215)
    # Files = ['Ages', 'Programming Languages']
    # chosenFile = ttk.Combobox(window,state=DISABLED,width=30)
    # chosenFile['values'] = Files
    # chosenFile['state'] = 'readonly'
    # chosenFile.place(x=275,y=220)
    # chosenFile.current(0)
    # #chosenFile.bind('<<ComboboxSelected>>',ChooseGraph)
    BUT_chooseStatistics=HoverButton(window,text="Descriptive",command=Descriptive, font = "Georgia", bg='#e2d3e4',fg='#2a5289', activebackground='#e2dfff')
    BUT_chooseStatistics.place(x=310,y=220)
#################################################DATA####################################################
    
    
    #For Sampling Window
    LbL_GRAPHs=Label(window,text="Sampling Measures", font= "Georgia",bg='#2a5289',fg='#e2d3f4').place(x=0,y=365)
    BUT_Length=HoverButton(window,text="Sampling",command = Sampling,font = "Georgia", bg='#e2d3e4',fg='#2a5289', activebackground="#e2dfff")
    BUT_Length.place(x=320,y=360)
    
def Sampling():
    window.withdraw()
    Sample = Tk()
    Sample.title("Sampling")
    Sample.geometry('550x600')
    Sample.configure(bg='#2a5289')
    LBL_Greating=Label(Sample,text="Sampling Analysis",bg='#2a5289',fg='#e2d3f4',font=("arial",18)).place(x=180, y=5)
    meansList = []
    def TextAreaGet():
        meansList.clear()
        n = Length_Input.get("1.0",END)
        count = Count_Input.get("1.0",END)
        for i in range(int(count)):
            print (int(n))
            global final 
            final = np.random.choice(x,int(n))
            print(np.mean(final))
            meansList.append(np.mean(final))
            print(final)
    
    def Plot_Sample(event):
        print(len(meansList))
        means = np.array(meansList)
        print(means)
        plt.plot(meansList)
        
        Graph_type=Graph_Sample.get()
        if(Graph_type=="Histogram"):
            Histogram(means)
        elif(Graph_type=="Box-plot"):
            box_Plot(means)
    
    
    # create a combobox for graphs
    selected_graph = tk.StringVar()
    LbL_Length=Label(Sample,text="Enter Length of Samples", font= "Georgia",bg='#2a5289',fg='#e2d3f4').place(x=0,y=150)
    Length_Input=tk.Text (Sample, height=0.5 ,width=25)
    Length_Input.place(x=250, y=155)
    LbL_Count=Label(Sample,text="Enter Number of Samples", font= "Georgia",bg='#2a5289',fg='#e2d3f4').place(x=0,y=240)
    Count_Input=tk.Text (Sample, height=0.5 ,width=25)
    Count_Input.place(x=250, y=245)
    BUT_Length=HoverButton(Sample,text="Store Length",command = TextAreaGet,font = "Georgia", bg='#e2d3e4',fg='#2a5289', activebackground="#e2dfff")
    BUT_Length.place(x=285,y=280)
    LbL_Measures=Label(Sample,text="Please Choose A Graph", font= "Georgia",bg='#2a5289',fg='#e2d3f4').place(x=0,y=400)
    Graphs = ('Histogram', 'Box-plot')
    Graph_Sample = ttk.Combobox(Sample,state=DISABLED,textvariable=selected_graph,width=30)
    Graph_Sample['values'] = Graphs
    Graph_Sample['state'] = 'readonly'  # normal
    Graph_Sample.place(x=250,y=405)
    Graph_Sample.current(0)
    Graph_Sample.bind('<<ComboboxSelected>>',Plot_Sample)
    def Exit_Data():
        Sample.destroy()
        window.deiconify()
    HoverButton(
    Sample, 
    text="Back", font = "Georgia", bg='#e2d3e4',fg='#2a5289', activebackground="#e2dfff", 
    command=Exit_Data
    ).place(x= 450, y=500)


def Descriptive():
    window.withdraw()
    Statistics = Tk()
    Statistics.title("Descriptive")
    Statistics.geometry('550x600')
    Statistics.configure(bg='#2a5289')
    LBL_Greating=Label(Statistics,text="Descriptive Statistics",bg='#2a5289',fg='#e2d3f4',font=("arial",18)).place(x=180, y=5)
    def Plot_Graph(event):
        Graph_type=GRAPH_cb.get()
        if(Graph_type=="Histogram"):
            Histogram(x)
        elif(Graph_type=="Bar-chart"):
            Bar_Chart(x)
        elif(Graph_type=="Box-plot"):
            box_Plot(x)
        elif(Graph_type=="Dot-diagram"):
            Dot_Plot(x)
    LbL_Measures=Label(Statistics,text="Please Choose A Graph", font= "Georgia",bg='#2a5289',fg='#e2d3f4').place(x=0,y=200)
    Graphs = ('Histogram', 'Bar-chart', 'Box-plot', 'Dot-diagram')
    GRAPH_cb = ttk.Combobox(Statistics,state=DISABLED,width=30)
    GRAPH_cb['values'] = Graphs
    GRAPH_cb['state'] = 'readonly'  # normal
    GRAPH_cb.place(x=250,y=205)
    GRAPH_cb.current(0)
    GRAPH_cb.bind('<<ComboboxSelected>>',Plot_Graph)
    MeasureResult=tk.Text (Statistics, height=0.5 ,width=60)
    MeasureResult.place(x=40, y=450)
    def Calc_Measure(event):
        Measure = MEASURES_cb.get()
        if (Measure == "Mean"):
            mean= np.mean(x)
            MeasureResult.delete("1.0", END)
            MeasureResult.insert(END, mean)
        elif(Measure=="Median"):
            median = np.median(x)
            MeasureResult.delete("1.0", END)
            MeasureResult.insert(END, median)
        elif(Measure=="Mode"):
            mode = stats.mode(x)
            MeasureResult.delete("1.0", END)
            MeasureResult.insert(END, mode[0][0])
        elif(Measure=="Standard Deviation"):
            stdDev = np.std(x)
            MeasureResult.delete("1.0", END)
            MeasureResult.insert(END, stdDev)
    
    Measures = ('Mean', 'Median', 'Mode', 'Standard Deviation')
    selected_measure = tk.StringVar()
    MEASURES_cb = ttk.Combobox(Statistics,state=DISABLED,textvariable=selected_measure,width=30)
    MEASURES_cb['values'] = Measures
    MEASURES_cb['state'] = 'readonly'  # normal
    MEASURES_cb.place(x=250,y=370)
    MEASURES_cb.current(0)
    MEASURES_cb.bind('<<ComboboxSelected>>',Calc_Measure)
    LbL_Measures=Label(Statistics,text="Please Choose A Measure", font= "Georgia",bg='#2a5289',fg='#e2d3f4').place(x=0,y=365)
    def Exit_Data():
        Statistics.destroy()
        window.deiconify()
    HoverButton(
    Statistics, 
    text="Back", font = "Georgia", bg='#e2d3e4',fg='#2a5289', activebackground="#e2dfff", 
    command=Exit_Data
    ).place(x= 450, y=500)


    
def Hypothesis():
        window.withdraw()
        Hypo= Tk()
        #Hypo = Toplevel(window)
        Hypo.title("Hypothesis")
        Hypo.geometry('550x600')
        Hypo.configure(bg='#2a5289')
        LBL_Greating=Label(Hypo,text="Salary Hypothesis",bg='#2a5289',fg='#e2d3f4',font=("arial",18)).place(x=180, y=5)
        #global data
        data=pd.read_csv('Salaries.csv')
        true_mean=data['Salary'].mean()
        true_std=data['Salary'].std()
        LbL_GRAPHs=Label(Hypo,text="Enter Your Expected Salary", font= "Georgia",bg='#2a5289',fg='#e2d3f4').place(x=0,y=100)
        ExpectedSalary=tk.Text (Hypo, height=0.5 ,width=20)
        ExpectedSalary.place(x=325, y=105)
        def GetExpectedSalary():
            global H0
            H0 = int(ExpectedSalary.get("1.0",END))
            print(H0)
        BUT_salary=HoverButton(Hypo,text="Store Salary",command=GetExpectedSalary, font = "Georgia", bg='#e2d3e4',fg='#2a5289'
        , activebackground="#e2dfff")
        BUT_salary.place(x=345,y=140)
        def GetExpectedValue(event):
            global con
            con = int(EXpectedValue.get())
            print (con)
        LBL_EXVALUE=Label(Hypo,text="Choose Level of Confidence",bg='#2a5289',fg='#e2d3f4',font="Georgia").place(x=0, y=240)
        EX_Values = ('99', '95')
        EXpectedValue = ttk.Combobox(Hypo,state=DISABLED,width=30)
        EXpectedValue['values'] = EX_Values
        EXpectedValue['state'] = 'readonly'  # normal
        EXpectedValue.place(x=300,y=245)
        EXpectedValue.current(0)
        EXpectedValue.bind('<<ComboboxSelected>>',GetExpectedValue)

        LBL_Result=Label(Hypo,text="Hypothesis Result",bg='#2a5289',fg='#e2d3f4',font="Georgia").place(x=0, y=400)
        HypoResult=tk.Text (Hypo, height=0.5 ,width=60)
        HypoResult.place(x=40, y=450)
        def GetResults():
            if(con==95):
                Zcritical=1.96
            else:
                Zcritical=2.575
            sample=data['Salary'][np.argsort(np.random.random(1500))[0:1000]]
            H1=sample.mean()
            z=(H1-H0)/(true_std/math.sqrt(1000))
            if(z>=Zcritical):
                str_res = "You may get paid this salary with "+str(con)+"% confidence"
                HypoResult.delete("1.0", END)
                HypoResult.insert(END, str_res)
            else:
                print(str)
                str_res = "It's almost impossible to get this salary"
                HypoResult.delete("1.0", END)
                HypoResult.insert(END,str_res)
        BUT_Result=HoverButton(Hypo,text="Get Results",command=GetResults, font = "Georgia", bg='#e2d3e4',fg='#2a5289', activebackground="#e2dfff")
        BUT_Result.place(x=230,y=300)
        def Exit_Data():
            Hypo.destroy()
            window.deiconify()
        HoverButton(
        Hypo, 
        text="Back", font = "Georgia", bg='#e2d3e4',fg='#2a5289', activebackground="#e2dfff", 
        command=Exit_Data
        ).place(x= 450, y=500)


window=Tk()
window.configure(bg='#2a5289')




Start(window)
window.mainloop()