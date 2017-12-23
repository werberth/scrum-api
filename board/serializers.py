from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model

from .models import Sprint, Task

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        source='get_full_name',
        read_only=True
    )

    class Meta:
        model = User
        fields = (
            'id', User.USERNAME_FIELD,
            'full_name', 'is_active'
        )


class SprintSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Sprint
        fields = ('id', 'name', 'description', 'end', 'link')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse(
                'sprint-detail',
                kwargs={'pk': obj.pk}, request=request,
            )
        }


class TaskSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    assigned = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, required=False,
        queryset=User.objects.all()
    )
    links = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'links',
            'description', 'sprint',
            'status', 'order', 'status_display',
            'assigned', 'started', 'due', 'completed',
        )

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse(
                'task-detail',
                kwargs={'pk': obj.pk}, request=request,
            )
        }
