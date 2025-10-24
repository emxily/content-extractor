#Libraries
import requests                                                                                                 #Library for sending HTTPS requests
import os                                                                                                       #Library for interacting with the os
import shutil                                                                                                   #Library for file copying and moving
import hashlib                                                                                                  #Library for hashing
import re                                                                                                       #Library for regex 
import sys                                                                                                      #Library for accessing command-line arguments
from bs4 import BeautifulSoup                                                                                   #Library for parsing HTML
from boilerpy3 import extractors                                                                                #Library for boilerplate removal and content extraction


#Run the command py.exe content-extractor.py <link_list_file>


#Start of main
if __name__ == "__main__":

#Variable Declarations
    URIList = set()                                                                                             #Set that contains all URIs that will be downloaded
    KeyMap = {}                                                                                                 #Dictionary that holds the legend to pair hash to URI
    extractor = extractors.ArticleExtractor()                                                                   #Sets up BoilerPy3 to extract main article content from HTML
    RawDirectory = "Raw HTML Files"                                                                             #Variable that holds the name of the directory that contains the raw HTML files
    ProcessedDirectory = "Processed Files"                                                                      #Variable that holds the name of the directory that contains the processed HTML files
    XMLXHTML = re.compile(r'^\s*(<\?xml|<rss|<feed|<sitemapindex|<html\s+xmlns)', re.IGNORECASE)                #Variable that folds the regex pattern for XML and XHTML

#Generate required directories
    os.makedirs(RawDirectory, exist_ok=True)                                                                    #Generates raw files directory
    os.makedirs(ProcessedDirectory, exist_ok=True)                                                              #Generates processed files directory

#Handle command-line argument
    if len(sys.argv) < 2:                                                                                       #Check if user provided a filename as a command-line argument
        print("Usage: py content-extractor.py <link_list_file>")                                                #If not, print correct usage format
        sys.exit(1)                                                                                             #Exit program since no file was provided

    linksFilePath = sys.argv[1].strip().strip('\'"')                                                            #Assign the first command-line argument to 'linksFilePath' and remove any surrounding quotes or extra spaces

#Handle relative paths
    if not os.path.isabs(linksFilePath):                                                                        #If the provided file path is not an absolute path
        script_dir = os.path.dirname(os.path.abspath(__file__))                                                 #Get the directory path where this Python script is located
        linksFilePath = os.path.join(script_dir, linksFilePath)                                                 #Combine the script directory with the given relative path to create a full path

    linksFilePath = os.path.normpath(linksFilePath)                                                             #Normalize the file path to clean up any redundant slashes or dots (e.g., ./ or ../)

#Check if the file exists before continuing
    if not os.path.isfile(linksFilePath):                                                                       #If the file path does not point to an existing file
        print(f"Error: file not found: {linksFilePath}")                                                        #Print an error message showing the invalid file path
        print(f"(cwd={os.getcwd()})")                                                                           #Print the current working directory to help identify where the script is running from
        sys.exit(1)                                                                                             #Exit the program since the file cannot be found or opened

#Grab links from the input file (diagnostic: count and sample)
    with open(linksFilePath, "r", encoding="utf-8-sig") as GrabbedLinksFile:                                    #Open the file; utf-8-sig auto-strips BOM on first line
        for URI in GrabbedLinksFile:                                                                            #Loop through each line of the file
            URI = URI.strip()                                                                                   #Strip whitespace/newlines
            if not URI or URI.startswith("#") or URI.startswith("//"):                                          #Skip blank lines and full-line comments
                continue                                                                                        #Skip this line
            URIList.add(URI)                                                                                    #Add URI to the set (deduplicates automatically)

    print("Links Acquired!")                                                                                    #Print confirmation when done
    print()                                                                                                     #Blank line
    print("Downloading webpages. . .")                                                                          #Print that now starts the downloading process
    print()                                                                                                     #Blank Line

    if len(URIList) == 0:                                                                                       #If no links were loaded, stop early
        print("No links found in the input file. Aborting.")                                                    #Explain why we are stopping
        sys.exit(1)                                                                                             #Exit so later stages don't silently do nothing

#Create unique file names for each URI, then write the page's HTML content to the file and save that file to the raw files directory
    for URI in URIList:                                                                                         #Loop through each URI in the set
        hashedURI = hashlib.md5(URI.encode("utf-8")).hexdigest()                                                #Generate md5 hash of URI
        filename = f"{hashedURI}.html"                                                                          #Name the file after the hash
        RawPath = os.path.join(RawDirectory, filename)                                                          #Create path for file inside raw files dirtectory

        try:                                                                                                    #Try to request the page
            response = requests.get(URI, timeout=10, allow_redirects=True)                                       #Send HTTP GET request
            if response.status_code == 200:                                                                     #If the request succeeded
                try:                                                                                            #Try to write content to the file 
                    with open(RawPath, "w", encoding="utf-8") as RawFile:                                       #Open file to write
                        RawFile.write(response.text)                                                            #Write raw HTML to file
                    KeyMap[hashedURI] = URI                                                                     #Add mapping of hash to URI to the dictionary
                    print(f"Saved: {URI} as {filename}")                                                        #Print confirmation of saved file
                except:                                                                                         #If the writing fails
                    continue                                                                                    #Skip
            else:                                                                                               #If the status code is not 200
                pass                                                                                            #Do nothing
        except requests.RequestException:                                                                       #If the request fails 
            continue                                                                                            #Skip
    print()                                                                                                     #Blank line
    print("Download completed!")                                                                                #Print that the download is done
    print()                                                                                                     #Blank line
    print("Extracting data. . .")                                                                               #Print now data is being extracted
    print()                                                                                                     #Blank line

