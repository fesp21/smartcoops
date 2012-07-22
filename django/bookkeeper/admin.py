from bookkeeper.models import *
from django.contrib import admin

#class CropInputAdmin(admin.ModelAdmin):
 ###   fieldsets = [
    #    (None,               {'fields': ['category']}),
     #   ('Date information', {'fields': ['name'], 'classes': ['collapse']}),
   # ]
#    fields = ['name','category'] #could be used to reorganize fields

class PurchasedItemInline(admin.TabularInline):
    model = PurchasedItem
    extra = 3

class PurchaseAdmin(admin.ModelAdmin):
    inlines = [PurchasedItemInline]
    list_display = ['farmer','purchaseDate']

admin.site.register(Province)
admin.site.register(MunicipalityCity)
admin.site.register(GPSCoord)
admin.site.register(StreetBarangay)
admin.site.register(Person)
admin.site.register(Coop)
admin.site.register(Item)
admin.site.register(CropInput)
admin.site.register(Crop)
admin.site.register(Farmer)
admin.site.register(Cultivation)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchasedItem)
