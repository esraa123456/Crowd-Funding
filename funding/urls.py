
from . import views
from django.urls import path
from .views import home_page
from funding.views import listAllFeaturedProjects , CreateAddProjectForm




urlpatterns =[
    path('',listAllFeaturedProjects),
    path('add', CreateAddProjectForm), # new
    path('home',home_page),
    path('<int:id>', views.user, name='user'),

]

