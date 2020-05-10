from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    for word in words:
        try:
            word_dictionary[word]+=1
        except:
            word_dictionary[word]=1
    
    return render(request, 'result.html', {'text':text,'word_dictionary': word_dictionary.items()})