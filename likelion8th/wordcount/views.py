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
    
    word_dictionary = sorted(word_dictionary.items(), key = lambda t: (-t[1],t[0]))

    word_count_dictionary = {}

    for i in word_dictionary:
        try:
            word_count_dictionary[i[1]].append(i[0])
        except:
            word_count_dictionary[i[1]] = [i[0]]

    
    word_count_dictionary = [[i,sorted(j)] for i,j in word_count_dictionary.items()]
    
    
    return render(request, 'result.html', {'text':text,'word_count_dictionary': word_count_dictionary})