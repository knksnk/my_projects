from django.contrib import admin

# Register your models here.

from .models import Gender, Type, Breed, Color, Photo, Animal, AnimalStatus, Announcement


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender_name',)
    list_display_links = ('gender_name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
    list_display_links = ('type_name',)


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('breed_name',)
    list_display_links = ('breed_name',)
    list_filter = ('type_name',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('coloring',)
    list_display_links = ('coloring',)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_url',)
    list_display_links = ('photo_url',)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    list_filter = ('type_name', 'breed_name', 'gender_name', 'coloring')
    search_fields = ('type_name', 'breed_name', 'gender_name', 'coloring')


@admin.register(AnimalStatus)
class AnimalStatusAdmin(admin.ModelAdmin):
    list_display = ('animal_status',)
    list_display_links = ('animal_status',)


@admin.register(Announcement)
class Announcement(admin.ModelAdmin):
    list_display = ('id', 'date', 'location')
    list_display_links = ('id',)
    list_filter = ('date', 'animal_status', 'is_published')
    search_fields = ('date', 'animal_status', 'is_published')
