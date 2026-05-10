from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, User, Application


def dashboard(request):
    return render(request, 'dashboard.html', {
        'jobs': Job.objects.count(),
        'applications': Application.objects.count(),
        'users': User.objects.count()
    })


def users_list(request):
    return render(request, 'users.html', {'users': User.objects.all()})

from django.db import IntegrityError

def add_user(request):
    if request.method == 'POST':
        try:
            User.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                address=request.POST.get('address'),
                qualification=request.POST.get('qualification'),
                skills=request.POST.get('skills')
            )
            return redirect('users')

        except IntegrityError:
            return render(request, 'add_user.html', {
                'error': "❌ Email already exists!"
            })

    return render(request, 'add_user.html')


def edit_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.address = request.POST.get('address')
        user.qualification = request.POST.get('qualification')
        user.skills = request.POST.get('skills')
        user.save()
        return redirect('users')

    return render(request, 'edit_user.html', {'user': user})


def view_user(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'view_user.html', {'user': user})


def delete_user(request, id):
    get_object_or_404(User, id=id).delete()
    return redirect('users')


def job_list(request):
    return render(request, 'jobs.html', {'jobs': Job.objects.all()})


# APPLY FROM JOB PAGE
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    users = User.objects.all()

    if request.method == 'POST':
        user = User.objects.get(id=request.POST['user'])

        # ❌ block if already applied
        if Application.objects.filter(user=user).exists():
            return render(request, 'apply.html', {
                'job': job,
                'users': users,
                'error': "User already applied to a job!"
            })

        Application.objects.create(user=user, job=job)
        return redirect('applications')

    return render(request, 'apply.html', {'job': job, 'users': users})


# 🔥 ADD APPLICATION FEATURE
def add_application(request):
    users = User.objects.all()
    jobs = Job.objects.all()

    if request.method == 'POST':
        user = User.objects.get(id=request.POST['user'])
        job = Job.objects.get(id=request.POST['job'])

        # ✅ CHECK FIRST (IMPORTANT)
        if Application.objects.filter(user=user).exists():
            return render(request, 'add_application.html', {
                'users': users,
                'jobs': jobs,
                'error': "❌ This user has already applied to a job!"
            })

        # ✅ CREATE ONLY IF NOT EXISTS
        Application.objects.create(user=user, job=job)
        return redirect('applications')

    return render(request, 'add_application.html', {
        'users': users,
        'jobs': jobs
    })


def applications_list(request):
    return render(request, 'applications.html', {
        'applications': Application.objects.all()
    })


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, 'job_detail.html', {'job': job})


def logout_view(request):
    return redirect('/')

def add_job(request):
    if request.method == 'POST':
        Job.objects.create(
            title=request.POST.get('title'),
            company=request.POST.get('company'),
            location=request.POST.get('location'),
            salary=request.POST.get('salary'),
            description=request.POST.get('description')
        )
        return redirect('jobs')

    return render(request, 'add_job.html')

def edit_job(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == 'POST':
        job.title = request.POST.get('title')
        job.company = request.POST.get('company')
        job.location = request.POST.get('location')
        job.salary = request.POST.get('salary')
        job.description = request.POST.get('description')
        job.save()
        return redirect('jobs')

    return render(request, 'edit_job.html', {'job': job})


def delete_job(request, id):
    job = get_object_or_404(Job, id=id)
    job.delete()
    return redirect('jobs')