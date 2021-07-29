
# Copyright 2021 Tim Morton
# Bible Analyzer Software


# Necessary imports
import codecs, re, string

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generate():

    # Open KJV file that has one verse per line
    avTxt = codecs.open('av1769.htm' , 'r', 'utf-8')
    
    # Convert file object to a list of all 31102 verses
    avList = avTxt.readlines()
    
    # Initialize a list with the first item being the csv headings
    csvWd = ['Reference,Word,Word Index,Characters,Total Characters,Vowels,Gematria (6)']
    
    # Open a file to write the word level output to
    csvwdout = codecs.open('kjv-wddata.csv' , 'w', 'utf-8')
    
    # Do the same for the verse level data
    csvVs = ['Reference,Words,Characters,Vowels,Gematria (6)']
    csvvsout = codecs.open('kjv-vsdata.csv' , 'w', 'utf-8')

    totalWdCnt = 1
    totalCharCnt = 0
    
    # Use a "for loop" to loop over each verse in the kjv list and extract data
    for idx, row in enumerate(avList):
    
        vsData = []
        gemVs = 0
        totalVowels = 0
    
        charsNvs = 0
        
        # Splits each verse line into it reference and verse text. A tab character ('\t') is the delimiter
        ref, vsTxt = row.split('\t')
        #chap, vs = ref.split(':')
        
        # Splits each verse text into a list of words
        wdList = vsTxt.split()
        
        # Work with each word in the list
        for num, wd in enumerate(wdList):
            
            # Remove the italics tags with a regular expression
            wd = re.sub(r'</?i>', r'', wd)
            
            # Remove punctuation at end. Does not remove apostrophes like in "Adam's"
            wd = wd.strip(string.punctuation)
            
            #print (wd)
            wdData = []
            wdVowels = 0
            #wdCon = 0
            
            # Counts characters in word
            char = len(wd)
            
            # Subtract 1 for hyphen in hyphenated word
            if '-' in wd:
                #print(wd)
                char -=1
            
            # Add to running character count
            totalCharCnt += char
            charsNvs += char
            
            gem = 0
            # Work with each character
            for c in wd.lower():
                if c.isalpha():
                
                    # Gets index of character from alpha list
                    cIdx = alpha.index(c)
                    gem += (cIdx +1) * 6
                    
                    # Check if vowel (This is not perfect in dealing with 'y' as a vowel, however 'y' usually is a vowel)
                    if c in ['a','e', 'i', 'o', 'u', 'y']:
                        wdVowels +=1
                    #else:
                    #    wdCon +=1
                    
            # Subtract if word starts with 'y' since it is not a vowel 
            if wd.lower().startswith('y'):
                wdVowels -=1
                        
            gemVs += gem
            totalVowels += wdVowels
            
            # Checks if this is the last word of the verse and adds data to verse level list
            if num == len(wdList) -1:
                wdsNvs = len(wdList)
                vsData.append(ref)
                vsData.append(str(wdsNvs))
                vsData.append(str(charsNvs))
                vsData.append(str(totalVowels))
                vsData.append(str(gemVs))
                
            # Adds data to word level list
            wdData.append(ref)
            wdData.append(wd)
            wdData.append(str(totalWdCnt))
            wdData.append(str(char))
            wdData.append(str(totalCharCnt))
            wdData.append(str(wdVowels))
            wdData.append(str(gem))
            
            totalWdCnt += 1
            
            wdLine = ','.join(wdData)
            csvWd.append(wdLine)
            
            #print(wdLine)
    
        # Combines data in list into a string and appends it to another list
        vsLine = ','.join(vsData)
        csvVs.append(vsLine)
    
    # Combines word data list into a string and writes it to a file
    csvwdout.write('\n'.join(csvWd))
    csvwdout.close()
    
    # Combines verse data list into a string and writes it to a file
    csvvsout.write('\n'.join(csvVs))
    csvvsout.close()

if __name__ == "__main__":
    generate()