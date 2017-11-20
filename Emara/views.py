from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from Emara.forms import ContactForm
from .models import Home, Sections, Papers, About, Contact
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from .forms import SignUpForm


# Create your views here.
class IndexPageView(TemplateView):
    def get(self, request, **kwargs ):
        return render(request, 'index.html', context=None)
        
class SectionsPageView(TemplateView):
    template_name ="section.html"
    
class PapersPageView(TemplateView):
    template_name = "papers.html"
    
class QuestionPageView(TemplateView):
    template_name ="question.html"
    
class LoginPageView(TemplateView):
    template_name = "login.html"
    
    
class NotesPageView(TemplateView):
    template_name = "notes.html"
    
    
class AboutPageView(TemplateView):
    template_name = "about.html"
    
class ContactPageView(TemplateView):
    template_view = "contact.html"
    
    def get(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect(request.path_info)    



def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # return redirect('/index')
            return render(request, 'index.html', { 'form': form })
            
            return render(request, 'signup.html', { 'form': form })
            
    else:
        form = SignUpForm()
        return render(request, 'signup.html', { 'form': form })
            
            
            
            
            
            
            
            
            
            
            
        










