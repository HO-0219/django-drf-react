# models/resume.py

from django.db import models
from django.conf import settings

class Skill(models.Model):
    name = models.CharField(max_length=50 , null=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=100,default='포트폴리오 제목')
    description = models.TextField(blank=True, null=True)  
    link = models.URLField(blank=True , null=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resumes')
    title = models.CharField(max_length=100, default='이력서 제목')
    summary = models.TextField(blank=True , null=True)  # 자기소개 등
    skills = models.ManyToManyField(Skill, blank=True, related_name='resumes')
    portfolios = models.ManyToManyField(Portfolio, blank=True, related_name='resumes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.user_id} - {self.title}"
