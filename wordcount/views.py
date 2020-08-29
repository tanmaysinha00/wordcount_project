from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.POST['fulltext']
    words = fulltext.split()
    dictionary ={}
    for word in words:
        if word in dictionary:
            dictionary[word]+=1
        else:
            dictionary[word]=1
    sortedcount = sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request, "count.html",{'fulltext':fulltext,'count':len(words),'sorted':sortedcount})
def about(request):
    return render(request,"about.html")