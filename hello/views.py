from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Funcionario, Permanencia

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def permanencia(request):
    func = Funcionario.objects.get(ra=1477048)
    #print ("Funcionario nao encontrado")
    return render(request, 'permanencia.html', {'permanencia': func})

