from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('created_at','completed_at')

    def validate(self, attrs):
        # when updating, check if status set to completed -> require report & worked_hours
        status = attrs.get('status', getattr(self.instance, 'status', None))
        if status == Task.STATUS_COMPLETED:
            # if instance exists, accept either attrs or existing fields
            report = attrs.get('completion_report') or getattr(self.instance, 'completion_report', None)
            hours = attrs.get('worked_hours') or getattr(self.instance, 'worked_hours', None)
            if not report:
                raise serializers.ValidationError("Completion report is required when marking task as completed.")
            if hours is None:
                raise serializers.ValidationError("Worked hours is required when marking task as completed.")
        return attrs

    def update(self, instance, validated_data):
        # automatically set completed_at when status becomes completed
        prev_status = instance.status
        instance = super().update(instance, validated_data)
        if prev_status != Task.STATUS_COMPLETED and instance.status == Task.STATUS_COMPLETED:
            instance.completed_at = timezone.now()
            instance.save()
        return instance
