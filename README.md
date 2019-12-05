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
$ chmod +x /opt/entree-detector/entree-detector.py
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
@reboot su - root -c "screen -dm -S entree-detector /opt/entree-detector/entree-detector.py"
```

Thats it, now restart and see if it works:
```
shutdown -r 0
```

To see the output use as root:
```
screen -x entree-detector
```