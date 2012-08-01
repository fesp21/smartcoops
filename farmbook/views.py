from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from xml.dom import minidom
from farmbook.models import *
import datetime, re, os

def index(request):
    farmerList = Farmer.objects.all()
    return render_to_response('farmbook/index.html', {'farmerList': farmerList})

def getSMSCommand(userPattern, smsCommands):
    """ Search through file names in smsCommands and match the name using re.IGNORECASE
    return baseMenu is user command is not found."""
    if smsCommands == []:
        return 'baseMenu'
    smsCmd = re.search(userPattern, smsCommands[0])
    if smsCmd:
        return smsCmd.group()[:-3] #remove .py
    return getSMSCommand(userPattern,smsCommands[1:])

def updateIncomingSMS(entry):
    new = IncomingSMS(
        msgType = entry['messageType'],
        msgId = entry['id'],
        source = entry['source'],
        target = entry['target'],
        msg = entry['msg'],
        udh = entry['udh'],
        timestamp = datetime.datetime.now(),
        )
    new.save()

    userCommand = re.split(' */ *',entry['msg'])[0]
    smsCommands = os.listdir('farmbook/smsCommands')
    smsCommand = getSMSCommand(re.compile(userCommand+'\.py', re.IGNORECASE),smsCommands)
    m = __import__(name='farmbook.smsCommands.'+smsCommand, 
                   fromlist=['farmbook', 'smsCommands'])
    func = getattr(m,smsCommand)
    func(entry)

@csrf_exempt
def process(request):
    if request.method != 'POST':
        raise Http404
    dom = minidom.parseString(request.body)
    xmlList = dom.getElementsByTagName('param')
    entry = {}
    for i in xmlList:
        name = i.getElementsByTagName('name')[0].childNodes[0]
        try:
            value = i.getElementsByTagName('value')[0].childNodes[0]
        except IndexError:
            entry[name.nodeValue] = ''
        else:
            entry[name.nodeValue] = value.nodeValue
    updateIncomingSMS(entry)
    return HttpResponse()

@csrf_exempt
def update(request):
    '''
    TODO: update method to return a list of new IncomingSMS
    entries given a specified time from POST
    '''
    if request.method != 'POST':
        raise Http404
    data = request.POST['time']
    latest = IncomingSMS.objects.latest('timestamp')
    return HttpResponse(data)

def show(request):
    smsList = IncomingSMS.objects.all()
    rendered = int(datetime.datetime.now().strftime('%s'))
    return render_to_response('index.html', {'texts': smsList,
            'render': rendered})
