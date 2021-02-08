from django.shortcuts import render
from newsapi import NewsApiClient
from django.http import HttpResponse
# Create your views here.

def index(request):
    newsapi = NewsApiClient(api_key = "333af33427f74d19b8bbdf4354fbbf2b")
    headlines = newsapi.get_top_headlines(sources='cnn , ign , bloomberg  , abc-news' )
    articles = headlines['articles']
    news = []
    desc = []
    img = []
    author = []
    url = []
    content = []
    date =[]
    for i in range(len(articles)):
        article = articles[i]
        desc.append(article["description"])
        news.append(article["title"])
        img.append(article['urlToImage'])
        author.append(article['author'])
        url.append(article['url'])
        content.append(article['content'])
        date.append(article['publishedAt'])

    mylist = zip(news , desc , img , author , url , content , date)
    return render(request , 'index.html' , context={"mylist":mylist})