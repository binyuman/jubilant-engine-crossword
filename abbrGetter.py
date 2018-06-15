#BAKER

import urllib2
from HTMLParser import HTMLParser


class myParser(HTMLParser) : #customizing Python's built in parser, it essentially just adds all suggestions to list

    def __init__(self) :
        HTMLParser.__init__(self)
        self.words = []
        self.inTag = False

    def handle_starttag(self, tag, attrs):

        if tag == "a" :

            for key, value in attrs :

                if key == "href" and "term" in value :

                    self.inTag = True

        else :

            self.inTag = False

    def handle_data(self, data) :

        if self.inTag :

            self.words.append(data)



def requestMaker(word) :

    newword = ""
    for char in word :

        if char == " " and newword[len(newword) - 1] == " " :

            pass

        else :

            newword = newword + char


    newword = newword.replace(" ", "%20")
    url = "https://www.abbreviations.com/abbreviation/" + newword

    req = urllib2.Request(url, None)
    html = urllib2.urlopen(req).read()
    return html


def clean(lof) :

    new = []
    for item in lof :

        if len(item) < 5 :

            new.append(item)

    return list(set(new))

def use(word): #WORKS - PROVIDES SUGGESTED ABBREVIATIONS FOR WORDS

    parser = myParser()
    parser.feed(requestMaker(word))
    print clean(parser.words)

use("National Basketball Association")