#Write all URI and hash pairs from the dictionary to a file 
    with open("KeyMap.txt", "w", encoding="utf-8") as KeyFile:                                                  #Open the file that will contain the hash to URI pairs
        KeyFile.write("Hash to URI\n")                                                                          #Write header line
        for hashedURI, URI in KeyMap.items():                                                                   #Loop through each pair
            KeyFile.write(f"{hashedURI} -> {URI}\n")                                                            #Write each pair to the file

#Copy raw HTML Files and move the copies to the Processed Files directory
    for files in os.listdir(RawDirectory):                                                                      #Loop through each file in the raw files directory 
        RawPath = os.path.join(RawDirectory, files)                                                             #Path to raw file
        ProcessedPath = os.path.join(ProcessedDirectory, files)                                                 #Path to the processed files directory
        try:                                                                                                    #Try to copy file
            shutil.copy2(RawPath, ProcessedPath)                                                                #Copy file
        except:                                                                                                 #If copy fails
            continue                                                                                            #Skip

#Clean and extract content of each file 
    for file in os.listdir(ProcessedDirectory):                                                                 #Loop through each file in the processed directory
        ProcessedPath = os.path.join(ProcessedDirectory, file)                                                  #Path to processed file
        fileHash = os.path.splitext(file)[0]                                                                    #Extract hash part of the file name
        fileURI = KeyMap.get(fileHash, "Unknown URI")                                                           #Get original URI
        
#Delete files that trigger UnicodeDecodeError to fix bugs
        try:                                                                                                    #Try to open file
            with open(ProcessedPath, "r", encoding="utf-8") as s:                                               #Open the file
                content = s.read()                                                                              #Read entire content into string
        except UnicodeDecodeError:                                                                              #If decoding  fails
            os.remove(ProcessedPath)                                                                            #Delete file
            print(f"Deleted {fileURI}: UnicodeDecodeError.")                                                    #Print that file was deleted
            continue                                                                                            #Skip

#XML/XHTML is deleted if detected to fix bugs
        if XMLXHTML.match(content):                                                                             #If the file contains XML/XHTML 
            os.remove(ProcessedPath)                                                                            #Delete  file
            print(f"Deleted {fileURI}: XML/XHTML detected.")                                                    #Print that file was deleted
            continue                                                                                            #Skip

#Fix nested links to fix bug                                                                                    
        soup = BeautifulSoup(content, "html.parser")                                                            #Parse content with bs4 using HTML Parser
        for link in soup.find_all("a"):                                                                         #Search each page for <a>
            if link.find("a"):                                                                                  #If it contains nested <a>
                link.name = "span"                                                                              #Change outer <a> to <span>
        cleanedContent = str(soup)                                                                              #Convert back to string
        
#Remove HTML Boilerplate
        try:                                                                                                    #Try to extract content with BoilerPy3
            processedHTML = extractor.get_content(cleanedContent)                                               #Extract main article content from cleaned HTML
        except UnicodeDecodeError:                                                                              #If UnicodeDecodeError occurs
            os.remove(ProcessedPath)                                                                            #Delete file 
            print(f"Deleted {fileURI}: UnicodeDecodeError.")                                                    #Print that file was deleted
            continue                                                                                            #Skip

#Delete empty files
        with open(ProcessedPath,"w", encoding="utf-8") as clean:                                                #Open the processed file for writing
            clean.write((processedHTML or "").strip())                                                          #Write the extracted text and strip empty content
        if os.path.getsize(ProcessedPath) == 0:                                                                 #If the file is 0B after writing
                os.remove(ProcessedPath)                                                                        #Delete  file
                print(f"Deleted {fileURI}: Dataless.")                                                          #Print that file was deleted

#Final messages
    print()                                                                                                     #Blank line
    print("Data Extracted.")                                                                                    #Print that data collection is done
    print()                                                                                                     #Blank Line
    print(f"{len(os.listdir(ProcessedDirectory))} Processed files.")                                            #Print number of files that are left after successful processing
    print("Data for each page has been extracted and can be found inside the 'Processed Files' directory")      #Print final message
    print()                                                                                                     #Blank line
  