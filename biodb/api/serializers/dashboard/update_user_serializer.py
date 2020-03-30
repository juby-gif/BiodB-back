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
    # date_of_birth = serializers.DateField(format="%Y-%m-%d", input_formats=['%Y-%m-%d', 'iso-8601'])
    # blood_type = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
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
        # date_of_birth = validated_data.get('date_of_birth',None)
        # blood_type = validated_data.get('blood_type',None)


        # This is for debugging purposes only.
        print(first_name, last_name, username, email)

        request = self.context.get('request')
        user = request.user
        user.last_name = last_name
        user.first_name = first_name
        # user.date_of_birth = date_of_birth
        # user.blood_type = blood_type
        user.save()

        return user
