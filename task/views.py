from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

class CreateTask(APIView):
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
        