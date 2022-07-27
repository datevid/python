
def getDatetimeStr():
    """
    return datetime in string with format YYYY-mm-dd.hh.mm.ss
    :return: 
    """
    # Converting datetime object to string
    dateTimeObj = datetime.datetime.now()
    timestampStr = dateTimeObj.strftime("%Y-%m-%d.%H.%M.%S")
    return timestampStr;
