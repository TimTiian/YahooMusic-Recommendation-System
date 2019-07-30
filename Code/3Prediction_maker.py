"""
Python script to take the scores file and convert the scores for each track into a 1 or 0.
3 tracks will be recommended to each user. 1 = Recommended, 0 = Not Recommended 

"""

import heapq as hp
import numpy as np
import itertools
file_name_rating='scores.txt'
output_file='prediction.txt'

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
        weight=[1.0,1.02, 1.01, 1.05, 1.03, 1.011]        #weights in order for each of the 6 tracks
        bias=[0.03, 0.02, 0.01, 0.05, 0.01, 0.01]         #biases in order for each of the 6tracks 
        score_vec[ii]= score*weight[ii]+bias[ii]
        ii=ii+1
        lastUserID=userID
        if ii==6:         
          n_largest=hp.nlargest(3,zip(score_vec, itertools.count()))
          [first,index1]=n_largest[0]
          [second,index2]=n_largest[1]
          [third,index3]=n_largest[2]
          rec=[0]*6
      
          if first>5:
            rec[index1]=1
          if second>5:
            rec[index2]=1
          if third>5:
            rec[index3]=1
          
          if first==0.05:
             rec[0]=1
             rec[1]=1
             rec[3]=1
          
          #print rec
          
   
          for nn in range(0,6):
            outStr= str(rec[nn])
            fOut.write(outStr + '\n')
            
fRating.close()
fOut.close()