# content-extractor

A Python-based web content extractor that downloads, cleans, and processes HTML webpages using multiple libraries to remove boilerplate and retain only main readable text.

<br />

# Project Overview

This program is an improved version of the CS432: Web Science – Homework 2, Question 1 content extraction implementation originally created by Prof. Nasreen Arif at Old Dominion University. It was enhanced to provide better automation, error handling, and data cleaning while maintaining the core goals of the original assignment. The script reads a file containing a list of webpage links, downloads each page using the requests library, and saves them using MD5 hash-based filenames for organization. It then removes unnecessary or invalid content, fixes nested HTML elements with BeautifulSoup4, and applies the BoilerPy3 library to extract the readable text body from each page. By separating raw and processed files, generating a KeyMap.txt for reference, and deleting malformed or empty pages, this improved version produces a cleaner, more reliable dataset ready for web analysis and ranking tasks.

## Original Assignment Requirements

* Use the requests library to download the HTML webpages.
* Access content using the text property.
* Save each page in a uniquely named file using the hashlib library.
* Create a file to act as a key for all of the hash pairs.
* Use BoilerPy3 library to remove HTML boilerplate.
* Keep the raw and processed files in seperate folders.


## Added Improvments

* User now enters the file containing HTML links to extract content from as a command-line argument.
* Automatically verifies file existence before processing.
* Creates Raw HTML Files and Processed Files directories automatically if not present.
* Implements exception handling for UnicodeDecodeError and requests.RequestException.
* Deletes malformed, XML/XHTML, or empty files to improve dataset quality.
* Fixes nested href tag errors to avoid parser crashes.
* Prints detailed progress and status messages throughout execution.


<br />

# Getting Started
## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have a Windows/Linux/MacOS system with Python installed
* You have installed the required libraries with: 

          pip install requests beautifulsoup4 boilerpy3


## Installing

* To install this program, clone or download this repository:

        git clone https://github.com/emxily/content-extractor.git

* Then, navigate into the project directory:

        cd content-extractor


## Executing program

* To run the program from the terminal:

        py.exe content-extractor.py <link_list_file>



### <u>Example Output</u>
``` ```
```

```


<br />


# Future Updates

* This program is currently written as a single main script; I plan to refactor it into custom functions for better readability, reusability, and testing in a future version.


<br \>


# Version History

* 0.1
    * Initial Release

*This program was tested and developed on Windows 10+ using Python 3.13.9*


<br />


# Authors

**Author:** Emily Nowak

*Based on ... **Homework 2 - Ranking Webpages** by **Prof. Nasreen Arif** for CS:432 Web Science, at Old Dominion University* 


<br />


# Acknowledgments

### Original Assignment
[Homework 2 - Ranking Webpages - Question 1](https://github.com/emxily/content-extractor/blob/578cd81dd377340e433a4761702072caf881708d/original-assignment-instructions.md)

### References
* Markdown Syntax: https://www.markdownguide.org/basic-syntax/#headings
* HTML Syntax: https://www.w3schools.com/tags
* Python Beautiful Soup Documentation: <https://www.crummy.com/software/BeautifulSoup/bs4/doc>
* Regex: <https://regex101.com/>
* Python Dictionary Documentation: <https://www.w3schools.com/python/python_dictionaries.asp>
* Python Hashlib Documentation: <https://docs.python.org/3/library/hashlib.html> 
* Python Boilerpy3 Documentation: <https://pypi.org/project/boilerpy3>
* Python Shutil Documentation: <https://docs.python.org/3/library/shutil.html>


