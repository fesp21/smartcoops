import pyglobe


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
                              msisdn='09158668018')
    service.sendSMS('First message sent by SMART Coops through Globe!')
except (pyglobe.PyGlobeInvalidServiceException,
        pyglobe.PyGlobeInvalidURLException,
        pyglobe.PyGlobeServerFaultException) as e:
    print "An error occurred: %s" % e
