from .models import Card, TaskList
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'task_list', 'name', 'description', 'timestamp',
                  'due_date', 'activity_log')


class TaskListSerializer(serializers.ModelSerializer):
    card_set = CardSerializer(many=True, read_only=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'card_set')
