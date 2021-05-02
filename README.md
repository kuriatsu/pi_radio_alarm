# pi_radio_alarm

## Description
Use fm_radio (RTL_SDR) as alarm with raspberry pi


## Requirements
* raspberry pi
* servomotor (SG90, MS18...)
* RTL-SDR


## Setup
```bash
$ sudo mkdir /usr/local/lib/pi_radio_alarm
$ sudo mv pi_alarm.py /usr/local/lib/
$ sudo mv radio_on.sh /usr/local/lib/
$ sudo mv radio_off.sh /usr/local/lib/
$ sudo mv pi_radio_alarm.service /etc/systemd/system/
$ sudo systemctl enable pi_radio_alarm.service
```

## Config
* pi_radio.py
	Time to automatically turn on/off the radio
	GPIO for servomotor output

* radio_on.sh
	change frequency for FM radio

## Todo
* Enable editing parameters (channel, volume, alart time etc.)
* Make UI
