from threading import Thread, Event
import datetime
import RPi.GPIO as GPIO
import time
import sys
import tweepy, time
auth = tweepy.OAuthHandler('6jj33wAEIhdQGLazNeWunjez8', 'dgNUJbzBEVfhr8ShGPeJRK4ecNlKXRKLtzx48y2agjynrBealh')
auth.set_access_token('166842701-iV01OtWPDkjQybnZuEIf1GWp0vc5fI71lz7LOfB2', 'FC7DpSxVuU7uKN2E0BE8G0rrz4h4I6NtDanxI3VOMLHas')
api = tweepy.API(auth)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.IN,
pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN,
pull_up_down=GPIO.PUD_UP)

event = Event()

counter1 = 0
counter2 = 0
    
def route1():
    global counter1
    current = True
    old = True

    while True:
        if event.is_set():
            return
        current = GPIO.input(8) 
        if current == True and old == False:
            counter1 += 1
            print ("Counter 1: {}".format(counter1))
            
        old = current
        
        if counter1 == 20:
            event.set()
            return
        #time.sleep(.005)

def route2():
    global counter2
    current = True
    old = True

    while True:
        if event.is_set():
            return
        current = GPIO.input(10) 
        if current == True and old == False:
            counter2 += 1
            print ("Counter 2: {}".format(counter2))

        old = current
        
        if counter2 == 3:
            event.set()
            return
        #time.sleep(.005)

def  main():
    while True:
        run()
        

def run():
    global counter1
    global counter2

    t1 = Thread(target=route1)
    t2 = Thread(target=route2)

    t1.start()
    t2.start()

    event.wait()

    print("Route 1: {},  Route 2: {}".format(counter1, counter2))


    if counter1 > counter2:
        tweet = ("Take Route 885")
    elif counter2 > counter1:
        tweet = ("Take Streets Run Road")
    else:
        tweet = ("Both routes the same")
    
    now = str(datetime.datetime.now())
    tweet = now+" "+tweet
    print(tweet)
    print("tweeting")
    api.update_status(tweet.strip())
    time.sleep(1)
    event.clear()

if __name__ == "__main__":
    main()
    
