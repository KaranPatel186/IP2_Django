from django.contrib import admin

from accounts.models import *

admin.site.register(CounsellingSession)
admin.site.register(Counseller)
admin.site.register(MoodTrackerData)
admin.site.register(SessionChanges)
admin.site.register(Client)
admin.site.register(VideoFiles)

