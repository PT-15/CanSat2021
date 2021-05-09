#!/bin/sh

python3 serialGps.py &
python3 radioSend.py &
misionCamara.py
