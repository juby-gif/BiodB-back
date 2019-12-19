from django.contrib.auth import authenticate, login, logout
from rest_framework import views, status, response
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
# from django_rest_passwordreset.signals import reset_password_token_created

from api.serializers import RegisterSerializer


class RegisterAPI(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_201_CREATED,
            data=serializer.data,
        )

class LogoutAPI(views.APIView):
    def post(self,request):
        try:
            logout(request)
            return response.Response(
                status=status.HTTP_200_OK,
                data={
                 "was_logged_out": True,
                 "reason": None,
            })
        except Exception as e:
            print(e)
            return response.Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                 "was_logged_out": False,
                 "reason": str(e),
            })
        return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                'ERROR' : str(e)
                })

# #the following codes taken from https://pypi.org/project/django-rest-passwordreset/
# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
#     context = {
#     'current_user': reset_password_token.user,
#     'username': reset_password_token.user.username,
#     'email': reset_password_token.user.email,
#     'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
#     }
#
#     # render email text
#     email_html_message = render_to_string('email/user_reset_password.html', context)
#     email_plaintext_message = render_to_string('email/user_reset_password.txt', context)
#
#     msg = EmailMultiAlternatives(
#     # title:
#     "Password Reset for {title}".format(title="Some website title"),
#     # message:
#     email_plaintext_message,
#     # from:
#     "noreply@somehost.local",
#     # to:
#     [reset_password_token.user.email]
#     )
#     msg.attach_alternative(email_html_message, "text/html")
#     msg.send()
#
# class RandomStringTokenGenerator(BaseTokenGenerator):
# # """
# # Generates a random string with min and max length using os.urandom and binascii.hexlify
# # """
#
#     def __init__(self, min_length=10, max_length=50, *args, **kwargs):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def generate_token(self, *args, **kwargs):
#     # """ generates a pseudo random code using os.urandom and binascii.hexlify """
#     # determine the length based on min_length and max_length
#         length = random.randint(self.min_length, self.max_length)
#
#     # generate the token using os.urandom and hexlify
#         return binascii.hexlify(
#         os.urandom(self.max_length)
#         ).decode()[0:length]
