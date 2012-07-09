import re, csv, time, random, getopt, sys, locale
from datetime import datetime
import philippinesData, cropInputsData

#Global variables
scn = "+63 915 866 8018" #Smart Coops number
sleepTime = .1 #to simulate time in between SMS messages, 1.5 secs more realistic
affirmativeAns = ['yes','y','ye','ya','oo','1']

provinces = philippinesData.provinces
citiesOrMunici = philippinesData.citiesOrMunici
coops = philippinesData.coops
crops = philippinesData.crops
cropInputs = cropInputsData.cropInputs

class Farmer():
    """Farmers have a name, a mobile phone number, and possibly belong to a coop"""

    def __init__(self, mobileNum = None, name = None, coop = None, crops = None, loanBal = 0, savingsBal = 0):
        self.mobileNum = mobileNum
        self.name = name
        self.coop = coop
        self.crops = crops
        self.loanBal = loanBal
        self.savingsBal = savingsBal

    def getMobileNum(self):
        return self.mobileNum
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
        return self.crops
    def setCrops(self, crops):
        self.crops = crops

    def getLoanBal(self):
        return self.loanBal
    def setLoanBal(self, loanBal):
        self.loanBal = loanBal

    def getSavingsBal(self):
        return self.savingsBal
    def savingsWithdraw(self,amount):
        self.savingsBal = self.savingsBal - amount
    def savingsDeposit(self,amount):
        self.savingsBal = self.savingsBal + amount

#For debugging purposes
sampleFarmer = Farmer(12341234,'Danny Castonguay','San Benito Multipurpose Coop',[{'name':'Cloves','size':1.5},{'name':'Cocoa beans','size':12.7},{'name':'Coconuts','size':6},{'name':'Coffee, green','size':22}],1200000,600000)

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

def searchList(myStr, myList):
    """Returns the set of strings resulting from a substring search"""
    pattern = re.compile(r'.*'+myStr+'.*', re.IGNORECASE)
    results = []
    for l in myList:
        r = re.search(pattern,l)
        if r is not None:
            results.append(r.group())
    return results

def makeListStr(myList):
    myStr = ''
    for i in range(1,len(myList)+1):
        myStr = myStr + ' ' + str(i) + ") " + myList[i-1] + ','
    return myStr[1:-1]

def affirmative(ans):
    return any([ans.lower() == x for x in affirmativeAns])

def phPesos(value):
    """Formats a numerical value into a string with thousand separators ','"""
    return 'P'+'{:,.2f}'.format(value)

def smsPrint(sendingNum, body):
    """Prints a pretty sms msg on the terminal"""
    smsSeparator = "=================================================================="
    width = len(smsSeparator)
    smsBorder = '-'*width
    print '\n\n'+smsSeparator
    print datetime.now().strftime("%a, %b %d at %I:%M%p") + ". New SMS from " + sendingNum + ":"
    print smsBorder
    print wrap_onspace(body, width)
    print smsSeparator
    time.sleep(sleepTime)

def getSMS():
    """Simulates the user sending an SMS to SMART Coops"""
    print '\n'
    prompt = 'Send a new SMS to ' + scn + ' (SMART Coops) :\nMessage Content > '
    newSMS = raw_input(prompt)
    print '\n                                     Message sent...\n\n\n\n\n',
    time.sleep(sleepTime)
    print '\n\n\n\n\n'
    return newSMS

def getName():
    """Retrieves and confirms the name of the farmer"""
    confirmation = ''
    while not affirmative(confirmation):
        smsPrint(scn, "Please reply to this SMS with your name (ex: Capitan, Sergio).")
        name = getSMS()
        smsPrint(scn, "Pleased to meet you "+name+". Did I get your name correctly? (Reply yes or no). ")
        confirmation = getSMS()
    smsPrint(scn, "Great, thank you for confirming your name, "+name+". SMART Coop helps you find out about prices for crop inputs, crop produce, loans, and more.")
    return name

def getGPSCoord():
    """presumably we would retrive information from the telco as to the location from where the farmer is calling from, and use that in the getCoop function, not implemented"""
    return 0

def getNearbyCoops(loc):
    """given a location, returns the nearby cooperatives"""
    return ['San Benito Multipurpose Coop', 'San Pablo Cooperative', 'Calamba Association of Rice Planters']


def getProvince():
    """getCityOrMunici and getProvince could be refactored into one"""
    confirmation = 'no'
    likelyProvinces = []
    while not affirmative(confirmation):
        reply = 'What province is your farm located in (e.g. '
        smsPrint(scn, reply + random.choice(provinces) + ')? Please try to spell the name as completely as possible.')
        likelyProvinces = searchList(getSMS(),provinces)
        if len(likelyProvinces) == 1:
            smsPrint(scn, "Is your farm located in "+likelyProvinces[0]+"? (yes or no)")
            confirmation = getSMS()
        elif len(likelyProvinces) == 0:
            smsPrint(scn, "Please be more specific, no province matches your spelling.")
        else:
            smsPrint(scn, "Please be more specific, many provinces match your spelling: " + makeListStr(likelyProvinces))
    return likelyProvinces[0]

