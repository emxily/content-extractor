# Homework 2 - Ranking Webpages

**Important:** This assignment requires the use of URIs collected in HW1.

### Q1. Data Collection

*For the following tasks, consider which items could be scripted, either with a shell script or with Python.  You may even want to create separate scripts for different tasks.  It's up to you to determine the best way to collect the data.*

Download the HTML content of the 500 unique URIs you gathered in HW1 and strip out HTML tags (called "boilerplate") so that you are left with the main text content of each webpage.  ***Plan ahead because this will take time to complete.***

Note: If you plan completing this question in Windows PowerShell (instead of Linux), you will need to be aware of how PowerShell [uses character encoding for string data](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding?view=powershell-7.1) (see also [Understanding file encoding in VS Code and PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/dev-cross-plat/vscode/understanding-file-encoding?view=powershell-7.1)).

#### Saving the HTML Files

We just want to save the HTML content.  In Python, we can use the [requests library](https://requests.readthedocs.io/en/latest/) to download the webpage. Once the webpage has been successfully requested, the [HTML response content can be accessed using the `text` property](https://requests.readthedocs.io/en/latest/user/quickstart/#response-content).

You'll need to save the HTML content returned from each URI in a uniquely-named file.  The easiest thing is to use the URI itself as the filename, but your shell will likely not like some of the characters that can occur in URIs (e.g., "?", "&").  My suggestion is to hash the URIs to associate them with their respective filename using a [cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function), like MD5.  

For example, https://www.cnn.com/world/live-news/nasa-mars-rover-landing-02-18-21 hashes to `2fc5f9f05c7a69c6d658eb680c7fa6ee`:
```console
$ echo -n "https://www.cnn.com/world/live-news/nasa-mars-rover-landing-02-18-21" | md5sum | awk '{print $1}'
2fc5f9f05c7a69c6d658eb680c7fa6ee
```
Notes:
* `md5sum` might be `md5` on some machines
* note the `-n` option to `echo` -- this removes the trailing newline
* `awk '{print $1}'` at the end prints only the characters before the first space in the output (i.e., the hash) -- *try the command without this to see the difference*

If you want to use Python for this, you can use the [hashlib library](https://docs.python.org/3/library/hashlib.html). Note that you'll want to strip any trailing whitespace or newline characters from the URI (using [`strip()`](https://www.w3schools.com/python/ref_string_strip.asp)) before you compute the MD5 hash.

For later analysis, you will need to map the content back to the original URI, so make sure to save a text file that contains all of the URI to hash mappings.

#### Removing HTML Boilerplate

Now use a tool to remove (most) of the HTML markup from your 500 HTML documents. 

The Python boilerpy3 library will do a fair job at this task.  You can use `pip` to install this Python package in your account on the CS Linux machines.  The [main boilerpy3 webpage](https://pypi.org/project/boilerpy3/) has several examples of its usage.

Keep both files for each URI (i.e., raw HTML and processed), and upload both sets of files to your GitHub repo. Put the raw and processed files in separate folders.  Remember that to upload/commit a large number of files to GitHub, [use the command line](https://docs.github.com/en/github/managing-files-in-a-repository/adding-a-file-to-a-repository-using-the-command-line).

Sometimes boilerpy3 isn't able to extract any useful information from the downloaded HTML (either it's all boilerplate or it's not actually HTML), so it produces no output, resulting in a 0B size file.  You may also run into HTML files that trigger UnicodeDecode exceptions when using boilerpy3.  You can skip files that have  these types of encoding errors, result in 0B output, or contain inappropriate content (whatever you define as such).  The main goal is to have enough processed files so that you can find 10 documents that contain your query term (for Q2 and later).

. . .

# Full Original Assignment
**Title:** Homework 2 - Ranking Webpages

**Author:** Professor Nasreen Arif

[Public Assignment Instructions](https://github.com/odu-cs432-websci/public-fall25/blob/c5036bd62b26b327f8b3ecd0cb6405c75d99dd71/HW2-search.md)

**This assignment was originally from CS432 Web Science, at Old Dominion University**