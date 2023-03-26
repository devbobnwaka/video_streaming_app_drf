from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(required=True, 
                max_length=255, 
                allow_blank=False, 
                write_only=True,
                style={'input_type': 'password'},
                validators=[validate_password],
                )
    confirm_password = serializers.CharField(required=True, 
                max_length=255, 
                allow_blank=False, 
                write_only=True,
                style={'input_type': 'password'}
                )

    class Meta:
        model = User
        fields =( 
            'email', 
            'first_name', 
            'last_name', 
            'password',
            'confirm_password',
            )

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user
    

    def validate(self, data):
        """
        Check if password match.
        """
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password does not match!!!")
        return data

