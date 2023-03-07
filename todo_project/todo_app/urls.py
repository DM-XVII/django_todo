from django.urls import path
from .views import *

urlpatterns =[
    path('',Home.as_view(),name='home'),
    path('addtask/',createtask,name='addtask'),
    path('updatetask/<str:pk>/',edittask,name='update'),
    path('readmore/<slug:task_slug>/', ReadMore.as_view(), name='readmore'),
    path('delete/<str:pk>/',DeleteTask,name='deletetask'),
    path('category/<slug:cat_slug>/',CategoryTask.as_view(),name='category'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/',logout_user,name='logout'),



]
