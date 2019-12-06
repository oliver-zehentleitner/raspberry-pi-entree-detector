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


def entree_detection():
    # Config:
    app_path = "/opt/raspberry-pi-entree-detector/"
    door_sensor_pin = 4
    door_bell_audio_file = app_path + "audio/On\ The\ Farm-SoundBible.com.mp3"
    door_too_long_open_audio_file = app_path + "audio/Turkey\ Putt-SoundBible.com.mp3"
    door_too_long_open_time_in_seconds = 600  # False = disabled
    raspberry_pi_max_volume_percent = 90
    log_file = app_path + "door_opening.log"

    print("Initializing ...")
    is_open = None
    is_open_since = None
    os.system("amixer set PCM,0 " + str(raspberry_pi_max_volume_percent) + "%")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(door_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    print("Start entree detection ...")
    while True:
        last_state = is_open
        is_open = GPIO.input(door_sensor_pin)
        if last_state == 0 and is_open == 1:
            print("Door is open!")
            is_open_since = time.time()
            os.system('mpg321 ' + door_bell_audio_file + ' &')
            file = open(log_file, "a")
            file.write("Door opened at " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\r\n")
            file.close()
        elif last_state == 1 and is_open == 1 and is_open_since is not None \
                and door_too_long_open_time_in_seconds is not False:
            if (time.time() - is_open_since) > door_too_long_open_time_in_seconds:
                os.system('mpg321 ' + door_too_long_open_audio_file + ' &')
                is_open_since = None
        elif last_state == 1 and is_open == 0:
            file = open(log_file, "a")
            file.write("Door closed at " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\r\n")
            file.close()
        time.sleep(1)


def main():
    try:
        entree_detection()
    except (IOError, KeyboardInterrupt):
        GPIO.cleanup()


if __name__ == '__main__':
    main()
