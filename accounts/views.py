from django.shortcuts import get_object_or_404, render,redirect
from django.views import View
from .forms import UserRegistrationForm,UserLoginForm,ProfileUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate 
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin



class UserRegisteration(View):
    form= UserRegistrationForm
    template_name = 'accounts/register.html'


    def get(self,request):
        form=self.form
        return render(request, 'accounts/register.html', {'form':form})


    def post (self, request):
        form=self.form(request.POST)
        if form.is_valid() :
            cd=form.cleaned_data
            user=User.objects.create_user(cd['username'], cd['email'], cd['password'])
            Profile.objects.create(user=user)
            messages.success(request, 'your login successfully', 'info')
            return redirect('core:home')
        return render(request, 'accounts/register.html', {'form':form})    



class UserLogin(View):
    form=UserLoginForm

    def get(self, request):
        form=self.form
        return render(request, 'accounts/login.html', {'form':form})


    def post(self, request):
        form=self.form(request.POST)
        if form.is_valid() :
            cd=form.cleaned_data
            user=authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None :
                login(request, user)
                messages.success(request, 'you are logged in', 'success')
                return redirect('core:home')
            else:
                messages.error(request, 'your input is incorrect', 'danger') 
               
        return render(request, 'accounts/login.html', {'form':form})   


class UserLogout(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request, 'you are logged in', 'success')
        return redirect('core:home')



class Dashboard(LoginRequiredMixin,View):
    def get(self,request,username):
        form=ProfileUserForm()
        user=get_object_or_404(User, username=username)
        return render(request, 'accounts/dashbord.html', {'user':user, 'form':form})    


    def post(self,request,*args,**kwargs):
       
        form=ProfileUserForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() :
         form.save()
         messages.success(request, 'your image uploaded', 'success')
         return redirect('accounts:dashboard', request.user.username) 






