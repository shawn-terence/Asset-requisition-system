#Serializer.py
from rest_framework import serializers
from .models import User, Asset, Request
from rest_framework.serializers import ModelSerializer,SerializerMethodField
import cloudinary
# user serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "department",
            "role",
            "password",
            "email",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# asset serializer
class AssetSerializer(ModelSerializer):
    image_url=SerializerMethodField()
    class Meta:
        model = Asset
        fields = [
            "id",
            "image_url",
            "name",
            "description",
            "category",
            "serial_number",
            "tag",
            "status",
            "asset_type",
        ]

    def create(self, validated_data):
        asset = Asset.objects.create(**validated_data)
        return asset
    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url  # Use Cloudinary's URL property
        return None

# request serializer
class RequestSerializer(ModelSerializer):
    asset = AssetSerializer()
    employee = UserSerializer()

    class Meta:
        model = Request
        fields = ["id", "asset", "employee", "status"]

    def create(self, validated_data):
        request = Request.objects.create(**validated_data)
        return request
