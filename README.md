# File-Searching
Searching for files in Python

First, the program reads a line of input that specifies which files are eligible to be found.
        The letter D, followed by a space, followed (on the rest of the line) by the path to a directory. In this case, all of the files in that directory will be under consideration, but no subdirectories (and no files in those subdirectories) will be. (You can think of the letter D here as standing for "directory.")
        The letter R, followed by a space, followed (on the rest of the line) by the path to a directory. In this case, all of the files in that directory will be under consideration, along with all of the files in its subdirectories, all of the files in their subdirectories, and so on. (You can think of the letter R here as standing for "recursive.")
        If this line of input does not follow this format, or if the directory specified does not exist, print the word ERROR on a line by itself and repeat reading this line of input; continue until the input is valid.
    
Next, the program prints the paths to every file that is under consideration. Each path is printed on its own line, with no whitespace preceding or following it, and with every line ending in a newline. Note, also, that the order in which the files' paths are printed is relevant; you must print them in the following order:
        First, the paths to all of the files in the directory are printed. These are printed in lexicographical order of the file's names. (More on lexicographical order a bit later, but note that this is the default way that strings are sorted.)
        Next, if the files in subdirectories are being considered, the files in each of the subdirectories are printed according to the same ordering rules here, with all of the files in one subdirectory printed before any of the others, and with the subdirectories printed in lexicographical order of their names.
    
The program now reads a line of input that describes the search characteristics that will be used to decide whether files are "interesting" and should have action taken on them. There are five different characteristics, and this line of input chooses one of them.
        If this line of input is the letter A alone on a line, all of the files found in the previous step are considered interesting.
        If this line of input begins with the letter N, the search will be for files whose names exactly match a particular name. The N will be followed by a space; after the space, the rest of the line will indicate the name of the files to be searched for.
            Note that filenames include extensions, so a search for boo would not find a file named boo.doc.
        If this line of input begins with the letter E, the search will be for files whose names have a particular extension. The E will be followed by a space; after the space, the rest of the line will indicate the desired extension.
            For example, if the desired extension is py, all files whose names end in .py will be considered interesting. The desired extension may be specified with or without a dot preceding it (e.g., E .py or E py would mean the same thing in the input), and your search should behave the same either way.
            Note, also, that there is a difference between what you might call a name ending and an extension. In our program, if the search is looking for files with the extension oc, a file named iliveinthe.oc would be found, but a file named invoice.doc would not.
        If this line of input begins with the letter T, the search will be for text files that contain the given text. The T will be followed by a space; after the space, the rest of the line will indicate the text that the file should contain in order to be considered interesting.
            For example, if this line of input reads T while True, any text file containing the text "while True" would be considered interesting.
            One thing to note is that not all files are text files, but that you can't determine that by their name or their extension. Any file that can be opened and read as a text file is considered a text file for our purposes here, regardless of its name. Any file that cannot be opened and read as a text file should be skipped (i.e., it is not considered interesting).
        If this line of input begins with the character <, the search will be for files whose size, measured in bytes, is less than a specified threshold. The < will be followed by a space; after the space, the rest of the line will be a non-negative integer value specifying the size threshold.
            For example, the input < 65536 means that files whose sizes are no more than 65,535 bytes (i.e., less than 65,536 bytes) will be considered interesting.
        If this line of input begins with the character >, the search will be for files whose size, measured in bytes, is greater than a specified threshold. The > will be followed by a space; after the space, the rest of the line will be a non-negative integer value specifying the size threshold.
            For example, the input > 2097151 means that files whose sizes are at least 2,097,152 bytes (i.e., greater than 2,097,151 bytes) will be considered interesting.
        If this line of input does not match one of the formats described above, print the word ERROR on a line by itself and repeat reading a line of input; continue until the input is valid. Note that it is not an error to specify a search characteristic that matches no files; it's only an error if this line of input is structurally invalid (i.e., it does not match one of the formats above).
    
  Next, the program prints the paths to every file that is considered interesting, based on the search characteristic. Each path is printed on its own line, with no whitespace preceding or following it, and with every line ending in a newline. The paths should be printed using the same ordering rules as the last time you printed them (i.e., lexicographical ordering, as described above), though, of course, you will likely print fewer this time, since not every file will necessarily meet the search characteristic.
    If there were no interesting files, the program ends; there is no action to take.
  
  The program now reads a line of input that describes the action that will be taken on each interesting file. There are three different actions, and this line of input chooses one of them.
        If this line of input contains the letter F by itself, print the first line of text from the file if it's a text file; print NOT TEXT if it is not.
        If this line of input contains the letter D by itself, make a duplicate copy of the file and store it in the same directory where the original resides, but the copy should have .dup (short for "duplicate") appended to its filename. For example, if the interesting file is C:\pictures\boo.jpg, you would copy it to C:\pictures\boo.jpg.dup.
        If this line of input contains the letter T by itself, "touch" the file, which means to modify its last modified timestamp to be the current date/time.
        If this line of input does not match one of the formats described above, print the word ERROR on a line by itself and repeat reading a line of input; continue until the input is valid.
  
  Once an action has been taken on all files, the program ends.
