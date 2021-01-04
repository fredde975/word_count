import operator

from django.http import HttpRequest
from django.shortcuts import render


def home(request: HttpRequest):
    return render(request, 'home.html', {'me': 'This is me'})


def count(request: HttpRequest):
    text: str = request.GET['fulltext']
    words = text.split(sep=' ')
    word_count = {}

    for word in words:
        if word not in word_count.keys():
            word_count[word] = 1
        else:
            word_count[word] += 1

    template_dict = {
        'number_of_words': len(words),
        'text': text,
        'word_count': sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
    }

    return render(request, 'count.html', template_dict )


def about(request:HttpRequest):
    about_text = "Fredde made this page"

    return render(request, 'about.html', {'text':about_text} )