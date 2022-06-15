from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
 
from authentication.models import User


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=80)
    password = serializers.CharField(min_length=6)
    phone_number = PhoneNumberField(allow_null=False,allow_blank=False)
    place = serializers.CharField(max_length=180)

    class Meta:
        model = User
        fields = ['id','username','email','password','phone_number','place']

    def validate(self,attrs):
        username_exist = User.objects.filter(username=attrs['username']).exists()
        if username_exist:
            raise serializers.ValidationError(detail='User with username exists')

        email_exist = User.objects.filter(email=attrs['email']).exists()
        if email_exist:
            raise serializers.ValidationError(detail='User with email exists')

        phonenumber_exist = User.objects.filter(phone_number=attrs['phone_number']).exists()
        if phonenumber_exist:
            raise serializers.ValidationError(detail='User with phonenumber exists')

        return super().validate(attrs)

