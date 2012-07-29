#!/usr/bin/env python
import re, csv, time, random, getopt, sys, locale
from datetime import datetime
import philippinesData, cropInputsData, crops

#Global variables
scn = "+63 915 866 8018" #Smart Coops number
sleepTime = 0 #to simulate time in between SMS messages, 1.5 secs more realistic
affirmativeAns = ['yes','y','ye','ya','oo','yeah','yup','1']

provinces = philippinesData.provinces
citiesOrM = philippinesData.citiesOrMunici
coops = philippinesData.coops
crops = crops.crops
cropInputs = cropInputsData.cropInputs

class Farmer():
    """Farmers have a name, a mobile phone number, and possibly belong to a coop"""

    def __init__(self, mobileNum = None, name = None, coop = None, crops = None, loanBal = 0, savingsBal = 0, purchaseHist = []):
        self.mobileNum = mobileNum
        self.name = name
        self.coop = coop
        self.crops = crops
        self.loanBal = loanBal
        self.savingsBal = savingsBal
        self.purchaseHist = purchaseHist

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

    def getPurchaseHist(self):
        return self.purchaseHist
    def setPurchaseHist(self, purchaseHist):
        self.purchaseHist = purchaseHist
    def add2PurchaseHist(self, purchase):
        self.purchaseHist.append(purchase)

#For debugging purposes
sampleFarmer = Farmer(12341234,'Danny Castonguay','San Benito Multipurpose Coop',[{'name':'Cloves','size':1.5},{'name':'Cocoa beans','size':12.7},{'name':'Coconuts','size':6},{'name':'Coffee, green','size':22}],1200000,600000)

class Location():
    """Each exchange has a location as provided by the telco, which we use to inform the farmer of prices or local resources"""
    def __init__(self, province = None, cityOrM = None, gpsCoord = None):
        self.province = province
        self.cityOrM = cityOrM
        self.gpsCoord = gpsCoord
    def getProvince(self):
        return self.province
    def setProvince(self, province):
        self.province = province
    def getCityOrM(self):
        return self.cityOrM
    def setCityOrM(self, cityOrM):
        self.cityOrM = cityOrM
    def getGPSCoord(self):
        return self.gpsCoord
    def setGPSCoord(self, name):
        self.gpsCoord = gpsCoord
    def getName(self):
        return self.cityOrM + ", " + self.province

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

def searchListDict(myStr, myListDict, key):
    """Returns the set of dictionaries resulting from a substring search over specific key"""
    pattern = re.compile(r'.*'+myStr+'.*', re.IGNORECASE)
    results = []
    for d in myListDict:
        r = re.search(pattern,d[key])
        if r is not None:
            results.append(d)
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

def smsPrint(body):
    """Prints a pretty sms msg on the terminal"""
    smsSeparator = "=================================================================="
    width = len(smsSeparator)
    smsBorder = '-'*width
    print '\n\n'+smsSeparator
    print datetime.now().strftime("%a, %b %d at %I:%M%p") + ". New SMS from " + scn + ":"
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
    smsPrint("Please reply to this SMS with your name (ex: Capitan, Sergio).")
    name = getSMS()
    smsPrint("Pleased to meet you "+name+". Did I get your name correctly? (Reply yes or no). ")
    if affirmative(getSMS()):
        reply = "Great, thank you for confirming your name, "+name
        reply += ". SMART Coops helps you find out about prices for crop inputs, crop produce, loans, and more."
        smsPrint(reply)
        return name
    else:
        return getName()

def getGPSCoord():
    """presumably we would retrive information from the telco as to the location from where the farmer is calling from, 
    and use that in the getCoop function, not implemented"""
    return 0

def getNearbyProvince(gpsCoord):
    return 'Laguna'

def getNearbyCityOrM(gpsCoord):
    return 'San Pablo'

def getNearbyCoops(loc):
    """given a location, returns the nearby cooperatives"""
    return ['San Benito Multipurpose Coop', 'San Pablo Cooperative', 'Calamba Association of Rice Planters']

