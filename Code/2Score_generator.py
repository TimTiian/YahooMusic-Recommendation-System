"""

Python script to apply initial weights to the collected Hierarchy scores, giving different weights to album score,
artist score, and any genre scores.
The output is of the form UserID|TrackID|Score 

"""

import numpy as np
import heapq as hp

ratingfile='Rankingf1.txt'
outputfile='scores.txt'

fRating=open(ratingfile,'r')
fOut=open(outputfile,'w')
for line in fRating:
        arr_test=line.strip().split('|')
        userID = arr_test[0]
        trackID= arr_test[1]
        track_score= float(arr_test[2])
        album_score = float(arr_test[3])
        artist_score = float(arr_test[4])
        genre_score = float(arr_test[5])
        user_rating=[album_score, artist_score, genre_score]

        if genre_score==0:
            score=float(1.8*album_score+0.8*artist_score)
        else:
            score=float(1.2*album_score+0.6*artist_score+0.3*genre_score)
        
        outStr=str(userID) + '|' + str(trackID)+ '|' + str(score)
        fOut.write(outStr + '\n')
        

fRating.close()
fOut.close()