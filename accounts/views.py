from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from  django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import RegisterForm
from  django.contrib.auth.decorators import login_required
from article.models import Article 
from accounts.models import UserProfile
from django.urls import reverse,reverse_lazy
from  django.contrib.auth.models import User


def registerView (request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/home")
        else:
            print(form.errors)
       
    else:
        form=RegisterForm()
    return render(request,"registration/register.html",{'form':form})

@login_required
def profileView (request):
    current_user =request.user 
    user_articles=Article.objects.filter(author =current_user)
    return render(request,"account/profile.html",{'user_articles':user_articles})


class UpdateProfileView (LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=UserProfile
    template_name='account/update_profile.html'
    fields = ('profile_pic','name','public_email','bio','website','company','title','location')

    def test_func(self):
        post=self.get_object()
        if self.request.user ==post.user:
            return True
        return False

    def get_object (self):
        return UserProfile.objects.get(user=self.request.user.profile.user)

    def get_success_url (self):
        return reverse_lazy ('profile')

    def form_valid (self,form):
        form.instance.user =self.request.user
        return super().form_valid(form)

class UpdateAccountView (LoginRequiredMixin,UpdateView):
    model=User
    template_name='account/update_account.html'
    fields = ('username','first_name','last_name','email')

  

    def get_object (self):
        return self.request.user

    def get_success_url (self):
        return reverse_lazy ('profile')

    def form_valid (self,form):
        form.instance.user =self.request.user
        return super().form_valid(form)