# RenameFilesInsideFolders
Simple python script to rename the pattern of names in files to the new pattern recursively.

To use the script, copy the script into the folder you want to rename the files in. Incase if I want to rename all the files in a folder called "Temp" and it's subfolders, I would place this script inside "Temp".

Usage : ```python3 renameFiles.py "pattern1" "pattern2"```

pattern1 here denotes the pattern in the file name that you want to replace
pattern2 denotes the pattern you want to replace pattern1 with

Example usage: ```python3 renameFiles.py "-" ""```

The above command removed the "-" from the all the filenames in the given folder and subfolders

# PS: Be careful while you run the script. Changes can be permanent and cannot be recovered.
