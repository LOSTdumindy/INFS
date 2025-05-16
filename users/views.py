from django.urls import reverse_lazy
from django.shortcuts import  render
from django.views import View
from .models import User
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import CreateView

class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'app/customerregistration.html'
    object_context_name = 'form'
    success_url = reverse_lazy('website:home')
    success_message = 'Registration successful!'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserRegistrationView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = UserProfileForm(instance=request.user)
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})
      
    def post(self, request):
        form = UserProfileForm(request.POST, instance=request.user)  
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Profile has been updated!')
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})


def login(request):
    return render(request, 'app/login.html')
