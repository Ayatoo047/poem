from django.urls import path
from . import views

urlpatterns = [
        path("", views.poems, name="poems"),
        path('poem/<str:pk>', views.poem, name="poem"),
        path('create/', views.newPoem, name="create"),
        path('delete/<str:pk>', views.delete, name="delete"),
        path('update/<str:pk>', views.updatePoem, name="update"),
        path('allpoems/', views.allpoems, name="allpoems"),
        path('about/', views.about, name="about"),
        path('contact/', views.contact, name="contact"),
        path('messages/<str:pk>', views.messagers, name="messages"),
        path('inbox/', views.inbox, name="inbox"),
        ]