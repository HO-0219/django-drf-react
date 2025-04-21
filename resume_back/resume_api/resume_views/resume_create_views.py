# resume_views/resume_create_views.py

from rest_framework import generics, permissions
from ..models import Resume
from ..serializers import ResumeSerializer

class ResumeCreateView(generics.CreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        print("현재 로그인된 유저:", self.request.user)  # ✅ 이거로 확인 가능!
        serializer.save(user=self.request.user)