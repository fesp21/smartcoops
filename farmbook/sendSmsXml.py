# sendSmsXml
"""

"""
import sys
import human_curl as requests

if (len(sys.argv) != 3):
    print "Usage: sendSmsXml url 'sms msg'. \nExample: \npython sendSmsXml.py http://tranquil-ocean-3872.herokuapp.com/process/ 'charge/charlie santos/24D/2/25'\npython sendSmsXml.py http://localhost:8000/process/ 'charge/charlie santos/24D/2/25'\n"
else:
    url = sys.argv[1]
    msg = sys.argv[2]

    content = """
<?xml version=\"1.0\" encoding=\"utf-8\"?>
<message>
        <param>
                <name>messageType</name>
                <value>SMS</value>
        </param>
        <param>
                <name>id</name>
                <value>319</value>
        </param>
        <param>
                <name>source</name>
                <value>09179860039</value>
        </param>
        <param>
                <name>target</name>
                <value>23737390</value>
        </param>
        <param>
                <name>msg</name>
                <value>%s</value>
        </param>
        <param>
                <name>udh</name>
                <value></value>
        </param>
</message>""" % msg

    r = requests.post(url, data=content)
    print r.status_code
