# post xml soap message

import sys, httplib

# a "as lighter as possible" soap message:

SM_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Header>
<tns:RequestSOAPHeader xmlns:tns="http://www.huawei.com/schema/osg/common/v2_1">
<tns:spId>001211</tns:spId>
<tns:spPassword>ad1dcbc1d2eeeab0376c2091112ff2b0</tns:spPassword>
<tns:timeStamp>20120525010101</tns:timeStamp>
<tns:serviceId>0012112000001316</tns:serviceId>
<tns:OA>%s</tns:OA>
<tns:FA></tns:FA>
<!--token>5639E3EF02E92C5C79969F588DC8C63A</token-->
</tns:RequestSOAPHeader>
</soapenv:Header>
<soapenv:Body>
<ns3:sendSms xmlns:ns3="http://www.csapi.org/schema/parlayx/sms/send/v2_2/local">
<ns3:addresses>tel:%s</ns3:addresses>
<ns3:senderName>406804</ns3:senderName>
<ns3:message>%s</ns3:message>
<!--ns3:receiptRequest>
<endpoint>http://10.132.107.82:18081/SmsNotificationService1</endpoint>
<interfaceName>SmsNotificationService</interfaceName>
<correlator>666</correlator>
</ns3:receiptRequest-->
</ns3:sendSms>
</soapenv:Body>
</soapenv:Envelope>
"""
num = raw_input("Enter Phone Number: ")
msg = raw_input("Enter your Message: ")

SoapMessage = SM_TEMPLATE%(num,num,msg)

print SoapMessage

#construct and send the header

webservice = httplib.HTTP("npwifi.smart.com.ph", 8080)
webservice.putrequest("POST", "/sdp/services/SendSmsService")
webservice.putheader("Host", "npwifi.smart.com.ph:8080")
webservice.putheader("Accept-Encoding", "gzip,deflate")
webservice.putheader("User-Agent", "Python post")
webservice.putheader("Content-type", "text/xml;charset=\"UTF-8\"")
webservice.putheader("Content-length", "%d" % len(SoapMessage))
webservice.putheader("SOAPAction", "\"\"")
webservice.endheaders()
webservice.send(SoapMessage)

# get the response

statuscode, statusmessage, header = webservice.getreply()
print "Response: ", statuscode, statusmessage
print "headers: ", header
res = webservice.getfile().read()
print res