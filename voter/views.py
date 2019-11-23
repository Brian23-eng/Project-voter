from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Rating
from rest_framework import viewsets
from . forms import PostForm, UpdateUserProfileForm,UpdateUserForm, RatingsForm
from .serializer import PostSerializer, ProfileSerializer, UserSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import random   


def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
    else:
        form = PostForm()
        
    try:
        posts = Post.objects.all()
        posts = posts[::-1]
        a_post = random.randint(0, 1(posts(-1)))
        random_post = posts[a_post]
        print(random_post.photo)
        
    except Post.DoesNotExist:
        posts = None
            
    return render(request,'home.html', {'posts':posts, 'forms':form, 'random_post':random_post})



class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile.html')

def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof
    }
    
    return render(requet,'userprofile.html', params)


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'edit.html', params)

