from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api_user/', include('user_managment.urls')),
    path('api_book/', include('book_managment.urls')),
]
