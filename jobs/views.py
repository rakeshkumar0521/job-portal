from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def create_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            return redirect("job_list")   
    else:
        form = JobForm()
    
    return render(request, 'jobs/create_job.html', {'form': form})

@login_required
def job_list(request):
    query = request.GET.get('q')
    location = request.GET.get('location')
    jobs = Job.objects.all()


    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(company__icontains=query)
        )

    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)

    if request.method == "POST":
        resume = request.FILES.get('resume')

        if Application.objects.filter(candidate=request.user, job=job).exists():
            return redirect('job_list')

        Application.objects.create(candidate=request.user, job=job, resume=resume)
        return redirect('job_list')

    return render(request, 'jobs/apply_job.html', {'job': job})
@login_required
def applicants_view(request, job_id):
    job = Job.objects.get(id=job_id)
    applications = Application.objects.filter(job=job)

    return render(request, 'jobs/applicants.html', {
        'applications': applications,
        'job': job
    })

@login_required
def update_status(request, app_id):
    application = Application.objects.get(id=app_id)

    if request.method == "POST":
        new_status = request.POST.get('status')
        application.status = new_status
        application.save()

    return redirect('applicants_view', job_id=application.job.id)

@login_required
def recruiter_dashboard(request):
    jobs = Job.objects.filter(recruiter=request.user)  
    return render(request, 'jobs/recruiter_dashboard.html', {"jobs": jobs})


@login_required
def candidate_dashboard(request):
    applications = Application.objects.filter(candidate=request.user)
    return render(request, 'jobs/candidate_dashboard.html', {'applications': applications})