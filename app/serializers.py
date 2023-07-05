from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    BooleanField,
    DateTimeField
)

from .models import Task


class TaskGetSerializer(Serializer):
    title = CharField()
    description = CharField()
    completed = BooleanField()
    created_at = DateTimeField()


class TaskPostSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

