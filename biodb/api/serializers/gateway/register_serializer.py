from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(
         validators=[
             UniqueValidator(queryset=User.objects.all())
         ]
    )
    username = serializers.CharField(
         validators=[
             UniqueValidator(queryset=User.objects.all())
         ]
    )
    password = serializers.CharField(write_only=True)


    def create(self, validated_data):
        first_name = validated_data.get('first_name', None)
        last_name = validated_data.get('last_name', None)
        email = validated_data.get('email', None)
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)

        # This is for debugging purposes only.
        print(first_name, last_name, username, email, password)

        user = User.objects.create_user(username, email, password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()

        return user
