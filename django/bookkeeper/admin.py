from bookkeeper.models import *
from django.contrib import admin

#class CropInputAdmin(admin.ModelAdmin):
 ###   fieldsets = [
    #    (None,               {'fields': ['category']}),
     #   ('Date information', {'fields': ['name'], 'classes': ['collapse']}),
   # ]
#    fields = ['name','category'] #could be used to reorganize fields

admin.site.register(Farmer)
admin.site.register(Coop)
admin.site.register(Crop)
admin.site.register(CropInput,CropInputAdmin)
