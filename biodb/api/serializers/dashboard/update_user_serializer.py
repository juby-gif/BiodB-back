from rest_framework import exceptions, serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class UpdateSerializer(serializers.Serializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField(
         validators=[
             UniqueValidator(queryset=User.objects.all())
         ]
    )
    email = serializers.EmailField(
             validators=[
                 UniqueValidator(queryset=User.objects.all())
             ]
        )

    def update(self, instance, validated_data):
        first_name = validated_data.get('first_name', None)
        last_name = validated_data.get('last_name', None)
        email = validated_data.get('email',None)
        username = validated_data.get('username',None)


        # This is for debugging purposes only.
        print(first_name, last_name, username, email)

        # Plug in our data from the request into our `User` model.
        request = self.context.get('request')
        user = request.user
        user.last_name = last_name
        user.first_name = first_name
        user.save()

        return user
