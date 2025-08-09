#1
from django.shortcuts import render
from django.http import HttpResponse

#2
from rest_framework import viewsets
from .models import Tarefa
from .serializer import TarefaSerializer
# Create your views here.

#1
def ola_django(request):
    return HttpResponse("ola, mundo")

#2
class tarefaviewset(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer