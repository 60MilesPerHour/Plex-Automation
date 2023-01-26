# get the name of all movies in a directory and store them in a md file 

import os
import sys

# ask if movies or shows or audiobooks
media_type = input("What type of media are you scanning? (movies, shows, audiobooks, music, All?): ")

if media_type == "movies":
    file = open("/home/USER/Documents/Plex-Movies.md", "w")
    
    #get list of directories and go line by line thru movies.txt
    with open("Movies.txt") as f:
        for line in f:
            # open the directory
            directory = line.strip()
            # get the name of all the files in the directory
            files = os.listdir(directory)
            # write the name of the files to the file
            for file_name in files:
                file.write(file_name + "\n")

elif media_type == "shows":
    file = open("/home/USER/Documents/Plex-Shows.md", "w")
    
    #get list of directories and go line by line thru movies.txt
    with open("Shows.txt") as f:
        for line in f:
            # open the directory
            directory = line.strip()
            # get the name of all the files in the directory
            files = os.listdir(directory)
            # write the name of the files to the file
            for file_name in files:
                file.write(file_name + "\n")

elif media_type == "audiobooks":
    file = open("/home/USER/Documents/Plex-Audiobooks.md", "w")
    
    #get list of directories and go line by line thru movies.txt
    with open("Audiobooks.txt") as f:
        for line in f:
            # open the directory
            directory = line.strip()
            # get the name of all the files in the directory
            files = os.listdir(directory)
            # write the name of the files to the file
            for file_name in files:
                file.write(file_name + "\n")

elif media_type == "music":
    file = open("/home/USER/Desktop/Plex-Music.md", "w")
    
    #get list of directories and go line by line thru movies.txt
    with open("Music.txt") as f:
        for line in f:
            # open the directory
            directory = line.strip()
            # get the name of all the files in the directory
            files = os.listdir(directory)
            # write the name of the files to the file
            for file_name in files:
                file.write(file_name + "\n")

file.close()