def getItemFromList(itemType, myList):
    """Obtains from the user an item from a list, offering the user to either enter a corresponding number or a substring search"""
    smsPrint("Select your "+itemType+" from this list: "+makeListStr(myList))
    ans = getSMS()
    try: #check if user entered a numeric value
        num = int(ans)
        if num in range(1, len(myList)+1):
            return myList[num-1]
        else:
            getItemFromList(itemType,myList)
    except ValueError: #it's ok, user might have written an answer instead of a numeric value
        matchingItems = searchList(ans,myList)
        if len(matchingItems) == 0:
            return getItemFromList(itemType,myList)
        if len(matchingItems) == 1:
            return matchingItems[0]
        if len(matchingItems) > 1:
            return getItemFromList(itemType,matchingItems)

def getItemFromListDict(itemType, myListDict, key):
    """Obtains from the user an item from a list of dictionaries using key, offering the user to either 
    enter a corresponding number or a substring search on the items addressed by the key"""
    myList = []
    for d in myListDict:
        myList.append(d[key])
    smsPrint("Select your "+itemType+" from this list: "+makeListStr(myList))
    ans = getSMS()
    try: #check if user entered a numeric value
        num = int(ans)
        if num in range(1, len(myListDict)+1):
            return myListDict[num-1]
        else:
            getItemFromListDict(itemType, myListDict, key)
    except ValueError: #it's ok, user might have written an answer instead of a numeric value
        matchingItems = searchListDict(ans, myListDict, key)
        if len(matchingItems) == 0:
            return getItemFromListDict(itemType, myListDict, key)
        if len(matchingItems) == 1:
            return matchingItems[0]
        if len(matchingItems) > 1:
            return getItemFromListDict(itemType, matchingItems, key)

def getProvince():
    reply = 'What province is your farm located in (e.g. '+ random.choice(provinces) 
    reply += ')? You may spell only a few letters and I will search for it.'
    smsPrint(reply)
    ans = getSMS()
    likelyProvinces = searchList(ans,provinces)
    if len(likelyProvinces) == 1:
        smsPrint("Is your farm located in "+likelyProvinces[0]+"? (yes or no)")
        if affirmative(getSMS()):
            return likelyProvinces[0]
        else:
            return getProvince()
    elif len(likelyProvinces) == 0:
        smsPrint("No provinces found that match '"+ans+"'.")
        return getProvince()
    else:
        return getItemFromList('province',likelyProvinces)

def getCityOrM(province):
    reply =  'Your farm is in '+province+' province. What city or municipality is it located nearest to (e.g. '
    reply += random.choice(citiesOrM[province])
    reply += ')? You may spell only a few letters and I will search for it.'
    smsPrint(reply)
    ans = getSMS()
    likelyCitiesOrM = searchList(ans,citiesOrM[province])
    if len(likelyCitiesOrM) == 1:
        smsPrint("Is your farm located in "+likelyCitiesOrM[0]+", "+province+"? (yes or no)")
        if affirmative(getSMS()):
            return likelyCitiesOrM[0]
        else:
            return getCityOrM(province)
    elif len(likelyCitiesOrM) == 0:
        smsPrint("No cities or municipalities found that match '"+ans+"'.")
        return getCityOrM(province)
    else:
        return getItemFromList('city or municipality',likelyCitiesOrM)

def getCoop(loc = None):
    if loc == None:
        gpsCoord = getGPSCoord()
        loc = Location(getNearbyProvince(gpsCoord), getNearbyCityOrM(gpsCoord), gpsCoord)
    coops = getNearbyCoops(loc)
    optionsStr = makeListStr(coops+['Other', 'Not member of a cooperative'])
    reply = "I see that you are sending messages from near "+loc.getName()
    reply += ". Which cooperative are you a member of? "+optionsStr
    smsPrint(reply)
    ans = getSMS()
    try:
        i = int(ans)
        if i in range(1,len(coops)+1):
            smsPrint("You are a member of "+coops[i-1]+", is this correct? (yes or no)")
            if affirmative(getSMS()):
                return coops[i-1]
            else:
                return getCoop(loc)
        elif i == len(coops)+1:
            loc.setProvince(getProvince())
            loc.setCityOrM(getCityOrM(loc.getProvince()))
            return getCoop(loc)
        elif i == len(coops)+2:
            return None
        else:
            raise ValueError
    except ValueError:
        smsPrint("I don't understand. Your answer '"+ans+"' is not one of the menu options.")
        getCoop(loc)

