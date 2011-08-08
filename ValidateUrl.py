#The following code validates a url. This is a 2 step process, to do that. 
#First I validate the domain and next the path attached to the domain.

from urlparse import urlparse
import urllib2
import socket
class ValidateURL:
    def __init__(self, url):
        self._url = url

    def startActivity(self):
        self._parts = urlparse(self._url)
        a = self._checkDomain(self._parts[1])
        if a:
            b = self._checkUrl(self._url)
            if b == 1:
                print self._url,' is valid'
            else:
                print 'The path ',self._parts[2],' is not valid'
        else:
            print self._parts[1],' domain does not exist'

    #Checks whether the domain is right or not
    def _checkDomain(self,domain):
        x = 1
        try:
            socket.gethostbyname_ex(domain)
        except socket.gaierror:
            x = 0
        except socket.error:
            x = 0
        finally:
            return x

    #Checks whether the path is right or not
    def _checkUrl(self,url):
        x = 1
        self._req = urllib2.Request(url)
        try: 
            urllib2.urlopen(self._req)
        except urllib2.URLError, e:
            #print e
            x = 0
        finally:
            return x

if __name__ == "__main__":
    valid = ValidateURL('http://stackoverflow.com/questions/invalid-urls-throw-an-exception-python')
    valid.startActivity()
    valid1 = ValidateURL('http://stackoverflow.com/questions/6414417/invalid-urls-throw-an-exception-python')
    valid1.startActivity()