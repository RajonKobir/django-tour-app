from django.shortcuts import render, redirect
from .models import Tour
from .forms import ContactForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username = username, password = password )
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form' : form})


def login_view(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'index'
            return redirect(next_url)
        else:
            error_message = 'Invalid Credentials'
    return render(request, 'accounts/login.html', {'error' : error_message})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('index')


@login_required
def index(request):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'tours/index.html', context)

@login_required
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save_in_db()
            return redirect('contact_success_view')
    else:
        form = ContactForm()
        context = {'form' : form}
        return render(request, 'tours/contact_form.html', context)

@login_required    
def contact_success_view(request):
    return render(request, 'tours/contact_success_view.html')


# protected view 
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'registration/protected.html')