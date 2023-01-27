from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import SiteUrl

import aiohttp
import asyncio
import time
from datetime import datetime
import schedule

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username"]

# Serializer to Register User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password],help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'})
    class Meta:
        model = User
        fields = ('username', 'password',)
        
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class StartSerializer(serializers.ModelSerializer):
    started=serializers.SerializerMethodField(read_only=True)
    class Meta :
        model=SiteUrl
        fields=[
            "id",
            "endpoint",
            "started",
        ]
        
        
    
    
    def get_started(self,obj):
        
        if not hasattr(obj, 'endpoint'):
            return "No"
        if not isinstance(obj, SiteUrl):
            return "No"
        else :
            start_time = datetime.now()

            return start_time
twohundredstatus = 0

# async def get_status(session, url):
#     async with session.get(url) as resp:
#         return resp.status
    

# def job():
#     # asyncio.run(main())
#     pass

# schedule.every().minutes.do(job())
# while True:
#     schedule.run_pending()
    

