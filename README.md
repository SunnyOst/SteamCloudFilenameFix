# SteamCloudFilenameFix
Downloading save files from Steam Cloud automatically inserts the full relative path to each file into it's name, separated by underscores.
This script uses the names to create an actual folder structure with correctly named files.

1. Download all the files you want from Steam Cloud via https://store.steampowered.com/account/remotestorageapp
  Different games can have overlapping folder structures, best to do one game at a time with a clean-up and reset in-between.
  
  !!!IMPORTANT!!!
  Use the "filename" column on the Steam Cloud website to isolate any files that contain UNDERSCORES ( _ ) in the correct path or name.
  This script CANNOT distinguish "underscores that are part of a file/folder name" from "underscores that are used to indicate separate folder/file names in the path".
  EVERY underscore in the name of any file in source directory will be treated as a separator between parts of the path.
  IE "backup_001.txt" will be treated as "backup/001.txt" and will result in a file "001.txt" inside a folder "backup".
  You may choose to rename and move incompatible files manually or modify this script to accomodate your specific situation.

2. Place the compatible files in a single folder.
3. Open the script in an editor to read the important part again and double-check.
4. Set the paths to directories you wish to use as a source and destination(optional) inside the script.
5. I am not responsible for any kind of data loss or other issues that could arise from using this script. Use at your own risk: Save and run.
6. The files should be renamed correctly and placed inside the folders according to the path written in their names.
