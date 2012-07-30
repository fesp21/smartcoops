from farmbook.models import *
from datetime import date
import random, urllib, csv

from farmbook.testCropInputs import cropInputs
from farmbook.testPhilippinesData import provinces, citiesOrMunici
from farmbook.testCrops import crops

coopFiles = [
#  'ARMM_1445',
#  'CARAGA_1076',
#  'CAR_746',
#  'NCR_2239',
#  'REGION_10_1495',
#  'REGION_11_1709',
#  'REGION_12_1042',
#  'REGION_1_1298.csv',
#  'REGION_2_811.csv',
#  'REGION_3_2079.csv',
#  'REGION_4_2533.csv',
#  'REGION_5_821',
#  'REGION_6_1362',
#  'REGION_7_1574',
#  'REGION_8_684',
#  'REGION_9_760',
#  '/Users/danny/Dropbox/SMART_Coops/Market_Data/Coop_List/test.csv',
  'farmbook/testCoops.csv',
  ]

coopUrls = [
  #"https://dl.dropbox.com/s/5suxefyfsjkaln5/test.csv?dl=1",
]

def getOrCreateItem(columns):
  print 'hello'

def getOrCreateCropInput(cropInput):
  #find if cropInput exits, if it doesn't, create it
  existingCI = list(CropInput.objects.filter(
      name = cropInput['productName'],
      manufacturer = cropInput['brand'],
      brand = cropInput['brand'],
      units = cropInput['units'],
      category =  cropInput['category'],
      ))
  if existingCI == []:
    ci = CropInput(
      name = cropInput['productName'],
      price = cropInput['price'],
      manufacturer = cropInput['brand'],
      activeIngredients = cropInput['productIngredient'],
      brand = cropInput['brand'],
      units = cropInput['units'],
      category =  cropInput['category'],
      recommendedUsage = cropInput['recommendedUsage'],
      )
    ci.save()
  else:
    ci = existingCI[0]
  return ci

for cropInput in cropInputs:
  getOrCreateCropInput(cropInput)

def getOrCreateCrop(name, price, cropInputs):
  #find if crop exits, if it doesn't, create it
  existingCrop = list(Crop.objects.filter(
      name = name
      ))
  if existingCrop == []:
    crop = Crop(
      name = name,
      price = price
      )
    for ci in cropInputs:
      crop.cropInputs.add(ci)
    crop.save()
  else:
    crop = existingCrop[0]
  return crop
  
for crop in crops:
  price = random.uniform(40,200)
  getOrCreateCrop(crop,price,[])

def getOrCreateCultivation(columns):
  print 'hello'

def getOrCreateFarmers(columns):
  print 'hello'

def getOrCreateProvince(pname):
  #find if province exits, if it doesn't, create it
  existingProvince = list(Province.objects.filter(
    name = pname
    ))
  if existingProvince == []:
    p = Province(
      name = pname,
      )
    p.save()
  else:
    p = existingProvince[0]
  return p

for p in provinces:
  getOrCreateProvince(p)

def getOrCreateMunicipality(p, mcname):
  #find if municipality city exits, if it doesn't, create it
  existingMunicipalityCity = list(MunicipalityCity.objects.filter(
    province = p,
    name = mcname,
    ))
  if existingMunicipalityCity == []:
    mc = MunicipalityCity(
      province = p,
      name = unicode(mcname),
      )
    mc.save()
  else:
    mc = existingMunicipalityCity[0]
  return mc

for prov in provinces:
  p = getOrCreateProvince(prov)
  if citiesOrMunici.has_key(prov):
    for cm in citiesOrMunici[prov]:
      getOrCreateMunicipality(p, cm)

def getOrCreateStreetBarangay(mc, sbname):
  #find if street barangay exits, if it doesn't, create it
  existingStreetBarangay = list(StreetBarangay.objects.filter(
    municipalityCity = mc,
    name = sbname,
    ))
  if existingStreetBarangay == []:
    gpsCoord = GPSCoord(
      longitude = random.uniform(90,120),
      latitude = random.uniform(90,120),
      )
    gpsCoord.save()
    sb = StreetBarangay(
      name = sbname,
      municipalityCity = mc,
      gpsCoord = gpsCoord,
      ) 
    sb.save()
  else:
    sb = existingStreetBarangay[0]
  return sb

