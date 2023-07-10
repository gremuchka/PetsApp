from django.shortcuts import render
from rest_framework import generics
from .serializers import PetDetailSerializer, PetListSerializer
from .models import Pet
from .permission import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class PetCreateView(generics.CreateAPIView):
    serializer_class = PetDetailSerializer


class PetListView(generics.ListAPIView):
    serializer_class = PetListSerializer
    queryset = Pet.objects.all()
    permission_classes = (IsAdminUser, )


class PetDetailViews(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PetDetailSerializer
    queryset = Pet.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
