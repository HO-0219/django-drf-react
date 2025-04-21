# resume_views/resume_detail_views.py

from rest_framework import generics, permissions
from ..models import Resume
from ..serializers import ResumeSerializer
from rest_framework.exceptions import PermissionDenied

class ResumeDetailView(generics.RetrieveAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        resume = super().get_object()
        if resume.user != self.request.user:
            raise PermissionDenied("이력서는 본인만 조회할 수 있습니다.")
        return resume
