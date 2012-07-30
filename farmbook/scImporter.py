from farmbook.models import Coop
from datetime import date
import random
import urllib

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
  'test',
  ]

coopUrls = [
#  "https://dl.dropbox.com/s/5suxefyfsjkaln5/test.csv?dl=1",
]

def getOrCreateItem(columns):
def getOrCreateCropInput(columns):
def getOrCreateCrop(columns):

def getOrCreateCultivation(columns):
def getOrCreateFarmers(columns):
  

def getOrCreateProvince(pname):
  #find if province exits, if it doesn't, create it
  existingProvince = Province.objects.filter(
    name = pname
    )
  if existingProvince == []:
    p = Province(
      name = pname,
      )
    p.save()
  else:
    p = existingProvince[0]
  return p

def getOrCreateMunicipality(p, mcname):
  #find if municipality city exits, if it doesn't, create it
  existingMunicipalityCity = MunicipalityCity.objects.filter(
    province = p,
    name mcname,
    )
  if existingMunicipalityCity == []:
    mc = MunicipalityCity(
      province = p,
      name mcname,
      )
    mc.save()
  else:
    mc = existingMunicipalityCity[0]
  return mc

def getOrCreateStreetBarangay(mc, sbname):
  #find if street barangay exits, if it doesn't, create it
  existingStreetBarangay = StreetBarangay.objects.filter(
    municipalityCity = mc,
    name = sbname,
    )
  if existingStreetBarangay == []:
    gpsCoord = GPSCoord(
      longtitue = random.uniform(90,120),
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
  existingPerson = Person.objetcs.filter(
    name = contactName,
    contactTelNum = contactTelNum,
    contactMobileNum = contactMobileNum,
    contactEmail = contactEmail,
    )
  if existingPerson == []:
    person = Person(
      name = name,
      contactTelNum = contactTelNum,
      contactMobileNum = contactMobileNum,
      contactEmail = contactEmail,
      dateOfBirth = datetime.date.today(),
    )
  else:
    person = existingPerson[0]
  return person

def createCoop(columns):
  i = 1
  coopId = int(columns[i]); i+=1
  coop.registrationNum = int(columns[i]); i+=1
  dateList = columns[i].split('/'); i+1 #mth, day, year
  coop.registrationDate = datetime.date(dateList[2],dateList[0],dateList[1])
  coop.oldRegistrationNumber = int(columns[i]); i+=1
  coop.oldRegistrationDate = int(columns[i]); i+=1
  coop.name = columns[i]; i+=1
  coop.category = columns[i]; i+=1
  coop.type = columns[i]; i+=1

  sbname = columns[i]; i+=1
  mcname = columns[i]; i+=1
  pname = columns[i]; i+=1
  p = getOrCreateProvince(pname)
  mc = getOrCreateMunicipality(p,mcname)
  coop.streetBarangay = getOrCreateStreetBarangay(mc, sbname)

  coop.bodMale = int(columns[i]); i+=1
  coop.bodFemale = int(columns[i]); i+=1
  coop.membesMale = int(columns[i]); i+=1
  coop.membesFemale = int(columns[i]); i+=1
  coop.numMembers = int(columns[i]); i+=1
  coop.totalAssets = int(columns[i]); i+=1
  coop.commonAuthorized = int(columns[i]); i+=1
  coop.preferredAuthorized = int(columns[i]); i+=1
  coop.commonSubscribed = int(columns[i]); i+=1
  coop.preferredSubscribed = int(columns[i]); i+=1
  coop.commonPaidUp = int(columns[i]); i+=1
  coop.preferredPaidUp = int(columns[i]); i+=1
  coop.birTin = columns[i]; i+=1

  contactName = columns[i]; i+=1
  contactTelNum = columns[i]; i+=1
  contactMobileNum = columns[i]; i+=1
  contactEmail = columns[i]; i+=1
  coop.contactPerson = getOrCreateContact(contactName, contactTelNum, contactMobileNum, contactEmail)
  coop.save()
  return coop

def getOrCreateCoop(columns):
  #find if coop exists, if it doesn't, create it
  existingCoop = Province.objects.filter(
    coopId = int(columns[1])
    )
  if existingCoop == []:
    coop = createCoop(columns)
  else:
    coop = existingCoop[0]
    print 'Coop '+coopId+' already exists. This is odd (should double check the data file).'
  return coop

for fname in coopUrls:
  f = urllib.urlopen(fname)
  for line in f.readline.split('\r')
    columns = line.split(',')
    for col in coopFilesColumns:
      getOrCreateCoop(getCoopParam(col))
  f.close()

for fname in coopFiles:
  f = open(fname)
  for line in f:
    columns = line.split(',')
    for col in coopFilesColumns:
      getOrCreateCoop(getCoopParam(col))
  f.close()
    
