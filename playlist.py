import os

playlist = open("playlist.txt", 'w')

path = "/Users/Teck Jun/Desktop/AY21 22/Tri 1/CSC 2005 Human Computer Interaction/github/csc2005-lab02-2021"
for filename in os.listdir(path):

    if filename.endswith(".txt"):
        songname = open(path + '/' + filename, 'r').readline()
        playlist.write(songname)
