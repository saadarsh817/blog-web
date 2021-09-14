"""geekyminiproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from geekymini import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.newhome,name="home"),
    path('about/', views.newabout,name="aabout"),
    path('contact/', views.newcontact,name="contact"),
    path('signup/',views.newsignup,name="signup"),
    path('dashboard/',views.newdashboard,name="dashboard"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('add/',views.add_post,name="add"),
    path('update/<int:id>/',views.update_post,name="update"),
    path('delete/<int:id>/',views.delete_post,name="delete"),
    #path('photo',views.new_photo,name="photo"),
    path('admin/', admin.site.urls),
    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
print(static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))

