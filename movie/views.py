from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


# Create your views here.

#def home(request):

    #  return HttpResponse("<h1>Welcome to the Movie Reviews Home Page!</h1>") - Antes
    #return render (request, 'home.html') # Después, se crea un archivo home.html en la carpeta templates y se llama a ese archivo desde la función home. De esta manera, se puede crear una página más completa y personalizada.
    #return render (request, 'home.html', {'Name': 'This is Isabella Cadavid Posada'}) # Se puede pasar un diccionario con datos a la plantilla para que se muestren en la página. En este caso, se pasa el nombre "Isabella" para que se muestre en la página.

def home(request):
    searchTerm = request.GET.get('searchMovie') #Obtiene lo que el usuario escribió en el input del buscador.

    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    return render(
        request,
        'home.html',
        {
            'searchTerm': searchTerm,
            'movies': movies
        }
    )

def about(request):

    #return HttpResponse("<h1>About Movie Reviews</h1><p>This is a website where you can find reviews of movies.</p>") - Antes, se muestra un mensaje simple con HttpResponse.
    return render(request, 'about.html') # Después, se crea un archivo about.html en la carpeta templates y se llama a ese archivo desde la función about. De esta manera, se puede crear una página más completa y personalizada.
