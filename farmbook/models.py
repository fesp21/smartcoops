from django.db import models

class Province(models.Model):
    name = models.CharField("Province", max_length=100)
    def __unicode__(self):
        return self.name

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
    coopId = models.PositiveIntegerField("Coop ID number")
    registrationNum = models.SlugField("Registration number", max_length=20)
    registrationDate = models.DateField('Date of registration')
    oldRegistrationNumber = models.CharField("Old registration number", max_length=20)
    oldRegistrationDate = models.DateField('Old registration date')
    name = models.CharField("Cooperative name", max_length=200)
    CATEGORY_CHOICES = ((u'Primary',u'Primary'),(u'Secondary',u'Secondary'))
    category = models.CharField("Category", max_length=50, choices=CATEGORY_CHOICES)
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
    streetBarangay = models.ForeignKey(StreetBarangay) #municipalityCity and province can be infered from streetBarangay
    bodMale = models.PositiveIntegerField("BOD Male")
    bodFemale = models.PositiveIntegerField("BOD Female")
    membesMale = models.PositiveIntegerField("Number of male members")
    membesFemale = models.PositiveIntegerField("Number of female members")
    numMembers = models.PositiveIntegerField("Number of members") #could be computed
    totalAssets = models.DecimalField("Total assets", max_digits=20,decimal_places=2)
    commonAuthorized = models.DecimalField("Common authorized assets", max_digits=20,decimal_places=2)
    preferredAuthorized = models.DecimalField("Preferred authorized assets", max_digits=20,decimal_places=2)
    commonSubscribed = models.DecimalField("Common subscribed assets", max_digits=20,decimal_places=2)
    preferredSubscribed = models.DecimalField("Preferred subscribed assets", max_digits=20,decimal_places=2)
    commonPaidUp = models.DecimalField("Common paid up assets", max_digits=20,decimal_places=2)
    preferredPaidUp = models.DecimalField("Preferred paid up assets", max_digits=20,decimal_places=2)
    birTin = models.TextField("BIR TIN")
    contactPerson = models.ForeignKey(Person)
    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField("Item", max_length=200)
    price = models.DecimalField("Price", max_digits=20,decimal_places=2)
    def __unicode__(self):
        return self.name

class CropInput(Item):
    manufacturer = models.CharField("Manufacturer", max_length=200)
    activeIngredients = models.TextField("Active ingredients")
    brand = models.CharField("Brand", max_length=200)
    units = models.CharField("Units", max_length=50)
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
    recommendedUsage = models.TextField("Recommended Usage")

class Crop(Item):
    cropInputs = models.ManyToManyField(CropInput)

class Farmer(Person):
    coop = models.ForeignKey(Coop) #could farmers be part of more than one coop?
    loanBalance = models.DecimalField("Loan balance", max_digits=20,decimal_places=2)
    savingsBalance = models.DecimalField("Savings balance", max_digits=20,decimal_places=2)

class Cultivation(models.Model):
    crop = models.ForeignKey(Crop)
    hectare = models.DecimalField("Number of hectares", max_digits=20,decimal_places=2)
    farmer = models.ForeignKey(Farmer)
    def __unicode__(self):
        return self.farmer.name + ": " + self.crop.name + " (" + str(self.hectare) + " hectares)"

class Purchase(models.Model):
    purchaseDate = models.DateTimeField('Date of purchase')
    farmer = models.ForeignKey(Farmer)
    def __unicode__(self):
        return "Purchase by " + self.farmer.name + " on " + str(self.purchaseDate)

class PurchasedItem(models.Model):
    quantity = models.DecimalField("Quantity", max_digits=20,decimal_places=2)
    item = models.ForeignKey(Item)
    price = models.DecimalField("Price", max_digits=20,decimal_places=2)
    purchase = models.ForeignKey(Purchase)
    def __unicode__(self):
        return self.purchase.farmer.name + " purchased " + str(self.quantity) + " units of " + self.item.name + " for a price of " + str(self.price)
        
class IncomingText(models.Model):
    msgType = models.CharField('Message Type', max_length=5)
    msgId = models.CharField('Message ID', max_length=50)
    source = models.CharField('Source', max_length=11)
    target = models.CharField('Target', max_length=8)
    msg = models.TextField('Message', blank=True)
    udh = models.TextField('User Data Header', blank=True)
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True)

    def __unicode__(self):
        return u'(%s) %s' % (self.source, self.msgType)
    
    class Meta:
        ordering = ['-timestamp']

