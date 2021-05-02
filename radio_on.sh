#!/bin/bash
rtl_fm -f 77600000 -s 1000000 -r 60000 - | aplay -r 60000 -f S16_LE -t raw -D plughw:Device
