#BAKER
#API FOR DICTIONARY WEBSITE

from HTMLParser import HTMLParser
import urllib2


class myParser(HTMLParser) :


    def __init__(self) :
        HTMLParser.__init__(self)
        self.words = []

    def handle_starttag(self, tag, attrs):

        if tag == 'a' :

            for key, value in attrs :

                if key == 'href' :

                    self.words.append(value)


def clean(letters, parser, length) :

    sug = parser.words
    corrected = []
    phrase = "/?w=" + letters

    for opt in sug :

        if phrase in opt :

            prod = opt.split("=")
            if len(prod[1]) == length :

                corrected.append(prod[1])

    return corrected




def requestMaker(letters) :

    url = "https://www.onelook.com/?w="

    for letter in letters :

        if ord(letter) == 63 :

            url += "%3F"

        else :

            url += letter


    url += "&ls=a"

    req = urllib2.Request(url, None)
    html = urllib2.urlopen(req).read()
    return html


def countQMarks(letters) :

    count = 0
    for let in letters :

        if ord(let) == 63 :

            count +=1

    return count

def decider(letters) :

    prod = letters.split("?", countQMarks())

    if len(prod[0]) > len(prod[1]) :

        return prod[0]

    return prod[1]


def use(letters) : #WORKS

    parser = myParser()
    parser.parser.feed(requestMaker(letters))
    return clean(decider(letters), parser, len(letters))




