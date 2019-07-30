from __future__ import print_function
import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.ml.recommendation import ALS

from pyspark.sql import SQLContext
import numpy as np
import os

def read_lines(file, num):
    lines = []
    line = file.readline()
    if line:
        lines.append(line.strip().split("|"))
        for i in range(1,num):
            lines.append(file.readline().strip().split("|"))
        return lines
    else:
        return line

if not os.path.isdir("result"):
    os.makedirs("result")


with open("trainData.txt","w") as trainData:
    with open("trainItem2.txt") as trainFile:
        for line in trainFile:
            if "|" in line:
                cur_user = line.split("|")[0]
                print(cur_user,end="\r")
            else:
                trainData.write(cur_user+"\t"+line)

with open("testData.txt","w") as testData:
    with open("testItem2.txt") as testFile:
        for line in testFile:
            if "|" in line:
                cur_user = line.split("|")[0]
                print(cur_user,end="\r")
            else:
                testData.write(cur_user+"\t"+line)


from pyspark.sql.types import *
from pyspark.sql.functions import col

sc = SparkContext()
sqlC = SQLContext(sc)

trainData = sc.textFile("trainData.txt").map(lambda line: line.split("\t"))
testData = sc.textFile("testData.txt").map(lambda line: line.split("\t"))


trainDataFrame = sqlC.createDataFrame(trainData,["user","item","rating"])

trainDataFrame = trainDataFrame.withColumn('user' , col('user').cast('int'))
trainDataFrame = trainDataFrame.withColumn('item' , col('item').cast('int'))
trainDataFrame = trainDataFrame.withColumn('rating' , col('rating').cast('int'))

testDataFrame = sqlC.createDataFrame(testData,["user","item"])

testDataFrame = testDataFrame.withColumn('user' , col('user').cast('int'))
testDataFrame = testDataFrame.withColumn('item' , col('item').cast('int'))

als = ALS(rank = 10,maxIter = 15)

model = als.fit(trainDataFrame)
predTestData = model.transform(testDataFrame)


prediction = sorted(predTestData.collect(), key = lambda r: int(r[0]))

with open("spark_prediction.txt","w") as predFile:
    for line in prediction:
        
        if line[2]!=line[2]:
            temp_str = "0"
        else:
            temp_str = str(int(line[2]))
        predFile.write(str(line[0])+"|"+str(line[1])+"|"+temp_str+"\n")

sc.stop()