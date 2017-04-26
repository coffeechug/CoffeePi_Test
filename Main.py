#!/usr/bin/env python3
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time
import vending

import ev3dev.ev3 as ev3
from ev3dev.auto import *


<<<<<<< Updated upstream
tags=['legovend']
words=[]
#Variables that contains the user credentials to access Twitter API
#Two versions, redudancy if the first fails...
access_token = '857031350850813954-b3rNrAR3lf7iCr3tFJ7gImH8wcWt37n'
access_token_secret = 'nls3o3VZOTwqG77RwTPTzSXZ1EsVIaY7FEUXeqgrPazVy'
consumer_key = 'DtPEXg53kCvL5ukzcmHm6e5O8'
consumer_secret = 'DOoP7yDRYG7ln9WuiGzEsssFL9DsakwK1LukL7h1aLWnwybRvy'

access_token2 = '857031350850813954-b3rNrAR3lf7iCr3tFJ7gImH8wcWt37n'
access_token_secret2 = 'nls3o3VZOTwqG77RwTPTzSXZ1EsVIaY7FEUXeqgrPazVy'
consumer_key2 = 'DtPEXg53kCvL5ukzcmHm6e5O8'
consumer_secret2 = 'DOoP7yDRYG7ln9WuiGzEsssFL9DsakwK1LukL7h1aLWnwybRvy'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        global mA,mB,home,cs, lastVend
        try:
            tweet = json.loads(data)
            tw
        except:
            pass

        if tags:
            if all(tag in tweet['text'].lower() for tag in tags):
                print (tweet['user']['screen_name'], ' - ', tweet['text'])
                
                if int(tweet['timestamp_ms'])>lastVend:
                    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
                    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
                    
                    vending.onTweet(mA, mB, cs, home)

                    time.sleep(2)
                    lastVend = int(round(time.time() * 1000))+1000
                    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
                    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        return True
    
    def on_error(self, status):
        print( status)
        return False


if __name__ == '__main__':
    
    #This handles Twitter authetification and the connection to Twitter Streaming API
    print( 'here')
    global mA,mB,home,cs, lastVend
    mA = ev3.MediumMotor('outA')
    mB = ev3.MediumMotor('outB')
    home = mA.position - 40
    cs=ColorSensor()
    lastVend = int(round(time.time() * 1000))
    
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    auth2 = OAuthHandler(consumer_key2, consumer_secret2)
    auth2.set_access_token(access_token2, access_token_secret2)
    stream2 = Stream(auth2, l)
    
    try:

        Sound.speak('Ready to go').wait()
        print ('trying 1')
        stream.filter(track=tags)
        print('trying 2')
        stream2.filter(track=tags)
        Sound.speak('Could not connect').wait()
    except Exception as e:
        print( e)
        
