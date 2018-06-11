#BAKER
#API FOR DICTIONARY WEBSITE

from HTMLParser import HTMLParser
import urllib2


class myParser(HTMLParser) : #customizing Python's built in parser, it essentially just adds all links to list


    def __init__(self) :
        HTMLParser.__init__(self)
        self.words = []

    def handle_starttag(self, tag, attrs):

        if tag == 'a' :

            for key, value in attrs :

                if key == 'href' :

                    self.words.append(value)


def requestMaker(letters) : #generates request url to website, finds most common words

    url = "https://www.onelook.com/?w="

    for letter in letters :

        if ord(letter) == 63 :

            url += "%3F"

        else :

            url += letter


    url += "&ssbp=1"

    req = urllib2.Request(url, None)
    html = urllib2.urlopen(req).read()
    return html


def clean(parser, length) : #receives list from parser and produces only the results i want
                           #simplified, but keeping old helper methods just in case

    sug = parser.words
    corrected = []
    phrase = "/?w="

    for opt in sug :

        if phrase in opt :

            prod = opt.split("=")
            if len(prod[1]) == length and noContain(prod[1]) :

                corrected.append(prod[1])

    return corrected

def noContain(phrase) : #MAKES SURE DOESNT CONTAIN NON ALPHABET CHARACHTERS

    phrase = phrase.lower()

    for letter in phrase :

        if ord(letter) < 97 or ord(letter) > 122 :

            return False

    return True



def use(letters) :

    #working function - you put in a part of a word and the rest with q marks.
    #eg i want words starting with l and ending with e that are 4 characters long
    #usage : use("l??e")

    parser = myParser()
    parser.feed(requestMaker(letters))
    return clean(parser, len(letters))





#OLD FUNCTIONS THAT MIGHT BE USEFUL BUT PROB NOT
def countQMarks(letters) : #counts question marks in phrase (thats how the dictionary works) for splitting

    count = 0
    for let in letters :

        if ord(let) == 63 :

            count +=1

    return count

def checkMultiplePlaces(letters) : #calculates how many sets of question marks exist

    IN = False
    count = 0

    for index in range(0, len(letters)) :

        if ord(letters[index]) == 63:

            IN = True

        else :

            if IN :
                count += 1

            IN = False

    if IN :

        count += 1

    return count


def decider(letters) : #only usefull when there is only one sequence of question marks

    prod = letters.split("?", countQMarks(letters))

    if len(prod[0]) > len(prod[1]) :

        return prod[0]

    return prod[1]
