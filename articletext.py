from bs4 import BeautifulSoup
import gethtml

def getArticleText(webtext):
    articleText = ''
    soup = BeautifulSoup(webtext)
    for tag in soup.findAll('p', attrs={'itemprop':'articleBody'}):
        articleText += tag.contents[0]
    return articleText

def getArticle(url):
    htmlText = gethtml.getHtmlText(url)
    return getArticleText(htmlText)

def getKeywords(articleText):
    word_dict = {}
    word_list = articleText.lower().split()
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        if word in word_dict:
            word_dict[word] += 1
    return word_dict

