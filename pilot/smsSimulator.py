import re, csv, time
from datetime import datetime


provinces = ['Abra','Agusan del Norte','Agusan del Sur','Aklan','Albay','Antique','Apayao','Aurora','Basilan','Bataan','Batanes','Batangas','Benguet','Biliran','Bohol','Bukidnon','Bulacan','Cagayan','Camarines Norte','Camarines Sur','Camiguin','Capiz','Catanduanes','Cavite','Cebu','Compostela Valley','Cotabato','Davao del Norte','Davao del Sur','Davao Oriental','Dinagat Islands','Eastern Samar','Guimaras','Ifugao','Ilocos Norte','Ilocos Sur','Iloilo','Isabela','Kalinga','La Union','Laguna','Lanao del Norte','Lanao del Sur','Leyte','Maguindanao','Marinduque','Masbate','Misamis Occidental','Misamis Oriental','Mountain Province','Negros Occidental','Negros Oriental','Northern Samar','Nueva Ecija','Nueva Vizcaya','Occidental Mindoro','Oriental Mindoro','Palawan','Pampanga','Pangasinan','Quezon','Quirino','Rizal','Romblon','Samar','Sarangani','Siquijor','Sorsogon','South Cotabato','Southern Leyte','Sultan Kudarat','Sulu','Surigao del Norte','Surigao del Sur','Tarlac','Tawi-Tawi','Zambales','Zamboanga del Norte','Zamboanga del Sur','Zamboanga Sibugay','Metro Manila']

locations = {'Abra': ['Blah','Bleh']}

class Farmer():
    """Farmers have a name, a mobile phone number, and possibly belong to a coop"""

    def __init__(self, mobileNum = None, name = None, coop = None):
        self.mobileNum = mobileNum
        self.name = name
        self.coop = coop

    def getMobileNum(self):
        return mobileNum
    def setMobileNum(self, mobileNum):
        self.mobileNum = mobileNum

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def getCoop(self):
        return self.coop
    def setCoop(self, coop):
        self.coop = coop

    def getCrops(self):
        return crops
    def setCrops(self, crops):
        self.crops = crops

    def getLoanBalance(self):
        return self.loanBalance
    def withDraw(self,amount):
        self.loanBalance = self.loanBalance - amount
    def deposit(self,amount):
        self.loanBalance = self.loanBalance + amount

class Location():
    """Each exchange has a location as provided by the telco, which we use to inform the farmer of prices or local resources"""
    def __init__(self, gpsCoord = None):
        self.gpsCoord = gpsCoord
        self.name = 'San Benito, Laguna' # we would need a function getNearestCity(gpsCoord)
    def getGPSCoord(self):
        return self.gpsCoord
    def setGPSCoord(self, name):
        self.gpsCoord = gpsCoord
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

# written by Mike Brown
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/148061
def wrap_onspace(text, width):
    """A word-wrap function that preserves existing line breaks
    and most spaces in the text. Expects that existing line
    breaks are posix newlines (\n).  """
    return reduce(lambda line, word, width=width: '%s%s%s' %
                  (line,
                   ' \n'[(len(line[line.rfind('\n')+1:])
                         + len(word.split('\n',1)[0]
                              ) >= width)],
                   word),
                  text.split(' ')
                 )

def smsPrint(sendingNum, body):
    """Prints a pretty sms msg on the terminal"""
    smsSeparator = "==================================================================="
    width = len(smsSeparator)
    smsBorder = '-'*width
    print '\n\n'+smsSeparator
    print datetime.now().strftime("%a, %b %d at %I:%M%p") + ". New SMS from " + sendingNum + ":"
    print smsBorder
    print wrap_onspace(body, width)
    print smsSeparator
    time.sleep(.5)

def firstTime():
    """Informs the farmer of what SMART Coop is, and of the cost"""
    s = "Hello, it is the first time you are using SMART Coops. "
    s = s + "Note that SMS sent to and received from SMART Coops are free of charge, so do not worry about your load balance."
    smsPrint(scn, s)

