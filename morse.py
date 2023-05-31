# import RPi.GPIO as GPIO
import time
import morse_talk as mtalk

long = 0.5
short = 0.3


def On():
        led = 14 #number of gpio pin in use
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, True)

def Off():
        led = 14 #number of gpio pin in use
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, False)


def Long():
        On()
        time.sleep(long)
        Off()
        time.sleep(long)
        # print("long")

def Short():
        On()
        time.sleep(short)
        Off()
        time.sleep(short)
        # print("sort")


def Pause():
        time.sleep(1)


def Say(text):
        m = mtalk.encode(text)
        test = m.split("   ")
        final = []

        for l in test:
                ls = l.lstrip(" ")
                if not l == "":
                        final.append(ls)
        for letter in final:
                for symbol in letter.strip():
                        if symbol == "-":
                                Long()
                        elif symbol == ".":
                                Short()
                Pause()

GPIO.cleanup()