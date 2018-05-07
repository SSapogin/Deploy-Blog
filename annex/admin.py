from django.contrib import admin
from annex.models import Company
from annex.models import Profile
from annex.models import Work

admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(Work)
