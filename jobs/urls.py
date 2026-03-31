from django.urls import path
from .views import*

urlpatterns = [
    path('create/',create_job, name="create"),
    path('list/', job_list, name='job_list'),
    path('apply/<int:job_id>/',apply_job, name='apply_job'),
    path('applicants/<int:job_id>/',applicants_view,name='applicants_view'),
    path('update-status/<int:app_id>/', update_status, name = 'update_status'),
    path('candidate-dashboard',candidate_dashboard,name='candidate_dashboard'),
    path('recruiter-dashboard',recruiter_dashboard,name='recruiter_dashboard'),
    path('my-applications/', candidate_dashboard, name='my_applications'),
   
    ]
