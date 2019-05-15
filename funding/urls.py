
from . import views
from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings
from .views import home_page,category,search
from funding.views import listAllFeaturedProjects , CreateAddProjectForm




urlpatterns =[
    path('',listAllFeaturedProjects),
    path('add', CreateAddProjectForm), # new
    path('home',home_page),
    path('category/<int:cat_id>/',category),
    path('search',search),
    path('user', views.view_profile, name='user'),
    # path('edit', views.edit_profile, name='edit'),
    path('delete', views.delete_profile, name='user'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)