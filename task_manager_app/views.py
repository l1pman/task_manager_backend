from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from .models import *
from .permissions import IsOwner
from .serializers import *
# Create your views here.


class ProjectList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Project.objects.filter(owner=self.request.user)
        return queryset
    serializer_class = ProjectSerializer
    permission_classes = (IsOwner,IsAuthenticated)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwner,IsAuthenticated)
    http_method_names = ['get', 'patch', 'delete']

class BoardList(generics.ListCreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = (IsOwner,IsAuthenticated)

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        queryset = Board.objects.filter(project__id=project_id, project__owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        project_id = self.kwargs['project_id']
        project = Project.objects.get(id=project_id)
        serializer.save(project=project)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BoardSerializer
    permission_classes = (IsOwner,IsAuthenticated)
    http_method_names = ['get', 'patch', 'delete']

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        queryset = Board.objects.filter(project__id=project_id, project__owner=self.request.user)
        return queryset


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsOwner,IsAuthenticated)

    def get_queryset(self):
        board_id = self.kwargs['board_id']
        project_id = self.kwargs['project_id']
        queryset = Task.objects.filter(board__id=board_id, board__project__owner=self.request.user, board__project__id=project_id)
        return queryset

    def perform_create(self, serializer):
        board_id = self.kwargs['board_id']
        board = Board.objects.get(id=board_id)
        serializer.save(board=board)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsOwner,IsAuthenticated)
    http_method_names = ['get', 'patch', 'delete']
    def get_queryset(self):
        board_id = self.kwargs['board_id']
        queryset = Task.objects.filter(board__id=board_id)
        return queryset


class BoardListAll(generics.ListAPIView):
    def get_queryset(self):
        queryset = Board.objects.filter(project__owner=self.request.user)
        return queryset
    serializer_class = BoardSerializer
    permission_classes = (IsOwner,IsAuthenticated)


class TaskListAll(generics.ListAPIView):
    def get_queryset(self):
        queryset = Task.objects.filter(board__project__owner=self.request.user)
        return queryset
    serializer_class = TaskSerializer
    permission_classes = (IsOwner,IsAuthenticated)

