#BAKER
import urllib2
from HTMLParser import HTMLParser

class myParser(HTMLParser) : #customizing Python's built in parser, it essentially just adds all suggestions to list
                             #works good


    def __init__(self) :
        HTMLParser.__init__(self)
        self.words = []
        self.inSection = False
        self.inLink = False

    def handle_starttag(self, tag, attrs):

        if tag == "div" :

            self.inLink = False

            for key, value in attrs :

                if key == "class" and value == "section NOUN-SECTION" :

                    self.inSection = True

        elif tag == "a" :

            self.inLink = True

        else :

            self.inLink = False

    def handle_data(self, data) :

        if self.inSection and self.inLink :

            self.words.append(data)


    def handle_endtag(self, tag) :

        if tag == "div" and self.inSection :

            self.inSection = False




def requestMaker(word) :



    url = "https://wordassociations.net/en/words-associated-with/" + word

    req = urllib2.Request(url, None)
    html = urllib2.urlopen(req).read()
    return html


def use(word) : #WORKS - GENERATES COMMON ASSOCIATIONS WITH WORD - HELPFUL FOR CLUE MAKING !!!!

    parser = myParser()
    parser.feed(requestMaker(word))
    print parser.words

#USAGE :
use("pig")