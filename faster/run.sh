#!/bin/bash
fswebcam -r 640x480 capture.jpg
python detect.py
dect=$(<detect_result.txt)
if [ $dect = "yes" ]
then
python sc.py
python main.py
res=$(<output.txt)
omxplayer sound/$res.mp3
fi

