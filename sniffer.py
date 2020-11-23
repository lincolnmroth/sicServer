import os
import schedule
import time
import datetime

UPDATE_TIME = 1 #update time in seconds
mydevices = [
    {
        "name": "LincolnComputer",
        "device": "pegasus",
        "active": False,
        "lastChange": datetime.datetime.now()
    },
    {
        "name": "LincolnPhone",
        "device": "phoenix",
        "active": False,
        "lastChange": datetime.datetime.now()
    },
    {
        "name": "LincolnTab",
        "device": "hydra",
        "active": False,
        "lastChange": datetime.datetime.now()
    }

]


def isActive(dev):
    return any(dev["device"] in s for s in os.popen('arp -a'))

def syncData():
    #Upload mydevices to server of choice, I'm using firebase but you can use whatever you want
    pass

def updateStatus():
    for dev in mydevices:
        activity = isActive(dev)
        if activity != dev["active"]:
            dev["active"] = activity
            dev["lastChange"] = datetime.datetime.now()
    syncData()

if __name__ == "__main__":
    schedule.every(UPDATE_TIME).seconds.do(updateStatus)
    while True:
        schedule.run_pending()
        time.sleep(1)
