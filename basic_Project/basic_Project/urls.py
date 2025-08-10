from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('basic_app.urls')),  # Connect app URLs
     path("__reload__/", include("django_browser_reload.urls")),

]
