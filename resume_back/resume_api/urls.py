from django.urls import path
from .resume_views import ResumeListView, ResumeDetailView, ResumeCreateView


urlpatterns = [
    path('resumes_lists/', ResumeListView.as_view(), name='resume_list'),
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
    path('resumes_create/', ResumeCreateView.as_view(), name='resume-create'),

]
