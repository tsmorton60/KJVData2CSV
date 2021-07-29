## KJVData2CSV
This Python utility will read and parse the included KJV text and export certain data to csv files.

### Requirements
Python 3.7+

### Usage
Simply place both the av1769.htm and extract2csv.py file in a folder and run the .py file. Two csv files will be generated, one with word level data and the other with verse level data. These files can be opened in any spreadsheet program such as Excel or Libre Office.

### Modification
The word data csv output includes each KJV word plus verse reference, word index, number of characters, running total of characters, vowels, and English gematria (based on 6). The verse data csv output includes each verse reference plus number of words, characters, vowels, and gematria.

This script is a basis for a new Python user to modify and output other textual data such as punctuation, capital letters, syllables per word, phrases per verse, word index in chapter, etc. 

### Other Bible Texts
Any Bible text can be used as long as it is one verse per line with a tab seprarating the verse reference from the text. Texts with added data such as Strong's Numbers can be used if the extract2csv.py code is modified to deal with extra the data.
