"""jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login,logout
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name="index"),

    url(r'^business_owners_info$', views.business_owners_info, name="business_owners_info"),

    url(r'^delete/(?P<job_id>.*)$', views.delete, name="delete"),

    url(r'^edit_job/(?P<job_id>.*)$', views.edit_job, name="edit_job"),

    url(r'^email_subscription$', views.email_subscription, name="email_subscription"),

    url(r'^employer_home$', views.employer_home, name="employer_home"),

    url(r'^Register/$', views.employer_signup, name="employer_signup"),

    url(r'^job_info/(?P<job_id>[0-9]+)/$', views.job_info, name="job_info"),

    url(r'^job_seekers_info', views.job_seekers_info, name="job_seekers_info"),

    url(r'^login/$', login, {'template_name': 'core/employer_login.html'}, name='login'),

    url(r'^logout/$', views.logout_view, name='logout'),

    url(r'^search$', views.job_query, name="search"),


    url(r'payment$', views.payment, name="payment"),



]
