# artist/views.py

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer

class RegisterAPIView(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = []

class WorkListAPIView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]

class WorkCreateAPIView(generics.CreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]

class WorkFilterByTypeView(generics.ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        work_type = self.request.query_params.get('work_type')
        return Work.objects.filter(work_type=work_type)

class WorkSearchByArtistView(generics.ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        artist_name = self.request.query_params.get('artist')
        return Work.objects.filter(artist__name=artist_name)
# Add other API views as needed
