from rest_framework import serializers
from .models import Tarefa
class TarefaSerializer(serializers.ModelSerializer):
    class meta:
        model = Tarefa
        fields = '__all__'