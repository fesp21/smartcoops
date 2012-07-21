from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class MunicipalityCity(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province)
    def __unicode__(self):
        return self.name

class GPSCoord(models.Model):
    longitude = models.DecimalField(max_digits=20,decimal_places=6)
    latitude = models.DecimalField(max_digits=20,decimal_places=6)
    def __unicode__(self):
        return str(self.longitude)+"-"+str(self.latitude)

class StreetBarangay(models.Model):
    name = models.CharField(max_length=100)
    municipalityCity = models.ForeignKey(MunicipalityCity)
    gpsCoord = models.OneToOneField(GPSCoord)
    def __unicode__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=200)
    contactTelNum = models.CharField("Telephone",max_length=200)
    contactMobileNum = models.CharField("Mobile",max_length=200)
    contactEmail = models.EmailField("Email")
    dateOfBirth = models.DateField("Date of birth")
    def __unicode__(self):
        return self.name

class Coop(models.Model):
    coopId = models.PositiveIntegerField()
    registrationNum = models.SlugField(max_length=20)
    registrationDate = models.DateField('Date registered')
    oldRegistrationNumber = models.CharField(max_length=20)
    oldRegistrationDate = models.DateField('Old date registered')
    name = models.CharField(max_length=200)
    CATEGORY_CHOICES = ((u'Primary',u'Primary'),(u'Secondary',u'Secondary'))
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    COOP_TYPE_CHOICES = (
        (u'Credit','Credit'),
	(U'Multi-Purpose','Multi-Purpose'),
	(U'Credit','Credit'),
	(U'Consumer','Consumer'),
	(U'Service','Service'),
	(U'Federation-Secondary','Federation-Secondary'),
	(U'Marketing','Marketing'),
	(U'Producer','Producer'),
	(U'Coop Bank-Secondary','Coop Bank-Secondary'),
	(U'Union-Secondary','Union-Secondary'),
	(U'Transport','Transport'),
        )
    coopType = models.CharField(max_length=50, choices=COOP_TYPE_CHOICES)
    streetBarangay = models.ForeignKey(StreetBarangay) #municipalityCity and province can be infered from streetBarangay
    bodMale = models.PositiveIntegerField()
    bodFemale = models.PositiveIntegerField()
    membesMale = models.PositiveIntegerField()
    membesFemale = models.PositiveIntegerField()
    numMembers = models.PositiveIntegerField() #could be computed
    totalAssets = models.DecimalField(max_digits=20,decimal_places=2)
    commonAuthorized = models.DecimalField(max_digits=20,decimal_places=2)
    preferredAuthorized = models.DecimalField(max_digits=20,decimal_places=2)
    commonSubscribed = models.DecimalField(max_digits=20,decimal_places=2)
    preferredSubscribed = models.DecimalField(max_digits=20,decimal_places=2)
    commonPaidUp = models.DecimalField(max_digits=20,decimal_places=2)
    preferredPaidUp = models.DecimalField(max_digits=20,decimal_places=2)
    birTin = models.TextField()
    contactPerson = models.ForeignKey(Person)
    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    def __unicode__(self):
        return self.name

class CropInput(Item):
    manufacturer = models.CharField(max_length=200)
    activeIngredients = models.TextField()
    brand = models.CharField(max_length=200)
    units = models.CharField(max_length=50)
    CATEGORY_CHOICES = (
        (U'Fertilizer','Fertilizer'),
        (U'Fungicides','Fungicides'),
        (U'Herbicide','Herbicide'),
        (U'Insecticide','Insecticide'),
        (U'Plant growth regulators','Plant growth regulators'),
        (u'Rat poison','Rat poison'),
        (u'Seed treatment','Seed treatment'),
        (U'Seeds','Seeds'),
        )
    category =  models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    recommendedUsage = models.TextField()

class Crop(Item):
    cropInputs = models.ManyToManyField(CropInput)

class Farmer(Person):
    coop = models.ForeignKey(Coop) #could farmers be part of more than one coop?
    loanBalance = models.DecimalField(max_digits=20,decimal_places=2)
    savingsBalance = models.DecimalField(max_digits=20,decimal_places=2)

class Cultivation(models.Model):
    crop = models.ForeignKey(Crop)
    hectare = models.DecimalField(max_digits=20,decimal_places=2)
    farmer = models.ForeignKey(Farmer)
    def __unicode__(self):
        return self.crop.name

class Purchase(models.Model):
    purchaseDate = models.DateTimeField('Purchase date')
    farmer = models.ForeignKey(Farmer)
    def __unicode__(self):
        return "Purchase by " + self.farmer.person.name 

class PurchasedItem(models.Model):
    quantity = models.DecimalField(max_digits=20,decimal_places=2)
    item = models.ForeignKey(Item)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    purchase = models.ForeignKey(Purchase)
    def __unicode__(self):
        return purchase.farmer.name + " purchased " + str(quantity) + " units of " + item.name + " for a price of " + str(price)
