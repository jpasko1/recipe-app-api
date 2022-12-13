"""Views for the user API"""

from rest_framework import generics

from user.serializers import UserSerialzer

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerialzer
