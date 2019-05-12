from django.shortcuts import render
from django.http import HttpResponse
from funding.models import Project
from .forms import CreateProjectForm

# Create your views here.
allFeaturedProjects = Project.objects.all()

def listAllFeaturedProjects(request):
    return render (request , 'project/allProjects.html', {'allFeaturedProjects' : allFeaturedProjects})

def CreateAddProjectForm (request):
    project_form = CreateProjectForm()
    return render (request , 'project/addProject.html' , {'project_form': project_form})