def getCropName():
    reply =  'What crop is your farm cultivating (e.g. ' + random.choice(crops)
    reply += ')? You may spell only a few letters and I will search for it.'
    smsPrint(reply)
    ans = getSMS()
    likelyCrops = searchList(ans,crops)
    if len(likelyCrops) == 1:
        smsPrint("Is your farm cultivating "+likelyCrops[0]+"? (yes or no)")
        if affirmative(getSMS()):
            return likelyCrops[0]
        else:
            return getCropName()
    elif len(likelyCrops) == 0:
        smsPrint("No crops found that matches '"+ans+"'.")
        return getCropName()
    else:
        return getItemFromList('crop',likelyCrops)

def getCropSize(crop):
    """Prompts user for the size of the crop farming"""
    ansEx =  str(random.randint(0,20))+'.'+str(random.randint(0,9))
    reply = 'Your farm is cultivating '+crop+', please try to estimate the number of hectares (e.g. '
    reply += ansEx + ') for this crop.'
    smsPrint(reply)
    ans = getSMS()
    try:
        if float(ans) >= 0:
            smsPrint("You are cultivating "+ans+" hectares of "+crop+", is this correct? (yes or no)")
            if affirmative(getSMS()):
                return float(ans)
            else:
                return getCropSize(crop)
        else:
            raise ValueError
    except ValueError:
        smsPrint("I cannot understand your response. '"+ans+"' is not a valid answer (e.g. "+ansEx+").")
        return getCropSize(crop)

def getCrops(crops = []):
    """Prompts farmer for all of the crops being cultivated"""
    cropName = getCropName()
    cropSize = float(getCropSize(cropName))
    crops.append({'name':cropName,'size':cropSize})
    cropNameSizeStrList = []
    for c in crops:
        cropNameSizeStrList.append(str(c['size']) + " hectares of " + c['name'])
        smsPrint("You are cultivating " + makeListStr(cropNameSizeStrList) + ". Are you cultivating anything else? (yes or no)")
    if affirmative(getSMS()):
        return getCrops(crops)
    else:
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
    s = s + "Note that SMS sent to and received from SMART Coops are FREE OF CHARGEfree of charge, so do not worry about your load balance. We are paying for all SMS you send to SMART Coops."
    smsPrint(s)
    f = Farmer()
    f.setName(getName())
    f.setCoop(getCoop())
    f.setCrops(getCrops())
    return f

def applyLoanMenu(farmer):
    reply = "SMART Coops apply for loan. Your current loan balance is "+phPesos(farmer.getLoanBal())
    reply += ". Please reply with the amount of loan you would like to apply for (numeric value only, in PHP)."
    smsPrint(reply)
    loan = getSMS()
    try:
        if int(loan)>0:
            smsPrint("You are about to apply for a loan of "+phPesos(int(loan))+", is the amount correct? (yes or no)")
            if affirmative(getSMS()):
                farmer.setLoanBal(farmer.getLoanBal()+int(loan))
                farmer.savingsDeposit(int(loan))
                reply = "Congratulation, your loan has been approved. "+phPesos(int(loan))+" has been deposited in your account. "
                reply += "Your new loan balance is "+phPesos(farmer.getLoanBal())+". Returning to previous menu."
                smsPrint(reply)
        else:
            raise ValueError
    except ValueError:
        smsPrint("Your reply: '" + loan + "' is not a positve numerical value.")
        applyLoanMenu(farmer)

def viewLoanBalMenu(farmer):
    reply = "SMART Coops loan balance. Your current loan balance is "+phPesos(farmer.getLoanBal())
    reply += ". You currently have "+phPesos(farmer.getSavingsBal())+" in your savings account, available to purchase crop inputs."
    smsPrint(reply + " Returning to previous menu.")

def makeLoanPaymentMenu(farmer):
    reply = "SMART Coops make loan payment. Your current loan balance is "+phPesos(farmer.getLoanBal())
    reply += " and your savings balance is "+phPesos(farmer.getSavingsBal())
    reply += ". Please reply with the amount of loan you would to pay back (numeric value only, in PHP)."
    smsPrint(reply)
    payment = getSMS()
    try:
        if 0 < int(payment) and int(payment) <= farmer.getSavingsBal() :
            smsPrint("You are about to make a loan payment of "+phPesos(int(payment))+", is the amount correct? (yes or no)")
            if affirmative(getSMS()):
                farmer.setLoanBal(farmer.getLoanBal()-int(payment))
                farmer.savingsWithdraw(int(payment))
                reply = "Congratulation, your loan payment has been processed. "+phPesos(int(payment))
                reply += " has been paid from your savings account. "
                reply += "Your new loan balance is "+phPesos(farmer.getLoanBal())+". Returning to previous menu."
                smsPrint(reply)
        else:
            raise ValueError
    except ValueError:
        reply = "Your reply '" + payment + "' is not a positive numerical value or is greater than "
        reply += phPesos(farmer.getSavingsBal()) + ", your current savings account balance."
        smsPrint(reply)
        makeLoanPaymentMenu(farmer)

