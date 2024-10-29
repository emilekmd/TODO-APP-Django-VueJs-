from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status

class CreateUser(APIView):
    def post (self,request): 
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CreateSuperUser(APIView):
    def post(self, request):
        # Utilise le serializer pour valider les données
        serializer = CustomUserSerializer(data=request.data)

        # Vérifie si les données sont valides
        if serializer.is_valid():
            # Créer un super utilisateur en appelant la méthode appropriée
            superuser = serializer.create_superuser(serializer.validated_data)
            superuser.save()
            return Response({'message': 'Super user created successfully', 'user': serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)