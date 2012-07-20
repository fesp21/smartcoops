from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=100)

class municipalityCity(models.Model):
    name = models.CharField(max_length=100
    province = models.ForeignKey(Province))

class GPSCoord(models.Model):
    longitude = models.DecimalField(decimal_places=6)
    latitude = models.DecimalField(decimal_places=6)

class streetBarangay(models.Model):
    name = models.CharField(max_length=100)
    municipalityCity = models.ForeignKey(municipalityCity))
    gpsCoord = models.OneToOneField(GPSCoord)

class Person(models.Model):
    name = models.CharField(max_length=200)
    contactTelNum = models.CharField(max_length=200)
    contactMobileNum = models.CharField(max_length=200)
    contactEmail = models.EmailField()
    dateOfBirth = models.DateField()

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
    streetBarangay = models.ForeignKey(StreamBarangay)
    municipalityCity = models.ForeignKey(MinicipalityCity)
    province = models.ForeignKey(Province)
    bodMale = models.PositiveIntegerField()
    bodFemale = models.PositiveIntegerField()
    membesMale = models.PositiveIntegerField()
    membesFemale = models.PositiveIntegerField()
    numMembers = models.PositiveIntegerField()
    totalAssets = models.DecimalField(decimal_places=2)
    commonAuthorized = models.DecimalField(decimal_places=2)
    preferredAuthorized = models.DecimalField(decimal_places=2)
    commonSubscribed = models.DecimalField(decimal_places=2)
    preferredSubscribed = models.DecimalField(decimal_places=2)
    commonPaidUp = models.DecimalField(decimal_places=2)
    preferredPaidUp = models.DecimalField(decimal_places=2)
    birTin = models.TextField()
    contactPerson = models.CharField(max_length=100)
    contactTelNum = models.CharField(max_length=200)
    contactMobileNum = models.CharField(max_length=200)
    contactEmail = models.EmailField()

class CropInput(models.Model):
    name = models.CharField(max_length=200)
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
    price = models.DecimalField(decimal_places=2)

class Crop(models.Model):
    name = models.CharField(max_length=200)
    cropInputs = models.ManyToManyField(CropInput)

class Cultivation(models.Model):
    crop = models.ForeignKey(Crop)
    hectare = models.DecimalField(decimal_places=2)

class purchaseItem(models.Model):
    quantity = models.DecimalField(decimal_places=2)
    item = models.ForeignKey(i
    prince
    
class Purchases(models.Model):
    purchaseDate = models.DateTimeField('Purchase date')
    purchaseItems = models.ManyToManyField(purchaseItem)

class Farmer(models.Model):
    name = models.CharField(max_length=200)
    coop = models.ForeignKey(Coop) #could farmers be part of more than one coop?
    mobileNum = models.CharField(max_lenght=100)
    cultivations = models.ManyToManyField(Cultivation)
    loanBalance = models.DecimalField(decimal_places=2)
    savingsBalance = models.DecimalField(decimal_places=2)
    purchaseHistory = models.ForeignKey(PurchaseHistory)

