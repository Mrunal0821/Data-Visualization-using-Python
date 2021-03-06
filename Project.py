import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sb
from sklearn import linear_model
import tkinter
from tkinter import *
import tabulate as tb
from tabulate import tabulate
from tkinter import filedialog
main=tkinter.Tk()
from tkinter.ttk import *
rad=IntVar()
main.title("**PLOTIFY**")
main.config(bg="white")
main.geometry('1000x300')
label1=Label(main,text="========PLOTIFY=======", font=("Times New Roman", 12))
label1.grid(column=1,row=0)
def clicked1():
    file1 = filedialog.askopenfile(initialdir ="E:", title = "Import Data")
    path= file1.name
    loc1=path
    database=pd.read_csv(loc1)
    df=pd.DataFrame(database)
    dataframe=tabulate(df, headers="keys", tablefmt="psql")
    def sel():
        selected_option=rad.get()
        if (selected_option==1):
            def lineplot():
                x=str(x_lineentry.get())
                y=str(y_lineentry.get())
                plt.plot(database[x],database[y])
                plt.xlabel(x)
                plt.ylabel(y)
                style.use("bmh")
                plt.grid()
                plt.show()
            line_label1=Label(main, text="****************LINE GRAPH*****************", font=("Times New Roman", 10))
            line_label1.grid(column=1, row=8)
            case_warning=Label(main, text="CASE SENSITIVE", font=("Times New Roman", 10))
            case_warning.grid(column=1,row=9)
            x_lineaxis=Label(main, text="Enter X AXIS LABEL:", font=("Times New Roman", 10))
            x_lineaxis.grid(column=0,row=10)
            y_lineaxis=Label(main, text="Enter Y AXIS LABEL:", font=("Times New Roman", 10))
            y_lineaxis.grid(column=0,row =11)
            x_line=Label(main, text="*CATEGORICAL TYPE*",font=("Times New Roman",10))
            x_line.grid(column=2, row=10)
            y_line=Label(main, text="**CONTINOUS TYPE**",font=("Times New Roman",10))
            y_line.grid(column=2,row=11)
            x_lineentry=Entry(main, width=25)
            x_lineentry.grid(column=1,row=10)
            y_lineentry=Entry(main, width=25)
            y_lineentry.grid(column=1, row=11)
            x_submit=Button(main, text="PLOT", command=lineplot)
            x_submit.grid(column=1,row=12)
        elif (selected_option==2):
            def barplot():
                x = str(x_barentry.get())
                y = str(y_barentry.get())
                plt.bar(database[x], database[y])
                plt.xlabel(x)
                plt.ylabel(y)
                style.use("bmh")
                plt.grid()
                plt.show()
            testlabel = Label(main, text="*****************BAR CHART*****************", font=("Times New Roman", 10))
            testlabel.grid(column=1, row=8)
            case_warning = Label(main, text="CASE SENSITIVE", font=("Times New Roman", 10))
            case_warning.grid(column=1, row=9)
            x_baraxis = Label(main, text="Enter X AXIS LABEL:", font=("Times New Roman", 10))
            x_baraxis.grid(column=0, row=10)
            y_baraxis = Label(main, text="Enter Y AXIS LABEL:", font=("Times New Roman", 10))
            y_baraxis.grid(column=0, row=11)
            x_bar = Label(main, text="*CATEGORICAL TYPE*", font=("Times New Roman", 10))
            x_bar.grid(column=2, row=10)
            y_bar = Label(main, text="**CONTINOUS TYPE**", font=("Times New Roman", 10))
            y_bar.grid(column=2, row=11)
            x_barentry = Entry(main, width=25)
            x_barentry.grid(column=1, row=10)
            y_barentry = Entry(main, width=25)
            y_barentry.grid(column=1, row=11)
            x_submit = Button(main, text="PLOT", command=barplot)
            x_submit.grid(column=1, row=12)
        elif (selected_option==3):
            def pieplot():
                x=str(x_pieentry.get())
                y=str(y_pieentry.get())
                plt.pie(labels=database[x],x=database[y], autopct='%1.1f%%')
                style.use("bmh")
                plt.grid()
                plt.show()
            testlabel = Label(main, text="*****************PIE CHART*****************", font=("Times New Roman", 10))
            testlabel.grid(column=1, row=8)
            case_warning = Label(main, text="CASE SENSITIVE", font=("Times New Roman", 10))
            case_warning.grid(column=1, row=9)
            x_pieaxis = Label(main, text="Enter SECTOR LABEL:", font=("Times New Roman", 10))
            x_pieaxis.grid(column=0, row=10)
            y_pieaxis = Label(main, text="Enter  VALUE LABEL:", font=("Times New Roman", 10))
            y_pieaxis.grid(column=0, row=11)
            x_pie = Label(main, text="*CATEGORICAL TYPE*", font=("Times New Roman", 10))
            x_pie.grid(column=2, row=10)
            y_pie = Label(main, text="**CONTINOUS TYPE**", font=("Times New Roman", 10))
            y_pie.grid(column=2, row=11)
            x_pieentry = Entry(main, width=25)
            x_pieentry.grid(column=1, row=10)
            y_pieentry = Entry(main, width=25)
            y_pieentry.grid(column=1, row=11)
            x_submit = Button(main, text="PLOT", command=pieplot)
            x_submit.grid(column=1, row=12)
        elif (selected_option==4):
            def boxplot():
                x=str(x_boxentry.get())
                y=str(y_boxentry.get())
                sb.boxplot(x=database[x],y=database[y],data=database)
                style.use("bmh")
                plt.grid()
                plt.show()
            testlabel = Label(main, text="*****************BOX CHART*****************", font=("Times New Roman", 10))
            testlabel.grid(column=1, row=8)
            case_warning = Label(main, text="CASE SENSITIVE", font=("Times New Roman", 10))
            case_warning.grid(column=1, row=9)
            x_boxaxis = Label(main, text="Enter X AXIS LABEL:", font=("Times New Roman", 10))
            x_boxaxis.grid(column=0, row=10)
            y_boxaxis = Label(main, text="Enter Y AXIS LABEL:", font=("Times New Roman", 10))
            y_boxaxis.grid(column=0, row=11)
            x_box = Label(main, text="*CATEGORICAL TYPE*", font=("Times New Roman", 10))
            x_box.grid(column=2, row=10)
            y_box = Label(main, text="**CONTINOUS TYPE**", font=("Times New Roman", 10))
            y_box.grid(column=2, row=11)
            x_boxentry = Entry(main, width=25)
            x_boxentry.grid(column=1, row=10)
            y_boxentry = Entry(main, width=25)
            y_boxentry.grid(column=1, row=11)
            x_submit = Button(main, text="PLOT", command=boxplot)
            x_submit.grid(column=1, row=12)
        elif (selected_option==5):
            def scatterplot():
                x=str(x_scatterentry.get())
                y=(y_scatterentry.get())
                plt.scatter(database[x],database[y])
                plt.xlabel(x)
                plt.ylabel(y)
                style.use("bmh")
                plt.grid()
                plt.show()
            testlabel = Label(main, text="***************SCATTER PLOT****************", font=("Times New Roman", 10))
            testlabel.grid(column=1, row=8)
            case_warning = Label(main, text="CASE SENSITIVE", font=("Times New Roman", 10))
            case_warning.grid(column=1, row=9)
            x_scatteraxis = Label(main, text="Enter X AXIS LABEL:", font=("Times New Roman", 10))
            x_scatteraxis.grid(column=0, row=10)
            y_scatteraxis = Label(main, text="Enter Y AXIS LABEL:", font=("Times New Roman", 10))
            y_scatteraxis.grid(column=0, row=11)
            x_scatter = Label(main, text="**CONTINOUS TYPE**", font=("Times New Roman", 10))
            x_scatter.grid(column=2, row=10)
            y_scatter = Label(main, text="**CONTINOUS TYPE**", font=("Times New Roman", 10))
            y_scatter.grid(column=2, row=11)
            x_scatterentry = Entry(main, width=25)
            x_scatterentry.grid(column=1, row=10)
            y_scatterentry = Entry(main, width=25)
            y_scatterentry.grid(column=1, row=11)
            x_submit = Button(main, text="PLOT", command=scatterplot)
            x_submit.grid(column=1, row=12)
        elif (selected_option==6):
            def scatterplotlr():

                x=str(x_scatterlrentry.get())
                y=str(y_scatterlrentry.get())
                plt.scatter(database[x],database[y])
                plt.xlabel(x)
                plt.ylabel(y)
                reg=linear_model.LinearRegression()
                reg.fit(database[[x]],database[y])
                coef=reg.coef_
                intercept=reg.intercept_
                a=database[x]
                b=database[y]
                sigma_x=np.std(a)
                sigma_y=np.std(b)
                coef_correlation=coef*sigma_x/sigma_y
                plt.plot(a,coef*a+intercept)
                lr_analysis = tkinter.Tk()
                v=IntVar()
                lr_analysis.title("REGRESSION ANALYSIS")
                lr_al1=Label(lr_analysis, text="SLOPE OF THE LINE IS :"+ str(coef), font=("Times New Roman", 10))
                lr_al1.grid(column=1,row=0)
                lr_al2=Label(lr_analysis,text="INTERCEPT OF THE LINE IS: "+ str(intercept), font=("Times New Roman",10))
                lr_al2.grid(column=1,row=1)
                lr_al3=Label(lr_analysis, text="Coefficient of Correlation is : "+str(coef_correlation), font=("Times New Roman",10) )
                lr_al3.grid(column=1,row=3)
                lr_al4=Label(lr_analysis,text="EQUATION OF LINE IS: Y=" +str(coef) +"X+" +str(intercept), font=("Times New Roman",10))
                lr_al4.grid(column=1,row=4)
                style.use("bmh")
                def get_estimate():
                    est1_lb1 = Label(lr_analysis, text=" ", font=("Times New Roman",10))
                    est1_lb1.grid(column=1, row=8)
                    est1_lb2 = Label(lr_analysis, text=" ", font=("Times New Roman", 10))
                    est1_lb2.grid(column=0, row=9)
                    est1_lb3 = Label(lr_analysis, text=" ", font=("Times New Roman", 10))
                    est1_lb3.grid(column=1, row=11)
                    def est1():
                        def ck1():
                            y = float(est1_ent1.get())
                            x = (y-intercept)/coef
                            est1_lb3.configure(text="ESTIMATED VALUE OF "+str.upper(x_scatterlrentry.get())+ " FOR "
                                                    +str.upper(y_scatterlrentry.get())+ "="+str(y)+"is"+str(x))
                        est1_lb1.configure(text="***ESTIMATE " +str.upper(x_scatterlrentry.get())
                                                +" FOR "+str.upper(y_scatterlrentry.get()) +"****",)
                        est1_lb2.configure(text= "ENTER VALUE OF "+str.upper(y_scatterlrentry.get()) +" >>>")
                        est1_ent1 = Entry(lr_analysis, width=25)
                        est1_ent1.grid(column=2, row=9)
                        est1_bt1 = Button(lr_analysis, text="GET ESTIMATE", command=ck1)
                        est1_bt1.grid(column=1, row=10)
                    def est2():
                        def ck2():
                            x = float(est2_ent1.get())
                            y = coef*x+intercept
                            est1_lb3.configure(text="ESTIMATED VALUE OF " +str.upper(y_scatterlrentry.get())+ " FOR "
                                                    +str.upper(x_scatterlrentry.get())+" = "+str(x)+" is "+str(y))
                        est1_lb1.configure( text="***ESTIMATE "+ str.upper(y_scatterlrentry.get()) +" FOR "+
                                                 str.upper(x_scatterlrentry.get())+"****")
                        est1_lb2.configure(text= "ENTER VALUE OF "+str.upper(x_scatterlrentry.get())+">>>")
                        est2_ent1 = Entry(lr_analysis, width=25)
                        est2_ent1.grid(column=2, row=9)
                        est2_bt1 = Button(lr_analysis, text="GET ESTIMATE", command=ck2)
                        est2_bt1.grid(column=1, row=10)
                    lb = Label(lr_analysis,text="****ESTIMATION****", font=("Times New Roman",10))
                    lb.grid(column=1, row=6)
                    rad1 = Radiobutton(lr_analysis,text="ESTIMATE " +str.upper(x_scatterlrentry.get())+ " FOR " +
                                                        str.upper(y_scatterlrentry.get()) , variable=v,value=1 ,
                                       command=est1)
                    rad2 = Radiobutton(lr_analysis,text="ESTIMATE " +str.upper(y_scatterlrentry.get()) +" FOR "
                                                        +str.upper(x_scatterlrentry.get()), variable=v,  value=2,
                                       command=est2)
                    rad1.grid(column=0, row=7)
                    rad2.grid(column=2, row=7)
                estimate_bt = Button(lr_analysis, text="Get Estimate Value",command=get_estimate)
                estimate_bt.grid(column=1, row=5)
                plt.grid()
                plt.show()
            testlabel = Label(main, text="****SCATTER PLOT WITH LINEAR REGRESSION****", font=("Times New Roman", 10))
            testlabel.grid(column=1, row=8)
            case_warning = Label(main, text="CASE SENSITIVE", font=("Times New Roman", 10))
            case_warning.grid(column=1, row=9)
            x_scatterlraxis = Label(main, text="Enter X AXIS LABEL:", font=("Times New Roman", 10))
            x_scatterlraxis.grid(column=0, row=10)
            y_scatterlraxis = Label(main, text="Enter Y AXIS LABEL:", font=("Times New Roman", 10))
            y_scatterlraxis.grid(column=0, row=11)
            x_scatterlr = Label(main, text="**CONTINUOS TYPE**", font=("Times New Roman", 10))
            x_scatterlr.grid(column=2, row=10)
            y_scatterlr = Label(main, text="**CONTINOUS TYPE**", font=("Times New Roman", 10))
            y_scatterlr.grid(column=2, row=11)
            x_scatterlrentry = Entry(main, width=25)
            x_scatterlrentry.grid(column=1, row=10)
            y_scatterlrentry = Entry(main, width=25)
            y_scatterlrentry.grid(column=1, row=11)
            x_submit = Button(main, text="PLOT", command=scatterplotlr)
            x_submit.grid(column=1, row=12)
    #NEW WINDOW1
    subwin1=tkinter.Tk()
    subwin1.title("DATA WINDOW")
    subwin1.configure(bg="white")
    #SAME MAIN WINDOW
    sublabel1=Label(main, text="YOU HAVE IMPORTED THE DATA SUCCESSFULLY", font=("Times New Roman",10))
    sublabel1.grid(column=1,row=3)
    sublabel2=Label(main, text="PLEASE KEEP THE DATA WINDOW OPEN TO REFER THE DATA FROM IMPORTED DATASET", font=("Times New Roman",10))
    sublabel2.grid(column=1,row=4)
    sublabel2=Label(subwin1, text= dataframe, font=("Times New Roman",10))
    sublabel2.grid(column=0,row=1)
    sublabel3=Label(main, text="Please select a option from below buttons", font=("Times New Roman", 10))
    sublabel3.grid(column=1,row=5)
    option1=Radiobutton(main, text="LINE GRAPH",variable=rad, value=1,command=sel)
    option2=Radiobutton(main, text="BAR GRAPH",variable=rad,  value=2,command=sel)
    option3=Radiobutton(main, text="PIE CHART", variable=rad, value=3, command=sel)
    option4=Radiobutton(main, text="BOX CHART", variable=rad, value=4, command=sel)
    option5=Radiobutton(main, text="SCATTER PLOT", variable=rad, value=5, command =sel)
    option6=Radiobutton(main, text="SCATTER PLOT ALONG WITH LINEAR REGRESSION", variable=rad, value=6, command=sel, )
    option1.grid(column=0,row=6)
    option2.grid(column=1,row=6)
    option3.grid(column=2,row=6)
    option4.grid(column=0,row=7)
    option5.grid(column=1,row=7)
    option6.grid(column=2,row=7)
extlabel1 = Label(main, text = "IMPORT ANY DATASET AND GET YOUR DATA VISUALIZATION DONE !", font = ("Times New Roman", 10))
extlabel1.grid(column= 1, row= 1)
button1 = Button(main, text="IMPORT DATA" ,command=clicked1)
button1.grid(column=1,row=2)
warininglab1 = Label(main, text= "only .csv dataformat", font = ("Times New Roman", 10))
warininglab1.grid(column=2,row=2)
mainloop()
