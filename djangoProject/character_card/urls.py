from django.urls import path
from . import views




"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# project/urls.py

from django.contrib import admin
from django.urls import include, path

app_name = 'character_card'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dice_roller/', include('dice_roller.urls')),
    #path('', views.character_view, name='character_view'),
    path('view/', views.character_view, name='character_view'),
    path('list/', views.list_characters, name='list_characters'),
    path('view/<int:character_id>/', views.character_view, name='character_view'),
    path('character_view/<int:pk>/', views.character_view),
    path('create/', views.character_edit, name='character_create'),
    path('character_edit/<int:pk>/', views.character_edit),
  path('edit/<int:character_id>/', views.character_edit, name='character_edit'),

    # Add other app URLs as needed
]


