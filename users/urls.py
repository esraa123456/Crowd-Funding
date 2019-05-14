from django.conf.urls import url
from django.urls import path
from users import views
# SET THE NAMESPACE!
app_name = 'users'
# Be careful setting the name to just /login use userlogin instead!

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('signup/', views.signup, name='signup'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]