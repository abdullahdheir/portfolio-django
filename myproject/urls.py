from django.urls import  path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("portfolioDetails",views.portfolioDetails,name = 'portfolioDetails'),
    path("innerPage",views.innerPage,name = 'innerPage'),
    path("register",views.register,name = 'register'),
    path("login",views.login,name = 'login'),
    path("logout",views.logout,name = 'logout'),
    path("blog",views.blog,name = 'blog'),

]



