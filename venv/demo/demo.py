import tkinter
from tkinter import *
from tkinter.ttk import *  #Widgets avec thèmes
from gui_function import gui_function
from ml_methods import ml_methodes
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
LARGE_FONT= ("Verdana", 12)

from matplotlib import pyplot as plt
import numpy as np

class MyProgramme(Tk):
    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        '''
        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
        '''
        frame = StartPage(container,self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tkinter.Frame):
    def hello(self):
        print("hello cmd")

    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        tkinter.Frame.__init__(self,parent)
        #Pre-configuration of interface
        self.winfo_toplevel().title("C2RMF Vibration Activity Recognition")
        self._root().geometry('888x548')

        '''start of menubar'''
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        self.gui = gui_function(self)
        filemenu.add_command(label ="New training file", command = self.gui.add_training_file)
        # add the label which indicate the file name
        filemenu.add_separator()
        filemenu.add_command(label ="exit", command = self.hello)
        menubar.add_cascade(label="File", menu = filemenu)
        self._root().config(menu=menubar)
        '''end of menubar'''

        #Frame0
        self.frame0 = Frame(self)
        #self.frame1.pack(fill = BOTH, side=TOP)
        self.frame0.pack(fill=X)
        self.frame0.config(borderwidth=2, relief=GROOVE)

        #Frame 1
        self.frame1 = Frame(self.frame0)
        #self.frame1.pack(fill = BOTH, side=TOP)
        self.frame1.grid(row=0,sticky=W)
        l1 = Label(self.frame1, text="Select your training file: ")
        l2 = Label(self.frame1, text=" ")
        b1 = Button(self.frame1, text="Training file", command=self.gui.add_training_file)
        l1.grid(row=0, column=0, sticky=W)
        b1.grid(row=1, column=0, sticky=W)
        l2.grid(row=2, column=0, sticky=W,ipady=10)

        #Frame 2
        frame2 = Frame(self)
        frame2.pack(fill=X)
        frame2.config(borderwidth=2, relief=GROOVE)
        l3 = Label(frame2, text="Select the method to extract data features: ")
        self.methodExtractFeature = ('TSLearn', 'Shapelet-based')
        self.listMethods = Combobox(frame2, values = self.methodExtractFeature, state = 'readonly')
        # Placement des widgets
        self.listMethods.grid(row=1, column=0, sticky=S)
        self.text_features = Text(frame2)
        b2 = Button(frame2, text="Extract features", command=self.extractFeature)
        l3.grid(row=0, column=0, sticky=W)
        b2.grid(row=2, column=0, sticky=N)
        self.text_features.grid(row=1, column=1, rowspan=2)

        #Frame 3
        frame3 = Frame(self)
        frame3.pack(fill=X)
        self.classifier = ('KNearestNeighbors', 'Decision tree', 'RandomForest', 'AdaBoost', 'GradientBoosting')
        self.listClassifier = Combobox(frame3, values = self.classifier, state = 'readonly')
        # Placement des widgets
        self.listClassifier.grid(row=1, column=0)
        b3 = Button(frame3, text="Train learning model", command=self.trainClassifier)
        b3.grid(row=1, column=1, sticky=W)
        def process_ongoing():
            self.text_features.insert(INSERT, "Extracting data features... \n")
        b3.bind("<Button-1>", process_ongoing)

        #Frame 4
        frame4 = Frame(self)
        frame4.pack(fill=X, ipady=10)
        #b4 = Button(frame4, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        b4 = Button(frame4, text="Visit Test Page ->", command=lambda: self.show_frame_plot(self))
        b4.grid(row=0, column=0)
        frame4.grid_columnconfigure(0, weight=1)

    def show_frame_plot(self, StartPageControl):
        frame = PageOne(self.parent, StartPageControl)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def extractFeature(self):
        if(self.gui.training_filename !="file name"):
            self.ml = ml_methodes(self.gui.training_filename, self)
            print(self.gui.training_filename)
            method = self.listMethods.get()
            if (method== 'TSLearn'):
                self.ml.ts_learn("train")
            else:
                if(method == "Shapelet-based"):
                    self.ml.ts_learn("train")

    def trainClassifier(self):
        if(self.listClassifier.get() is not None):
            self.ml.train_model(self.listClassifier.get())

