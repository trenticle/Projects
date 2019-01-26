import time
from datetime import datetime as dt


# hosts_path= 'C:\\Windows\\WinSxS\\amd64_microsoft-windows-w..ucture-other-minwin_31bf3856ad364e35_10.0.17763.1_none_2605875bbd3b5e2e\\hosts'

hosts_path= 'C:\\users\\trent\\desktop\\Blocker\\hosts'

redirect= '127.0.0.1'

website_list= ['www.facebook.com','facebook.com', 'trenticle.mail.live.com', 'www.trenticle.mail.live.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):

        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect +' '+ website +'\n')
    else:
        with open(hosts_path, 'r+') as file:
            content= file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)