from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

def index(request):
    my_dict = {
        'insert_something':"ますのは夢の中です",
        'test':"ますのはエッチです",
		'name':"MASUNO",
        'images_titles': ['100', '101', '102'],
    }

    return render(request, 'index.html',my_dict)

#def index2(request):
#    return HttpRespnse("MASUNO SLEEP MODE")
