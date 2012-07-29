from farmbook.models import Coop
from datetime import date
import random

coopFiles = [
#  'ARMM_1445',
#  'CARAGA_1076',
#  'CAR_746',
#  'NCR_2239',
#  'REGION_10_1495',
#  'REGION_11_1709',
#  'REGION_12_1042',
  'REGION_1_1298.csv',
  'REGION_2_811.csv',
  'REGION_3_2079.csv',
  'REGION_4_2533.csv',
#  'REGION_5_821',
#  'REGION_6_1362',
#  'REGION_7_1574',
#  'REGION_8_684',
#  'REGION_9_760',
  ]

def createCoop(col):
  coop = Coop()  
  i = 0
  coop.coopId = int(columns[i]); i+=1
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

  #find if province exits, if it doesn't, create it
  existingProvince = Province.objects.filter(
    name = pname
    )
  if existingProvince == []:
    p = existingProvince
  else:
    p = Province(name = pname)
    p.save()

  #find if municipality city exits, if it doesn't, create it
  existingMunicipalityCity = MunicipalityCity.objects.filter(
    province = p,
    name mcname,
    )
  if existingMunicipalityCity == []:
    mc = existingMunicipalityCity
  else:
    mc = existingMunicipalityCity(
      province = p,
      name mcname,
      )
    mc.save()

  #find if street barangay exits, if it doesn't, create it
  existingStreetBarangay = StreetBarangay.objects.filter(
    name = sbname,
    municipalityCity = mc,
    )
  if existingStreetBarangay == []:
    sb = existingStreetBarangay
  else:
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

  coop.streetBarangay = sb

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

  name = columns[i]; i+=1
  contactTelNum = columns[i]; i+=1
  contactMobileNum = columns[i]; i+=1
  contactEmail = columns[i]; i+=1
  
  existingPerson = Person.objetcs.filter(
    name = name,
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
    person = existingPerson
  coop.contactPerson = person
  
  coop.save()

for fname in coopFiles:
  f = open(fname)
  for line in file:
    columns = line.split(',')
  
    for col in coopFilesColumns:
      createCoop(col)
  file.close()
    
