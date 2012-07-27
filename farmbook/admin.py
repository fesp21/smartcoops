from farmbook.models import *
from django.contrib import admin
from django.db import models

admin.site.register(Province)
admin.site.register(MunicipalityCity)
admin.site.register(GPSCoord)
admin.site.register(StreetBarangay)
admin.site.register(Person)
admin.site.register(Coop)
admin.site.register(Item)
admin.site.register(CropInput)
admin.site.register(Crop)

class CultivationInline(admin.TabularInline):
    model = Cultivation
    extra = 3

class FarmerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name','coop']}),
        ('Contact information', {'fields':['contactTelNum','contactMobileNum','contactEmail']}),
        ('Financial',{'fields':['loanBalance','savingsBalance']}),
        ]
    inlines = [CultivationInline]
    list_display = ['name','loanBalance','savingsBalance','coop']
    list_filter = ['coop']
    search_fields = ['name']

admin.site.register(Farmer, FarmerAdmin)
admin.site.register(Cultivation)

class PurchasedItemInline(admin.TabularInline):
    model = PurchasedItem
    extra = 3

class PurchaseAdmin(admin.ModelAdmin):
    inlines = [PurchasedItemInline]
    list_display = ['farmer','purchaseDate']
    list_filter =  ['farmer','purchaseDate']
    date_hierarchy = 'purchaseDate'

admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchasedItem)

admin.site.register(IncomingText)
