# In Python 3.5

from urllib import request, parse

def read_text():
    quotes = open(r"C:\Users\Suvro\OneDrive\Suvro Banerjee_Personal\Profession\Udacity\Nanodegree\Full Stack Web Developer Nanodegree\Codes\movie_quotes.txt") # raw path
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    url = "http://www.wdylike.appspot.com/?q="
    url = url + parse.quote(text_to_check)
    connection = request.urlopen(url) # it opens the url and check for that text if it's profane or not
    output = connection.read()  # read the output
    print(output)
    connection.close()  # closing the connection
    if b"true" in output:
        print("Profanity Alert!!")
    elif b"false" in output:
        print("This document has no curse words")
    else:
        print("Could not scan the document properly")

read_text()

# In Python 2.x

##import urllib
##
##def read_text():
##    quotes = open('movie_quotes.txt') # raw path
##    contents_of_file = quotes.read()
##    quotes.close()
##    check_profanity(contents_of_file)
##
##def check_profanity(text_to_check):
##    url = "http://www.wdylike.appspot.com/?q="
##    #url = url + urllib.parse.quote(text_to_check)
##    connection = urllib.urlopen(url+text_to_check) # it opens the url and check for that text if it's profane or not
##    output = connection.read()  # read the output
##    print(output)
##    connection.close()  # closing the connection
##    if "true" in output:
##        print("Profanity Alert!!")
##    elif "false" in output:
##        print("This document has no curse words")
##    else:
##        print("Could not scan the document properly")
##
##read_text()
