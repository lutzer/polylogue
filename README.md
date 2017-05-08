# Polylogue

An interactive installation for transmediale 2016

![](anxiety.png)

## Setup IDE

* to install node modules, install npm and run `npm install`
* to compile sass scripts, run `compass watch`

### Python configuration

* `pip2 install Pillow` auf pi: `sudo pacman -S python2-pillow
* `pip2 install socketIO-client`
* `pip2 install pyserial`

### Other Tools

* font generation by SpriteFontBuilder for mac
* font conversion with this script: <https://github.com/playcanvas/fonts/blob/master/fnt_to_json.py>


### Create virtual Serial Port



## Call Test scripts

* Within scripts dir, execute: `python -m polylogue.test.print_test.py`

## Installation

### Create startup scripts

* start node server automatically by calling `pm2 start app.js` and then `pm2 save`
* create python startup script `nano /etc/systemd/system/polylogue.service`



* ``` 
  [Unit]

  Description=Launches polylogue print server script

  After=network.target

  [Service]

  Type=simple

  WorkingDirectory=/home/pi/scripts/polylogue/

  ExecStart=/bin/python2 polylogue_print_server.py

  RemainAfterExit=true

  [Install]

  WantedBy=multi-user.target
  ```
  ​


* `sudo systemctl enable polylogue.servive` to automatically start

## Twitter polylogue

### for normal polylogue disable internet and redirect all trafic to rasp pi

* go to network -> wifi -> "the wan wifi" -> disable
* login by ssh : `ssh root@192.168.72.1`
  * uncomment line in */etc/dnsmasq.conf*: `address=/#/192.168.72.2`

### edit tag



edit `nano ~/polylogue/twitterserver/config.js` change

```
tags : '#rp17' // see https://dev.twitter.com/rest/public/search for how to setup the search query

	/*
		#love OR #hate : one or the other
		#love #hate : contains both tags
	*/
```