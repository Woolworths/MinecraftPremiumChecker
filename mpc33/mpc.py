from urllib.request import urlopen

#while true to make sure we dont need to keep restarting it every time we find the user status
class Check(object):
        
    def __init__(self, user):
        self.user = user
            
        # gets the url
        url = 'https://minecraft.net/haspaid.jsp?user=%s' % (self.user)
        
        # opens url and reads it (and stores it in string)
        resp = urlopen(url)
        html = resp.read()
        self.html = str(html)
    
    #  this is the part that checks is user is premium or not
    def run(self):
        # if the success label in the html code (if user is premium) then print
        if('true' in self.html): return True
        # else if success label NOT in html then print
        elif('false' in self.html): return False
        # if a strange error has occured
        else: raise('error')
        
def usage():
    print('SEE TESTS.PY FOR EXAMPLES')

if __name__ == "__main__":
    usage()