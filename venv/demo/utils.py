import pandas as pd
import numpy as np

class Shapelet(object):
    def __init__(self):
        self.id = 0.0
        self.Class = ''
        self.subseq = None
        self.DD = 0.0
        self.thresh = 0.0

def convertShapelet(path, filename):
    testFile =  pd.read_csv(path+filename, header=None)
    Class = testFile[0][0]
    shapData = testFile[1][0]
    shapData = shapData.strip('()').replace('[','').replace(']','')
    shapeletList = []
    #shapObjectList: DD, Thresh
    shapObjectList = shapData.split("),(")
    for shapObject in shapObjectList:
        shap = Shapelet()
        shapObject = shapObject.split(',')
        shap.DD = float(shapObject[0])
        shap.thresh = float(shapObject[1])
        shap.subseq = [float(s) for s in shapObject[2:]]
        shapeletList.append(shap)
    return shapeletList


class timeseries(object):
    def __init__(self):
        self.id = None
        self.Class = ''
        self.seq = None

def convertTS(path, filename):
    tsObjectList1 = []
    tsObjectList2 = []
    testFile = pd.read_csv(path + filename, header=None)
    tsClass1 = testFile[testFile[1] == 1]
    tsClass2 = testFile[testFile[1] == -1]
    for i in tsClass1.index:
        ts = timeseries()
        row = tsClass1.loc[i]
        ts.id = row[0]
        ts.Class = row[1]
        ts.seq = row[2].split(',')
        ts.seq = [float(val) for val in ts.seq]
        tsObjectList1.append(ts)

    for i in tsClass2.index:
        ts = timeseries()
        row = tsClass2.loc[i]
        ts.id = row[0]
        ts.Class = row[1]
        ts.seq = row[2].split(',')
        ts.seq = [float(val) for val in ts.seq]
        tsObjectList2.append(ts)

    return tsObjectList1, tsObjectList2