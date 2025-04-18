from django.urls import path
from ani_app import views

urlpatterns = [
    path("gender/", views.GenderView.as_view()),
    path("gender/<int:pk>/", views.OneGenderView.as_view()),
    path("type/", views.TypeView.as_view()),
    path("type/<int:pk>/", views.OneTypeView.as_view()),
    path("breed/", views.BreedView.as_view()),
    path("breed/<int:pk>/", views.OneBreedView.as_view()),
    path("color/", views.ColorView.as_view()),
    path("color/<int:pk>/", views.OneColorView.as_view()),
    path("photo/", views.PhotoView.as_view()),
    path("photo/<int:pk>/", views.OnePhotoView.as_view()),
    path("animal_status/", views.AnimalStatusView.as_view()),
    path("animal_status/<int:pk>/", views.OneAnimalStatusView.as_view()),
    path("animal/", views.AnimalView.as_view()),
    path("animal/<int:pk>/", views.OneAnimalView.as_view()),
    path("announcement/", views.AnnouncementView.as_view()),
    path("announcement/<int:pk>/", views.OneAnnouncementView.as_view()),
]
