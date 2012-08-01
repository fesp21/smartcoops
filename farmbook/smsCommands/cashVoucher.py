from farmbook.smsfct import *

def cashVoucher(entry):
    """
    Description:
    When the coop disburses cash loans to member farmers; also used for when they incur expenses, eg. Xerox Php14.00

    Fields:
    Date
    Name
    Description (pre-filled in the voucher with "Amount payable", "Gasoline and oil", etc. but any will do)
    Amount
    Explanation (a more detailed description but can be combined with "Description")

    Sample SMS Format:
    CASHVOUCHER/loan/member name/amount/Description
    CASHVOUCHER/suppliers/supplier name/amount/Description

    Examples:
    `cashvoucher/loan/Charlie Santos/20000/for rice fields`
    `cashvoucher/supplies/Onyo Aquino/1400/xerox` in this case, Onyo is the coop officer who used his personal money to buy a xerox and then got reimbursed by the coop
    """

    params = getParams(entry)
    #params[0] is smsCommand
    farmerName = params[1]
    description = params[2]
    amount = params[3]
    #print "CASHVOUCHER. farmerName:%s. description:%s. amount:%s." % (farmerName, description, amount)
    try:
        amount = float(params[3])
    except ValueError: 
        reply = "Could not complete cash voucher, amount entered is not numerical. "
        reply += "Example of a valid entry would be: "+smsCommand+"/"
        reply += farmerName+"/"+description+str(450.50)
        print reply

