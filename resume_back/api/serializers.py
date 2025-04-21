from rest_framework import serializers
from .models import CustomUser , Certification




#login
class LoginSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128, write_only=True)  # 비밀번호는 쓰기 전용

#signup 
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('user_id', 'username', 'email', 'phone', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class RecruiterRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('user_id', 'username', 'email', 'phone', 'password', 'role')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_id', 'username', 'email','phone']

