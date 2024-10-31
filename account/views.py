from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status

from .models import CustomUser
from django.shortcuts import get_object_or_404

from .utils import *
from rest_framework.exceptions import AuthenticationFailed

class CreateUser(APIView):
    def post (self,request): 
        serializer = CustomUserSerializer(data=request.data)
        #checking data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CreateSuperUser(APIView):
    def post(self, request):
        # we use the serializer to validate data
        serializer = CustomUserSerializer(data=request.data)

        # check if data are correct
        if serializer.is_valid():
            # Créer un super utilisateur en appelant la méthode appropriée
            superuser = serializer.create_superuser(serializer.validated_data)
            superuser.save()
            return Response({'message': 'Super user created successfully', 'user': serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        
        user = get_object_or_404(CustomUser,email=email)
        
        if user.check_password(password):
            #   there we generate the token
            token=create_jwt(user)
            user.token=token
            user.is_authenticated = True
            user.save()
            
        response = Response({
                            "token":token,
                            "id":user.pk,
                            "first_name":user.first_name,
                            "last_name":user.last_name,
                            "token":token
                        }
                        ,status=status.HTTP_200_OK)
        
        # add token to cookies
        response.set_cookie(
            key='jwt',
            value=token,
            httponly=True,  # disabled javascript acces
            samesite='Lax'  # disbled sending cookies by request
        )
        return response
    
class LogoutUser(APIView):
    def post(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('unauthentificated')
        
        id = decode_jwt(token)

        user = CustomUser.objects.get(pk=id)
        if user is None:
            raise AuthenticationFailed('user not found')
        
        user.is_authenticated = False
        user.token=""
        user.save()

        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie(key='jwt')
        
        return response