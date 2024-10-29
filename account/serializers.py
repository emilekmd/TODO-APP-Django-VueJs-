from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email','first_name','last_name','password','is_active','is_staff']
    
    def create(self, validated_data):
        # Créer un utilisateur normal
        user = CustomUser.objects.create_user(**validated_data)
        
        return user

    def create_superuser(self, validated_data):
        # Créer un super utilisateur
        user = CustomUser.objects.create_superuser(**validated_data)
        return user