def getOrCreateContact(contactName, contactTelNum, contactMobileNum, contactEmail):
#find if person exits, if it doesn't, create it
  existingPerson = list(Person.objects.filter(
    name = contactName,
    contactTelNum = contactTelNum,
    contactMobileNum = contactMobileNum,
    contactEmail = contactEmail,
    ))
  if existingPerson == []:
    person = Person(
      name = contactName,
      contactTelNum = contactTelNum,
      contactMobileNum = contactMobileNum,
      contactEmail = contactEmail,
      dateOfBirth = date.today(),
    )
    person.save()
  else:
    person = existingPerson[0]
  return person

def createCoop(columns):
  i = 1 #ignore first column with useless id
  coopId = int(columns[i]); i+=1
  registrationNum = columns[i]; i+=1
  dateList = columns[i].split('/'); i+=1 #mth, day, year
  registrationDate = date(1900+int(dateList[2]),int(dateList[0]),int(dateList[1]))
  oldRegistrationNumber = columns[i]; i+=1
  dateList = columns[i].split('/'); i+=1 #mth, day, year
  oldRegistrationDate = date(1900+int(dateList[2]),int(dateList[0]),int(dateList[1]))
  name = columns[i]; i+=1
  category = columns[i]; i+=1
  coopType = columns[i]; i+=1

  sbname = columns[i]; i+=1
  mcname = columns[i]; i+=1
  pname = columns[i]; i+=1
  p = getOrCreateProvince(pname)
  mc = getOrCreateMunicipality(p,mcname)
  streetBarangay = getOrCreateStreetBarangay(mc, sbname)

  bodMale = columns[i]; i+=1
  bodFemale = columns[i]; i+=1
  membesMale = columns[i]; i+=1
  membesFemale = columns[i]; i+=1
  numMembers = int(columns[i]); i+=1
  totalAssets = columns[i]; i+=1
  commonAuthorized = columns[i]; i+=1 #float(columns[i].replace(',', '')); i+=1
  preferredAuthorized = columns[i]; i+=1
  commonSubscribed = columns[i]; i+=1
  preferredSubscribed = columns[i]; i+=1 
  commonPaidUp = columns[i]; i+=1
  preferredPaidUp = columns[i]; i+=1
  birTin = columns[i]; i+=1

  contactName = columns[i]; i+=1
  contactTelNum = columns[i]; i+=1
  contactMobileNum = columns[i]; i+=1
  contactEmail = columns[i]; i+=1
  contactPerson = getOrCreateContact(contactName, contactTelNum, contactMobileNum, contactEmail)
  
  coop = Coop(
    coopId = coopId,
    registrationNum = registrationNum,
    registrationDate = registrationDate,
    oldRegistrationNumber = oldRegistrationNumber,
    oldRegistrationDate = oldRegistrationDate,
    name = name,
    category = category,
    coopType = coopType,
    streetBarangay = streetBarangay,
    bodMale = bodMale,
    bodFemale = bodFemale,
    membesMale = membesMale,
    membesFemale = membesFemale,
    numMembers = numMembers,
    totalAssets = totalAssets,
    commonAuthorized = commonAuthorized,
    preferredAuthorized = preferredAuthorized,
    commonSubscribed = commonSubscribed,
    preferredSubscribed = preferredSubscribed,
    commonPaidUp = commonPaidUp,
    preferredPaidUp = preferredPaidUp,
    birTin = birTin,
    contactPerson = contactPerson,
    )  
  coop.save()
  return coop

def getOrCreateCoop(columns):
  #find if coop exists, if it doesn't, create it
  existingCoop = list(Coop.objects.filter(
    coopId = int(columns[1])
    ))
  if existingCoop == []:
    coop = createCoop(columns)
    print 'Coop '+columns[1]+' created'
  else:
    coop = existingCoop[0]
    print 'Coop '+columns[1]+' already exists. This is odd (should double check the data file).'
  return coop

#TODO fix the problem iwht universal-newline mode
for fname in coopUrls:
  f = urllib.urlopen(fname, "rU")
  line = csv.reader(f, dialect='excel')
  line.next() #ignore header line lines[0]
  for col in line:
    getOrCreateCoop(col)
  f.close()
  
#/Users/danny/Dropbox/SMART_Coops/Market_Data/Coop_List/test.csv
for fname in coopFiles:
  f = open(fname, "U")
  line = csv.reader(f, dialect='excel')
  line.next() #ignore header line lines[0]
  for col in line:
    getOrCreateCoop(col)
  f.close()

