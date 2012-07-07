import re, csv, time, random, getopt, sys
from datetime import datetime


provinces = ['Abra','Agusan del Norte','Agusan del Sur','Aklan','Albay','Antique','Apayao','Aurora','Basilan','Bataan','Batanes','Batangas','Benguet','Biliran','Bohol','Bukidnon','Bulacan','Cagayan','Camarines Norte','Camarines Sur','Camiguin','Capiz','Catanduanes','Cavite','Cebu','Compostela Valley','Cotabato','Davao del Norte','Davao del Sur','Davao Oriental','Dinagat Islands','Eastern Samar','Guimaras','Ifugao','Ilocos Norte','Ilocos Sur','Iloilo','Isabela','Kalinga','La Union','Laguna','Lanao del Norte','Lanao del Sur','Leyte','Maguindanao','Marinduque','Masbate','Misamis Occidental','Misamis Oriental','Mountain Province','Negros Occidental','Negros Oriental','Northern Samar','Nueva Ecija','Nueva Vizcaya','Occidental Mindoro','Oriental Mindoro','Palawan','Pampanga','Pangasinan','Quezon','Quirino','Rizal','Romblon','Samar','Sarangani','Siquijor','Sorsogon','South Cotabato','Southern Leyte','Sultan Kudarat','Sulu','Surigao del Norte','Surigao del Sur','Tarlac','Tawi-Tawi','Zambales','Zamboanga del Norte','Zamboanga del Sur','Zamboanga Sibugay','Metro Manila']

locations = {'Abra': ['Bangued','Boliney','Bucay','Bucloc','Daguioman','Danglas','Dolores','La Paz','Lacub','Lagangilang','Lagayan','Langiden','Licuan-Baay','Luba','Malibcong','Manabo','Penarrubia','Pidigan','Pilar','Sallapadan','SanIsidro','SanJuan','SanQuintin','Tayum','Tineg','Tubo','Villaviciosa'], 'Agusan del Norte':['Butuan City','Cabadbaran City','Buenavista','Carmen','Jabonga','Kitcharao','Las Nieves','Magallanes','Nasipit','Remedios T. Romualdez','Santiago','Tubay']} #http://en.wikipedia.org/wiki/List_of_cities_and_municipalities_in_the_Philippines using 

coops = {'Bangued':['Some coop', 'Another coop', 'Yet another coop']}

crops = ['Agave Fibres Nes','Almonds, with shell','Anise, badian, fennel, corian.','Apples','Apricots','Arecanuts','Artichokes','Asparagus','Avocados','Bambara beans','Bananas','Barley','Beans, dry','Beans, green','Berries Nes','Blueberries','Brazil nuts, with shell','Broad beans, horse beans, dry','Buckwheat','Cabbages and other brassicas','Canary seed','Carobs','Carrots and turnips','Cashew nuts, with shell','Cashewapple','Cassava','Castor oil seed','Cauliflowers and broccoli','Cereals, nes','Cherries','Chestnuts','Chick peas','Chicory roots','Chillies and peppers, dry','Chillies and peppers, green','Cinnamon (canella)','Citrus fruit, nes','Cloves','Cocoa beans','Coconuts','Coffee, green','Coir','Cow peas, dry','Cranberries','Cucumbers and gherkins','Currants','Dates','Eggplants (aubergines)','Fibre Crops Nes','Figs','Flax fibre and tow','Fonio','forage Products','Fruit Fresh Nes','Fruit, tropical fresh nes','Garlic','Ginger','Gooseberries','Grapefruit (inc. pomelos)','Grapes','Groundnuts, with shell','Hazelnuts, with shell','Hemp Tow Waste','Hempseed','Hops','Jute','Karite Nuts (Sheanuts)','Kiwi fruit','Kolanuts','Leeks, other alliaceous veg','Leguminous vegetables, nes','Lemons and limes','Lentils','Lettuce and chicory','Linseed','Lupins','Maize','Maize, green','Mangoes, mangosteens, guavas','Manila Fibre (Abaca)','Maté','Melonseed','Millet','Mixed grain','Mushrooms and truffles','Mustard seed','Natural rubber','Nutmeg, mace and cardamoms','Nuts, nes','Oats','Oil palm fruit','Oilseeds, Nes','Okra','Olives','Onions (inc. shallots), green','Onions, dry','Oranges','Other Bastfibres','Other melons (inc.cantaloupes)','Papayas','Peaches and nectarines','Pears','Peas, dry','Peas, green','Pepper (Piper spp.)','Peppermint','Persimmons','Pigeon peas','Pineapples','Pistachios','Plantains','Plums and sloes','Popcorn','Poppy seed','Potatoes','Pulses, nes','Pumpkins, squash and gourds','Pyrethrum,Dried','Quinces','Quinoa','Ramie','Rapeseed','Raspberries','Rice, paddy','Roots and Tubers, nes','Rye','Safflower seed','Seed cotton','Sesame seed','Sisal','Sorghum','Sour cherries','Soybeans','Spices, nes','Spinach','Stone fruit, nes','Strawberries','String beans','Sugar beet','Sugar cane','Sugar crops, nes','Sunflower seed','Sweet potatoes','Tangerines, mandarins, clem.','Taro (cocoyam)','Tea','Tobacco, unmanufactured','Tomatoes','Triticale','Tung Nuts','Vanilla','Vegetables fresh nes','Vetches','Walnuts, with shell','Watermelons','Wheat','Yams','Yautia (cocoyam)']


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
    time.sleep(sleepTime)

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
    print '\n                          Sending message\n\n\n\n\n',
    time.sleep(sleepTime)
    print '\n\n\n\n\n'
    return newSMS

