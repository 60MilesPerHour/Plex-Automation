
# Plex-Automation
A simple Python script that automates the process of logging all of the files in your Plex media collection.

## Requirements
- SSHFS to be installed and configured to mount your Plex drives
- Directories to be written in the script's directory

## Usage
1. Clone the repository to your local machine
2. Install the necessary dependencies
3. Run the script and the log file will be created in the user's home directory

The script goes through each directory in your Plex collection and copies the names of all the files into a text file. This allows for easy management of your entire collection without having to manually navigate through each drive.

## Note
This script is intended for Plex users with many drives and wants to know about their entire collection without having to go in and manage it themselves.
