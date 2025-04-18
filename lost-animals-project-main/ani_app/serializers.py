from rest_framework import serializers
from .models import Gender, Type, Breed, Color, Photo, Animal, AnimalStatus, Announcement


class GenderSerialize(serializers.ModelSerializer):
    """Gender serializer"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Gender
        fields = "__all__"


class TypeSerialize(serializers.ModelSerializer):
    """Type serializer"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Type
        fields = "__all__"


class BreedSerialize(serializers.ModelSerializer):
    """Breed serializer"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    type_name = serializers.SlugRelatedField(
        slug_field="type_name",
        queryset=Type.objects.all()
    )

    class Meta:
        model = Breed
        fields = "__all__"


class ColorSerialize(serializers.ModelSerializer):
    """Color serializer"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Color
        fields = "__all__"


class AnimalStatusSerialize(serializers.ModelSerializer):
    """Animal status serializer"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AnimalStatus
        fields = "__all__"


class PhotoSerialize(serializers.ModelSerializer):
    """Photo serializer"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Photo
        fields = "__all__"


class AnimalSerialize(serializers.ModelSerializer):
    """Animal serializer"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    type_name = serializers.SlugRelatedField(
        slug_field="type_name",
        queryset=Type.objects.all()
    )
    breed_name = serializers.SlugRelatedField(
        slug_field="breed_name",
        queryset=Breed.objects.all()
    )
    gender_name = serializers.SlugRelatedField(
        slug_field="gender_name",
        queryset=Gender.objects.all()
    )
    coloring = serializers.SlugRelatedField(
        slug_field="coloring",
        queryset=Color.objects.all()
    )
    photo = serializers.SlugRelatedField(
        slug_field="photo_url",
        queryset=Photo.objects.all()
    )

    class Meta:
        model = Animal
        fields = "__all__"


class AnnouncementSerialize(serializers.ModelSerializer):
    """Announcement serializer"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    animal_status = serializers.SlugRelatedField(
        slug_field="animal_status",
        queryset=AnimalStatus.objects.all()
    )

    class Meta:
        model = Announcement
        fields = "__all__"
