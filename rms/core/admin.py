from django.contrib import admin
from .models import Responsibility, JobDescription, Skill, JobDescriptionToSkillMapping, \
    JobDescriptionToResponsibilityMapping

admin.site.register(Responsibility)
admin.site.register(JobDescription)
admin.site.register(Skill)
admin.site.register(JobDescriptionToSkillMapping)
admin.site.register(JobDescriptionToResponsibilityMapping)
