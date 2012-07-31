from farmbook.models import *
from django.contrib import admin
from django.db import models

admin.site.register(Province)
admin.site.register(MunicipalityCity)
admin.site.register(GPSCoord)
admin.site.register(StreetBarangay)

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
                    'name',
                    'dateOfBirth',
                    ]}),
        ('Contact', {'fields':[
                    'contactTelNum',
                    'contactMobileNum',
                    'contactEmail',
                    ]}),
        ]
    list_display = ['name','dateOfBirth','contactMobileNum']

admin.site.register(Person, PersonAdmin)

class CoopAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
                    'name',
                    ]}),
        ('General', {'fields':[
                    'streetBarangay',
                    'coopType',
                    'category',
                    ]}),
        ('Registration',{'fields':[
                    'coopId',
                    'registrationNum',
                    'registrationDate',
                    'oldRegistrationNumber',
                    'oldRegistrationDate',
                    ]}),
        ('People',{'fields':[
                    'contactPerson',
                    'numMembers',
                    'bodMale',
                    'bodFemale',
                    'membesMale',
                    'membesFemale',
                    ]}),
        ('Finance',{'fields':[
                    'totalAssets',
                    'commonAuthorized',
                    'preferredAuthorized',
                    'commonSubscribed',
                    'preferredSubscribed',
                    'commonPaidUp',
                    'preferredPaidUp',
                    'birTin',
                    ]}),
        ]
    list_display = ['name','coopType','numMembers','streetBarangay']
    list_filter = ['streetBarangay']
    search_fields = ['name']

admin.site.register(Coop, CoopAdmin)
admin.site.register(Item)

class CropInputAdmin(admin.ModelAdmin):
    list_display = ['name','price','units','brand']
    list_filter = ['brand']
    search_fields = ['name']

admin.site.register(CropInput, CropInputAdmin)

class CropAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    #list_filter = ['name']
    search_fields = ['name']

admin.site.register(Crop, CropAdmin)

class CultivationInline(admin.TabularInline):
    model = Cultivation
    extra = 1

class FarmerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
                    'name',
                    'dateOfBirth',
                    'coop',
                    ]}),
        ('Contact information', {'fields':[
                    'contactTelNum',
                    'contactMobileNum',
                    'contactEmail']}),
        ('Financial',{'fields':[
                    'loanBalance',
                    'savingsBalance']}),
        ]
    inlines = [CultivationInline]
    list_display = ['name','loanBalance','savingsBalance','coop']
    list_filter = ['coop']
    search_fields = ['name']

admin.site.register(Farmer, FarmerAdmin)

class CultivationAdmin(admin.ModelAdmin):
    list_display = ['farmer','crop','hectare']
    list_filter = ['farmer__name']
    search_fields = ['farmer__name','crop__name']

admin.site.register(Cultivation, CultivationAdmin)

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

class IncomingSMSAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
                    'source',
                    'timestamp',
                    'msg',
                    ]}),
        ('SMS Info', {'fields': [
                    'msgType',
                    'msgId',
                    'target',
                    'udh',
                    ]}),
        ]
    list_display = ['source','timestamp','msg']
    list_filter = ['timestamp']
    search_fields = ['source']

admin.site.register(IncomingSMS, IncomingSMSAdmin)
