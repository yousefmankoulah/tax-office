from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import User_file
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.



#########Authentication ######################
def signInView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in.")
                return redirect('mainH')
            else:
                messages.error(request,"Invalid username or password.")

        else:
            messages.error(request,"Invalid username or password.")

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signOut(request):
    logout(request)
    return redirect('login')

#########Authentication ######################


#########Dashboard ######################

@login_required
def dash(request, id):
    user_info = User_file.objects.filter(user=request.user.id)
    return render(request, 'dash.html', {'info': user_info})



#########Home page and contact ######################

def main_home_page(request):
    return render(request, 'mainhomepage.html')


def contact_page(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        name = request.POST['name']
        message = request.POST['describe']
        email = request.POST['email']
        reciever = [settings.EMAIL_HOST_USER,]
        full_message = "You Recieved email from: " + name + "\n"  + "His Email Address is: " + email + '\n' + message
        send_mail(subject, full_message, email, reciever)
     
    return render(request, 'contactus.html')

