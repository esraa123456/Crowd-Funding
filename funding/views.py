from django.shortcuts import render, redirect
from .models import User
from funding.models import Category,Project,Project_Image
from django.http import HttpResponse
from .forms import CreateProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
# Create your views here.

@login_required()
def view_profile (request):
    # userSet = User.objects.filter(id = id)
    # for oneUser in userSet:
    #     user = oneUser


    # if request.user.is_authenticated:
    args ={ 'user': request.user }
    # else:
    #     return redirect('views.login')
    return render(request, 'users/show.html', args)

def home_page(request):
    categories = Category.objects.all()

    latest_projects = Project.objects.all()[:5]
    latest_project_image = []
    for proj in latest_projects:
        img = Project_Image.objects.filter(project_id = proj.id)[:1]
        latest_project_image.append(img[0])

    featured_projects = Project.objects.filter(isFeatured = 1)[:5]
    featured_project_image = []
    for proj in featured_projects:
        img = Project_Image.objects.filter(project_id = proj.id)[:1]
        featured_project_image.append(img[0])


    context={'categories':categories,
             'featured_projects':featured_projects,
             'featured_project_image':featured_project_image,
             'latest_projects':latest_projects,
             'latest_project_image':latest_project_image,
    }
    return render(request,"funding/homePage.html",context)




allFeaturedProjects = Project.objects.all()

def listAllFeaturedProjects(request):
    return render (request , 'project/allProjects.html', {'allFeaturedProjects' : allFeaturedProjects})

def CreateAddProjectForm (request):
    project_form = CreateProjectForm()
    return render (request , 'project/addProject.html' , {'project_form': project_form})

