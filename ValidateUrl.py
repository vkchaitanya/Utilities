#The following code validates a url. This is a 2 step process, to do that.
#First I validate the domain and next the path attached to the domain.

from urlparse import urlparse
import urllib2
import socket

class ValidateURL:
    def __init__(self, url):
        self._url = url
        self._startActivity(self._url)        

    def _startActivity(self,url):
        self._parts = urlparse(url)
        if self._checkDomain(self._parts[1]):
            print 'The domain: ', self._parts[1], ' is valid'
            if self._checkUrl(url):
                print url,' is valid'
            else:
                print 'The path ',self._parts[2],' is not valid'
        else:
            print self._parts[1],' domain does not exist'

    #Checks whether the domain is right or not
    def _checkDomain(self,domain):
        x = True
        try:
            socket.gethostbyname_ex(domain)
        except socket.gaierror:
            x = False
        except socket.error:
            x = False
        finally:
            return x

    #Checks whether the path is right or not
    def _checkUrl(self,url):
        x = True
        self._req = urllib2.Request(url)
        try:
            urllib2.urlopen(self._req)
        except urllib2.URLError, e:
            x = False
        finally:
            return False

if __name__ == "__main__":
    valid = ValidateURL('http://www.bbc.co.uk/news/world-europ/')
    valid = ValidateURL('http://bb1qqcl.co.uk/')