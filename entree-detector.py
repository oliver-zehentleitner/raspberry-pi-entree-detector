#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# File: entree-detector.py
#
# Part of ‘raspberry-pi-entree-detector’
# Project website: https://github.com/oliver-zehentleitner/raspberry-pi-entree-detector
#
# Author: Oliver Zehentleitner
#         https://about.me/oliver-zehentleitner
#
# Sponsor: ResiGrass GmbH, https://www.kunst-rasen.at
#
# Copyright (c) 2019, Oliver Zehentleitner
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import RPi.GPIO as GPIO
import time
import os
import datetime

def entryDetection():
    APP_PATH = "/opt/entree-detector/"
    DOOR_SENSOR_PIN = 4
    DOOR_BELL_SOUND_FILE = APP_PATH + "bell.mp3"
    DOOR_TOO_LONG_OPEN_SOUND_FILE = APP_PATH + "close_the_door.mp3"
    # False = disabled; 120 = play 'close_the_door.mp3' if the door remains open longer than 120 seconds
    DOOR_TOO_LONG_OPEN_TIME_IN_SECONDS = False
    RASPBERRY_PI_MAX_VOLUME_PERCENT = 90
    LOG_FILE = APP_PATH + "door_opening.log"

    isOpen = None
    lastState = None
    isOpenSince = None

    print("Initializing ...")
    os.system("amixer set PCM,0 " + str(RASPBERRY_PI_MAX_VOLUME_PERCENT) + "%") # set raspberry pi volume
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    print("Start entree detection ...")
    while True:
        lastState = isOpen
        isOpen = GPIO.input(DOOR_SENSOR_PIN)
        if lastState == 0 and isOpen == 1:
            print("Door is open!")
            isOpenSince = time.time()
            os.system('mpg321 ' + DOOR_BELL_SOUND_FILE + ' &')
            f = open(LOG_FILE, "a")
            f.write("Door opened at " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\r\n")
            f.close()
        elif lastState == 1 and isOpen == 1 and isOpenSince is not None and DOOR_TOO_LONG_OPEN_TIME_IN_SECONDS is not False:
            if (time.time() - isOpenSince) > DOOR_TOO_LONG_OPEN_TIME_IN_SECONDS:
                os.system('mpg321 ' + DOOR_TOO_LONG_OPEN_SOUND_FILE + ' &')
                isOpenSince = None
        elif lastState == 1 and isOpen == 0:
            f = open(LOG_FILE, "a")
            f.write("Door closed at " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\r\n")
            f.close()
        time.sleep(1)


def main():
    try:
        entryDetection()
    except (IOError, KeyboardInterrupt):
        GPIO.cleanup()


if __name__ == '__main__':
    main()
