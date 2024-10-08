"""
URL configuration for blog1 project.

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
from django.contrib import admin
from django.urls import include, path
from .views import AddPostView, DeletePostView, HomeView,ArticleDetailView, UpdatePostView,DraftPostView,LikeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name = 'home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name = 'article_details'),
    path('add_post/',AddPostView.as_view(),name = 'add_post'),
    path('update_post/<int:pk>',UpdatePostView.as_view(),name = 'update_post'),
    path('delete_post/<int:pk>/remove',DeletePostView.as_view(),name = 'delete_post'),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('memuser.urls')),
    path('draft/',DraftPostView.as_view(),name='draft_home'),
    path('like/<int:pk>',LikeView,name = 'like_post'),
]
