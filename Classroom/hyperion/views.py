from django.shortcuts import render, redirect
from hyperion.models import *
from django.contrib import messages
#from django.contrib.sessions.models import Session
from django.views.generic import ListView
from django.views import View
from abc import  ABC ,abstractmethod
import requests
import json
from django.shortcuts import get_object_or_404



"""class UserAccount(ABC):
    #userdata=user.objects.all()
    pass

class Teacher(UserAccount):
    pass

class Student(UserAccount):
    pass


class AccountControllerTemplate(ABC):
    pass

class RegistrationController(AccountControllerTemplate,View):
    pass



#Login To the system

class LoginController(AccountControllerTemplate,View):
    user_login = user_login
    log = 'login.html'

    def login(request):
        if request.session.has_key('is_logged'):
            return redirect('classes')
        if request.method == 'POST':
            User = request.POST['userId']
            pswd = request.POST['Password']
            # uid = user.objects.get(ID = User)
            # dcheck = user.objects.filter(Email = User )                 #matching the user email. as user mail is not in the login model.
            count = user_login.objects.filter(User_ID=User, Password=pswd).count()
            if count > 0:
                request.session['is_logged'] = User  # fetching the currentlu logged in users information
                return redirect('classes')
            else:
                messages.error(request, ' Invalid Credentials ')
                return redirect('login')

        else:
            return render(request, 'login.html')

    def logout(request):
        del request.session['is_logged']
        return redirect('login')
class AccountManagementController(AccountControllerTemplate):

class LoginView(View):
    def post(self, request):
        User = request.POST['userId']
        pswd = request.POST['Password']
        user = user_login.objects.filter(User_ID = User, Password=pswd)

class LogoutView(view):             #log out from the system
    def logout(request):
        #del request.session['is_logged']   #Deleting Session
        return redirect('login')

#Abstract Class Associating ClassroomControllerTemplate
class ClassroomViewTemplate(ABC):
    # fetching the currentlu logged in users information
    classdata = classroom.objects.all()


#Inheriting parent class "ClassroomViewTemplate"
class ClassroomHomeView(ClassroomViewTemplate):
    pass

#Inheriting parent class "ClassroomViewTemplate"
class ClassroomListView(ClassroomViewTemplate):
    context_object_name = 'classdata' """

sid = student.objects.filter(ID= '4')

for a in sid:
    n = a.Class_ID  # all class Id of the user
    fetchdata = classroom.objects.filter(ID=n.ID)  # matching with class ID
    print(fetchdata)

'''print(classroom.objects.all())
for a in p:
    print(a)

T_ID = student.objects.filter(ID='4')
        arr = []
        for a in T_ID:
            n = a.Class_ID     #all class Id of the user
            fetchdata = classroom.objects.filter(ID=n.ID)    #matching with class ID
            arr.append(fetchdata)
        for a in arr:
            # storing in a array
            print(a)'''

#p = classroom.objects.raw('SELECT * FROM `hyperion_classroom` WHERE ClassCode="retake"')
#r = classroom.objects.get()

def classes(request):
    if request.session.has_key('is_logged'):
        T_ID = teacher.objects.filter(ID=request.session['is_logged'])
        S_ID = student.objects.filter(ID=request.session['is_logged'])
        '''arr = []
        if T_ID.count()>0:
            for a in T_ID:
                n = a.Class_ID     #all class Id of the user
                fetchdata = classroom.objects.filter(ID=n.ID)    #matching with class ID
                arr.append(fetchdata)               # storing in a array
            return render(request, 'classes.html', {'fdata':arr}) # passing to template
        if S_ID.count()>0:
            for a in S_ID:
                n = a.Class_ID
                fetchdata = classroom.objects.filter(ID=n.ID)
                arr = []
                arr.append(fetchdata)'''
        arr = classroom.objects.all()
        return render(request, 'classes.html', {'fdata': arr})
        #else:
            #return render(request, 'classes.html')

            # sid = student.objects.get(ID=request.session['is_logged'])
            # T_id = classroom.objects.get(Creator_ID=request.session['is_logged'])

            # fetchdata= classroom.objects.all(ID )      #Fetching all data from classroom to show in template

    else:
        return redirect('login')