def getCityOrMunici(province):
    """getCityOrMunici and getProvince could be refactored into one"""
    confirmation = 'no'
    likelyCitiesOrMunici = []
    while not affirmative(confirmation):
        reply =  'Your farm is in '+province+' province. What city or municipality is it located nearest to (e.g. '
        reply += random.choice(citiesOrMunici[province]) + ')? '
        smsPrint(scn, reply + 'Please try to spell the name as completely as possible.')
        likelyCitiesOrMunici = searchList(getSMS(),citiesOrMunici[province])
        if len(likelyCitiesOrMunici) == 1:
            smsPrint(scn, "Is your farm located in "+likelyCitiesOrMunici[0]+"? (yes or no)")
            confirmation = getSMS()
        elif len(likelyCitiesOrMunici) == 0:
            smsPrint(scn, "Please be more specific, no city or municipality matches your spelling.")
        else:
            reply = "Please be more specific, many cities or manucipalities match your spelling: "
            smsPrint(scn, reply + makeListStr(likelyCitiesOrMunici))
    return likelyCitiesOrMunici[0]

def getCoop(loc):
    coops = getNearbyCoops(loc)
    optionsStr = makeListStr(coops+['Other', 'Not member of a cooperative'])
    confirmation = ''
    reply = "I see that you are sending messages from near "+loc.getName()
    smsPrint(scn, reply +". Which cooperative are you a member of? "+optionsStr)
    while not affirmative(confirmation):
        ans = getSMS()
        try:
            i = int(ans)
            if i in range(1,len(coops)+1):
                smsPrint(scn, "You are a member of "+coops[i-1]+", is this correct? (yes or no)")
                confirmation = getSMS()
            elif i == len(coops)+1:
                province = getProvince()
                city = getCityOrMunici(province)
                loc.setName(city + ',' + province)
                coops = getNearbyCoops(loc)
                optionsStr = makeListStr(coops+['Other', 'Not member of a cooperative'])
                reply = "I see that you are sending messages from near "+loc.getName()
                smsPrint(scn, reply + +". Which cooperative are you a member of? " + optionsStr)
            elif i == len(coops)+2:
                return None
        except ValueError:
            smsPrint(scn, "Please reply with a numeric value. Which cooperative are you a member of?" + optionsStr)
    return coops[i-1]

def getCropName():
    """getCityOrMunici and getProvince could be refactored into getCityOrMunici and getProvince"""
    confirmation = 'no'
    likelyCrop = []
    while not affirmative(confirmation):
        reply =  'What other crop are you cultivating (e.g. '
        smsPrint(scn, reply + random.choice(crops) + ')? Please try to spell the name as completely as possible.')
        likelyCrop = searchList(getSMS(),crops)
        if len(likelyCrop) == 1:
            smsPrint(scn, "Are you cultivating "+likelyCrop[0]+"? (yes or no)")
            confirmation = getSMS()
        elif len(likelyCrop) == 0:
            smsPrint(scn, "Please be more specific, no crop matches your spelling.")
        else:
            smsPrint(scn, "Please be more specific, many crops match your spelling: " + makeListStr(likelyCrop))
    return likelyCrop[0]

def getCropSize(crop):
    """Prompts user for the size of the crop farming"""
    confirmation = 'no'
    reply = 'You are cultivating '+crop+', please try to estimate the number of hectares on which you are cultivating '+crop
    while not affirmative(confirmation):
        smsPrint(scn, reply)
        ans = getSMS()
        try:
            i = float(ans)
            smsPrint(scn, "You are cultivating "+ans+" hectares of "+crop+", is this correct? (yes or no)")
            confirmation = getSMS()
        except ValueError:
            smsPrint(scn, "Please reply with a numeric value. "+reply)
    return ans

def getCrops():
    """Prompts farmer for all of the crops being cultivated"""
    confirmation = 'no'
    crops = []
    while not affirmative(confirmation):
        cropName = getCropName()
        cropSize = getCropSize(cropName)
        crops.append({'name':cropName,'size':cropSize})
        cropList = []
        for c in crops:
            cropList.append(str(c['size']) + " hectares of " + c['name'])
        smsPrint(scn, "You are cultivating " + makeListStr(cropList) + ". Are you cultivating anything else? (yes or no)")
        ans = getSMS()
        if affirmative(ans):
            confirmation = 'no'
        else:
            confirmation = 'yes'
    return crops

