# CURRENT TEST FILE AND MVP (Minimum viable product), NOT PRODUCTION AND NOT USABLE

from time import sleep

import pypresence.exceptions
from pypresence import Presence, Client
from win32gui import GetWindowText, GetForegroundWindow


def updateDiscordPresence():
    status_state = GetWindowText(GetForegroundWindow())
    status_state = exceptions(status_state)
    if status_state == "":
        status_state = "Unknown Window"

    try:
        RPC.set_activity(7908, state=status_state, details="Current Window", small_text="Bloo",
                         small_image="https://static.onecms.io/wp-content/uploads/sites/28/2017/05/blue0517.jpg")
    except pypresence.exceptions.ServerError:
        RPC.set_activity(7908, state="Error: Current foreground window name too long", details="Current Window",
                         small_text="Bloo",
                         small_image="https://static.onecms.io/wp-content/uploads/sites/28/2017/05/blue0517.jpg")



    return status_state


def exceptions(status_state):  # will def change this later
    # print("Before exception", status_state)
    if "Brave" in status_state:
        status_state = "Brave Browser"

    if "Discord" in status_state and not "py" in status_state:
        status_state = "Discord"

    if "Notepad" in status_state:
        status_state = "Notepad"

    if "Minecraft" in status_state or "lunarclient" in status_state or "Lunar" in status_state:
        status_state = "Overriding native game activity"
    return status_state


def sleepAndWarn():
    sleep(10)
    secondCounter = 5
    for x in range(5):
        print(f'Updating in {secondCounter} seconds')
        secondCounter = secondCounter - 1
        sleep(1)


if __name__ == '__main__':
    sleep(2)
    client_id = '978056128967618641'
    RPC = Client(client_id)
    RPC.start()
    print(updateDiscordPresence())

    while True:
        sleepAndWarn()
        print(updateDiscordPresence())
