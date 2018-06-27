import urllib.request
import pickle
import sys
from time import ctime
from apscheduler.schedulers.blocking import BlockingScheduler
from twilio.rest import TwilioRestClient

#accountSID =
#authToken

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=3600)
def check_website():
    request = urllib.request.Request("https://secondstopeurope.weebly.com/blog")
    response = urllib.request.urlopen(request) # Make the request
    htmlString = response.read()

    try:
        file = pickle.load(open("blog.p", 'rb'))
        if file == htmlString:
            print("Janie has not updated the website ("+ctime()+")\n")
        else:
            print("Janie updated the blog!!!\nSaving... ("+ctime()+")\n")
            print('\a')
            pickle.dump(htmlString, open('blog.p', 'wb'))

    except IOError:
        pickle.dump(htmlString, open("blog.p", 'wb'))
        print("Creating fresh file ("+ctime()+")")



sched.start()
