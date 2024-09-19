from rest_framework import serializers
from django.contrib.auth.models import User

"""
User모델을 직렬화

extra -> password필드를 write_only로 함
클라가 데이터 입력할때 json에 비밀번호 포함 제외

"""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password' : {'write_only' : True}}
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user