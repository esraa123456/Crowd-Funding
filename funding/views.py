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

    # user = request.user
    # projects = user.projects_set.all()
    # donations = user.donation_set.all()
    args ={ 'user': request.user}
    return render(request, 'users/show.html', args)

@login_required()
def delete_profile(request):
    user = request.user
    user.delete()
    return HttpResponse("user deleted!")

# def edit_profile(request):
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('/profile/user')
#         else:
#             form = UserChangeForm(instance=request.user)
#             args = {'form': form}
#             return render(request, 'users/edit.html', args)

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

def category(request,cat_id):
    cat_name = Category.objects.filter(id=cat_id)[0].name
    category_projects = Project.objects.filter(category_id = cat_id)
    project_images = []
    for proj in category_projects:
        img = Project_Image.objects.filter(project_id=proj.id)[:1]
        project_images.append(img[0])
    context = {'projects':category_projects,
               'images':project_images,
               'cat_name':cat_name}
    return render(request,"funding/category.html",context)

def search(request):
    search_projects = Project.objects.filter(title__contains = request.POST.get('search'))
    project_images = []
    for proj in search_projects:
        img = Project_Image.objects.filter(project_id=proj.id)[:1]
        project_images.append(img[0])
    context = {'projects':search_projects,
               'images':project_images,
               'search':request.POST.get('search')}
    return render(request,"funding/search.html",context)

allFeaturedProjects = Project.objects.all()

def listAllFeaturedProjects(request):
    return render (request , 'project/allProjects.html', {'allFeaturedProjects' : allFeaturedProjects})

def CreateAddProjectForm (request):
    project_form = CreateProjectForm()
    return render (request , 'project/addProject.html' , {'project_form': project_form})

