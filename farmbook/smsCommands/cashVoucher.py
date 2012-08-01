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
    try:
        smsCommand = params[0]
        cvType = params[1] #either 'loan' or 'supplies'
        receiver = params[2] #who received the cash
        amount = float(params[3])
        description = params[4]
        reply "CASHVOUCHER. %s PAID out to:%s. Amount:%s. For:" % (cvType, receiver, phPesos(amount),description)
    except ValueError: 
        reply = "Could not complete CASHVOUCHER."
    sendSMS(getMobile(entry),reply)
