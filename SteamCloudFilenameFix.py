import os
import shutil

# !!!!IMPORTANT!!!!
# This script ONLY works correctly when the correct/final names of the files and folders DO NOT contain underscores ( _ )!
# This script interprets EVERY underscore in the name as a slash in the path to the file.
# IE "backup_001.txt" will be treated as "backup/001.txt" and will result in a file "001.txt" inside a folder "backup".
# It is YOUR job to manually go through files and isolate files containing underscores in the name or the path.
# You may rename and move incompatible files manually or modify this script to accomodate your specific situation if you're some sort of a genius. (Simple example function given)

# I am not responsible for any kind of data loss or other issues that could arise from using this script. Use at your own risk!


# SETUP:

# Define the source and destination directories

# Set the path to the folder containing raw files with broken names:
source_dir = "joe mama's source directory"

# If you want to use the same folder as the location of this script, remove the # here:
#source_dir = os.path.dirname(os.path.abspath(__file__))

# Set the path to a folder where you want all the folders and files to end up at! By default, same folder as the source.
dest_dir = source_dir

# Here is a simple function to combat underscores when there is a lot of them present in a consistent manner:
def manualrename(name):
    # Here is an example of how you could remove false positive underscores (remove the #):
    #name = name.replace("joe_mama","joeUNDERSCOREmama")
    # This will reaplce EVERY instance of "joe_mama" with "joeUNDERSCOREmama", including situations where "joe/mama" path would be correct, so double check.
    # You may add as many of these rules as you want inside this function, one per line
    # !IMPORTANT! You will need to find a way to fix the names of these files/folders back to original names - whether manually or via another function! Otherwise, the files might not work correctly!


    # End of function
    return name

# END OF SETUP


# ACTUAL CODE:

# Check if the paths are valid and get a list of files in the source directory

if not os.path.exists(source_dir) or not os.path.isdir(source_dir):
    print("The specified source directory is not a valid folder path.")
    input("Open the script in an editor, read the instructions and make sure all the paths are set correctly!")
    exit()
    
try:
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
except FileNotFoundError:
    print("The specified source path does not exist or does not have any files.")
    input("Open the script in an editor, read the instructions and make sure all the paths are set correctly!")
    exit()
    
if not os.path.exists(dest_dir) or not os.path.isdir(dest_dir):
    print("The specified destination directory is not a valid folder path.")
    input("Open the script in an editor, read the instructions and make sure all the paths are set correctly!")
    exit()
    

# Loop through all files in the source directory
for filename in files:
    # Execute the de-underscorer function to remove potential issues
    newfilename = manualrename(filename)
    
    # If steam has added a special folder before all the other folder names, format it to be the same as others
    if newfilename.startswith("%"):
        newfilename = newfilename.replace("%","",1)
        newfilename = newfilename.replace("%","_",1)
    
    # Separate all the name parts into a list
    path = newfilename.split('_')
    # Get the complete new path to the file
    newpath = os.path.join(dest_dir, *path[0:-1])
    # Create the folder structure if not present
    os.makedirs(newpath, exist_ok=True)
    # Move the file into the new directory and update the name to remove the path
    shutil.move(os.path.join(source_dir, filename), os.path.join(newpath, path[-1]))
    
    print("Moved ",os.path.join(source_dir, filename)," to ",os.path.join(newpath, path[-1]))
    
input("Done!")