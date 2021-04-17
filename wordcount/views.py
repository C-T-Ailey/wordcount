from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, "home.html")     #set homepage to return the contents of "home.html"

def count(request):
    fulltext = request.GET["fulltext"]      #request the "fulltext" from home.html and set it to var fulltext

    wordlist = fulltext.split()

    worddict = {}

    for word in wordlist:
        if word in worddict:
            #Increase
            worddict[word] += 1
        else:
            #Add to the dictionary
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html",{"fulltext":fulltext, "count":len(wordlist), "worddict":sortedwords})
"""
    ^allows the count.html file to request the fulltext, len(wordlist) and sortedwords values under the names
    "fulltext", "count" and "worddict".
"""

def about(request):
    return render(request, "about.html")