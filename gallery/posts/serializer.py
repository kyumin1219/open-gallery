# myapp/serializers.py
from rest_framework import serializers
from .models import MyModel 

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'  # 모든 필드 직렬화