class PageOne(tkinter.Frame):

    def __init__(self, parent, StartPageControl):
        self.ml = StartPageControl.ml
        self.gui = gui_function(self)
        tkinter.Frame.__init__(self, parent)
        #Frame0
        self.frame0 = Frame(self)
        #self.frame1.pack(fill = BOTH, side=TOP)
        self.frame0.pack(fill= tkinter.X)
        self.frame0.config(borderwidth=2, relief=GROOVE)
        #Frame 1
        self.frame1 = Frame(self.frame0)
        self.frame1.grid(row=0,sticky=W)
        l1 = Label(self.frame1, text="Select your testing file: ")
        l2 = Label(self.frame1, text=" ")
        b1 = Button(self.frame1, text="Testing file", command=self.gui.add_testing_file)
        l1.grid(row=0, column=0, sticky=W)
        b1.grid(row=1, column=0, sticky=W)
        l2.grid(row=2, column=0, sticky=W,ipady=10)

        frame2 = Frame(self)
        frame2.pack(fill= tkinter.X)
        b2 = Button(frame2, text="Test", command=self.output_result)
        b2.grid(row=0, column=0, sticky=E)
        b3 = Button(frame2, text="Back to Home", command=lambda: StartPageControl.controller.show_frame(StartPage))
        b3.grid(row=0, column=1, sticky=W)
        frame2.grid_columnconfigure(0, weight=1)
        frame2.grid_columnconfigure(1, weight=1)

    def output_result(self):
        if(self.gui.testing_filename !="file name"):
        #step 1: predict class
            label = tkinter.Label(self, text="Data on processing...", font=LARGE_FONT)
            label.pack(pady=10,padx=10)
            y_predict = self.ml.predict_class(self.gui.testing_filename)
        #step 2: plot the figure
            #step 2.1: plot the original data
            #step 2.2: for different segments in the plot figure, adjust their colors which represent the prediction class
            colors = {
                1: 'blue', #'Transport en camion du Louvre à l’entrepôt Air France', #20 Janv, 10:40-11:25, 21 Janv, 05:25-16:s00
                2: 'green', #'Déchargement du camion',#20 Janv, 11:25-13:30
                3: 'red', #'Transport en zone de fret et chargement de l’avion',#20 Janv,16:48-16:55
                4: 'black', #'Décollage',#20 Janv, 18:31-18:52
                5: 'yellow', #'Vol',#20 Janv, 18:52 - 21 Janv, 01:51
                6: 'fuchsia', #'Atterrissage',#21 Janv, 01:51-02:36
                7: 'sienna', #'Déchagement de l\'avion et chargement du camion' #21 Janv, 03:00-05:25
                8: 'white' #'Déchagement de l\'avion et chargement du camion' #21 Janv, 03:00-05:25
            }

            # length(self.ml.test_df) = 20 * length(y_predict)
            #len_data_i = self.ml.test_df['sum'].size
            #X = np.arange(0, len_data_i, 1)

            f = Figure(figsize=(5,5), dpi=100)
            a = f.add_subplot(111)
            a.set_title("Plot figure")
            X = [t for t in self.ml.test_df['time']]
            c = [colors[y] for y in y_predict]
            c = np.repeat(c, 20)
            datemin = self.ml.test_df['time'][0]
            datemax = self.ml.test_df['time'][-1]
            a.set_xlim(datemin, datemax)
            a.scatter(X, self.ml.test_df['sum'], c=c, s=3)

            import matplotlib.patches as mpatches

            classes = ['1.Transportation by truck','2.Unloading the truck','3.Transport in cargo area and loading of the plane', '4.Takeoff', '5.In flight', '6.Landing', '7.Unloading from the plane and loading to the truck', '8.No activity']
            class_colours = ['blue','green','red', 'black', 'yellow', 'fuchsia', 'sienna', 'white']
            recs = []
            for i in range(0,len(class_colours)):
                recs.append(mpatches.Rectangle((0,0),1,1,fc=class_colours[i]))
            a.legend(recs,classes,loc='upper right', fontsize='x-small')
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=True)
            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
            #a.plot(X, self.ml.test_df['sum'], linewidth=0.5)

            label['text'] = "Processing finished, the prediction result: "
if __name__ == '__main__':
    application = MyProgramme()
    application.mainloop()

'''
    # <Button-1>: event produced by the left button of mouse
    #frame.bind("<ButtonRelease-1>", popup)
'''


