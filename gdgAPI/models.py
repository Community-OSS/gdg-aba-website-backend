from django.db import models

# Create your models here.
class CommunityTalent(models.Model):
    full_name = models.CharField(max_length=255)
    tech_niche = models.JSONField()
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    behance_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name