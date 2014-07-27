import urllib2

print 'courtesy of doctormckay.com'

#while true to make sure we dont need to keep restarting it every time we find the user status
while True:
        
    # gets username, makes sure it's a string and makes it lowercase
    user = raw_input('>>> = ')
    user = str(user)
    user = user.lower()
    
    # gets the url
    url = 'https://www.doctormckay.com/utilities/mc_checker.php?u=' + user
    
    # opens url and reads it (and stores it in string)
    parse = urllib2.urlopen(url)
    html = parse.read()

    #  this is the part that checks is user is premium or not
    def runName(name):
        # if the success label in the html code (if user is premium) then print
        if '<span class="label label-success">premium</span>' in html:
            print 'The user' + ' ' + name + ' ' + 'is premium!'
            
        # else if success label NOT in html then print
        elif '<span class="label label-success">premium</span>' not in html:
            print 'The user' + ' ' + name + ' ' + 'is not premium!'

        # if a strange error has occured
        else:
            print 'An error has occured, we could not find the user' + ' ' + name

    # here we just run the function
    runName(user)
