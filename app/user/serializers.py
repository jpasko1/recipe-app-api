""" Serializers for teh user API View"""

from django.contrib.auth import get_user_model

from rest_framework import serializers

class UserSerialzer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        print("In serialzers.Meta()")
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        print("in serializers.create()")
        return get_user_model().objects.create_user(**validated_data)
