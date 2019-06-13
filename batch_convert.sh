#!/bin/bash


# mkdir -p output
for i in *.aiff; do ffmpeg -i "$i" "output/$(echo ${i%.*}).wav"; done
