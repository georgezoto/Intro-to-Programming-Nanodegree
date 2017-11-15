import urllib

def read_text():
    quotes  = open('movie_quotes.txt')
    content = quotes.read()
    print content
    quotes.close()
    if check_profanity(content):
        print 'Alert!'
    else:
        print 'Clean document.'

def check_profanity(text):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=' + text)
    output = connection.read()
    print output
    connection.close()

read_text()
