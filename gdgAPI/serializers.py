from dataclasses import field
from .models import CommunityTalent
from rest_framework import serializers


class CommunityTalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityTalent
        fields = ('id', 'full_name', 'tech_niche', 'twitter_url',
                  'linkedin_url', 'github_url', 'behance_url')
        
    tech_niche = serializers.DictField(source='tech_niche')
