from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema

class AuthView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Authenticated ! '}
        return Response(content)


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    @swagger_auto_schema(operation_description="plz enter an appropriate username and password ", operation_summary="register user ", responses={200: "successful"})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
