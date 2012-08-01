import re, pyglobe
from farmbook.models import *



def getParams(entry):
    return re.split(' *?/ *?',entry['msg'])

def getMobile(entry):
    return entry['source']

danny = '09158668018'
leah = '09158668019'

def sendSMS(phoneNumber,msg):
    # WSDL: http://iplaypen.globelabs.com.ph:1881/axis2/services/Platform?wsdl
    # URL endpoint: http://iplaypen.globelabs.com.ph:1881/axis2/services/Platform
    # Access Number or Short-code: 2373
    # SMS and MMS Suffix (for receiving messages): 7388
    # Username (uName): 5txhcoj0x
    # Password (uPin): 21738420
    # URL CALLBACK: null
    # Before using the API, make sure to define your URL call back and registered Globe
    # numbers. To do this, go to https://202.126.34.119:1888/login.aspx, then login using
    # the username(uName) and password(uPin) contained in this email. You'll be
    # presented with a webtool that you can use to define / edit your callback URL and
    # registered Globe numbers.

    try:
        service = pyglobe.PyGlobe(uname='5txhcoj0x',
                                  pin='21738420',
                                  msisdn=phoneNumber)
        service.sendSMS(msg)
    except (pyglobe.PyGlobeInvalidServiceException,
            pyglobe.PyGlobeInvalidURLException,
            pyglobe.PyGlobeServerFaultException) as e:
        print "An error occurred: %s" % e

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
