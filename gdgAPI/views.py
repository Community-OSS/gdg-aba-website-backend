from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CommunityTalentSerializer
from .models import CommunityTalent
# Create your views here.


class CommunityTalentViewSet(viewsets.ModelViewSet):
    queryset = CommunityTalent.objects.all()
    serializer_class = CommunityTalentSerializer