def firstTime():
    """Informs the farmer of what SMART Coop is, and of the cost"""
    print """
  ___ __  __   _   ___ _____    ___                  
 / __|  \/  | /_\ | _ \_   _|  / __|___  ___ _ __ ___
 \__ \ |\/| |/ _ \|   / | |   | (__/ _ \/ _ \ '_ (_-<
 |___/_|  |_/_/ \_\_|_\ |_|    \___\___/\___/ .__/__/
                                            |_|      
"""
    print "\n"
    print "                    |-------------------------------------------|"
    print "                    | SMART Coops SMS Simulator. For demo only. |" 
    print "                    |                      All rights reserved. |"
    print "                    |-------------------------------------------|"
    print "\n\n"
    print "Context:"
    print " The first time around, the farmer sends an SMS to SMART Coops."
    print " The sms could be empty, or could require a passcode or a"
    print " keyword like 'join' for the system to engage.\n\n\n"
    s = "Hello, it is the first time you are using SMART Coops. "
    s = s + "Note that SMS sent to and received from SMART Coops are free of charge, so do not worry about your load balance."
    smsPrint(scn, s)
    f = Farmer()
    f.setName(getName())
    loc = Location(getGPSCoord())
    f.setCoop(getCoop(loc))
    f.setCrops(getCrops())
    return f

def applyLoanMenu(farmer):
    confirmation = 'no'
    while not affirmative(confirmation):
        reply = "SMART Coops apply for loan. Your current loan balance is "+phPesos(farmer.getLoanBal())
        reply = reply+". Please reply with the amount of loan you would like to apply for (numeric value only, in PHP)."
        smsPrint(scn, reply)
        loanAmount = getSMS()
        try:
            l = int(loanAmount)
            smsPrint(scn, "You are about to apply for a loan of "+phPesos(l)+", is the amount correct? (yes or no)")
            ans = getSMS()
            if affirmative(ans):
                farmer.setLoanBal(farmer.getLoanBal()+l)
                farmer.savingsDeposit(l)
                reply = "Congratulation, your loan has been approved. "+phPesos(l)+" has been deposited in your account. "
                reply += "Your new loan balance is "+phPesos(farmer.getLoanBal())+". Returning to previous menu."
                smsPrint(scn, reply)
                confirmation = 'yes'
            else:
                confirmation = 'no'
        except ValueError:
            smsPrint(scn, "Please reply with a numeric value. Your reply: '" + ans + "' is not a numerical value.")

def viewLoanBalMenu(farmer):
    reply = "SMART Coops loan balance. Your current loan balance is "+phPesos(farmer.getLoanBal())
    reply += ". You currently have "+phPesos(farmer.getSavingsBal())+" in your savings account, available to purchase crop inputs."
    smsPrint(scn, reply + " Returning to previous menu.")

def makeLoanPaymentMenu(farmer):
    smsPrint(scn, "This menu is not complete yet... Returning to previous menu")

def loansMenu(farmer):
    optionsStr = makeListStr(['Apply for loan','View loan balance','Make loan payment','Main menu'])
    confirmation = 'no'
    while not affirmative(confirmation):
        smsPrint(scn, "SMART Coops loans menu. What would you like to do: "+optionsStr)
        ans = getSMS()
        try:
            if int(ans) == 4:
                confirmation = 'yes'
            else:
                {1:applyLoanMenu,2:viewLoanBalMenu,3:makeLoanPaymentMenu}[int(ans)](farmer)
        except ValueError:
            smsPrint(scn, "Please reply with a numeric value. Your reply: '" + ans + "' is not one of the menu options")

