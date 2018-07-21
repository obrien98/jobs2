from django.shortcuts import render, redirect
from .models import User, Job, EmailSubscriber
from .forms import EmployerSignupForm, JobPostForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import os
import stripe


from django.http import HttpResponse




# Create your views here.
def delete(request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()
    return redirect("employer_home")

def edit_job(request, job_id):
    job =Job.objects.get(id=job_id)
    form = JobPostForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            job_object = form.save(commit=False)
            job_object.poster = request.user.employer
            job_object.save()
            return redirect('employer_home')
    else:
        form = JobPostForm(instance=job)

    return render(request, 'core/edit_job.html', {'form':form})



def email_subscription(request):
    email = request.GET.get('email')
    zip_code = request.GET.get('zip_code')
    email_subscriber = EmailSubscriber(email = email, zip_code = zip_code)
    email_subscriber.save()

    query = zip_code
    jobs_matching_query = Job.objects.filter(zip_code__iexact=query) | Job.objects.filter(
        city__iexact=query) | Job.objects.filter(state__iexact=query)
    number_of_results = 0
    for job in jobs_matching_query:
        number_of_results = number_of_results + 1
    return render(request, 'core/subscribed.html',
                  {'query': query, 'jobs_matching_query': jobs_matching_query, 'number_of_results': number_of_results})



@login_required
def employer_home(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job_object = form.save(commit=False)
            job_object.poster = request.user.employer
            job_object.save()
            return redirect('employer_home')


    else:
        form = JobPostForm()

    active_posts = Job.objects.filter(poster=request.user.employer)
    return render(request, 'core/employer_home.html', {'form': form, 'active_posts': active_posts})

def employer_login_and_signup(request):
    if request.method == 'POST':
        form = EmployerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password = raw_password)
            login(request, user)
            return redirect('employer_home')


    else:
        form = EmployerSignupForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employer_home')

    return render(request, 'core/employer_login_and_register.html', {'form':form})

def employer_signup(request):
    if request.method == 'POST':
        form = EmployerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password = raw_password)
            login(request, user)
            return redirect('employer_home')
    else:
        form = EmployerSignupForm()
    return render(request, 'core/employer_signup.html', {'form': form})


def job_info(request, job_id):

    job = Job.objects.get(id=job_id)

    return render(request, 'core/job_info.html', {"job" : job})


def job_query(request):
    if request.method == "GET":
        query = request.GET.get('query')
        jobs_matching_query = Job.objects.filter(zip_code__iexact = query) | Job.objects.filter(city__iexact=query) | Job.objects.filter(state__iexact=query)
        number_of_results = 0
        for job in jobs_matching_query:
            number_of_results = number_of_results + 1
        return render(request, 'core/search.html', {'query': query ,'jobs_matching_query': jobs_matching_query, 'number_of_results': number_of_results})




def index(request):
    jobs = Job.objects.all
    return render(request, 'core/index.html', {'jobs' :jobs })




def logout_view(request):
    logout(request)
    return render(request, 'core/index.html',)


def payment(request):
    # Set your secret key: remember to change this to your live secret key in production
    # See your keys here: https://dashboard.stripe.com/account/apikeys
    stripe.api_key = "sk_test_BJUliYkgS5VZEKFM1UQAz9cF"

    # Token is created using Checkout or Elements!
    # Get the payment token ID submitted by the form:
    token = request.POST['stripeToken']

    charge = stripe.Charge.create(
        amount=999,
        currency='usd',
        description='Example charge',
        source=token,
    )
