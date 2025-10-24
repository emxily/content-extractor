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

* A .txt document containing the URIs you want to extract content from with one URI per line.

## Executing program

* To run the program from the terminal:

        py content-extractor.py testlinks.txt



### <u>Example Output</u>
```py content-extractor.py testlinks.txt```
```
Links Acquired!

Downloading webpages. . .

Saved: https://services.github.com/ as 039473af4d424b6294cb0642b4dbdf55.html
Saved: https://github.com/ as 008ec4453ff31513f43893cba7aa31c8.html
Saved: https://docs.github.com/copilot/managing-copilot/configure-personal-settings/installing-the-github-copilot-extension-in-your-environment as 1c90c8cddf22e72a673d9bb5463153e7.html
Saved: https://github.com/enterprise as ef4bd4b96e95f14a01607838015b86da.html
Saved: https://www.instagram.com/github/ as 2a1b3d9bf2c63920710fb241b341421f.html
Saved: https://github.com/customer-stories?type=enterprise as 8f8052a376f09eec76d566d13af6925b.html
Saved: https://github.com/github as c9df189541785f07c4d2ac331cf9ad46.html
Saved: https://github.blog/open-source/social-impact/ as 970831fb58b9cd98ffc38901a8e7dd62.html
Saved: https://www.youtube.com/playlist?list=PL0lo9MOBetEHEHi9h0k_lPn0XZdEeYZDS as 6e4c1eccbba42d86f0e4439a55e7e588.html
Saved: https://github.blog/news-insights/research/the-state-of-open-source-and-ai/ as 1ccf5df09b90c822a0358f1c183073db.html
Saved: https://github.blog/author/davelosert/ as 09a457c326e21a1e8c4346241d8a5175.html

Download completed!

Extracting data. . .

Deleted https://www.instagram.com/github/: Dataless.
Deleted https://www.youtube.com/playlist?list=PL0lo9MOBetEHEHi9h0k_lPn0XZdEeYZDS: Dataless.

Data Extracted.

9 Processed files.
Data for each page has been extracted and can be found inside the 'Processed Files' directory

```


<br />


# Future Updates

* This program is currently written as a single main script; I plan to refactor it into custom functions for better readability, reusability, and testing in a future version.


<br />


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
* Markdown Syntax: <https://www.markdownguide.org/basic-syntax/#headings>
* HTML Syntax: <https://www.w3schools.com/tags>
* Python Beautiful Soup Documentation: <https://www.crummy.com/software/BeautifulSoup/bs4/doc>
* Regex: <https://regex101.com/>
* Python Dictionary Documentation: <https://www.w3schools.com/python/python_dictionaries.asp>
* Python Hashlib Documentation: <https://docs.python.org/3/library/hashlib.html> 
* Python Boilerpy3 Documentation: <https://pypi.org/project/boilerpy3>
* Python Shutil Documentation: <https://docs.python.org/3/library/shutil.html>


