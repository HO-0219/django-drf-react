# resume_views/resume_list_views.py

from rest_framework import generics, permissions
from ..models import Resume
from ..serializers import ResumeSerializer

class ResumeListView(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # 로그인된 유저의 이력서만 필터링
        return Resume.objects.filter(user=self.request.user).order_by('-created_at')
