from SQL import SQL
import pUtils
import os
import json
import uuid

###   Takes path to directory where the "standard files" exist   ###
def push(dirFullPath):
    
    sql = SQL()
    sql.conn()
    
    testRunID = str(uuid.uuid4())
    
    fileFullPath = os.path.join(dirFullPath,'TestRun.csv')
    s,v = prepsForTestRun(fileFullPath,testRunID)
    if s!='': sql.execute(s,v)
    fileFullPath = os.path.join(dirFullPath,'TestMeasurement.csv')
    s,v = prepsForTestMeasurement(fileFullPath,testRunID)
    if s!='': sql.execute(s,v)
    
    fileFullPath = os.path.join(dirFullPath,'StringDictionary.json')
    s,v = prepsForDictionary(fileFullPath,testRunID)
    if s!='': sql.execute(s,v)
    fileFullPath = os.path.join(dirFullPath,'DoubleDictionary.json')
    s,v = prepsForDictionary(fileFullPath,testRunID)
    if s!='': sql.execute(s,v)
    fileFullPath = os.path.join(dirFullPath,'FileDictionary.json')
    s,v = prepsForDictionary(fileFullPath,testRunID)
    if s!='': sql.execute(s,v)
    
    sql.commit()
    sql.close()
    

def prepsForTestRun(fileFullPath,testRunID):
    s = 'INSERT INTO TestRun'
    s+= ' (testRunID,SN,siteID,stationID,startTimestamp,endTimestamp,isPass,lastTestEntered)'
    s+= ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s);'
    
    data = pUtils.quickFileRead(fileFullPath)
    v = [testRunID]+data.split(',')
    return s,v
   
def prepsForTestMeasurement(fileFullPath,testRunID):
    data = pUtils.quickFileRead(fileFullPath)
    measurementList = data.split('\n')
    if len(measurementList)==0: return '',[]
    
    s = 'INSERT INTO TestMeasurement'
    s+= ' (testRunID,startTimestamp,endTimestamp,testName,testMeasurementName,dataType,stringMin,stringMeasurement,stringMax,doubleMin,doubleMeasurement,doubleMax,isPass)'
    s+= ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    s+= ',(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'*(len(measurementList)-1)
    s+= ';'
    
    v = []
    for measurement in measurementList:
        data = measurement.split(',')
        if data[4]=='DOUBLE':
            v += [testRunID]+data[0:8]+data[5:8]+data[8:]
        else: #Is dataTtype is string or something else just store it as string
            v += [testRunID]+data[0:8]+[0,0,0]+data[8:]
            
    return s,v
   
   
def prepsForDictionary(fileFullPath,testRunID):
    data = pUtils.quickFileRead(fileFullPath)
    d = json.loads(data)
    if len(d)==0: return '',[]
    
    s = 'INSERT INTO StringDictionary'
    s+= ' (testRunID,key,value)'
    s+= ' VALUES (%s,%s,%s)'
    s+= ',(%s,%s,%s)'*(len(d)-1)
    s+= ';'
    
    v = []
    for key in d:
        v += [testRunID]+[key]+[d[key]]
    return s,v
