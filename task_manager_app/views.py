from django.shortcuts import render
from rest_framework import generics
from .models import *
from .permissions import IsOwner
from .serializers import *
# Create your views here.


class ProjectList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Project.objects.filter(owner=self.request.user)
        return queryset
    serializer_class = ProjectSerializer
    permission_classes = (IsOwner,)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwner,)


class BoardList(generics.ListCreateAPIView):
    serializer_class = BoardSerializer

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

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        queryset = Board.objects.filter(project__id=project_id, project__owner=self.request.user)
        return queryset


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        board_id = self.kwargs['board_id']
        queryset = Task.objects.filter(board__id=board_id, board__project__owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        board_id = self.kwargs['board_id']
        board = Board.objects.get(id=board_id)
        serializer.save(board=board)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        board_id = self.kwargs['board_id']
        queryset = Task.objects.filter(board__id=board_id)
        return queryset