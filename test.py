# CURRENT TEST FILE AND MVP (Minimum viable product), NOT PRODUCTION AND NOT USABLE

import datetime
import time

import pypresence
from time import sleep
from pypresence import Presence, Client

client_id = '978056128967618641'
RPC = Client(client_id)
RPC.start()
RPC.set_activity(7908,state="Free, I can do stuff now",details="Free")
while True:
    sleep(120)
# sleep(60)
# RPC.clear_activity()
sleep(15)