def loansMenu(farmer):
    optionsStr = makeListStr(['Apply for loan','View loan balance','Make loan payment','Main menu'])
    smsPrint("SMART Coops loans menu. What would you like to do: "+optionsStr)
    ans = getSMS()
    try:
        if int(ans) in range(1,4):
            {1:applyLoanMenu,2:viewLoanBalMenu,3:makeLoanPaymentMenu}[int(ans)](farmer)
        elif int(ans) == 4:
            return
        else:
            raise ValueError
    except ValueError:
        smsPrint("Please reply with a numeric value. Your reply: '" + ans + "' is not one of the menu options")
        loansMenu(farmer)

def purchaseInput(farmer, likelyInputs):
    name, price, units = likelyInputs["productName"], likelyInputs["price"], likelyInputs["units"]
    reply = "Are you interested in buying "+name+" for the price of "
    reply += phPesos(price)+" per "+units+"? (yes or no)"
    smsPrint(reply)
    if affirmative(getSMS()):
        reply = "How many units of "+name+" (e.g. 5) do you want to buy for the price of "
        reply += phPesos(price)+" per "+units+"?"
        smsPrint(reply)
        ans = getSMS()
        try:
            quantity = int(ans)
            amount = quantity*price
            if 0 <= amount and amount <= farmer.getSavingsBal():
                farmer.savingsWithdraw(amount)
                pHist = likelyInputs.copy()
                pHist["purchaseDate"] = datetime.now().strftime("%a, %b %d at %I:%M%p")
                pHist["quantity"], pHist["amount"] = quantity, amount
                farmer.add2PurchaseHist(pHist)
                reply = "You have purchased "+str(quantity) + " units of " + units + " of "
                reply += name + " for the total amount of " + phPesos(amount)
                reply += ". Your new savings account balance is " + phPesos(farmer.getSavingsBal()) + "."
                smsPrint(reply)
            else:
                reply = "Cannot proceed with purchase, total amount for purchase is " + phPesos(amount)
                reply += " but should be between P0.00 and " + phPesos(farmer.getSavingsBal()) 
                reply += " (your current savings bal)."
                smsPrint(reply)
        except ValueError:
            smsPrint("Please reply with a whole number. Your reply: '" + ans + "' is not valid")
            purchaseInput(farmer, likelyInputs)

def buyInputMenu(farmer, crop):
    randomInput = random.choice(cropInputs)
    reply = "Buy inputs, " + crop + " menu. Please enter the name of the product you are looking for (e.g. "
    reply += randomInput["productName"] + ' manufactured by ' + randomInput["brand"] 
    reply += ') or reply 0 to return to previous menu. You may spell only a few letters and I will search for it.'
    smsPrint(reply)
    ans = getSMS()
    if ans == '0':
        return farmer
    likelyInputs =  searchListDict(ans, cropInputs, "productName")
    if len(likelyInputs) == 1:
        return purchaseInput(farmer,likelyInputs[0])
    elif len(likelyInputs) == 0:
        smsPrint("Unfortunately, no crop input matches your spelling.")
        buyInputMenu(farmer,crop)
    else:
        purchaseInput(farmer,getItemFromListDict('crop input', likelyInputs, 'productName'))

def inputsMenu(farmer):
    optionsList = []
    for c in farmer.getCrops():
        optionsList += [c["name"] + " inputs"]
    optionsStr = makeListStr(["Search all products"] + optionsList + ["Main menu"])
    reply = "Buy inputs menu. You currently have "+phPesos(farmer.getSavingsBal())
    reply += " in your savings account. What would you like to buy: "+optionsStr
    smsPrint(reply)
    ans = getSMS()
    try:
        if int(ans) <= 0:
            raise ValueError
        elif int(ans) == 1:
            buyInputMenu(farmer,'all products')
        elif int(ans) > len(farmer.getCrops())+1: #+1 bcz 'View all products' is first option
            return #go back to main menu
        else:
            buyInputMenu(farmer,farmer.getCrops()[int(ans)-2]['name']) #-2 because of 'View all products' option
    except ValueError:
        smsPrint("Please reply with a numeric value. Your reply: '" + ans + "' is not one of the menu options")
        inputsMenu(farmer)

