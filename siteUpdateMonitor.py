import time
import hashlib
from urllib.request import urlopen, Request
from threading import Thread
from win10toast import ToastNotifier

# URL to monitor
url = Request('https://staticdress.bigcartel.com/', headers={'User-Agent': 'Mozilla/5.0'})
 
# GET request on site URL
response = urlopen(url).read()

# Hash the response
currentHash = hashlib.sha224(response).hexdigest()

toaster = ToastNotifier()

toaster.show_toast(title="Static Dress", msg="BigCartel webstore has been updated", threaded=True, duration=10)

print("Script started")

def pollChanges():
    runThread = True
    while runThread:
        try:
            response = urlopen(url).read()
            currentHash = hashlib.sha224(response).hexdigest()
            time.sleep(30)
            response = urlopen(url).read()
            newHash = hashlib.sha224(response).hexdigest()

            if newHash != currentHash:
                print("Site has been updated")

                toaster.show_toast(title="Static Dress", msg="BigCartel webstore has been updated", threaded=True, duration=10)

                runThread = False

        except Exception as e:
            print("Something went wrong " + e)

    return

pollingThread = Thread(target=pollChanges)
pollingThread.start()

while pollingThread.is_alive():
    print("Checking for changes.  ", end='\r')
    time.sleep(5)
    print("Checking for changes.. ", end='\r')
    time.sleep(5)
    print("Checking for changes...", end='\r')
    time.sleep(5)