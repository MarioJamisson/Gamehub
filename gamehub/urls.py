from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gamehub_app.urls')),  # esse aqui é OBRIGATÓRIO
]
