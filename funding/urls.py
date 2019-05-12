from django.urls import path
from funding.views import listAllFeaturedProjects , CreateAddProjectForm




urlpatterns =[
    path('',listAllFeaturedProjects),
    path('add', CreateAddProjectForm) # new




]