def getSMS():
    """Simulates the user sending an SMS to SMART Coops"""
    print '\n'
    prompt = 'Send a new SMS to ' + scn + ' (SMART Coops) :\nMessage Content > '
    newSMS = raw_input(prompt)
    print '\n                          Sending message',
    for i in range(1,8):
        print '.',
        time.sleep(.25)
    print '\n\n\n\n\n'
    return newSMS

def getName():
    """Retrieves and confirms the name of the farmer"""
    s = ''
    while s.lower() != 'yes':
        smsPrint(scn, "Please reply to this SMS with your name (ex: Capitan, Sergio).")
        name = getSMS()
        smsPrint(scn, "Pleased to meet you "+name+". Did I get your name correctly? (Reply yes or no). ")
        s = getSMS()
    smsPrint(scn, "Great, thank you for confirming your name, "+name+". SMART Coop helps you find out about prices for crop inputs, crop produce, loans, and more.")
    return name

def getGPSCoord():
    """presumably we would retrive information from the telco as to the location from where the farmer is calling from, and use that in the getCoop function, not implemented"""
    return 0

def getNearbyCoops(loc):
    """given a location, returns the nearby cooperatives"""
    return ['San Benito Multipurpose Coop', 'San Pablo Cooperative', 'Calamba Association of Rice Planters']

def searchList(myStr, myList):
    """Returns the set of strings resulting from a substring search"""
    pattern = re.compile(r'.*'+myStr+'.*')
    results = []
    for l in myList
        r = re.search(pattern,l)
        if r is not None:
            results.append(r)
    return results

def makeListStr(myList):
    myStr = ''
    for i in range(1,len(myList)+1):
        myStr = myStr + ' ' + str(i) + ")" + myList[i-1] + ','
    return myStr

def getProvince():
    ans = ''
    likelyProvinces = []
    while ans != 'yes':
        reply = 'What province is your farm located in (e.g. '
        smsPrint(scn, reply + random.choice(provinces) + ', please try to spell the name as completely as possible)?')
        likelyProvinces = searchProvinces(getSMS())
        ans = ''
        if len(likelyProvinces) == 1:
            smsPrint(scn, "Is your farm located in "+likelyProvince[0]+"? (yes or no)")
            ans = getSMS()
        else:
            smsPrint(scn, "Unfortunately the following provinces match your spelling: " + makeListStr(likelyProvinces))
    return likelyProvinces[0]

def getLoc(province):
    ans = ''
    likelyProvinces = []
    while ans != 'yes':
        reply =  'What city or baranguay is your farm located nearest to (e.g. '
        smsPrint(scn, reply + random.choice(locations) + ', please try to spell the name as completely as possible)?')
        likelyProvinces = searchProvinces(getSMS())
        ans = ''
        if len(likelyProvinces) == 1:
            smsPrint(scn, "Is your farm located in "+likelyProvince[0]+"? (yes or no)")
            ans = getSMS()
        else:
            smsPrint(scn, "Unfortunately the following provinces match your spelling: " + makeListStr(likelyProvinces))
    return likelyProvinces[0]



    

def getCoop(loc):
    coops = getNearbyCoops(loc)
    optionsStr = makeListStr(coops+['Other', 'Not member of a cooperative'])
    s = ''
    smsPrint(scn, "I see that you are sending messages from near "+loc.getName()+". Which cooperative are you a member of?" + optionsStr)
    while s.lower != 'yes':
        ans = getSMS()
        if ans in range(1,len(coops)+1):
            smsPrint(scn, "You are a member of "+coops[coopId]+", is this correct? (yes or no)")
            s = getSMS()
        elif ans == len(coops):
            loc.setName() = getLoc(getProvince)
    
   

scn = "+63 151 888 4444" #Smart Coops number
getSMS()

f = Farmer()
firstTime()
f.setName(getName())
loc = Location(getGPSCoord())
f.setCoop(getCoop(loc))
