#!/bin/sh

python grabber.py

sort mylinks.txt | uniq > filtered_links.txt

wget -i filtered_links.txt -P contents/ -q --show-progress