def getName():
    """Retrieves and confirms the name of the farmer"""
    confirmation = ''
    while confirmation.lower() != 'yes':
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
    return myStr

def getProvince():
    """getLoc and getProvince could be refactored into one"""

    confirmation = 'no'
    likelyProvinces = []
    while confirmation.lower() != 'yes':
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

def getLoc(province):
    """getLoc and getProvince could be refactored into one"""

    confirmation = 'no'
    likelyLoc = []
    while confirmation.lower() != 'yes':
        reply =  'Your farm is in '+province+' province. What city or baranguay is it located nearest to (e.g. '
        smsPrint(scn, reply + random.choice(locations['Abra']) + ')? Please try to spell the name as completely as possible.')
        likelyLoc = searchList(getSMS(),locations['Abra'])
        if len(likelyLoc) == 1:
            smsPrint(scn, "Is your farm located in "+likelyLoc[0]+"? (yes or no)")
            confirmation = getSMS()
        elif len(likelyLoc) == 0:
            smsPrint(scn, "Please be more specific, no location matches your spelling.")
        else:
            smsPrint(scn, "Please be more specific, many locations match your spelling: " + makeListStr(likelyLoc))
    return likelyLoc[0]

def getCoop(loc):
    coops = getNearbyCoops(loc)
    optionsStr = makeListStr(coops+['Other', 'Not member of a cooperative'])
    confirmation = ''
    smsPrint(scn, "I see that you are sending messages from near "+loc.getName()+". Which cooperative are you a member of?"+optionsStr)
    while confirmation.lower() != 'yes':
        ans = getSMS()
        try:
            i = int(ans)
            if i in range(1,len(coops)+1):
                smsPrint(scn, "You are a member of "+coops[i-1]+", is this correct? (yes or no)")
                confirmation = getSMS()
            elif i == len(coops)+1:
                loc.setName(getLoc(getProvince()))
                coops = getNearbyCoops(loc)
                optionsStr = makeListStr(coops+['Other', 'Not member of a cooperative'])
                smsPrint(scn, "I see that you are sending messages from near "+loc.getName()+". Which cooperative are you a member of?" + optionsStr)
            elif i == len(coops)+2:
                return None
        except ValueError:
            smsPrint(scn, "Please reply with a numeric value. Which cooperative are you a member of?" + optionsStr)
    return coops[i-1]

def getCrop():
    """getLoc and getProvince could be refactored into getLoc and getProvince"""

    confirmation = 'no'
    likelyCrop = []
    while confirmation.lower() != 'yes':
        reply =  'What crop are you cultivating (e.g. '
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

def offerMenu():
    optionsStr = makeListStr(['Rice','Mango','Pineapple','Banana','Coconut','Other (you can also just name them)'])
    smsPrint(scn, "What crops, produce are you currently growing?"+optionsStr)
    ans = getSMS()
    

#Global variables
scn = "+63 915 866 8018" #Smart Coops number
sleepTime = .1 #to simulate time in between SMS messages, 1.5 secs more realistic

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
        getSMS()
        f = Farmer()
        firstTime()
        f.setName(getName())
        loc = Location(getGPSCoord())
        f.setCoop(getCoop(loc))
        offerMenu()
        
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
