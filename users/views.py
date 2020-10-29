from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,TemplateView, FormView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from users.models import Profile
from posts.models import Post
#Forms
from users.forms import UpdateProfileForm, SignupForm, LoginForm

from users.my_functions import error_form_list

class UserProfileView(LoginRequiredMixin, DetailView):
    """User profile view."""
    template_name="users/profile.html"
    slug_field='username'
    slug_url_kwarg='username'
    queryset=User.objects.all()
    context_object_name="user"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user=self.get_object()
        context["posts"] = Post.objects.filter(user=user).order_by("-created")
        return context


class LoginView(auth_views.LoginView):
    template_name="users/login.html"
    
# Views functions
def login_view(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect("posts:feed")
        else:
            list_errors=error_form_list(str(form.errors))
            
    else:
        form=LoginForm()
        list_errors=[]
    
    context={
        "form": form,
        "errors": list_errors,
    }
    return render(request, 'users/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

""" 
class SignupView(FormView):
    template_name="users/signup.html"
    form_class=SignupForm
    success_url=reverse_lazy("posts:feed")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["errors"] = error_form_list(str(self.form_class.errors))
        return context
    
    def form_valid(self, form):
        form.save(self.request)
        return super().form_valid(form)
"""

def signup_view(request):
    
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('users:login')
        else:
            list_errors=error_form_list(str(form.errors))
            ###print(list_errors)
    else:
        form=SignupForm()
        list_errors=[]

    context={
        "form": form,
        "errors": list_errors,
    }
        
    return render(request, 'users/signup.html', context)

@login_required
def update_profile_view(request):

    user=request.user
    profile=user.profile
    form=UpdateProfileForm()

    errors=[]
    if request.method=='POST':
        form=UpdateProfileForm(request.POST, request.FILES)
        if (not profile.picture) and (not request.FILES):
            errors.append("Please enter an picture")
        else:
            if form.is_valid():
                form.save(user, profile)
                return redirect("users:update_profile")
        
    if len(errors)==0:
        errors=False
    context={
        'profile': profile,
        'user': user,
        'form': form,
        'errors': errors,
    }
    return render(request, 'users/update_profile.html', context)
