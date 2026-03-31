from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
User=settings.AUTH_USER_MODEL


class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    description = models.TextField()


    recruiter = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    STATUS_CHOICES = (
        ('applied,','Applied'),
        ('shortlisted','Shortlisted'),
        ('interview','Interview'),
        ('selected','Selected'),
        ('rejected','Rejected'),
    )
    candidate = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)  
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='resumes/',validators=[FileExtensionValidator(allowed_extensions=['pdf','docx,'])],null=True,blank=True)
    def __str__(self):  
        return f"{self.candidate} - {self.job}"

