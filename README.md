# file-searching
Searching for files in Python

First line of input:
   a. D path -> only files in directory (no subdirectories)
   b. R path -> "recursive" search

   If not in this format or directory does not exist, prints ERROR and asks for input until input is valid

Program prints paths to every file under consideration. Each path is printed on its own line, with no whitespace preceding or following it.

Second line of input:
   a. A -> all previous files
   b. N name -> files with a particular name
   c. E extension -> files with a particular extension (with or without dot in extension)
   d. T text -> files with the particular text
   e. < size -> files smaller than a particular size (in bytes)
   d. > size -> files larger than a particular size (in bytes)

   If input does not match this, prints ERROR and asks for input until input is valid.

Program prints paths to every file under consideration. Each path is printed on its own line, with no whitespace preceding or following it. If no files, program ends.

Else, third line of input:
   a. F -> first line of text from the file if it is a text file or NOT TEXT if the file is not a text file
   b. D -> duplicate file and store it in the same directory as the original with the duplicate having .dup
   c. T -> touch the file (modify file last modified timestamp to be the current date/time).
    
   If input does not match this, prints ERROR and asks for input until input is valid.
    
Program ends