def buyInputMenu(farmer,crop):
    confirmation = 'no'
    likelyInput = []
    while not affirmative(confirmation):
        reply = "Buy inputs, " + crop + " menu. Please enter the name of the product you are looking for (e.g. "
        randomInput = random.choice(cropInputs)
        smsPrint(scn, reply + randomInput["productName"] + ' manufactured by ' + randomInput["brand"] + ')? Please try to spell the name as completely as possible.')
        likelyInput = searchList(getSMS(),cropInputs)
        if len(likelyInput) == 1:
            smsPrint(scn, "Are you  "+likelyCrop[0]+"? (yes or no)")
            confirmation = getSMS()
        elif len(likelyCrop) == 0:
            smsPrint(scn, "Please be more specific, no crop matches your spelling.")
        else:
            smsPrint(scn, "Please be more specific, many crops match your spelling: " + makeListStr(likelyCrop))
    return likelyCrop[0]
    

    smsPrint(scn, "Current market price for gasolina is P45/litre and LPG P344/tank. Would you like to play an order for: 1) Gasolina, 2) LPG, 3) Back to inputs menu, 4) Back to main menu.")
    smsPrint(scn,"Buy inputs, general products gasolina menu. How many litres of gasolina would you like to purchase? (ex: 34)")
    smsPrint(scn, "You are about to purchase 10 litres for a total of P450, which will be devited from your account which currently holds P19,000. Reply 'yes' to confirm or 'no' to cancel")
    smsPrint(scn, "Excellent. The purchase order has been sent to {{coop sales}}. Once the transaction is confirmed, your account will be debited by that amount. What category of product are you looking for? 1) General products, 2) Papayas inputs, 3) Mangoes inputs, 4) Eggs inputs, 5) Tilapia inputs, 6) Back to main menu")
    smsPrint(scn, "Buy inputs, papayas input. What inputs are you interested in? 1) Crop medicine, 2) Fertilizer, 3) Seeds")
    smsPrint(scn, "Buy inputs, papayas crop medicine menu. What crop medicine are you intersted in? 1) 2-4-D (weed killer), 2) Rogue (herbicide), 3) Puridan (insecticide), 4) Cynbus (insecticide), 5) Visokill (insecticide), 6) back to input menu, 7) Back to main menu")
    smsPrint(scn, "Hello! How many SMART Coops help you today? 1) Loan, 2) Buy inputs, 3) Sell produce, 4) Harvesting education, 5) Update farm profile, 6) Send SMART Coops a message")
    smsPrint(scn, "Buy inputs menu. You currently have P19,000 in your electronic account. What category of product are you looking for? 1) General products, 2) Papayas inputs, 3) Mangoes inputs, 4) Eggs inputs, 5) Tilapia inputs, 6) Back to main menu")
    smsPrint(scn, "Buy inputs, mangoes inputs. What inputs are you interested in? 1) Crop medicine, 2) Fertilizer, 3) Seeds, 4) back to input menu, 5) Back to main menu")
    smsPrint(scn, "Buy inputs, mangoes fertilizer menu. What are you intersted in? 1) Organic fertilizer, 2) Triple 14 (fertilizer), 3) back to input menu, 5) Back to main menu")

def inputsMenu(farmer):
    optionsList = []
    for c in farmer.getCrops():
        optionsList += [c["name"] + " inputs"]
    optionsStr = makeListStr(["View all products"] + optionsList + ["Main menu"])
    confirmation = 'no'
    while not affirmative(confirmation):
        reply = "Buy inputs menu. You currently have "+phPesos(farmer.getSavingsBal())
        reply += " in your savings account. What would you like to buy: "+optionsStr
        smsPrint(scn, reply)
        ans = getSMS()
        try:
            if int(ans) == len(farmer.getCrops())+1: #+1 bcz 'View all products' is first option, which means main menu is selected option
                confirmation = 'yes'
            elif ans == '1':
                buyInputMenu(farmer,'All products')
            else:
                buyInputMenu(farmer,farmer.getCrops()[int(ans)-2]['name']) #-1 bcz indexing list, -1 because of 'All products' option
        except ValueError:
            smsPrint(scn, "Please reply with a numeric value. Your reply: '" + ans + "' is not one of the menu options")

def harvestMenu(farmer):
    optionsStr = makeListStr(['Loans','Buy inputs','Sell harvest','Farm advices','View my profile','Contact SMART Coops'])
    smsPrint(scn, "This menu is not complete yet... Returning to main menu")
def adviceMenu(farmer):
    optionsStr = makeListStr(['Loans','Buy inputs','Sell harvest','Farm advices','View my profile','Contact SMART Coops'])
    smsPrint(scn, "This menu is not complete yet... Returning to main menu")
def farmerProfileMenu(farmer):
    optionsStr = makeListStr(['Loans','Buy inputs','Sell harvest','Farm advices','View my profile','Contact SMART Coops'])
    smsPrint(scn, "This menu is not complete yet... Returning to main menu")
def contactSCMenu(farmer):
    optionsStr = makeListStr(['Loans','Buy inputs','Sell harvest','Farm advices','View my profile','Contact SMART Coops'])
    smsPrint(scn, "This menu is not complete yet... Returning to main menu")

def mainMenu(farmer):
    optionsStr = makeListStr(['Loans','Buy inputs','Sell harvest','Farm advices','View my profile','Contact SMART Coops'])
    while True:
        smsPrint(scn, "SMART Coops main menu. What would you like to do: "+optionsStr)
        ans = getSMS()
        try:
            {1:loansMenu,2:inputsMenu,3:harvestMenu,4:adviceMenu,5:farmerProfileMenu,6:contactSCMenu}[int(ans)](farmer)
        except ValueError:
            smsPrint(scn, "Please reply with a numeric value. Your reply: '" + ans + "' is not one of the menu options")
    

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    """ As suggested in http://www.artima.com/weblogs/viewpost.jsp?thread=4829 """

    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
             raise Usage(msg)
        mainMenu(firstTime())
        
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
