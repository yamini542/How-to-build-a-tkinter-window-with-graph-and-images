import tkinter
#---  import tkinter for the GUI window
import matplotlib.pyplot as pt
#---- matplot library for the grpahs plotting and assigning to the matplot to pt
import pandas as pd
#-- pandas library assigned to the pd
import numpy as np
import pymongo
#--- for database to connect to MongoDb
from pymongo import MongoClient
from sklearn import tree
import pydotplus
#from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
#to embedded figure in the GUi windoe we use canvas----------------
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from PIL import ImageTk, Image

"""
#we created a documents 
if you wan to insert u can use use ---------mycollection.insert_one(mydict)-------------
insert_one insert only one time
we are searching from the data base we sed go to line 111 to check the condition 
 for documents in the database name login_valid if the username is equalt to the value in the username key and 
 password value in the password key then go to next page


"""

class Show_DataAnalysis:
    
    def __init__(self):
        
       
        #****************************************************
        client=MongoClient("mongodb+srv://Yamini_admin:oKov2HN7On5CBD4n@ranking.opqbg9f.mongodb.net/?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
        mydb=client["Predict_Income"]
#---- collection name is Income_data we are imported the csv file from the mongodb---------
        Name_Collection = mydb["Income_data"]
        self.Convert_to_Dataframe = pd.DataFrame(list(Name_Collection.find()))
        #--- converting the json files in to the Data frames from the MongoDB
        #***********************************
        self.mw2=tkinter.Tk()
        #--- mw2 to open the tkinter window
        self.mw2.minsize(1000,1000)
        self.mw2.maxsize(1000,1000)
        #size of the window
        self.mw2.title("Analysis of the Income Data set")
        #---title of the window-----
        self.Heading1=tkinter.Label(self.mw2,text="Prediction of the Income data a person can make more than 50k or not", font=(18))
        #---- heading label and given text
        self.Heading1.pack(side="top")
        #--- pack for the position of the heading label and to show
        
        #self.Click_ScatterPlot_get=tkinter.Button(self.mw2,text="Display_ScatterPlot", command=self.Decision_Scatter)
        #self.Click_ScatterPlot_get.pack(side="top")
        
        
        
        self.Click_DecisionTree=tkinter.Button(self.mw2,text="Display_DecisionTree", command=self.Display_DecisionTree)
        self.Click_DecisionTree.pack(side="top")
        
        
        #****************************************************
        
        self.Click_Graph=tkinter.Button(self.mw2,text="Display_Graph", width=15,command=self.Display_Graph)
        #--- Button and it gives command to open once Display_Graph once click on the button
        self.Click_Graph.pack(side="top")
        
        #******************************************
        
        tkinter.mainloop()
    def Display_Graph(self):
        
        data=self.Convert_to_Dataframe
        #assigning the Data frames to the variable data
        plt.scatter(data['educational-num'], data['education'])
        #-- post-id and page_followers are the columns names whcih choosen to shown on the graph
        plt.xlabel('educational-num')
        #--- xlabl Post_id show on the x-axis
        plt.ylabel('education')
        #y-axis
        plt.show()
        #--- tos how the plotting of the graph ----------------
        plt.legend()
        #to show the graph
        
        self.figure_show = Figure(
            figsize = (20, 20),
                 dpi = 60)
  #-----specifing the size of the widown within the gui mainwindow--------------
        plot =self.figure_show.add_subplot(111)
        plot.plot(data['educational-num'], data['education'], color = "blue", marker="x", linestyle=" ")
        plot.set_title('Prediction of Income')
        plot.set_xlabel('educational-num')
        plot.set_ylabel('education')
        plot.legend()
        
        canvas = FigureCanvasTkAgg(self.figure_show, self.mw2)
        
        canvas.get_tk_widget().pack()
       
        
        canvas.draw()
    #canvas used to display th graph -------------------
    
    def Display_DecisionTree(self):
        #---------------function name Display_DecisionTree---------------       
         #self.mw3 = tkinter.Tk()
#-------------showing in a another window for clear visualization-------------------      
         #self.mw3.geometry('800x800') 
         self.d = ImageTk.PhotoImage(Image.open("dtree_10rows.png"))
         self.label =tkinter.Label(image = self.d)
#-------------------embedding a image in a label---------------------       
         self.label.pack(side="bottom")
#------positioning the label-----------------
         tkinter.mainloop()
         #--to run the gui window------------------
         
    
           
            
            
        
        
Show_DataAnalysis()

