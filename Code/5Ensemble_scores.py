"""
Python script to Ensemble all the scores obtained using Linear Regression and Matrix Factorization and come up with a 
final Combined Ensemble prediction list.

"""

import numpy as np

file_name_rating='Rankingf1.txt'

#Add Prediction text file here.

YY1=r'Results\62138.txt'
YY2=r'Results\69603.txt'
YY3=r'Results\69624.txt'
YY4=r'Results\86746.txt'
YY5=r'Results\87193.txt'
YY6=r'Results\87374.txt'
YY7=r'Results\87410.txt'
YY8=r'Results\87446.txt'
YY9=r'Results\87527.txt'
YY10=r'Results\87529.txt'
YY11=r'Results\87554.txt'
YY12=r'Results\87557.txt'

output_file='output.txt'

fRating=open(file_name_rating,'r')
fOut=open(output_file,'w')

# calculation start from here
YX=[0]*12
YX[0]=(2*0.62138-1)*120000
YX[1]=(2*0.69603-1)*120000
YX[2]=(2*0.69624-1)*120000
YX[3]=(2*0.86746-1)*120000
YX[4]=(2*0.87193-1)*120000
YX[5]=(2*0.87374-1)*120000
YX[6]=(2*0.87410-1)*120000
YX[7]=(2*0.87446-1)*120000
YX[8]=(2*0.87527-1)*120000
YX[9]=(2*0.87529-1)*120000
YX[10]=(2*0.87554-1)*120000
YX[11]=(2*0.87557-1)*120000




y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
y9 = []
y10 = []
y11 = []
y12 = []

with open(YY1) as f1:
  Y1 = f1.read().splitlines()
for item in Y1:
    y1.append(float(item))
with open(YY2) as f2:
  Y2 = f2.read().splitlines()
for item in Y2:
    y2.append(float(item))
with open(YY3) as f3:
  Y3 = f3.read().splitlines()
for item in Y3:
    y3.append(float(item))
with open(YY4) as f4:
  Y4 = f4.read().splitlines()
for item in Y4:
    y4.append(float(item))
with open(YY5) as f5:
  Y5 = f5.read().splitlines()
for item in Y5:
    y5.append(float(item))
with open(YY6) as f6:
  Y6 = f6.read().splitlines()
for item in Y6:
    y6.append(float(item))
with open(YY7) as f7:
  Y7 = f7.read().splitlines()
for item in Y7:
    y7.append(float(item))
with open(YY8) as f8:
  Y8 = f8.read().splitlines()
for item in Y8:
    y8.append(float(item))
with open(YY9) as f9:
  Y9 = f9.read().splitlines()
for item in Y9:
    y9.append(float(item))
with open(YY10) as f10:
  Y10 = f10.read().splitlines()
for item in Y10:
    y10.append(float(item))
with open(YY11) as f11:
  Y11 = f11.read().splitlines()
for item in Y11:
    y11.append(float(item))
with open(YY12) as f12:
  Y12 = f12.read().splitlines()
for item in Y12:
    y12.append(float(item))


f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
f10.close()
f11.close()
f12.close()


y1=np.matrix(y1)
y2=np.matrix(y2)
y3=np.matrix(y3)
y4=np.matrix(y4)
y5=np.matrix(y5)
y6=np.matrix(y6)
y7=np.matrix(y7)
y8=np.matrix(y8)
y9=np.matrix(y9)
y10=np.matrix(y10)
y11=np.matrix(y11)
y12=np.matrix(y12)


Y1=2*y1.T-1
Y2=2*y2.T-1
Y3=2*y3.T-1
Y4=2*y4.T-1
Y5=2*y5.T-1
Y6=2*y6.T-1
Y7=2*y7.T-1
Y8=2*y8.T-1
Y9=2*y9.T-1
Y10=2*y10.T-1
Y11=2*y11.T-1
Y12=2*y12.T-1


Y=np.concatenate((Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12),axis=1)
YY=np.dot(Y.T,Y)
inv_YY= np.linalg.inv(YY)
YX= np.matrix(YX)
YX=YX.T
A=inv_YY*YX
NEW=Y1*A[0]+Y2*A[1]+Y3*A[2]+Y4*A[3]+Y5*A[4]+Y6*A[5]+Y7*A[6]+Y8*A[7]+Y9*A[8]+Y10*A[9]+Y11*Y[10]+Y12*A[11]

i=0
for line in fRating:
        arr_test=line.strip().split('|')
        userID = arr_test[0]
        trackID= arr_test[1]
        outStr=str(userID) + '|' + str(trackID)+ '|' + str(NEW.item(i))
        fOut.write(outStr + '\n')
        i=i+1

fRating.close()
fOut.close()


#Covert outfile in to Prediction 
import heapq as hp
import numpy as np
import itertools

file_name_rating='output.txt'
output_file='prediction_ensemble.txt'

fRating=open(file_name_rating,'r')
fOut=open(output_file,'w')

score_vec=[0]*6
lastUserID=-1
for line in fRating:
        arr_test=line.strip().split('|')
        userID = int(arr_test[0])
        trackID= arr_test[1]
        score= float(arr_test[2])
        if userID != lastUserID:
                ii=0
        weight=[0.97,0.96, 0.99, 0.998, 0.999, 1]
        score_vec[ii]= score
        ii=ii+1
        lastUserID=userID
        if ii==6:
          rec=[0]*6   
          n_largest=hp.nlargest(3,zip(score_vec, itertools.count()))
          [first,index1]=n_largest[0]
          [second,index2]=n_largest[1]
          [third,index3]=n_largest[2]
          rec[index1]=1
          rec[index2]=1
          rec[index3]=1

          for nn in range(0,6):
            #outStr=str(userID) + '|' + str(trackID)+ '|' + str(rec[nn])
            outStr= str(rec[nn])
            fOut.write(outStr + '\n')

fRating.close()
fOut.close()
