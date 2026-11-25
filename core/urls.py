
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # logout do usuario
    

   path('logout/', LogoutView.as_view(next_page='home'), name='logout'), 
]
