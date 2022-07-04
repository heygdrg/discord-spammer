import time
import requests
from requests import get
import json
import pystyle
from pystyle import *
System.Size(150, 47)
banner1 = """











▄▄▌ ▐ ▄▌ ▄▄▄·    .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. • ▌ ▄ ·. ▄▄▄ .▄▄▄  
██· █▌▐█▐█ ▄█    ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪·██ ▐███▪▀▄.▀·▀▄ █·
██▪▐█▐▐▌ ██▀·    ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄ 
▐█▌██▐█▌▐█▪·•    ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██ ██▌▐█▌▐█▄▄▌▐█•█▌
 ▀▀▀▀ ▀▪.▀        ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀
                                                         
"""
banner2 = """

             _                      _______                      _
          _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
         dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
         V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
                  `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
                   `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
              __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
            ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
         _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
                     `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
             ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
           ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
          ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
          MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
          YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
           `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
             `'                  `OObNNNNNdOO'                   `'
                                  `~OOOOO~'

"""
banner = Add.Add(banner1, banner2)

print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(banner + '\n\n')))

webhook_url = Write.Input("[?] enter the webhook URL ->", Colors.purple, interval=0.005)
print()
#webhook_url = "https://discord.com/api/webhooks/985856019840237618/opDyjvsd025DgAd6TLWek_cID1zYjqAU85C7kMEXIjMO8LV0hB80skjCBcUej7B9NwUe"

content_message = Write.Input("[?] what you wanna say ->", Colors.purple, interval=0.005)
print()
number = int(Write.Input("[?] how manny time you want to repeat the message ->", Colors.purple, interval=0.005))

for i in range(number):
    webhook_url = "https://discord.com/api/webhooks/985856019840237618/opDyjvsd025DgAd6TLWek_cID1zYjqAU85C7kMEXIjMO8LV0hB80skjCBcUej7B9NwUe"
    message = '\n'.join([content_message
                ])
    r = requests.post(webhook_url, json={'username': 'wp bot', 'content': message})

Write.Input("[!] messages sent to the webhook", Colors.purple, interval=0.005)