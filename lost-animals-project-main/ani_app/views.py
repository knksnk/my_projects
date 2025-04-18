import rest_framework
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic.base import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Gender, Type, Breed, Color, Photo, AnimalStatus, Animal, Announcement
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import GenderSerialize, TypeSerialize, BreedSerialize, ColorSerialize, PhotoSerialize, AnimalStatusSerialize, AnimalSerialize, AnnouncementSerialize


class GenderView(generics.ListCreateAPIView):
    """Get all genders"""
    serializer_class = GenderSerialize
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        gens = Gender.objects.all()
        return gens


class OneGenderView(generics.RetrieveUpdateDestroyAPIView):
    """Get gender by id"""
    queryset = Gender.objects.all()
    serializer_class = GenderSerialize
    permission_classes = (IsAdminOrReadOnly,)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=204)


class TypeView(generics.ListCreateAPIView):
    """Get all types"""
    serializer_class = TypeSerialize
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        types = Type.objects.all()
        return types


class OneTypeView(generics.RetrieveUpdateDestroyAPIView):
    """Get type by id"""
    queryset = Type.objects.all()
    serializer_class = TypeSerialize
    permission_classes = (IsAdminOrReadOnly,)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=204)


class BreedView(generics.ListCreateAPIView):
    """Get all breeds"""
    serializer_class = BreedSerialize
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        breeds = Breed.objects.all()
        return breeds


class OneBreedView(generics.RetrieveUpdateDestroyAPIView):
    """Get breed by id"""
    queryset = Breed.objects.all()
    serializer_class = BreedSerialize
    permission_classes = (IsAdminOrReadOnly,)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=204)


class ColorView(generics.ListCreateAPIView):
    """Get all colors"""
    serializer_class = ColorSerialize
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        colors = Color.objects.all()
        return colors


class OneColorView(generics.RetrieveUpdateDestroyAPIView):
    """Get color by id"""
    queryset = Color.objects.all()
    serializer_class = ColorSerialize
    permission_classes = (IsAdminOrReadOnly,)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=204)


class PhotoView(generics.ListCreateAPIView):
    """Get all photos"""
    serializer_class = PhotoSerialize

    def get_queryset(self):
        photos = Photo.objects.all()
        return photos


class OnePhotoView(generics.RetrieveUpdateDestroyAPIView):
    """Get photo by id"""
    queryset = Photo.objects.all()
    serializer_class = PhotoSerialize
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=204)


class AnimalStatusView(generics.ListCreateAPIView):
    """Get all animal statuses"""
    serializer_class = AnimalStatusSerialize
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        stats = AnimalStatus.objects.all()
        return stats


class OneAnimalStatusView(generics.RetrieveUpdateDestroyAPIView):
    """Get animal status by id"""
    queryset = AnimalStatus.objects.all()
    serializer_class = AnimalStatusSerialize
    permission_classes = (IsAdminOrReadOnly,)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=204)


class AnimalView(generics.ListCreateAPIView):
    """Get all animals"""
    serializer_class = AnimalSerialize
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type_name', 'breed_name', 'gender_name', 'coloring']

    def get_queryset(self):
        animals = Animal.objects.all()
        return animals


class OneAnimalView(generics.RetrieveUpdateDestroyAPIView):
    """Get animal by id"""
    queryset = Animal.objects.all()
    serializer_class = AnimalSerialize
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=204)


class AnnouncementView(generics.ListCreateAPIView):
    """Get all announcements"""
    serializer_class = AnnouncementSerialize
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'animal_status', 'is_published']

    def get_queryset(self):
        anns = Announcement.objects.all()
        return anns


class OneAnnouncementView(generics.RetrieveUpdateDestroyAPIView):
    """Get announcement by id"""
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerialize
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=204)
