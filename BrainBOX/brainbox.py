from NeuroPy import NeuroPy
import pyautogui as pi
from win32api import GetSystemMetrics
import pytweening
import time
import win32gui
import numpy 
import site
from twilio.rest import Client
from flask import Flask, render_template, jsonify, request
def map(x, oFrom, oTo, nFrom, nTo):
    return x * ((nTo-nFrom)/(oTo-oFrom))
    pass
print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))
print("Connecting")
ob = NeuroPy("COM8")
print("Connected")
ob.start()
print("started")
count=0
slevel=0
flag=1
lastAttention = 0
print("beta gamma alpha--", ob.highBeta, ob.lowGamma, ob.attention)
i=0
account_sid = 'AC0f1740dc01c6053984534124f3e1c5fd'
auth_token = 'fddb95928a64d151a884e049d7925921'

client = Client(account_sid, auth_token)
while(True):
    time.sleep(0.8)
    i=0
    count=0
    while(i<5):
        i = i+1
        print("count=",count)
        print("slevel=",slevel)
        if ob.highBeta > ob.lowBeta and ob.lowGamma > ob.midGamma:
                    print("HB-",ob.highBeta,"\tLB-", ob.lowBeta,"\tLG-",ob.lowGamma,"\tMG-",ob.midGamma,"\tHA-",ob.highAlpha)
                    count = count+1
                    print(count)
        else:
            count =0
        if(ob.highBeta>ob.highAlpha and ob.lowBeta>ob.lowAlpha):
            slevel = slevel+1
        else:
            if(ob.highAlpha>ob.highBeta and ob.lowAlpha>ob.lowBeta):
                print("The person is happy")

            slevel=0
        if(slevel==5):
            print("The person is stressed")
            break
        elif ob.meditation > 65:
            print("The person is meditating")
        if(count==4):
            print("Person is depressed")
            break
        else:
            print("Person is normal")
            pass
    if(count==4):
        print("message D sent")
        message = client.messages \
                .create(
                     body="Patient is depressed",
                     from_='+18084001532',
                     to='+918838797398'
                 )
    elif(slevel>4):
        print("message S sent")
        message = client.messages \
                .create(
                     body="Patient is stressed",
                     from_='+18084001532',
                     to='+918838797398'
                 )
        pass
    else:
        print("message N sent")
        message = client.messages \
                .create(
                     body="Person is normal",
                     from_='+18084001532',
                     to='+918838797398'
                 )

    time.sleep(4)

while(True):
    pass 
while(1):
    k=0
ob.stop()
ob.save()

