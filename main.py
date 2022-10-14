import requests
from bs4 import BeautifulSoup


# source code of main domain page organized by HTML tags<>
def CreateSoup(URL: str):
    Soup = BeautifulSoup(requests.get(URL).text, 'html.parser')
    return Soup


# URL --> List
# This Function gathers all the links embedded in html anchor tags<a> in URL page source into a list: Links
def HrefFinder(Soup: BeautifulSoup):
    Links = []
    AnchorTags = Soup.find_all('a')
    for i in AnchorTags:
        if i.has_attr('href'):
            Links.append(i['href'])
    return Links


# List --> List
# This function gathers all links from list Links, and parses out only the accessible links to the requested
# domain and stores them inside list FilteredLinks, i.e. no instagram references or photo links
def CleanList(Links):
    FilteredLinks = []
    for i in Links:
        if URL == i[0:len(URL)] or URLshort == i[0:len(URLshort)]:
            FilteredLinks.append(i)
        elif "/" == i[0:1]:
            FilteredLinks.append(URL + i)
    return list(dict.fromkeys(FilteredLinks))


# String --> String(s)
# This function accepts source code as a giant string and finds all instances of "@" and prints out
# the associated text to display possible email addresses
def FindEmails(page_source: str):
    # string = " "
    # a = 20
    for i in range(len(page_source)):
        if page_source[i] == '@':
            if page_source[i + 1].isalpha():
                if page_source[i - 1].isalnum():
                    # while a > -21:
                    #     string = string + page_source[i-a]
                    #     a -= 1
                    # print(string)

                    print(page_source[i - 19] + page_source[i - 18]
                          + page_source[i - 17] + page_source[i - 16] + page_source[i - 15]
                          + page_source[i - 14] + page_source[i - 13] + page_source[i - 12]
                          + page_source[i - 11] + page_source[i - 10] + page_source[i - 9]
                          + page_source[i - 8] + page_source[i - 7] + page_source[i - 6]
                          + page_source[i - 5] + page_source[i - 4] + page_source[i - 3]
                          + page_source[i - 2] + page_source[i - 1] + page_source[i]
                          + page_source[i + 1] + page_source[i + 2] + page_source[i + 3]
                          + page_source[i + 4] + page_source[i + 5] + page_source[i + 6]
                          + page_source[i + 7] + page_source[i + 8] + page_source[i + 9]
                          + page_source[i + 10] + page_source[i + 11] + page_source[i + 12]
                          + page_source[i + 13] + page_source[i + 14] + page_source[i + 15]
                          + page_source[i + 16] + page_source[i + 17] + page_source[i + 18]
                          + page_source[i + 19])


# List --> String(s)
# This function takes the list FilteredLinks and requests the source code of each link and
# converts the source codes into giant strings and feeds them to FindEmails()
def SourceCodes(FilteredLinks):
    for i in FilteredLinks:
        print(i)
        FindEmails(requests.get(i).text)
        print('\n')


while True:
    try:
        URL = input("Please insert a URL in the exact form of \"https://www.example.xyz\" for accurate results ")
        requests.get(URL)
        URLshort = "https://" + URL[12:len(URL)]
        SourceCodes(CleanList(HrefFinder(CreateSoup(URL))))
    except requests.exceptions.RequestException as e:
        print("This link is unreachable for some reason, try again")
        continue
    break

