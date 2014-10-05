from urllib2 import urlopen

def Check(user):
    # get the url
    url = 'https://minecraft.net/haspaid.jsp?user=%s' % (user)
    
    # opens url and reads it (and stores it in string)
    resp = urlopen(url)
    html = resp.read()
    html = str(html)
    
    #  this is the part that checks is user is premium or not

    # if the success label in the html code (if user is premium) then print
    if('true' in html): return True
    # else if success label NOT in html then print
    elif('false' in html): return False
    # if a strange error has occured
    else: raise('error')
        
def usage():
    print('SEE TESTS.PY FOR EXAMPLES')

if __name__ == "__main__":
    usage()