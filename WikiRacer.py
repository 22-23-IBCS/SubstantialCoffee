import urllib
from urllib.error import HTTPError
from urllib.request import urlopen
import json


def fetch(url: str):
    try:
        response = urlopen("https://en.wikipedia.org/w/rest.php/v1/page/" + url)

        return json.loads(response.read())
    except HTTPError:
        return None


def getLinks(wikiEndpoint: str):
    data = str(fetch(wikiEndpoint))

    links = []
    saving = False

    currentString = ""

    i = 0
    while i < len(data) - 1:
        if data[i] == '[' and data[i + 1] == '[':
            saving = True
            i += 2
            continue
        if data[i] == ']' and data[i + 1] == ']':
            saving = False

            currentString = currentString.split("|")[0]
            currentString = currentString.replace(" ", "_")

            links.append(currentString)
            currentString = ""
        if saving:
            currentString += data[i]
        i += 1

    return links


def getPath(startingPage: str, endingPage: str):
    adjacent = getLinks(startingPage)

    for page in adjacent:
        if page.lower() == endingPage.lower():
            return [startingPage, endingPage]

    i = 0
    while True:

        i += 1



def main():
    startingPage = "Earth"
    endingPage = "astronomical_object"

    print(getPath(startingPage, endingPage))
    # a = [1,2,3,4]
    # for i in range(len(a)):
    #     a.append(a[0]**2)
    #     a.pop(0)
    # print(a)

if __name__ == "__main__":
    main()