def classcreating(request):
    if request.session.has_key('is_logged'):
        if request.method == 'POST':  # fetching the class creation data from the template
            title = request.POST['Title']
            description = request.POST['Description']
            creator_id = user.objects.get(ID=request.session['is_logged'])
            classcode = title +'join'

            classdataob = classroom(Title=title, Description=description,Creator_ID = creator_id, ClassCode = classcode)   #Passing data to a object
            # classdataob.creator_id_ID = creator_id
            classdataob.save()                  #Saving the classroom object
            clss_id = classroom.objects.latest('ID')  #passing class id to classroom object
            teachertable = teacher(ID = creator_id, Class_ID = clss_id)     #saving information to teacher table
            teachertable.save()
            return redirect('createdclass')

        #return render(request, 'createdclass.html')
    else:
        return redirect('login')

def createdclass(request):  # actually it views the classes user has created.
    if request.session.has_key('is_logged'):
        T_ID = user.objects.filter(ID=request.session['is_logged'])
        if T_ID:
            fetchdata = classroom.objects.filter(Creator_ID = request.session['is_logged'])   #matching with class ID
            return render(request, 'createdclass.html', {'fdata':fetchdata})
        else:
            return redirect('classes')
    else:
        return redirect('login')


def setting(request):
    return render(request, 'setting.html')

def joinclass(request):
    if request.method == "POST":
        ccode = request.POST['CCode']
        desiredclass= classroom.objects.get(ClassCode = ccode)
        desiredclassid = desiredclass.ID
        cid = user.objects.get(ID=request.session['is_logged'])
        classidinstance = classroom.objects.get(ID=desiredclassid)
        joinC = student(ID = cid, Class_ID = classidinstance )
        joinC.save()
        return redirect('classes')
    else:
        #messages.error(request, ' Invalid ClassCode ')
        return redirect('classes')

def contact(request):
    return render(request, 'contact.html')


def calendar(request):
    return render(request, 'calendar.html')


def individualclass(request):
    return render(request, 'individualclass.html')



def registration(request):
    if request.method == "POST":  # to deal with post&get method
        fname = request.POST['FirstName']
        lname = request.POST['LastName']
        dob = request.POST['DoB']
        email = request.POST['Email']
        uid = user.objects.latest('ID')
        password = request.POST['Password']

        uservar = user(FirstName=fname, LastName=lname, DoB=dob, Email=email)
        uservar.save()
        uid = user.objects.latest('ID')
        logvar = user_login(User_ID=uid, Password=password)
        logvar.save()
        if uservar is None:
            return redirect('registration')
        else:
            messages.error(request, ' Successfully Registered ')
            return redirect('login')
    else:
        return render(request, 'registration.html')

#x = user.objects.get(Email='elonmask@gmail.com')
#print(x.ID)
def login(request):
    if request.session.has_key('is_logged'):
        return redirect('classes')
    if request.method == 'POST':
        #User = request.POST['userId']
        pswd = request.POST['Password']
        #sql = 'SELECT ID FROM hyperion_user WHERE Email ="elonmask@gmail.com"'
        uid = user.objects.get(Email = request.POST['userId'])   #Fetching userID from email address
        #umail = user.objects.get(Email = User)
        lid = uid.ID
        #dcheck = user.objects.filter(Email = User )                 #matching the user email. as user mail is not in the login model.
        count = user_login.objects.filter(User_ID = lid, Password=pswd).count()
        if count > 0:
            request.session['is_logged'] = lid        # fetching the currentlu logged in users information
            return redirect('classes')
        else:
            messages.error(request, ' Invalid Credentials ')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    del request.session['is_logged']
    return redirect('login')

