# file-searching
Installation instructions

1. git clone https://github.com/avanishd-3/file-searching
2. Run file_searching.py

Searching for files in Python

First line of input (choose one):
1. D path -> Prints only files in directory (no subdirectories)
2. R path -> Prints files recursively

If not in this format or directory does not exist, prints ERROR and asks for input until input is valid

Second line of input (choose one):
1. A -> Prinst all previous files
2. N name -> Prints files with a particular name
3. E extension -> Prints files with a particular extension (with or without dot in extension)
4. T text -> Prints files with the particular text
5. < size -> Prints files smaller than a particular size (in bytes)
6. > size -> Prints files larger than a particular size (in bytes)

If input does not match this, prints ERROR and asks for input until input is valid.

If files exist that match the search, third line of input (choose one):
1. F -> Prints first line of text from each file that is a text file or NOT TEXT if the file is not a text file
2. D -> Creates duplicate of each file and store them in the same directory as the originals with the duplicate having .dup
3. T -> Touches each file (modifies the file's last modified timestamp to be the current date/time).
    
If input does not match this, prints ERROR and asks for input until input is valid.
