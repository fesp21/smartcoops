from django.db import models

class Province(models.Model):
    name = models.CharField("Province", max_length=100)
    def __unicode__(self):
        return self.name
    #TODO: figure out how to ensure uniqueness of Provinces    
    #class Meta:
    #    unique = True

class MunicipalityCity(models.Model):
    name = models.CharField("Municipality or city", max_length=100)
    province = models.ForeignKey(Province)
    def __unicode__(self):
        return self.name + ", " + self.province.name

class GPSCoord(models.Model):
    longitude = models.DecimalField("GPS longitude", max_digits=20,decimal_places=6)
    latitude = models.DecimalField("GPS latitude", max_digits=20,decimal_places=6)
    def __unicode__(self):
        return "("+str(self.longitude)+", "+str(self.latitude)+")"

class StreetBarangay(models.Model):
    name = models.CharField("Street or barangay", max_length=100)
    municipalityCity = models.ForeignKey(MunicipalityCity)
    gpsCoord = models.OneToOneField(GPSCoord)
    def __unicode__(self):
        return self.name

class Person(models.Model):
    name = models.CharField("Name", max_length=200)
    contactTelNum = models.CharField("Telephone",max_length=200)
    contactMobileNum = models.CharField("Mobile",max_length=200)
    contactEmail = models.EmailField("Email")
    dateOfBirth = models.DateField("Date of birth")
    #    address = models.TextField()
    def __unicode__(self):
        return self.name

class Coop(models.Model):
    name = models.CharField("Cooperative name", max_length=200)
    streetBarangay = models.ForeignKey(StreetBarangay) #municipalityCity and province can be infered from streetBarangay 
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
    coopType = models.CharField("Type of cooperative", max_length=50, choices=COOP_TYPE_CHOICES)
    CATEGORY_CHOICES = ((u'Primary',u'Primary'),(u'Secondary',u'Secondary'))
    category = models.CharField("Category", max_length=50, choices=CATEGORY_CHOICES)
    coopId = models.PositiveIntegerField("Coop ID number")
    registrationNum = models.CharField("Registration number", max_length=20)
    registrationDate = models.DateField('Date of registration')
    oldRegistrationNumber = models.CharField("Old registration number", max_length=20)
    oldRegistrationDate = models.DateField('Old registration date')
    contactPerson = models.ForeignKey(Person)
    numMembers = models.PositiveIntegerField("Number of members") #could be computed
    bodMale = models.CharField("BOD Male", max_length=20)
    bodFemale = models.CharField("BOD Female", max_length=20)
    membesMale = models.CharField("Number of male members", max_length=20)
    membesFemale = models.CharField("Number of female members", max_length=20)
    totalAssets = models.CharField("Total assets", max_length=20)
    commonAuthorized = models.CharField("Common authorized assets", max_length=20)
    preferredAuthorized = models.CharField("Preferred authorized assets", max_length=20)
    commonSubscribed = models.CharField("Common subscribed assets", max_length=20)
    preferredSubscribed = models.CharField("Preferred subscribed assets", max_length=20)
    commonPaidUp = models.CharField("Common paid up assets", max_length=20)
    preferredPaidUp = models.CharField("Preferred paid up assets", max_length=20)
    birTin = models.TextField("BIR TIN")

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField("Item", max_length=200)
    price = models.DecimalField("Price", max_digits=20,decimal_places=2)
    def __unicode__(self):
        return self.name

class CropInput(Item):
    units = models.CharField("Units", max_length=50)
    brand = models.CharField("Brand", max_length=200)
    manufacturer = models.CharField("Manufacturer", max_length=200)
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
    category =  models.CharField("Category", max_length=50, choices=CATEGORY_CHOICES)
    activeIngredients = models.TextField("Active ingredients")
    recommendedUsage = models.TextField("Recommended Usage")

class Crop(Item):
    cropInputs = models.ManyToManyField(CropInput,blank=True)

class Farmer(Person):
    coop = models.ForeignKey(Coop) #could farmers be part of more than one coop?
    loanBalance = models.DecimalField("Loan balance", max_digits=20,decimal_places=2)
    savingsBalance = models.DecimalField("Savings balance", max_digits=20,decimal_places=2)

class Cultivation(models.Model):
    farmer = models.ForeignKey(Farmer)  
    crop = models.ForeignKey(Crop)
    hectare = models.DecimalField("Number of hectares", max_digits=20,decimal_places=2)
    def __unicode__(self):
        return self.farmer.name + ": " + self.crop.name + " (" + str(self.hectare) + " hectares)"

class Purchase(models.Model):
    purchaseDate = models.DateTimeField('Date of purchase')
    farmer = models.ForeignKey(Farmer)
    def __unicode__(self):
        return "Purchase by " + self.farmer.name + " on " + str(self.purchaseDate)

class PurchasedItem(models.Model):
    item = models.ForeignKey(Item)
    quantity = models.DecimalField("Quantity", max_digits=20,decimal_places=2)
    price = models.DecimalField("Price", max_digits=20,decimal_places=2)
    purchase = models.ForeignKey(Purchase)
    def __unicode__(self):
        return self.purchase.farmer.name + " purchased " + str(self.quantity) + " units of " + self.item.name + " for a price of " + str(self.price)

class IncomingSMS(models.Model):
    msgType = models.CharField('Message Type', max_length=5)
    msgId = models.CharField('Message ID', max_length=50)
    source = models.CharField('Source', max_length=11)
    target = models.CharField('Target', max_length=8)
    msg = models.TextField('Message', blank=True)
    udh = models.TextField('User Data Header', blank=True)
    timestamp = models.DateTimeField('Timestamp') #, auto_now=True)
    def __unicode__(self):
        return u'(%s) %s' % (self.source, self.msgType)
    class Meta:
        ordering = ['-timestamp']
