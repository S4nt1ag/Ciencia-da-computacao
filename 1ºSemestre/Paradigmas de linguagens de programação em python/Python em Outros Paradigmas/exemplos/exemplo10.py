import threading
import time
import urllib2

start = time.time()
HTTP = 'http://'
urls = [f'{HTTP}www.google.com', f'{HTTP}www.Apple.com', f'{HTTP}www.Microsoft.com',
        f'{HTTP}www.instagram.com']

def chamaUrl(url):
  req = urllib2.request(url)
  response = urllib2.urlopen(req)
  thePage = response.read()
  print (url, (time.time) - start)

threads = [threading.Thread(target=chamaUrl, args=(url,)) for url in urls]

for thread in threads:
  thread.start()
for thread in threads:
  thread.join()

print ((time.time()) - start)