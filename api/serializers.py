from rest_framework import serializers
from .models import User,Asset,Request


#user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['first_name','last_name', 'phone_number', 'department', 'role','password','email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user