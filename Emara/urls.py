from django.conf.urls import url
from django.contrib import admin
from Emara import views
from django.contrib.auth import views as auth_views
from . import views as Emara_views


urlpatterns = [
    url(r'^$', views.IndexPageView.as_view()),
    url(r'^sections/$', views.SectionsPageView.as_view()),
    url(r'^papers/$', views.PapersPageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^question/$', views.QuestionPageView.as_view()),
    #url(r'^login/$', auth_views.login, {'template_name':'Emara/login.html'}, name = 'login'),
    url(r'^logout/$', auth_views.logout),
    url(r'^notes/$', views.NotesPageView.as_view()),
    url(r'^login/$', views.LoginPageView.as_view()),
    url(r'^signup/$', Emara_views.signup),
    url(r'^contact/$', views.ContactPageView.as_view()),
]
   