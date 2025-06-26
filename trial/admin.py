from django.contrib import admin
from .models import content, TrialReview, Store, trialcertificate

class TrialReviewInLine(admin.TabularInline):
   model = TrialReview
   extra = 1
   
class TrialContentAdmin(admin.ModelAdmin):
   list_display = ('name','type','date_added')
   inlines = [TrialReviewInLine]
   
class StoreAdmin(admin.ModelAdmin):
   list_display = ['name']
   filter_horizontal = ['contents']
    
class TrialCertAdmin(admin.ModelAdmin):
   list_display = ('trial', 'certificate_number')
   
   
admin.site.register(content, TrialContentAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(trialcertificate, TrialCertAdmin)