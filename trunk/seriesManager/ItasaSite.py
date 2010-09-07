from BeautifulSoup import BeautifulSoup
import cookielib, urllib, urllib2

ITASAURL = "http://www.italiansubs.net/index.php"

class ItasaSite(object):
    def __init__(self):
        self.itasa=BeautifulSoup(urllib.urlopen(ITASAURL))
        pass

    def getReturnValue(self):
        return self.itasa.find('input',value='1')['name']

    def getOtherValue(self):
        return self.itasa.find('input',{'name':'return'})['value']

    def login(self, username, password):
        data={'username':username,'passwd':password,'remember':'yes','Submit':'Login','option':'com_user','task':'login','silent':'true'}
        data['return']=self.getReturnValue()
        data['1']=self.getOtherValue()

        #cookiejar = cookielib.CookieJar()
        #urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
        #urlOpener.addheaders = [("User-agent","Mozilla/5.0 (compatible)")]
        #urllib2.install_opener(urlOpener)
        encodedData = urllib.urlencode(data)
        #request = urllib2.Request(ITASAURL, encodedData)
        #self.url = urlOpener.open(request)
        #return cookiejar
        self.url=urllib.urlopen(ITASAURL,encodedData)
