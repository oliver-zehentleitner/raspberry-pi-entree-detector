[![python 3](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/downloads/)
[![stable](https://img.shields.io/badge/status-stable-brightgreen.svg)](https://github.com/oliver-zehentleitner/raspberry-pi-entree-detector/issues)
[![Donations/week](http://img.shields.io/liberapay/receives/oliver-zehentleitner.svg?logo=liberapay)](https://liberapay.com/oliver-zehentleitner/donate)
[![Patrons](http://img.shields.io/liberapay/patrons/oliver-zehentleitner.svg?logo=liberapay")](https://liberapay.com/oliver-zehentleitner/donate)

# raspberry-pi-entree-detector
Door entree detector with Raspberry PI written in Python

## Description
- Play a sound file when the door opens
- Log date and time to a text file, when the door gets opened/closed
- Play a sound file, if the door stays open (optional)

## Requirements
- [Raspberry PI](https://www.amazon.de/gp/search/ref=as_li_qf_sp_sr_tl?ie=UTF8&tag=oliverzehentl-21&keywords=raspberry+pi&index=aps&camp=1638&creative=6742&linkCode=ur2&linkId=40fbf0af9433bd9342388439233dc913) /
[Raspberry PI Starterkit](https://www.amazon.de/gp/product/B01CI5879A/ref=as_li_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B01CI5879A&linkCode=as2&tag=oliverzehentl-21&linkId=ae25625f0490ffbfa2ca4ffb0047b8d9)
- [Door/Window GPIO kit](https://www.amazon.de/gp/product/B00DBDT6TY/ref=as_li_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B00DBDT6TY&linkCode=as2&tag=oliverzehentl-21&linkId=b24085cc7ae90e2ceae103b494cad697)
- [Speaker for the Raspberry PI](https://www.amazon.de/gp/search/ref=as_li_qf_sp_sr_tl?ie=UTF8&tag=oliverzehentl-21&keywords=pc+speaker&index=aps&camp=1638&creative=6742&linkCode=ur2&linkId=68bce6b6bb4104ae94453af49c907824)

## Installation
```
$ sudo apt-get install python-dev python-rpi.gpio mpg321
```
[Download the latest release](https://github.com/oliver-zehentleitner/raspberry-pi-entree-detector/releases/latest) to
`/opt/`.

Make it executable
```
$ chmod +x /opt/raspberry-pi-entree-detector/entree-detector.py
```

Add your [mp3 files](http://soundbible.com) and set them up in the config section of `entree-detector.py`. 

If necessary change the sensor pin number.

Start it:
```
$ ./entree-detector.py
```

## Autostart and access to the console output
Install `screen`:
```
apt install screen
```

Create a cronjob as root with:
```
crontab -e
```

Insert the line:
```
@reboot su - root -c "screen -dm -S entree-detector /opt/raspberry-pi-entree-detector/entree-detector.py"
```

Thats it, now restart and see if it works:
```
shutdown -r 0
```

To see the output use as root:
```
screen -x entree-detector
```

Dont close screen, just leave it with the detach command `Ctrl+a d`. For more information about screen visit 
https://linuxize.com/post/how-to-use-linux-screen/#working-with-linux-screen-windows

## Contributing
[raspberry-pi-entree-detector](https://github.com/oliver-zehentleitner/raspberry-pi-entree-detector) is an open 
source project which welcomes contributions which can be anything from simple documentation fixes to new features. To 
contribute follow 
[this guide](https://github.com/oliver-zehentleitner/raspberry-pi-entree-detector/blob/master/CONTRIBUTING.md).
 
### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=oliver-zehentleitner/raspberry-pi-entree-detector)](https://github.com/oliver-zehentleitner/raspberry-pi-entree-detector/graphs/contributors)

We ![love](https://s3.gifyu.com/images/heartae002231c41d8a80.png) open source!

### Donate
Since you are probably a developer yourself, you will understand very well that the creation of open source software is 
not free - it requires technical knowledge, a lot of time and also financial expenditure.

If you would like to help me to dedicate my time and energy to this project, donations are very welcome.

[![Donate using Liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/oliver-zehentleitner/donate)

```
BTC: 39fS74fvcGnmEk8JUV8bG6P1wkdH29GtsA
DASH: XsRhBuPkXGF9WvifdpkVhTGSmVT4VcuQZ7
ETH: 0x1C15857Bf1E18D122dDd1E536705748aa529fc9C
LTC: LYNzHMFUbee3siyHvNCPaCjqXxjyq8YRGJ
XMR: 85dzsTRh6GRPGVSJoUbFDwAf9uwwAdim1HFpiGshLeKHgj2hVqKtYVPXMZvudioLsuLS1AegkUiQ12jwReRwWcFvF7kDAbF
ZEC: t1WvQMPJMriGWD9qkZGDdE9tTJaawvmsBie
```
## You need a Python Dev?
If you would like to [hire me](https://about.me/oliver-zehentleitner) for a Python project, you can book me through 
my company [LUCIT](https://www.lucit.dev).
