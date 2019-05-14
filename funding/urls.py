
from . import views
from django.urls import path
from .views import home_page,category
from funding.views import listAllFeaturedProjects , CreateAddProjectForm




urlpatterns =[
    path('',listAllFeaturedProjects),
    path('add', CreateAddProjectForm), # new
    path('home',home_page),
    path('category/<int:cat_id>/',category),
    path('user', views.view_profile, name='user'),
    # path('edit', views.edit_profile, name='edit'),
    path('delete', views.delete_profile, name='user'),

]

