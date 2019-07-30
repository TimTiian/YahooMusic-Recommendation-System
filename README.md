# YahooMusic-Recommendation-System
Kaggle Competition: https://www.kaggle.com/c/ee627A-Spring2019/leaderboard 
2nd place - Team HRM

# Overview
![Alt Text](https://github.com/barbeque-sauce/YahooMusic-Recommendation-System/blob/master/yahoo.png)

## The Data
* trainItem2.txt - the training set
* testItem2.txt - the test set
* trackData2.txt -- Track information formatted as: TrackId|AlbumId|ArtistId|Optional GenreId_1|...|Optional GenreId_k
* albumData2.txt -- Album information formatted as: AlbumId|ArtistId|Optional GenreId_1|...|Optional GenreId_k
* artistData2.txt -- Artist listing formatted as: ArtistId
* genreData2.txt -- Genre listing formatted as: GenreId
* testTrack_hierarchy.txt -- UserID|TrackID|Album|Artist|Genre1|Genre2|…
* Each user has 6 tracks that are assigned in the dataset; which have to be recommended/ not recommended to that user. 

## Usage
All outputs are of the form:

![Alt Text](https://github.com/barbeque-sauce/YahooMusic-Recommendation-System/blob/master/prediction.png)


### Download the project
* Create a new folder, cd to it and run the command:
* git clone https://github.com/barbeque-sauce/YahooMusic-Recommendation-System.git
 
 
### Run the code 

#### For Linear Regression(first 3 programs in Code folder)
* Go to the 'Data' directory and move all files into the 'Code' directory.
* Run Code 1,2 and 3 one by one. Each program will produce a new file.
* The output of Program 3 is the list of recommended/not recommended tracks.
  
#### For Matrix Factorization
  * Open a Jupyter Notebook and open Program 4 in 'Code'.
  * Run it, providing the paths to 'trainItem2.txt' and 'testItem.txt'; which are in the 'Data' folder.
  * The program will output the recommendations in a txt file.

#### For Ensemble(Merging all the predictions to get a new one) 
  * Copy the ensemble_scores into the 'Code' directory.
  * Run the code and get the new recommendation txt file.
  
  
  
  
 
