from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task,Cathegorie
from account.models import CustomUser
from .serializers import TaskSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

class CreateCathegorie(APIView):
    def post(self,request):
        try:
            cathegorie , _= Cathegorie.objects.get_or_create(name=request.data['name'])
            if not _:
                return Response('already exist',status=status.HTTP_200_OK)        
        except:
            return Response('name not provide',status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

class DeleteCathegorie(APIView):
    def post(self,request):
        try:
            cathegorie = get_object_or_404(Cathegorie,name=request.data['name'])
            cathegorie.delete()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_201_CREATED)

class UpdateCathegorie(APIView):
    def post(self,request):
        try:
            cathegorie = get_object_or_404(Cathegorie,name=request.data['old_name'])
            cathegorie.name=request.data['new_name']
            cathegorie.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
    
class CreateTask(APIView):
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        
        if serializer.is_valid():
            
            user = None
            cathegorie,_ = Cathegorie.objects.get_or_create(name="")
            
            #user
            try:
                id = request.data['id']
                user = get_object_or_404(CustomUser,pk=id)
            except:
                return Response("user not found",status=status.HTTP_404_NOT_FOUND)
            
            #add cathegorie if exist
            try:
                cath_name = request.data['cath_name']
                if cath_name!="":
                    cathegorie = Cathegorie.objects.get(name=cath_name)
            except:
                pass
            
            serializer.save(user=user,cathegorie=cathegorie)
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetTasks(APIView):
    def get(self,request):            
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            
            return Response({"tasks": serializer.data})

class GetTask(APIView):
    def get(self,request):
        id = request.data['id']
        
        if not id:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task)
        
        return Response({"task":serializer.data})

class UpdateTask(APIView):
    def post(self, request):
        id = request.data['id']
        new_description = request.data['description']
        
        if id and new_description:
            task = Task.objects.get(id=id)
            task.description = new_description
            task.save()
            
            return Response("updated",status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class DeleteTask(APIView):
    def get(self, request):
        id = request.data['id']
        try:
            task_to_delete = get_object_or_404(Task,id=id)
            task_to_delete.delete()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response('deleted',status=status.HTTP_200_OK)
        