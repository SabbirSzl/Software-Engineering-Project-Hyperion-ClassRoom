

from django.conf.urls import url, include
from django.urls import path
from hyperion import views
#from hyperion.views import AccountControllerTemplate,LoginController

urlpatterns = [
    path("", views.classes, name = 'classes'), #this empty path will be redirect to classes
    path("individualclass/", views.individualclass, name = 'individualclass'),
    path("classes", views.classes, name = 'classes'),
    path("createdclass/", views.createdclass, name = 'createdclass'),
    path("calendar/", views.calendar, name = 'calendar'),
    path("setting/", views.setting, name = 'setting'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("registration/", views.registration, name = 'registration'),
    path("classcreating/", views.classcreating, name = 'classcreating'),
    path("joinclass/", views.joinclass, name='joinclass'),


    #path('registrationView/', RegistrationController.as_view(), name='registration'),
    #path('login/', LoginController.as_view(), name='login')
]