def harvestMenu(farmer):
    cropNameList = []
    for c in farmer.getCrops():
        cropNameList.append(c['name'])
    reply = "Select the crop you are interested in selling: " + makeListStr(cropNameList)
    smsPrint(reply)
    ans = getSMS()
    try:
        if int(ans) <= len(farmer.getCrops()):
            reply = "The current price for " + cropsfarmer.getCrops()[int(ans)]
        else:
            raise ValueError
    except ValueError:
        smsPrint("Please reply with a numeric value. Your reply: '" + ans + "' is not one of the menu options")

def adviceMenu(farmer):
    optionsStr = makeListStr(['Loans','Buy inputs','Sell harvest','Farm advices','View my profile','Contact SMART Coops'])
    smsPrint("This menu is not complete yet... Returning to main menu")

def purchaseHist(farmer):
    reply = ''
    for p in farmer.getPurchaseHist():
        reply = "On " + p['purchaseDate'] + " you bought " + str(p['quantity']) + p['units']
        reply += " of " + p['productName'] + " at " + phPesos(p['price']) + " for a total of " + phPesos(p['amount']) + ".\n"
    smsPrint(reply)

def changeName(farmer):
    farmer.setName(getName())

def changeCoop(farmer):
    farmer.setCoop(getCoop())

def changeCrops(farmer):
    farmer.setCrops(getCrops()) #eventually should probably allow to edit/remove existing crops instead of back to basic

def farmerProfileMenu(farmer):
    reply = "Name: "+ farmer.getName() + ". "
    reply += "Coop: "+ farmer.getCoop() + ". "
    cropNameSizeStrList = []
    for c in farmer.getCrops():
        cropNameSizeStrList.append(c['name']+" on "+str(c['size'])+" hectares")
    reply += "Crops cultivated: "+ makeListStr(cropNameSizeStrList) + ". "
    reply += "Current loan balance: " + phPesos(farmer.getLoanBal()) + ". "
    reply += "Current savings balance: " + phPesos(farmer.getSavingsBal()) + ". "
    optionsStr = makeListStr(['View purchase history', 'Change name', 'Change coop', 'Change crops', 'Main menu'])
    reply += "What actions would you like to take: "+optionsStr
    smsPrint(reply)
    ans = getSMS()
    try:
        if int(ans) in range(1,5):
            {1:purchaseHist,2:changeName,3:changeCoop,4:changeCrops}[int(ans)](farmer)
        elif int(ans) == 5:
            return
        else:
            raise ValueError
    except ValueError:
        smsPrint("Please reply with a numeric value. Your reply: '" + ans + "' is not one of the menu options")
        farmerProfileMenu(farmer)

def shortCommands(farmer):
    reply = "Which command would you like to learn more information about: "
    reply += makeListStr(['Product charge invoice','article delivery receipt','official receipt',
                              'cash voucher','commodity slip','stock cards','ledger'])
    smsPrint(reply)

def contactSCMenu(farmer):
    reply = "Hello. Please explain briefly your reason for contacting us. "
    reply += "The more complete your message is, the better we will be able to serve you. "
    reply += "We will reply to your message prompty."
    smsPrint(reply)
    ans = getSMS() #for demo, throw away message
    reply = "Thank you. We have received your message '" + ans + "'. Thank you for using SMART Coops."
    smsPrint(reply)

def mainMenu(farmer):
    optionsStr = makeListStr(['Loans','Buy inputs','Sell harvest','Farm advices',
                              'View my profile','View shortcuts','Contact SMART Coops'])
    while True:
        smsPrint("SMART Coops main menu. What would you like to do: "+optionsStr)
        ans = getSMS()
        try:
            {1:loansMenu,2:inputsMenu,3:harvestMenu,4:adviceMenu,5:farmerProfileMenu,
             6:shortCommands,7:contactSCMenu}[int(ans)](farmer)
        except ValueError:
            smsPrint("Please reply with a numeric value. Your reply: '" + ans + "' is not one of the menu options")

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

