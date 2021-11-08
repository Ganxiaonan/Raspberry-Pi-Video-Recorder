# Python 3
import time
import os
from glob import glob, iglob
from pathlib import Path
import glob
import datetime 
from datetime import datetime
import sys


# Directory validation function
def valid_dir(dir):
    #Checking if the path exists or not
    if not os.path.exists(dir):

        #Get current directory where the script has been executed
        cwd = os.getcwd()

        #Create .txt file for log
        f = open(cwd+"/log_createdAt_"+str(datetime.now().timestamp())+".txt",'w')

        #Write in the .txt file
        f.write("* Script execution started at : " + str(currentDate) +"\n"+"\n")
        f.write("This is not a valid path!"+"\n"+"\n")
        f.write("* Script execution stopped at : " + str(currentDate) +"\n"+"\n")
        print("Please provide valid path ")

        #exit
        sys.exit(1)

    #Checking if it is directory or not
    if not os.path.isdir(dir):

        #Get current directory where the script has been executed
        cwd = os.getcwd()

        #Create .txt file for log
        f = open(cwd+"/log_createdAt_"+str(datetime.now().timestamp())+".txt",'w')

        #Write in the .txt file
        f.write("* Script execution started at : " + str(currentDate) +"\n"+"\n")
        f.write("This is not a valid directory path!"+"\n"+"\n")
        f.write("* Script execution stopped at : " + str(currentDate) +"\n"+"\n")
        print("Please provide directory path ")

        #exit
        sys.exit(2)

# Function to convert list into string 
def listToString(s): 

    # initialize an empty string
    str1 = " , " 

    # return string  
    return (str1.join(s))

# Function to list all files and folders recursively inside a directory 
def search_filesNFolders(root_dir,log_dir,limit_day=14):

    #Current date
    currentDate = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    
    #Date to compare with file modification date
    compareDate = datetime.today()

    #Iteration integer
    i = 0

    #Create .txt file for log
    f = open(log_dir+"/log_createdAt_"+str(datetime.now().timestamp())+".txt",'w')

    f.write("* Script execution started at : " + str(currentDate) +"\n"+"\n")
    f.write("* Script execution Directory : " + root_dir +"\n")
    f.write("* Log file Directory : " + log_dir+"\n"+"\n")

    f.write("* Date to check with how older the file is : " + str(compareDate)+"\n"+"\n")

    #Loop to search all files and folders in the given directory recursively
    for currentpath, folders, files in os.walk(root_dir):

        #currentpath.replace('\','/')
        f.write("* Current path : "+ currentpath)
        f.write("\n")
        #currentpath.replace('\','/')

        #Iteration integer
        i = 0
        i = i+1

        #Check whether there are any folders in each path or not i.e length of folders list
        #Here there are no folders inside the current directory
        if(len(folders) == 0):

            #Writing the number of files and folders in the log file
            f.write("   Number of Folders : 0"+"\n")
            f.write("   Number of Files: " + str(len(files))+"\n")

            #Check whether there are any files in each folders in the same directory or not i.e length of files list
            if(len(files)==0):

                #Delete the subfolder as it is empty, No files and No folders inside
                os.rmdir(currentpath)

                f.write("   Note: This empty directory has been deleted!"+"\n")
            else:
                f.write("   Filenames: "+"\n")
            print("Folders : 0")

        #Here there are subfolders inside the current directory
        else:
            f.write("   Number of Folders: " + str(len(folders))+"\n")
            f.write("   Foldernames: " + listToString(folders)+"\n")
            f.write("   Number of Files: " + str(len(files))+"\n")

            #If there are files inside the current directory 
            if(len(files)!=0):
                f.write("   Filenames: "+"\n")

            print(folders)

        #Loop to get the metadata and check each file inside current directory
        for file in files:

            #Get the modification time of each file
            t = os.stat(os.path.join(currentpath,file))[8]

            #Check how older the file is from compareDate
            filetime = datetime.fromtimestamp(t) - compareDate
            print(filetime.days)

            #Log the record of file modification date time
            f.write("       "+str(i)+". "+file +"\n"+"          Modifiction date :"+str(datetime.fromtimestamp(t))+"\n"+"          File path : " +currentpath+"/"+file+ "\n")

            i = i+1

            #Check if file is older than 1 day
            if filetime.days < -limit_day:

                #Remove the file
                os.remove(currentpath+"/"+file)

                #Write the delete status in log file
                f.write("       Note: This file has been deleted!"+"\n"+"\n")
                print('Deleted')
            else:
                print(f'Not older than {limit_day} day!')
            print(file)

        f.write("\n"+"\n")

    #Execution stopped time recorded in log file
    f.write("* Script execution stopped at : " + str(datetime.today().strftime("%Y-%m-%d %H:%M:%S")) +"\n"+"\n")

def delete_old_files(root_dir,log_dir,limit_day):

    #Calling the function to validate the root directory
    valid_dir(root_dir)

    #Calling the function to validate the log file directory
    valid_dir(log_dir)

    #Calling the function to search files and folders, delete the older files and empty folders and keep record in log file. 
    search_filesNFolders(root_dir,log_dir,limit_day=14)

if __name__=="__main__":

    #Define the directory where you want to run this script
    #root_dir = 'C:/Users/Zeaul.Shuvo/Music/Test'
    root_dir = r"C:\Users\ASUSuser\PiRecorder"


    #Define the directory where you want to log the records
    #log_dir = 'C:/Users/Zeaul.Shuvo/Music'
    log_dir = r"C:\Users\ASUSuser\PiRecorder\logfiles"

    # folder/file created before limit_day will be removed
    limit_day = 14

    #Current date
    currentDate = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    #Calling the function to validate the root directory
    valid_dir(root_dir)

    #Calling the function to validate the log file directory
    valid_dir(log_dir)

    #Calling the function to search files and folders, delete the older files and empty folders and keep record in log file. 
    search_filesNFolders(root_dir,log_dir,limit_day=14)

    #exit
    sys.exit(4)