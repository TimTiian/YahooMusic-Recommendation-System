""" 

Python script to take in the testTrack_hierarchy.txt and the trainItem2.txt files, process them, and produce a new 
file consisting of the 6 tracks to be recommended to a user, along with all the hierarchical ratings that the user
has already given for the track(Album,Artist,Genres). 
The output is of the form UserID|TrackID|TrackScore(always 0.0 intitally)|AlbumScore|ArtistScore|Genre_1Score|..Genre_nScore

"""    

from __future__ import print_function
import time
import sys

OUTPUT_FILE = "Rankingf1.txt"
H_FILE = "testTrack_hierarchy.txt"
TRAIN_FILE = "trainItem2.txt"

user_rate = {}
start_time = time.time()
with open(TRAIN_FILE) as train:
    for line in train:
        if "|" in line:
            cur_user = line.strip("\n").split("|")[0]
            user_rate[cur_user]={}
            continue
        item_id,item_score=line.strip("\n").split()
        user_rate[cur_user][item_id]=item_score                  

with open(OUTPUT_FILE, "w") as output:
    with open(H_FILE) as record:                                  
        for line in record:
            gen_out=""
            user,track=line.strip("\n").split("|")[0],line.strip("\n").split("|")[1]  
            items=line.strip("\n").split("|")[2:]                 
            if len(items)==0:                                     
                
                album_score=0.0
                artist_score=0.0
            if len(items)==1:
               
                album=items[0]
                try:
                    album_score=float(user_rate[user][album])
                except KeyError:
                    album_score=0.0
                artist_score=0.0
            if len(items)==2:
                album = items[0]
                artist = items[1]
                
                try:
                    album_score=float(user_rate[user][album])
                except KeyError:
                    album_score=0.0
                try:
                    artist_score=float(user_rate[user][artist])
                except KeyError:
                    artist_score=0.0
            if len(items)>2:
                try:
                    album_score=float(user_rate[user][items[0]])
                except KeyError:
                    album_score=0.0
                try:
                    artist_score=float(user_rate[user][items[1]])
                except KeyError:
                    artist_score=0.0
                genr=items[2:]
                for g in genr:
                    try:
                        gen_out = gen_out +"|"+ user_rate[user][g]
                    except KeyError:
                        pass
            if gen_out:        
                output.write(user + "|" + track + "|" + str(0.0) + "|" + str(album_score) + "|"+str(artist_score) + str(gen_out) + "\n")
                
            else: 
                output.write(user + "|" + track + "|" + str(0.0) + "|" + str(album_score) + "|"+str(artist_score) + "|" + str(0.0) + "\n")


print("Finished, Spend %.2f s" % (time.time() - start_time))

