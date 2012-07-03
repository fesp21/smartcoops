import re, csv
from datetime import datetime

provinces = ['Abra','Agusan del Norte','Agusan del Sur','Aklan','Albay','Antique','Apayao','Aurora','Basilan','Bataan','Batanes','Batangas','Benguet','Biliran','Bohol','Bukidnon','Bulacan','Cagayan','Camarines Norte','Camarines Sur','Camiguin','Capiz','Catanduanes','Cavite','Cebu','Compostela Valley','Cotabato','Davao del Norte','Davao del Sur','Davao Oriental','Dinagat Islands','Eastern Samar','Guimaras','Ifugao','Ilocos Norte','Ilocos Sur','Iloilo','Isabela','Kalinga','La Union','Laguna','Lanao del Norte','Lanao del Sur','Leyte','Maguindanao','Marinduque','Masbate','Misamis Occidental','Misamis Oriental','Mountain Province','Negros Occidental','Negros Oriental','Northern Samar','Nueva Ecija','Nueva Vizcaya','Occidental Mindoro','Oriental Mindoro','Palawan','Pampanga','Pangasinan','Quezon','Quirino','Rizal','Romblon','Samar','Sarangani','Siquijor','Sorsogon','South Cotabato','Southern Leyte','Sultan Kudarat','Sulu','Surigao del Norte','Surigao del Sur','Tarlac','Tawi-Tawi','Zambales','Zamboanga del Norte','Zamboanga del Sur','Zamboanga Sibugay','Metro Manila']

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
    def __init__(self, name = None):
        self.name = name
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

# written by Mike Brown
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/148061
def wrap_onspace(text, width):
    """
    A word-wrap function that preserves existing line breaks
    and most spaces in the text. Expects that existing line
    breaks are posix newlines (\n).
    """
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
    smsBorder = '-'*len(smsSeparator)
    width = len(smsSeparator)
    print '\n\n'+smsSeparator
    print datetime.now().strftime("%a, %b %d at %I:%M%p") + ". New SMS from " + sendingNum + ":"
    print smsBorder
    try:
        print wrap_onspace(body, width)
    except WordLengthError as e:
        print 'Error', e.value
    print smsSeparator

def firstTime():
    """Informs the farmer of what SMART Coop is, and of the cost"""
    s = "Hello, it is the first time you are using SMART Coops. "
    s = s + "Note that SMS sent to and received from SMART Coops are free of charge, so do not worry about your load balance."
    smsPrint(scn, s)

def getSMS():
    print '\n'
    prompt = 'Send a new SMS to ' + scn + ' (SMART Coops) :\nMessage Content > '
    newSMS = raw_input(prompt)
    print '\n                          Message Sent....\n\n\n\n\n'
    return newSMS

def getName():
    """Retrieves and confirms the name of the farmer"""
    s = ''
    while s.lower() != 'yes':
        smsPrint(scn, "Please reply to this SMS with your name (ex: Capitan, Sergio).")
        name = getSMS()
        smsPrint(scn, "Pleased to meet you "+name+". Did I get your name correctly? (Reply yes or no). ")
        s = getSMS()
    return name

def getNearbyCoops(loc):
    """presumably we would retrive information from the telco as to the location from where the farmer is calling from, and use that in the getCoop function"""
    return ['San Benito Multipurpose Coop', 'San Pablo Cooperative', 'Calamba Association of Rice Planters']

def getCoop(loc):
    s = 'no coop'
    coops = getNearbyCoops(loc)
    coopsStr = ''
    for i in range(1,len(coops)+1):
        coopsStr = coops[i-1] + str(i) + ") "
    otherOptionsStr = str(i+1) + ") Other, " + str(i+2) + ") I am not a member of a cooperative"
    smsPrint(scn, "I see that you are sending me messages from near "+loc.getName()+". Which cooperative are you a member of? Type the corresponding number: " + coopsStr + otherOptionsStr) 
    s = getSMS()
    while s.lower != 'yes':
        if s in ['1', '2', '3']:
            smsPrint(scn, "You are a member of "+nearbyCoopsStr)
            s = 'yes'
        else:
            smsPrint(scn, 'boohoo')
    
scn = "+63 151 888 4444" #Smart Coops number

getSMS()

f = Farmer()
firstTime()
f.setName(getName())
smsPrint(scn, "Great, thank you for confirming your name, "+f.getName()+". SMART Coop helps you find out about prices for crop inputs, crop produce, loans, and more.")

loc = Location("San Pablo, Languna")
f.setCoop(getCoop(loc))
